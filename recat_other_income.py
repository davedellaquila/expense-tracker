#!/usr/bin/env python3
"""Recategorize expense-typed 'Other Income' transactions to 'Uncategorized'.

Leftover from the PDF import fix (rows reclassified income->expense kept the
'Other Income' category). Only touches rows with txn_type != 'income'.
Income-typed 'Other Income' rows are correct and are left alone.

Tax handling: the 'Other Income' category's default tax_category is ''.
Rows whose tax_category equals that default (or is empty) get tax_category=''
(the Uncategorized default); any other value is preserved.
"""
import json, time
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from concurrent.futures import ThreadPoolExecutor

URL = "https://script.google.com/macros/s/AKfycbzUQJ2Kjuu5-udsVZO49fQ4Mb89JyrhKETIIyjW-HPqC4Upv3F2XMzksg3uzk2cmQR8cg/exec"
LOG = "/home/hatch/workspace/expense-tracker/recat_other_income.log"

sess = requests.Session()
retry = Retry(total=8, backoff_factor=3, status_forcelist=[500, 502, 503, 504],
              allowed_methods=['GET', 'POST'])
sess.mount('https://', HTTPAdapter(max_retries=retry))
sess.headers.update({'Accept-Encoding': 'gzip, deflate',
                     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'})

def log(msg):
    line = '%s %s' % (time.strftime('%H:%M:%S'), msg)
    print(line, flush=True)
    with open(LOG, 'a') as f:
        f.write(line + '\n')

def api_get(params, tries=4):
    last = None
    for a in range(tries):
        try:
            r = sess.get(URL, params=params, timeout=120)
            r.raise_for_status()
            j = r.json()
            if j.get('ok'):
                return j
            last = j.get('error')
        except Exception as e:
            last = str(e)[:160]
        log('list fetch attempt %d failed: %s' % (a + 1, last))
        time.sleep(4 * (a + 1))
    raise RuntimeError('list fetch failed: %s' % last)

def api_post(body, tries=4):
    for a in range(tries):
        try:
            r = sess.post(URL, data=json.dumps(body),
                          headers={'Content-Type': 'text/plain'}, timeout=120)
            j = r.json()
            if j.get('ok'):
                return True
            last = j.get('error')
        except Exception as e:
            last = str(e)[:160]
        time.sleep(3 * (a + 1))
    return 'ERR %s' % last

def main():
    cats = api_get({'action': 'list', 'tab': 'Categories'})['rows']
    oi = [c for c in cats if c.get('name') == 'Other Income']
    oi_default_tax = oi[0].get('tax_category') if oi else ''
    log('Other Income category default tax_category=%r' % oi_default_tax)

    rows = api_get({'action': 'list', 'tab': 'Transactions'})['rows']
    log('fetched %d transaction rows' % len(rows))

    targets = [r for r in rows
               if r.get('txn_type') != 'income' and r.get('category') == 'Other Income']
    log('%d expense-typed Other Income rows to recategorize' % len(targets))
    if not targets:
        return

    ok, failed = 0, []

    def do(r):
        row = dict(r)  # full-row JSON: backend updates replace entire rows
        row['category'] = 'Uncategorized'
        cur_tax = row.get('tax_category') or ''
        # keep expenses out of income tax buckets; preserve deliberate values
        row['tax_category'] = '' if cur_tax in ('', oi_default_tax) else cur_tax
        res = api_post({'action': 'update', 'tab': 'Transactions',
                        'id': r['id'], 'row': row})
        desc = (r.get('merchant') or r.get('description') or '')[:50]
        return (r['id'], r.get('date', '')[:10], r.get('amount'), desc, res)

    with ThreadPoolExecutor(max_workers=4) as ex:
        for i, (rid, date, amt, desc, res) in enumerate(ex.map(do, targets)):
            if res is True:
                ok += 1
            else:
                failed.append(rid)
                log('FAILED %s %s %s (%s): %s' % (rid, date, amt, desc, res))
            if (i + 1) % 10 == 0:
                log('progress %d/%d' % (i + 1, len(targets)))

    total = sum(float(r.get('amount') or 0) for r in targets)
    log('done: %d ok, %d failed, $%.2f moved' % (ok, len(failed), total))
    if failed:
        log('failed ids: %s' % ','.join(failed))

if __name__ == '__main__':
    main()
