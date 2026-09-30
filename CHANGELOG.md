# Changelog

Running record of what ships in the expense tracker, kept for future
documentation. Newest first.

## 2026-09-29

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
