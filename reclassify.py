#!/usr/bin/env python3
"""Reclassify income/expense on Dave's expense-tracker Transactions tab.
Mirrors guessTypeFromDesc() in index.html. Only flips rows with a confident
guess that differs from the current value. Logs every change."""
import json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

URL = "https://script.google.com/macros/s/AKfycbzUQJ2Kjuu5-udsVZO49fQ4Mb89JyrhKETIIyjW-HPqC4Upv3F2XMzksg3uzk2cmQR8cg/exec"
LOG = "/home/hatch/workspace/expense-tracker/reclassify.log"

def api_get(params):
    q = '&'.join('%s=%s' % (k, v) for k, v in params.items())
    with urllib.request.urlopen(URL + '?' + q, timeout=90) as r:
        return json.load(r)

def api_post(body, tries=4):
    data = json.dumps(body).encode()
    for a in range(tries):
        try:
            req = urllib.request.Request(URL, data=data, headers={'Content-Type': 'text/plain'})
            with urllib.request.urlopen(req, timeout=90) as r:
                j = json.load(r)
            if j.get('ok'):
                return True
        except Exception as e:
            if a == tries - 1:
                return 'ERR %s' % e
            time.sleep(2 * (a + 1))
    return 'ERR failed'

def guess(desc):
    d = (desc or '').lower()
    if re.search(r'purchase return|refund', d): return 'income'
    if re.search(r'payroll|deposit|interest payment|zelle from|instant pmt from', d): return 'income'
    if 'transfer' in d: return 'income' if re.search(r'\bfrom\b', d) else 'expense'
    if re.search(r'purchase authorized|purchase with cash back|\bchecks?\b|withdrawal|bill pay|online pmt|\bfee\b|moneylink|\bmtg\b|mortgage|\bloan\b|\bpymts?\b|\bpayment\b|premium', d): return 'expense'
    return None

def log(msg):
    line = '%s %s' % (time.strftime('%H:%M:%S'), msg)
    print(line, flush=True)
    with open(LOG, 'a') as f:
        f.write(line + '\n')

def main():
    rows = api_get({'action': 'list', 'tab': 'Transactions'})['rows']
    log('fetched %d rows' % len(rows))
    jobs = []
    for r in rows:
        g = guess(r.get('merchant') or r.get('description'))
        if g and g != r.get('txn_type'):
            jobs.append((r, g))
    log('%d rows need reclassification' % len(jobs))
    if not jobs:
        return
    ok = 0
    failed = []

    def do(job):
        r, g = job
        row = dict(r)
        row['txn_type'] = g
        res = api_post({'action': 'update', 'tab': 'Transactions', 'id': r['id'], 'row': row})
        return (r['id'], g, (r.get('merchant') or r.get('description') or '')[:60], res)

    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, (rid, g, desc, res) in enumerate(ex.map(do, jobs)):
            if res is True:
                ok += 1
            else:
                failed.append(rid)
                log('FAILED %s -> %s (%s): %s' % (rid, g, desc, res))
            if (i + 1) % 25 == 0:
                log('progress %d/%d' % (i + 1, len(jobs)))
    log('done: %d ok, %d failed' % (ok, len(failed)))
    if failed:
        log('failed ids: %s' % ','.join(failed))

if __name__ == '__main__':
    main()
