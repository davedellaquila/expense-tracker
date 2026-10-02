# Feature ideas

A parking lot for future expense-tracker features. Nothing here is scheduled —
it's where ideas wait until Dave says "build it."

**Adding an idea:** just tell Zuki "add _<idea>_ to the feature list" and it lands here.

## Proposed

- **Multiple storage backends + data connectors** (2026-09-29, Dave): allow saving
  and syncing to more than one storage system at the same time (not just picking
  one of This device / Google Sheets / Firebase). Build data connectors for
  Supabase, Airtable, and other popular database systems.
- **User documentation** (2026-09-29, Dave): write end-user docs for the app —
  how to import statements, categorize, use filters and drill-through, read the
  reports, manage budgets and bills — so anyone (e.g. Nancy) can learn it
  without a walkthrough.
- **Better app name** (2026-09-29, Dave): think about a better name for the app
  than "Expense Tracker".
- **Track merchant details** (2026-09-29, Dave): a dedicated place to keep notes
  and details for each merchant.
- **Test CSV import** (2026-10-01, Dave): try out the CSV importer — e.g. a
  built-in sample CSV or a dry-run mode that previews the import without saving
  anything.

## Completed features

Everything built so far, grouped by area (late Sep 2026). The Google Doc is the
live copy of this list.

### Transactions
- Full add/edit form: full-width fields, auto-growing merchant/description,
  compact date picker.
- Filter card: search, category dropdown, type, bank, period presets + custom;
  two-column layout on iPhone.
- Sort menu in the filter card and in the sticky search bar, kept in sync.
- Floating sticky search bar appears on scroll, with Bulk update / Tidy / Reset
  shortcuts.
- Chart drill-through starts from a clean slate: previous filters are cleared first,
  then a dismissible filter pill holds the drill context (temporary);
  single-category drills also set the category dropdown.
- Select mode with floating action bar: bulk update (bank, merchant name), bulk
  delete with undo.
- Tidy merchant names: editable suggestions, applied in bulk.
- Export transactions to CSV: exports the filtered list with all fields,
  spreadsheet-ready.
- Split a transaction across multiple categories: each part gets its own
  category and amount; the parts must add up exactly to the original amount.
- Data cleanup: strip statement headers/boilerplate and Wells Fargo debit-card
  prefixes from merchants, with preview.

### Home
- Income / Expenses / Net tiles (whole dollars), tappable for drill-through.
- Sticky filter-summary tile appears when the filters scroll off-screen (tap
  jumps back to the filters).
- Category Mix donut + table, tappable; Income listed above Expenses.
- Category chips: multi-select filter for the whole page ("All" clears).
- Bills card: overdue and due-this-week at a glance; "+ Add bill" button opens
  the bill form right from the home page.
- Chart cards: add/remove, drag to reorder, order saved.

### Reports
- Summary tiles (Income, Expenses, Net, Avg/month) tappable: each opens
  Transactions filtered to that tile's data, carrying the report filters.
- Sticky filter-summary panel appears when the filters scroll off-screen (tap
  jumps back to the filters).
- 18 chart cards: monthly trend, weekday pattern, top merchants, category mix
  donut, monthly category bars (each month's categories side by side),
  transaction size bands, owner split (Dave/Nancy), card split by bank,
  category volume, average ticket, category spend trend, owner vs category,
  spend Pareto, category x month heatmap, budget vs actual, income by category,
  largest expenses.
- Category chips multi-select: each selected category renders as its own colored
  series with a legend.
- Every chart element clickable, drilling into the transactions behind it.
- Chart cards: add/remove, drag to reorder via grip, order saved per page;
  re-added charts land at the bottom.
- Collapsible category picker (state saved).
- Largest expenses card: merchant prominent, description below, both wrap so
  Category and Amount stay visible on iPhone.

### Budget
- Budget Bot: monthly proposals per category with locks, YTD averages,
  paycheck-only income detection.
- Recurring bills floor the proposals; warns when bills + budget exceed income.
- Sticky summary pill: proposed total, percent of income, expected income.

### Bills
- Bills tab: month calendar with bill dots (red = overdue), tap-a-day details,
  upcoming list with badges.
- Add/edit bills (name, amount, due date, recurrence, category, account, notes);
  mark paid with optional transaction creation (off by default); recurring bills
  advance with month-end clamping; delete with confirmation.

### Import
- In-browser CSV + PDF statement import with auto-categorization and duplicate
  detection.
- Transfer auto-detection: "Transfer" in the description imports as a transfer,
  not income/expense.
- Credit-card cash back imports as separate income rows (uncheckable in preview).
- Citi AAdvantage parser: strips rewards boilerplate, cardholder headers, sale
  dates.
- Apple Card boilerplate scrubber.
- Import log: 100 statements grouped by bank, then account, with month
  backfill; original files kept in Firebase Storage with View buttons.

### Scanners
- On-device bill scanner (nothing uploaded): pre-fills biller, amount, due date.
- On-device receipt scanner: pre-fills merchant, total, date.
- Verify-before-save always; scanned photos retained.

### Sync & storage
- Firebase (Firestore) backend with multi-device sync; Google Sheets and
  on-device options.
- Signed-in status card in Settings with sign-out beside it.
- Setup → Categories: rename any category (collisions offer merge or a unique
  name) or delete it (merge into another category or move everything to
  Unassigned); transactions, budgets, planner state, filters, and drill pills
  follow.
- Robust sign-in migration (fixed the stale anonymous identity bug).

### General
- Filter selections persist across page reloads (Transactions, Reports, Home,
  Budget month); search text and the drill pill stay transient by design.
- Icon bar order: Home, Transactions, Reports, Import, Budget, Bills, Tax, Setup.

## Shipped

_(Ideas move here with the date they went live.)_

- Export transactions to CSV (2026-09-29).
- Split a transaction across multiple categories (2026-09-29).
- "+ Add bill" button on the Home page Bills card (2026-09-29).
