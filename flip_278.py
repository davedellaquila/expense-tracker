#!/usr/bin/env python3
"""Flip the 278 misclassified income rows to expense (Dave confirmed 2026-09-27).
Only touches rows that are STILL marked income at update time; anything Dave or
Nancy changed since the analysis is left alone. Logs every change."""
import json, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

URL = "https://script.google.com/macros/s/AKfycbzUQJ2Kjuu5-udsVZO49fQ4Mb89JyrhKETIIyjW-HPqC4Upv3F2XMzksg3uzk2cmQR8cg/exec"
IDS = json.load(open('/tmp/flip_ids_final.json'))
LOG = "/home/hatch/workspace/expense-tracker/reclassify.log"

def log(msg):
    line = '%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg)
    print(line, flush=True)
    with open(LOG, 'a') as f:
        f.write(line + '\n')

def api_get(params, tries=4):
    q = '&'.join('%s=%s' % (k, v) for k, v in params.items())
    for a in range(tries):
        try:
            with urllib.request.urlopen(URL + '?' + q, timeout=90) as r:
                return json.load(r)
        except Exception as e:
            if a == tries - 1:
                raise
            time.sleep(2 * (a + 1))

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

def main():
    rows = api_get({'action': 'list', 'tab': 'Transactions'})['rows']
    by_id = {r['id']: r for r in rows}
    log('flip-278: fetched %d rows, %d ids to process' % (len(rows), len(IDS)))
    jobs, skipped = [], []
    for rid in IDS:
        r = by_id.get(rid)
        if not r:
            skipped.append((rid, 'not found'))
        elif r.get('txn_type') != 'income':
            skipped.append((rid, 'no longer income (%s)' % r.get('txn_type')))
        else:
            jobs.append(r)
    log('flip-278: %d to flip, %d skipped' % (len(jobs), len(skipped)))
    for rid, why in skipped:
        log('SKIP %s: %s' % (rid, why))

    ok, failed = 0, []
    def do(r):
        row = dict(r)
        row['txn_type'] = 'expense'
        res = api_post({'action': 'update', 'tab': 'Transactions', 'id': r['id'], 'row': row})
        return (r['id'], (r.get('merchant') or r.get('description') or '')[:60], res)

    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, (rid, desc, res) in enumerate(ex.map(do, jobs)):
            if res is True:
                ok += 1
            else:
                failed.append(rid)
                log('FAILED %s (%s): %s' % (rid, desc, res))
            if (i + 1) % 50 == 0:
                log('flip-278 progress %d/%d' % (i + 1, len(jobs)))
    log('flip-278 done: %d ok, %d failed' % (ok, len(failed)))
    if failed:
        log('failed ids: %s' % ','.join(failed))

if __name__ == '__main__':
    main()
