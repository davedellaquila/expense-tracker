# Changelog

Running record of what ships in the expense tracker, kept for future
documentation. Newest first.

## 2026-09-30

### Budget page: bot card buttons aligned to the bottom
- The Budget Bot and Income Bot cards are now flex columns with their
  "Propose" buttons pinned to the bottom, so the buttons line up even
  though the intro text is different lengths.

### Budget page: live totals pill + real-time bars while dragging
- The sticky month bar at the top now carries a live totals pill: total
  budget vs total income target, plus the budget as a percentage of
  income (turns red when the budget exceeds the income target).
- Dragging a budget/target slider now repaints its row in real time: the
  "$spent of $budget" header, the spend-vs-budget bar (goes red when
  over), and the share-of-total bar all follow the drag before anything
  is saved. The totals pill updates too. Income target rows behave the
  same way.

### Budget page: each bar labeled directly
- Every row now labels its bars in place: "Spent vs monthly budget" above
  the green bar, "Share of total budget · 24% of $17,455" above the blue
  one (income rows read "Received vs monthly target" / "Share of total
  income target"). The card-top legend was removed as redundant.

### Budget page: bot cards side by side, row dividers
- Budget Bot and Income Bot cards now sit next to each other horizontally;
  on iPhone they stack vertically as before.
- Category rows in the budget/income cards (and the Reports Budget vs
  Actual card) are separated by divider lines, so it's clear where one
  category ends and the next begins.

### Budget page: drag sliders + clearer cards
- Category budgets and Income targets rows now set the amount with a drag
  slider synced to a compact number box: drag for speed, type for precision,
  then Save. The old full-width inputs (with spinner arrows) are gone.
- Each card now explains its two bars up top: green = spent/received vs this
  month's budget/target; blue = that budget's share of the total budget.
- Amount controls are labeled ("Budget:" / "Target:") so it's obvious which
  row you're editing.

### Import log: rename accounts, delete statements
- Account groups on the Import page have a Rename link, so cryptic imported
  names ("xxxxxx8345") can get readable labels. Renaming applies to every
  statement in that bank/account group and syncs to other devices.
- Each statement row has a Delete button (with confirmation): it removes the
  entry from the import history and deletes its stored file copy from
  Firebase Storage. Imported transactions are left untouched.
- Deletes are tombstoned and synced, so a delete on one device can't be
  resurrected by another device's stale copy. Clear history tombstones too.

### Floating add button is translucent
- The floating + button background is now 85% opaque, so content behind it
  shows through. The + itself stays fully white.

### Delete confirmations are red
- Confirmation dialogs now use a red button for destructive actions labeled
  Delete (they used to be green for every custom label). Non-destructive
  confirmations (Sign in, Proceed, etc.) stay green.

### Home category filter now applies to transfers
- The Transfers donut in Category Mix used to ignore the Home category
  filter (transfers always passed), so it showed every transfer in the
  period while the Transactions page (Type + Category must both match)
  correctly showed none. Transfers are now filtered by their own category,
  matching the Transactions page.
- Fixed the related drill-through bug: tapping a Transfers donut slice or
  its title carried the Home category selection into the Transactions
  category dropdown, which then conflicted with the drill's own category
  and showed zero transactions. The title/center drill now carries the
  donut's actual transfer categories, so it shows exactly what the donut
  showed (an empty donut drills to an empty list, not all transfers).
### Footer tooltip delay
- Tab-bar buttons now use a custom tooltip with a 1000ms hover delay
  (native title timing isn't controllable; was 500ms). Mouse-only; touch
  taps still navigate immediately.
- Fixed the tooltip overflowing the screen edge: its position is now
  clamped using its real rendered width.

## 2026-09-29

### Sheet drag-to-resize + longer tab tooltips
- Bottom sheets can now be resized by dragging the thumb at the top: the
  bottom edge stays put, the sticky footer stays pinned, and content slides
  behind it. Clamped between a collapsed peek and 92% of the viewport;
  dragging down never dismisses (Cancel / tap-outside / Esc still do).
- Tab-bar tooltips now carry a slightly longer description of each tab
  plus its 1–8 keyboard shortcut.

### Toast ghost + tooltips
- Fixed the toast's brief ghost at the bottom of the screen: dismissing no
  longer strips its position class mid-fade, so it fades out in place.
- Tooltips: Bulk update link buttons (dynamic: describes the mode, flips
  to "Exit bulk update mode" while active), all 8 tab-bar icons (with
  their 1–8 keyboard shortcuts), and the add-transaction + button.

### Filter card Reset position
- Reset moved to the bottom-right edge of the Transactions filter card
  (mirrored in the floating sticky card).
- Reset's tooltip notes the Esc keyboard shortcut does the same thing.
- Esc now also activates a dialog's Done button, not just Cancel.

### Bulk update bar animations + Undo rules
- The bar now appears with a soft fade/rise when Bulk update is tapped.
- When the Update button's label changes width (count changes, or it
  becomes "Undo Bulk Update"), All/Clear and Delete glide to their new
  positions instead of jumping (FLIP animation; skipped under
  prefers-reduced-motion).
- "Undo Bulk Update" now stays until any change to the selection: row
  toggles, All/Clear, any filter/sort/search change, Reset, drill
  changes, or closing bulk mode.

### Sticky card transition
- The floating sticky card now fades and slides in/out instead of popping
  when the filter card scrolls off/on screen. The bulk update bar fades
  along with it when docking/undocking. Respects prefers-reduced-motion.

### Filter card + Done pill polish
- The Done pill in bulk update mode is roomier (more background around
  the label).
- Less white space at the bottom of the Transactions filter card.

### Bulk update bar polish
- The Update button reads "Update 0 transactions" with no ellipsis when
  nothing is selected; the ellipsis appears once rows are selected.
- More space between the Delete button and the dismiss ✕ at the bar's
  right edge, to avoid mis-taps.

### Bulk update bar docks into the sticky card
- While bulk update mode is on and the floating sticky card is visible
  (filter card scrolled off-screen), the bulk update bar docks into the
  sticky card as an attached section instead of scrolling away with the
  page. One node is moved between the two homes, so all buttons and state
  keep working.

### Bulk update mode affordance + tighter filter card
- The Transactions filter card's bottom margin is reduced so the bulk
  update toolbar sits tight beneath it.
- The Bulk update/Done toggle now gets an active pill background while
  bulk update mode is on, in both the filter card and the sticky clone.

### Bulk update bar: Update button doubles as Undo
- Removed the selection count and the standalone Undo button.
- The Update button now reads "Update N transactions…" (with ellipsis).
- After a bulk update completes, the Update button becomes "Undo Bulk
  Update"; selecting any row switches it back to the Update button. The
  ✕/Done behavior is unchanged.

### Bulk update bar button layout
- Buttons rearranged into three zones: All/Clear (plus the selection
  count) on the left, Update centered, Delete/Undo and the dismiss ✕ on
  the right edge.

### Bulk update bar repositioned and restyled
- The bulk selection bar is no longer a floating bar at the bottom of the
  screen; it now sits in the page flow directly below the filter card and
  above the transaction list (in-flight bulk-job progress bars moved with
  it). The obsolete bottom-padding compensation is removed.
- Restyled as an editing-mode toolbar: blue accent edge, neutral "N
  selected" pill instead of red text, softer shadow, and a slimmer dismiss
  button.

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

### Home Bills card layout
- The Bills card is now two lines: "Bills" + "+ Add bill" on the first
  row, the overdue/due-this-week status on its own line below, so nothing
  scrunches together on iPhone.

### Budget drill carries the month
- Tapping a category on the Budget page now sets the Transactions period
  to the budget month selected in the sticky bar, instead of leaving the
  old period in effect.

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
