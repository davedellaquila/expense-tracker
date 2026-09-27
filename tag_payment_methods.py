#!/usr/bin/env python3
"""Tag payment_method on existing expense rows based on bank description patterns.

- Capital One card statements: ALL-CAPS merchant lines -> 'Capital One'
- Wells Fargo checking: 'Purchase authorized on...', transfers, ATM, Bill Pay, etc.
  -> 'Wells Fargo <masked acct>' when an account/card number is in the
  description, else plain 'Wells Fargo'
Only touches rows whose payment_method is currently 'Other'/empty (never
overwrites Dave/Nancy's manual entries) and only rows typed as expense.

Usage: ./tag_payment_methods.py           # dry run (report only)
       ./tag_payment_methods.py --apply   # write changes back
"""
import json, re, sys, time, urllib.request
from concurrent.futures import ThreadPoolExecutor

URL = 'https://script.google.com/macros/s/AKfycbzUQJ2Kjuu5-udsVZO49fQ4Mb89JyrhKETIIyjW-HPqC4Upv3F2XMzksg3uzk2cmQR8cg/exec'
APPLY = '--apply' in sys.argv
LOG = 'tag_payment_methods.log'

def log(msg):
    line = '%s %s' % (time.strftime('%Y-%m-%d %H:%M:%S'), msg)
    print(line, flush=True)
    with open(LOG, 'a') as f:
        f.write(line + '\n')

def api_get(params, tries=4):
    q = '&'.join('%s=%s' % (k, urllib.parse.quote(str(v))) for k, v in params.items())
    last = None
    for i in range(tries):
        try:
            with urllib.request.urlopen(URL + '?' + q, timeout=90) as r:
                return json.load(r)
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise last

def api_post(action, row):
    body = json.dumps({'action': action, 'tab': 'Transactions', 'id': row['id'], 'row': row}).encode()
    for i in range(4):
        try:
            req = urllib.request.Request(URL, data=body, headers={'Content-Type': 'text/plain'})
            with urllib.request.urlopen(req, timeout=90) as r:
                res = json.load(r)
            if res.get('ok'):
                return True
            raise Exception('server refused: %s' % json.dumps(res)[:120])
        except Exception as e:
            if i == 3:
                raise
            time.sleep(2 * (i + 1))

def bank_of(desc):
    d = desc or ''
    dl = d.lower()
    if re.search(r'authorized on|recurring transfer|online transfer|atm withdrawal|'
                 r'bill pay|mobile deposit|tnxi payroll|paypal|money transfer|'
                 r'monthly service fee|balance on|overdraft|debit card purchase|'
                 r'\bpos purchase\b|checkcard|zelle to', dl):
        return 'WF'
    if d and len(d.strip()) > 8 and d == d.upper() and re.search(r'[A-Z]{2,}', d):
        return 'CapOne'
    return None

def wf_label(desc):
    m = re.search(r'x{2,}(\d{3,4})', desc or '', re.I)
    if m:
        return 'Wells Fargo ' + 'x' * (len(m.group(0)) - len(m.group(1))) + m.group(1)
    m = re.search(r'\bcard\s*\d{4}', desc or '', re.I)
    if m:
        return 'Wells Fargo ' + ' '.join(m.group(0).split()).title()
    return 'Wells Fargo'

def main():
    rows = api_get({'action': 'list', 'tab': 'Transactions'})['rows']
    log('fetched %d rows' % len(rows))
    plan = []   # (row_id, new_payment_method, desc)
    for r in rows:
        if r.get('txn_type') != 'expense':
            continue
        if (r.get('payment_method') or '').strip() not in ('', 'Other'):
            continue
        desc = r.get('merchant') or r.get('description') or ''
        bank = bank_of(desc)
        if bank == 'CapOne':
            plan.append((r['id'], 'Capital One', desc))
        elif bank == 'WF':
            plan.append((r['id'], wf_label(desc), desc))
    from collections import Counter
    counts = Counter(pm for _, pm, _ in plan)
    log('plan: %d expense rows to tag' % len(plan))
    for pm, n in counts.most_common():
        log('  %s: %d' % (pm, n))
    for rid, pm, desc in plan[:15]:
        log('  sample: %-28s %s' % (pm, desc[:60]))
    if not APPLY:
        log('dry run only; rerun with --apply to write')
        return
    ok = fail = 0
    def one(item):
        rid, pm, _ = item
        r = next(x for x in rows if x['id'] == rid)
        if (r.get('payment_method') or '').strip() not in ('', 'Other'):
            return ('skip', rid)
        r['payment_method'] = pm
        try:
            api_post('update', r)
            return ('ok', rid)
        except Exception as e:
            return ('fail', rid, str(e)[:100])
    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, res in enumerate(ex.map(one, plan), 1):
            if res[0] == 'ok':
                ok += 1
            elif res[0] == 'fail':
                fail += 1
                log('FAILED %s: %s' % (res[1], res[2]))
            if i % 50 == 0:
                log('progress %d/%d' % (i, len(plan)))
    log('done: %d ok, %d failed' % (ok, fail))

if __name__ == '__main__':
    import urllib.parse
    main()
