# Changelog

Running record of what ships in the expense tracker, kept for future
documentation. Newest first.

## 2026-09-29

### Budget vs Actual category filter
- The Home page's Budget vs Actual card now also respects the selected
  categories at the top of the page, matching the Reports behavior: with
  categories selected it shows only those budgeted categories; a selected
  budgeted category with no transactions still shows with $0 actual; if none
  of the selected categories has a budget it says "No budgets for the selected
  categories."

### Budget vs Actual drill-through
- Tapping a category row (or the Total row) in the Home page's Budget vs
  Actual card now opens the matching transactions, like the other Home
  charts. Rows show a pointer cursor on hover and work with the keyboard
  (Enter/Space).

### Chart drill-through audit
- Audited every chart on Home, Reports, Budget, and Tax: all chart
  elements now drill into their transactions. Fixed the two that didn't:
  the Home "Transaction Size Bands" bars (drill to the amount range) and
  the Home "Owner Split" donut slices (drill to that owner's expenses).

### Budget page sticky month bar
- The month picker now lives in a sticky panel pinned under the app
  header, so it's always visible while scrolling the Budget page.
  (The redundant "Month" label was dropped; the input keeps an
  accessible name.)

### Layout
- New tablet tier (iPad): the content column widens to 1000px and bottom
  sheets to 880px, so the app uses the tablet's width instead of the narrow
  phone-width column, at full-size type. Applies to every iPad size, including
  large tablets (e.g. 12.9") that previously fell into the shrunken desktop
  zoom tier — that tier now applies only to fine-pointer (mouse/trackpad)
  screens 1200px and up.

### Home
- New Bank filter in the first row of the Home filters (Period, Account, Bank).
  All Home charts, stat tiles, and category chips respect it; it persists across
  reloads and appears in the sticky filter summary; tile and chart
  drill-throughs carry it to Transactions.
- Fixed: chart drills (e.g. Top merchants bars) went dead after the Bank filter
  was added — the drill function reads its context from shared dashboard data,
  which didn't include the new filter yet.

### Bulk update (Transactions)
- Fields reordered: Merchant name, Type, Account (Personal/Business), Category,
  Tax category, Payment method, Bank, Description, Notes.
- Type and Account are now segmented tab controls instead of dropdowns
  ("No change" selected by default).
- New Description field: set a new description across the selected transactions
  (blank = no change).
- The Done button exits bulk-update/select mode; Cancel still resets the
  Transactions filters.

### Bills
- Upcoming bills redesigned as professional tiles: separate rounded tiles with
  border, soft shadow, clipped full-height proportional color wash; two-line
  layout (name / due date / amount, then category + days-left countdown + Paid).
- Tile fill shows amount relative to the most expensive active bill
  (most expensive fills the whole tile).
- Fill color shows urgency: red for due soon, transitioning through yellow to
  green for the furthest-out bill.
- Each bill shows a prominent days-until-due countdown ("6 days left",
  "due today", "3 days overdue"), colored with the same urgency hue.
- Due dates sit in a fixed-width vertically aligned column.
- Mark-paid sheet redesigned.

### Keyboard
- Shift+Return activates the primary button (Save, Add, Apply, Delete,
  Mark paid, Use these details) in the topmost open sheet.
- Plain 1–8 jumps between tabs (Home 1 … Setup 8); Cmd/Ctrl+Shift+1–8 is a
  modifier variant (browsers reserve Cmd+1–8 for their own tabs).
- Escape cancels the topmost open sheet; during bulk-update mode it exits that
  mode; on Transactions with nothing open it resets the filter card.

### Reports
- New Bank filter on the same row as Period and Account. All report charts,
  tables, and stat tiles respect it; it persists across reloads, appears in
  the sticky filter summary and report subtitle; chart drill-throughs carry
  it to Transactions.
- Budget vs Actual table: tapping a column header (Category, Budget, Actual,
  Variance, % of budget) sorts by that column; tapping again flips direction.
  The Total row stays pinned at the bottom.
- Budget vs Actual budgets now scale to the report period: each category counts
  at its monthly average × the number of months in the period, so a September-only
  budget shows 3× on a 3-month report instead of one month against three months
  of actuals. Applies to the Home budget card too.
- Income by category table gained a % of total column.
- Budget vs Actual now honors the selected categories even when a selected
  category has no transactions in the period: previously the selection was
  silently pruned (e.g. combined with the bank filter) and the chart reset to
  all budgeted categories. Selecting categories with no budgets shows an
  honest "No budgets for the selected categories" empty state.

### Transactions
- Export CSV button: exports the filtered, sorted list with all fields,
  spreadsheet-ready.
- Split a transaction across multiple categories (parts must sum exactly to
  the original; original row is replaced).

### Home
- New Largest expenses chart card (top ten expenses for the selected period).
- Card Split donut now drills to Transactions using the selected bank.
- Bills card gained a + Add bill button.

### Feature list
- New ideas: Track merchant details, Export transactions to CSV,
  better app name, user documentation.

### Scanners
- Re-scanning a bill or receipt rolls back what the previous scan set instead
  of leaving stale values; the old payment-info block is replaced, not doubled.
- Bill scanner extracts where-to-pay info and payment instructions into Notes.

### Setup / misc
- Setup → Firebase tab has an "Open Firebase console" link.
- Desktop type ~30% smaller (zoom .56); dropdown menus sized to match.
- Selected footer tab shows an accent-faint rounded pill, not just colored icon.
- Mac desktop icon: rounded squircle with transparency + subtle green gradient.
