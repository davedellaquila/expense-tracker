# Changelog

<!-- Version convention: under each ## date, add ### App YYYYMMDDHHMM (UTC) matching
     APP_VERSION / version.json for that deploy, newest first. "See what's new" shows
     every ### App block newer than the tab's running APP_VERSION (skipped builds grouped). -->

## 2026-10-03
### App 202610031513
- Tax: new **Business income** card showing business income by category (with counts and totals), plus its own Download CSV. Tapping a row drills into those transactions.
### App 202610031507
- Tax: fixed blank **CPA report PDF** — the report is now rendered visibly in the page (html2canvas can't capture off-screen elements) before generating the PDF.
### App 202610031505
- Tax: **CPA report (PDF)** now generates and downloads a real PDF file (`tax-summary-YYYY.pdf`) instead of relying on the print dialog, which silently fails in the iPhone home-screen web app. Falls back to print on desktop if the PDF library can't load.
### App 202610031454
- Tax: new **CPA report (PDF)** button — prints a clean summary for your CPA with business/personal income and deductions as category totals (no transaction detail), plus a totals box. Save as PDF in the print dialog; the CSVs still carry transaction detail.
### App 202610031406
- Tax: category amounts are now plain weight; only the Total is bold.
### App 202610030642
- Appearance Customize → Color: **Apply** (and tap the hex) uses the swatch’s current color without reopening the picker.
- Max Headroom Stripes card: angle can **animate continuously** between lower/upper limits (plus period); fixed angle when Animate is off.
- iPhone: page backgrounds stay **viewport-fixed** while content scrolls (same as desktop) — static fills use a fixed plate; dynamic `#bg-dynamic` no longer uses negative z-index.
- Max Headroom editor **locks its open height** so layer pills don’t move the top edge; drag the grab handle to see more.
### App 202610030437
- Settings: background preset swatches are now hardcoded HTML (no JS rendering) — they should appear on all devices.
### App 202610030433
- Settings: background swatches use setAttribute for styles (another attempt at iPad rendering).
### App 202610030351
- Settings: background preset swatches now force their backgrounds with !important to override any theme CSS.
### App 202610030348
- Settings: build stamp now shows just the last 4 digits (HHMM) — the only part that changes during the day.
### App 202610030347
- Settings: build stamp now formats the version as YYYYMM-DDHHMM (e.g. 202610-030347).
### App 202610030344
- Settings: the build stamp at the bottom now shows the actual app version number, so you can verify what version you're running.
### App 202610030340
- Settings: collapse button triangle is now 50% smaller (button stays the same size).
### App 202610030333
- Max Headroom wireframe preset now rotates the grid planes (slow oscillation, like the OG) in addition to scrolling.
### App 202610030331
- AI background is now real AI image generation (via Pollinations): describe the image, preview it, then use it as your background or save it to My backgrounds. The old keyword-to-pattern matcher is gone.
### App 202610030326
- Settings: the card collapse button now sits at the far right of the header, outside any card controls (e.g. after Data cleanup's Scan button).
### App 202610030324
- What's New button pulse is now more noticeable (larger scale + glow) when an update is available.
### App 202610030322
- Settings: the card collapse button is now 48px with a stronger background and bolder chevron — much easier to see and tell what it is.
### App 202610030318
- Settings: background preset swatches are larger (44px) with a visible border in both themes, so the colors/patterns are actually perceptible.
### App 202610030316
- Settings: the Side margins slider now works on iPad/tablet too (was desktop-only).
### App 202610030315
- Settings: the collapse chevron is now a 44px round button with a larger symbol, matching the other round buttons' press animation.
## 2026-10-02
### App 202610022356
- Settings: cards are now collapsible too — tap the chevron in any card header to collapse/expand it. Collapsed state is saved on this device.
### App 202610022355
- Settings: cards can now be rearranged by dragging the ⋮⋮ grip in each card header. Order is saved on this device.
### App 202610022341
- Charts: text now stays a fixed readable size regardless of content width — no more tiny labels when side margins are large.
### App 202610022334
- Settings → Appearance: new "Side margins" slider controls the left/right margin of the content on wide desktop screens (default 100px, up to 300px), so the page background shows through. Saved on this device.
### App 202610022330
- Budget: the "Prev month" stat now shows last month's budget (not actuals); tapping it copies that budget into the current month.
### App 202610022328
- Bill scan: scanned values only fill blank fields — if you've already typed a name, amount, or changed the due date, the scan won't overwrite them. Re-scanning also won't wipe edits you made to previously scanned values.
### App 202610022351
- Max Headroom Grid card: plane rotation can **animate continuously** between a **lower** and **upper** limit (plus period). Fixed rotation remains when Animate is off.
### App 202610022340
- Max Headroom editor: **layer pills** (`.catchip`) — All / None / Grid / Scanlines / Stripes / Glitch / City·shapes / Ambient. Enabled pill shows that layer’s settings card; disabled hides the card and turns the layer off in live preview.
- Always-visible **Colors** + **Motion** cards above the pills; Grid card holds rotation, vanishing point, VP motion, and randomness.
### App 202610022330
- Max Headroom editor: **Esc** dismisses via Cancel when present, else `overlay._dismiss` (same as ✕ / tap-outside) — sticky footers no longer block Esc.
- Max Headroom editor: sticky stacking — fixed **sheet-head** (title + ✕) above sticky **Live preview** caption/stage; controls scroll underneath; ✕ never over neon artwork.
- Max Headroom editor: footer uses `btnrow stickybar` — Apply (`.btn.small`), Save & apply / Reset defaults / **Cancel** all `.btn.small.ghost` (Cancel no longer a link).
- Max Headroom: layer master **All layers off/on**; ambient glow / horizon / vignette / chroma gated; grid plane rotation, vanishing-point X/Y + motion + randomness; all-off = static base color only.
- Appearance: **AI background…** — on-device keyword→MH recipe (e.g. asteroid field), preview, Apply / Save & apply into My backgrounds.
### App 202610022220
- Max Headroom editor: sticky in-dialog **Live preview** (~200px) using the same `mh-custom` layers/CSS vars — updates on every slider change (page bg still live-updates too).
- Header **Hi, Name** chip is tappable — opens “Who’s entering?” to rename (Dave/Nancy quick picks + field); saves via the same path as Settings.
### App 202610022216
- Max Headroom editor: sticky in-dialog **Live preview** (~200px) using the same `mh-custom` layers/CSS vars as the page bg — updates on every slider change.
### App 202610022210
- Appearance: polished **Customize** block (Color / Picture / Editor rows) plus **My backgrounds** library with Apply, Export, Copy share code, Delete, and Import.
- Appearance: portable `.expensebg.json` share format (recipe-first; optional image data with size guard) + paste share-code import.
- Appearance: **Max Headroom editor** — layered CRT engine (`mh-custom`) with live sliders for colors, grid, scanlines, stripes, glitch, city/shapes, intensity/speed/vignette/chroma, and freeze; Save & apply into My backgrounds.
### App 202610022155
- Settings → Appearance: redesigned background card — Subtle/Medium/Bold intensity tabs (one panel at a time), labeled swatch rows, compact tool tiles (color / picture / editor), Motion & effects in a collapsed `<details>`, uniform swatches with a calm accent ring.
### App 202610022140
- Settings → Data storage: auth row cleaned up — Sign in primary; Create account / Continue with Google use opaque light ghost fills (no page-bg bleed); Forgot password on its own quiet line.
- Appearance: decorative backgrounds paint via `--page-bg` so theme chrome (`--bg` / ghost buttons / chips) stays readable on white cards over bold solids, journeys, and Max Headroom.
- Appearance: **Dynamic gradients** presets (Aurora blobs, Mesh shift, Sunset flow, Conic spin, Wave wash, Candy march) — CSS animations, reduced-motion static.
- Appearance: **Background editor** — compose solid/gradient + optional pattern; save/apply/delete customs; optional **Animate gradient** toggle.
### App 202610022118
- Appearance: Subtle / Medium / Bold preset ranges; Mac-style picture upload (Size to fit + Repeating); Max Headroom contrast fix (dynamics don’t overwrite `--bg`); new **Motion · Journeys** dynamics — space fly-through, aerial mountains, aerial ocean, mountain road.
### App 202610022114
- Max Headroom: CRT neon stage no longer overwrites `--bg` — ghost buttons (Create account / Continue with Google) and other card chrome keep light-theme contrast on white cards.
### App 202610022109
- Max Headroom backgrounds: darker CRT stage, hotter cyan/magenta/yellow neon, faster grids/scanlines/stripes/glitch/geometry; dynamics work in any theme (solids/gradients/patterns stay light-only).
### App 202610022106
- Settings → Appearance: new **Dynamic · Max Headroom** backgrounds (CSS-only) — wireframe grid, CRT scanlines, neon stripes, soft glitch, and city-pulse geometry. Light mode only (same as other page backgrounds); reduced-motion shows a static fallback; animations pause when the tab is hidden.
### App 202610022104
- Ship: Home category chips + Upcoming Bills polish, Settings rename/appearance/compact layouts, trash vs circle-✕ affordances, What’s New (header control, pulse, scroll lock, sticky Load new version only when an update exists), and desktop chart labels ~16–18px.
### App 202610022058
- What’s new: hide “Load new version” when you’re already on the latest logged build (header browse); still show it when an update is detected or there are newer changelog entries.
### App 202610022049
- What’s new: fix scroll — panel was parked off-screen after page scroll (sticky header rect went negative under overflow lock). Now uses a fixed body lock, viewport-safe positioning, and one scrollable panel body with sticky “Load new version” so Earlier changes scroll inside the dialog.
### App 202610022039
- What’s new panel: Expanding Earlier changes scrolls inside the dialog (page behind locked); sticky button label is “Load new version”.
- Header What’s new: slow pulse while an update is available; clears when opened from the header, banner dismissed, or new version loaded. Respects reduced-motion.
- Desktop/tablet chart labels: CSS sizes account for SVG viewBox scaling so labels land ~16–18px on wide screens.
### App 202610022034
- Desktop/tablet charts: SVG labels capped around 16–18px via CSS so wide screens don’t blow up user-unit text; phone chart label sizing unchanged.
### App 202610022033
- Header: lasting “What’s new” control (next to the user chip) opens the changelog panel anytime — without forcing the update banner; real updates still show the blue banner and auto-open the panel.
### App 202610022029
- What’s new panel: Refresh is a centered sticky strip between the scrollable “new since your version” list and Earlier changes (not lost when recent notes are long). Banner stays title + circle dismiss only; ≥30px gap under the blue bar.
### App 202610022023
- Update banner is slimmer (title + circle dismiss only); What’s new auto-opens with Refresh between “new since your version” and Earlier changes; panel sits with a gap under the banner; panel close is an animated circle ✕ (banner stays until its own dismiss).
### App 202610022017
- Clarified remove affordances: soft-red trash = delete data (bills, categories, split parts, planners); Home/Reports chart hide is a small circle ✕ again, with the same grow+fade press-out as sheet close.
### App 202610022015
- Data-delete ✕ controls use the shared soft-red trash chip (Settings categories, Budget/Income planner remove-category, split remove-part). Close/dismiss ✕ unchanged.
### App 202610022012
- Update banner: What’s new opens automatically the first time a newer version is detected; closing the panel (Esc / ✕ / scrim) leaves the banner up, and focus checks don’t re-open it — use “See what’s new” to peek again.
### App 202610021957
- Delete bill? confirm sheet: more space under the payee/amount line before Cancel/Delete; uses a plain button row (not stickybar) so short confirms don’t dock tight against the text.
### App 202610021941
- Bills delete controls (Home Upcoming Bills, Bills tiles, Paid list): unified soft-red `.row-del` chip with a trash-can SVG instead of mixed ghost ✕ styles.
### App 202610021911
- Settings → Appearance: page backgrounds expand beyond solids — more solid swatches, CSS gradients, subtle patterns (dots/grid/paper/diagonals/mesh), plus an explicit Custom color picker; light mode only; cards stay opaque for readability.
- Settings → Data cleanup: “Scan for statement junk” is a compact header-row button (title left, button right), matching Who’s entering? / Upcoming Bills.
### App 202610021858
- Settings → Data storage: Firebase auth actions are compact (Sign in primary; Create account / Google as small ghosts; Forgot password + Download backup as quiet links) instead of oversized full-width blocks.
- Settings → Who's entering?: Save name sits beside the name field on one row (stacks on very narrow phones).
- Update banner What’s new: shows everything newer than the version you’re running (skipped builds grouped), with earlier history collapsed; CHANGELOG now uses `### App YYYYMMDDHHMM` markers tied to APP_VERSION.
### App 202610021832
- Settings (formerly Setup tab): Appearance now includes a background color picker, a few presets, and Reset to default — saved on this device and applied in Light mode via `--bg`.
- Tab bar: the Setup tab is renamed to Settings (internal screen id unchanged).
- Update banner: “See what’s new” is now a clear outlined button (was an easy-to-miss underline link), with subtitle “See what’s changed, then refresh when you’re ready.”
- Update banner: new What's new control opens a lightweight panel with the newest CHANGELOG sections (fetched live); Esc, ✕, or tap outside closes it without blocking Refresh / Dismiss.
- Home Upcoming Bills: each row now has a delete ✕ next to Paid (same confirm + delete path as the Bills page).
- Home Upcoming Bills: adding, editing, or deleting a bill from Home now refreshes the card immediately (was only re-rendering the Bills page).
- Home Upcoming Bills empty state now says "All clear! Yay!" (was "all clear").
- Round buttons (sheet ✕, selection-bar ✕, + FAB, search clear): press still grows to 1.5× and now fades to invisible in sync (150ms); sheet ✕ delays dismiss so the fade finishes as the sheet closes.
- Home Upcoming Bills: marking a bill Paid now refreshes the Home card so the bill leaves the list immediately (was only re-rendering the Bills page).
- Home Upcoming Bills card: lists bills due in the next 14 days (plus overdue), with name, due date, days-left, amount, and a Paid button — capped at 6 rows with a link to the full Bills page.
- Home (and Reports) category filter chips now include categories from the Categories list — so a category created via Add bill / Add transaction shows up immediately, even before any transaction uses it.
- Update banner: on window focus (and visibility), the app re-checks same-origin `version.json` + `index.html` (throttled) and shows the blue "new version" bar when the tab is stale — including after a git pull / file change without leaving the tab. Refresh reloads past the cache; Dismiss hides until a newer build appears.
- Add/Edit bill: the category menu now includes ＋ New category… (same as Add/Edit transaction) and saves the new category to the Categories list.
- Scan bill / receipt: new "Paste from clipboard" option (and ⌘V / Ctrl+V) runs the same on-device recognition as Choose photo — images and PDFs when the browser exposes them.
- Transactions: opening the page (including on load) no longer auto-focuses the search box — click or tap to type.
- Desktop: wide mouse/trackpad screens no longer apply `html { zoom: .56 }` (which shrank the 760px column into a tiny strip); full-size type with a wide content column (up to 1600px; sheets 1100px). iPhone and iPad/tablet tiers unchanged.
### App 202610021438
- Bills: redesigned bill cards — the name now wraps to two lines instead of truncating, and the due date moved into the meta line (category · account · due date), removing the wasted fixed-width spacer column.
### App 202610021404
- Reports: the Monthly Trend month table now fits all columns (Month/Income/Expenses/Net) on iPhone without sideways scrolling.
### App 202610021357
- Reports: grouped bar charts pack the month groups tighter (5% gap instead of 20%).
### App 202610021352
- Reports: the Expense report stat tiles are centered (removed the stale 4-column grid override).
### App 202610021345
- Reports: removed the Net tile from the Expense report summary cards.
## 2026-10-01
### App 202610020823
- iPhone: the parenthetical hints on the Transactions filter labels (Type, Account) are hidden; desktop still shows them.
### App 202610020816
- Sheet drag handle keeps its 42px line but the grab target is taller (45px) for easier finger drags.
- Round-button press grows the button itself to 1.5x in its own color (white ripple removed).
### App 202610020540
- Round-button press ripple is 25% smaller (1.5x diameter).
### App 202610020535
- Round-button press is now a white ripple: it appears instantly on press and fades quickly on release (replaces the grow effect).
### App 202610020532
- Sheet ✕ close button: fixed the top margin so it truly matches the right margin (the sticky offset was measured from below the sheet's padding, pushing the button down).
- Round buttons (sheet ✕, selection-bar ✕, + FAB, search clear ×) now grow 25% and brighten on press, easing back on release.
- Sheet ✕ close button is 50% bigger (45px) with equal margins on the top and right.
- Bills calendar header: the next-month › button now sits right after the month/year, with the monthly total alone on the far right.
- New Info tab (far right): shows the app version and renders this change log live from the repo — room to add documentation sections later.
- Pull-to-check-for-updates: dragging down from the very top of any screen runs the update check (same as the automatic one) — no sheet open, page scrolled to top.
- Bills calendar header now shows the month's total on the right, balancing the month title on the left.
- Transactions selection bar: Update and Delete now spread evenly across the space between Clear and the far-right ✕; Delete is the word "Delete" in white on red instead of the 🗑️ icon.
- Transactions search is now word-based AND: every word typed must occur somewhere in the record (text fields or amount). "Safeway Jackson" matches only records containing both words — no longer "Safeway Fuel".
- Delete buttons standardized on edit dialogs: the full word "Delete" everywhere except iPhone, which uses 🗑️ to save space (transaction form, bill form, delete confirmations, category delete).
- Every sheet now has a sticky ✕ in a circle at the top-right that closes it (same as Cancel/tap-outside) — it stays visible while the sheet scrolls, so no scrolling to find Cancel.
- Dragging the sheet's handle down far enough now dismisses the sheet (drag up still resizes).
- The transaction form's bill button re-checks when the bill sheet closes: if the bill was deleted it now reads "🔔 Create Bill Reminder" instead of the stale "Open bill reminder".
- iPhone: the selection bar's undo button now reads just 'Undo' (was 'Undo Bulk Update', which overlapped the neighboring buttons).
- iPhone: fixed unreachable sheet fields when the keyboard is open — the sheet's max-height now subtracts the keyboard height (dvh doesn't shrink with the keyboard, but the overlay is lifted by it, so tall sheets overflowed the top and the first fields couldn't be scrolled to). Drag-resize also restores the CSS max-height cap afterwards.
- iPhone: swipe right closes the topmost open sheet or dialog (same as tapping outside it); ignored when the gesture starts in a text field, on the grab handle, or moves mostly vertically.
- iPhone: the tab bar no longer glides up over page content when the keyboard opens — it stays behind the keyboard, so typing in Search no longer hides the results behind it.
- iPhone: all modal button bars are now static end-of-content rows — extended from the sheet sticky bars to the page-style bars docked in the bill form, scanner review, budget copy, and delete-bill sheets. Other platforms unchanged.
- iPhone: sheet button bars (bulk update, transaction form) no longer float — they're a static end-of-content row, since the floating panel could cover the focused field when the keyboard is open. Other platforms keep the floating bar.
- Transactions selection bar: Delete is now a 🗑️ trash can icon (narrower, so the single row no longer overlaps on iPhone); All/Clear no longer get squeezed under the Update button.
- Setup Categories: per-row delete is now the ✕ icon, matching the delete buttons used in the Bills list and budget planner (replacing the one-off 🗑️).
- Fixed: reloading the app while on the Setup tab left the Categories list empty — showing Settings now always refreshes the list, not just when the tab is tapped.
- Setup Categories: the per-row Delete button is now a 🗑️ trash can icon (with a "Delete category" label for accessibility).
- Transaction form: when the transaction already has a bill reminder, the "🔔 Add bill reminder" button becomes "🔔 Open bill reminder" and opens that bill's edit form (stacked, so unsaved transaction edits are kept).
- Tapping a transaction's 🔔 bell badge now jumps to the Bills page with the linked bill reminder scrolled into view and flashed, instead of opening the edit form (tapping the bill itself still opens the form).
- Transactions selection bar: tidied into a single row — compact "Update 3" count label, Delete still midway between Update and ✕, and Update/Delete are visibly disabled with nothing selected instead of toasting.
- Transactions: no longer auto-focuses the search box on iPhone (the popping keyboard covered the list); desktop and iPad keep the auto-focus.
- Largest expenses table: category names now wrap to multiple lines instead of truncating with an ellipsis, on both Home and Reports.
- Largest expenses table: amounts now show whole dollars with no cents (same formatting as the Home summary cards), on both Home and Reports.
- Largest expenses table: fixed the Category/Amount overlap on iPhone — long category names now truncate with an ellipsis inside their own column instead of spilling under the amount. Category column widened slightly (27%) to compensate. Applies on both Home and Reports.
- In-app update checker: the app now fetches version.json on launch, every 30 minutes, and whenever it returns to the foreground; when a newer build is deployed it shows a blue "A new version is available" banner with a Refresh button that reloads past the cache — no more deleting/re-adding the home-screen app to get updates.
- Income by category table: columns now size dynamically to the viewport (no more 640px minimum forcing sideways scroll) — all three columns visible on iPhone, on both Home and Reports.
- Category Bars: tapping an "Other" bar now labels the drill "Other" in the info card instead of expanding to the first underlying category ("Rent and Lease + 2 more").
- Home: Category Bars and Income by category are now Home chart cards too — every chart is available on both Home and Reports from here on; existing installs get the two new cards appended at the bottom.
- Bulk update: the Delete button now sits midway between Update and the ✕ done button on the selection bar.
- Bulk update: the "Update N transactions" dialog now puts the cursor in the Merchant name field on open.
- Setup: new Categories card — rename or delete any category. Rename collisions offer merging into the existing category or picking a unique name; delete offers merging into another category or moving everything to Unassigned. Transactions, budgets (all months), planner order/removed-memory/padlocks, saved filters, and the drill pill all follow the change.
- Reports: "Category Bars" reworked — each month now shows every category side by side (grouped vertical bars), top 7 categories + Other like the donut; tapping a bar drills into that month + category.
- Reports: "Category Bars" readability fix — with many categories it now shows the top 12 + a combined Other bar (tap Other to drill into its categories); crowded charts drop per-bar value labels and stagger x labels over two rows.
- Reports: new "Category Bars" chart — vertical bars comparing categories side by side (not stacked), with tap-to-drill like the other charts.
- Split sheet: tapping "+ Add part" auto-fills the new part with the remaining unallocated amount (when there is one).
- Sheets no longer dismiss when a text-selection drag slides off the dialog edge — only a tap that starts outside the dialog closes it, so edits are never lost this way.
- Bills: new "Every 6 months" option in the Repeats menu.
- Transactions: switching to the tab now puts the cursor in the search box (the floating clone if the filter card is scrolled off).
- Bills calendar: day background green deepens with the day's bill total — under $100 a whisper, $100+ light, $500+ medium, $2,000+ full.
- Bills calendar: tapping the month title jumps back to the current month.
- Bills calendar: days with bills get a light-green background; dots are bigger (multiple dots per day were already shown).
- Bills page: scrolling the upcoming list now pins a sticky header under the app header showing the current month, its total, and an Add bill button.
- Bill form: new bills default to Uncategorized instead of the first category in the list.
- App header: the gradient app icon now sits left of the "Expense Tracker" name.
- Bills page: tapping a bill tile opens the edit form, so the per-tile Edit button is gone (Paid and ✕ still work without triggering edit).
- Bills page: upcoming and paid tiles are now grouped by month under labeled headers with each month's total.
- Budget page: the sticky totals pill now wraps on narrow screens instead of cutting figures off with "…".
- Budget planner: manual row order, removed-category memory, and 🔒 padlocks now sync through Firebase — the Budget page looks the same on every machine.
- Split transactions: in a transaction's detail sheet, the split-parts breakdown rows are now tappable — tapping a sibling part opens that part's transaction (the part you're viewing stays inert).
- Financial goal: fixed the suggestion engine to respect the planner's ✓/🔒 distinction. Since the planner refactor, "locked" means checked/included-in-budget and the padlock is a separate flag — but the goal code still used the old meaning, so trim suggestions were proposed on unchecked rows (which save as $0 and can't move the total) and "cut a category" refused checked categories. Suggestions now target checked, unpadlocked rows.
- Financial goal (Budget page) has a new option: "Save ___% of income per month". Enter a percent (e.g. 15) and the target is computed off average paycheck income; if the budget already leaves enough unspent it says so, otherwise the cut allocator proposes trims for the shortfall.
- Budget planner drag-to-reorder rebuilt: the dragged row is now a fixed ghost that follows the pointer exactly (no more jumping to the top on slight drags), and a dashed placeholder marks the drop position as you drag — the same affordance chart cards already had.
- Sheet Save/Cancel buttons now show a tooltip after hovering for one second: Save-type buttons read e.g. "Save (Shift+Return)", Cancel/Done buttons read "Cancel (Esc)". The tooltip system was generalized from the tab bar to any button (mouse/trackpad hover only).
- Transaction filter card labels now read "Type (Income/Expense/Transfer)" and "Account (Personal/Business)" so the options are visible at a glance.
- Bills page visual polish: the calendar now marks today with a filled accent circle, the selected day gets an accent border, bill dots are slightly larger with consistent spacing, tiles use the app's standard card radius with a softer urgency fill, amounts and due dates use tabular numerals, the days-left text is now a status pill (red overdue / amber due-soon, matching the Budget page badges), and the Paid/Edit/✕ buttons are a touch more compact. No behavior or layout changes — same controls in the same places.
- Navigating to the Transactions page with a new filter selection (including chart drill-throughs) now starts the list at the first row instead of restoring the previous scroll position; returning with the selection unchanged still restores where you were.
- The 🔔 bill-reminder badge now sits right before the amount in the transaction list, and tapping it opens the linked bill reminder.
- Each tab now reopens at its previous scroll position after a page refresh (positions are saved per tab, throttled while scrolling, on tab switch, and on refresh/close).
- Transactions with a bill reminder set now show a 🔔 badge in the list (bills created via "Add bill reminder" link back to their source transaction; deleting the bill clears the badge).
- Transactions page now remembers all filter criteria across reload: the Account (Personal/Business) and Tax category filters are persisted alongside category/type/bank and the period. Search text and the drill pill stay transient by design.
- Transaction detail (edit mode) now has an Add bill reminder button next to Split: it opens the bill form pre-filled from the transaction (name, amount, date as due date, category, Personal/Business), stacked above so unsaved edits are kept; frequency is left for the user to pick before saving.
- Bill scanner: new Upload PDF option — the first page is rendered on-device with PDF.js and read by the same OCR pipeline; the original PDF is retained in bill-scans/ (or the rendered page locally). Also available in the receipt scanner via the shared sheet.
- Tapping a statement on the Import page now opens an in-app preview of the stored file (PDF renders inline, CSV shows text), with an Open full button for the new-tab view; View opens the same preview. Rows without a stored file are unchanged.
- Home page Budget vs Actual card now renders the same paired-bar chart as Reports (Budget teal / Actual green-red with variance labels), replacing the old progress bars; tap a bar to drill into the category. Sorted by budget, largest first.


Running record of what ships in the expense tracker, kept for future
documentation. Newest first.

## 2026-10-02

### Desktop uses the large layout
- Wide mouse/trackpad screens no longer apply `html { zoom: .56 }`, which
  had shrunk the 760px phone column into a tiny centered strip. Desktop now
  keeps full-size type and a wide content column (up to 1600px; sheets
  1100px). iPhone (≤560px) and iPad/tablet tiers are unchanged.

## 2026-10-01

### Wells Fargo combined statements import per account
- A Wells Fargo "Combined Statement of Accounts" (checking + savings in one
  file) now stamps each transaction with its own account — e.g. "Wells Fargo
  Crown Banking xxxx7356", "Wells Fargo Way2Save Savings xxxx4175", and
  separate labels for each Platinum Savings account — instead of labeling
  every row with the first account name found in the file. The import log
  groups these files as "Wells Fargo (N accounts)". Single-account statements
  behave exactly as before.
- Fixed alongside: split two-column headers in savings sections ("…
  Additions … ctions … balance") flipped the parser into the income section,
  typing savings withdrawals (e.g. mortgage payments) as income. Table
  column-header lines no longer flip the income/expense section.

### Tap "This month" to fill the budget amount
- Tapping the "This month $X" line on a budget/income planner row copies
  that actual into the category's amount field (same behavior as the
  YTD avg / Prev month taps: enables the row and saves).

### Cancel is always on the left
- Every sheet with a Cancel + action button pair now puts Cancel first:
  copy-budget, bill form, delete-bill confirm, and the import-log account
  rename. Sheets that already had it (bulk edit, scrubber, split, txn form,
  confirms) are unchanged.

### Bill notes field auto-resizes
- The Notes field on the add/edit bill form now grows and shrinks to fit
  its contents (also refits when a scan pre-fills or clears payment info).

### Tap a reference stat to fill the budget amount
- Tapping the YTD avg or Prev month value on a budget/income planner row
  copies it into that category's amount field, enables the row (like the
  slider does), and saves. Padlocked rows ignore taps.

### Budget tiles: "Last month" → "Prev month"
- The reference stat on budget/income planner rows (and its column header)
  now reads "Prev month".

### Renamed merchants keep their original name for import dedup
- Editing a transaction's merchant name now stashes the statement's
  original name in a new `merchant_orig` field (first rename wins; later
  renames don't overwrite it). Import duplicate detection matches against
  both the current and original names, so a cleaned-up merchant no longer
  causes the same statement row to import twice. The scrubber and bulk
  "update similar" writes preserve it too. `merchant_orig` is included in
  CSV exports and the Apps Script column list (takes effect on the next
  Code.gs redeploy).

### Sticky header shows remaining budget
- The totals pill under the month picker now ends with the unbudgeted
  remainder (income minus proposed budget), e.g. "$4,500 remaining" in
  green — or "$1,000 over" in red when the budget exceeds income — so it's
  clear at a glance how much is left to allocate to new categories.

### Bills-due line updates on month change
- The "Bills due" line at the top of the Budget planner was stuck showing the
  previous month's bills until a row was edited — it now re-renders for the
  newly selected month immediately.

### Bills-due line moves to the top of the Budget planner
- The "Bills due" cash-flow line now sits at the top of the Budget planner's
  scrolling list instead of pinned at the card bottom — it scrolls away with
  the categories instead of staying stuck.

### Split transactions: visible badge + parts on the detail sheet
- Split transactions now show a small "split" badge in the Transactions list.
- Opening a split part shows every part of the split (category + amount,
  with the current one marked) and the parts total, so the other amounts
  are visible right on the detail page.

### Split save: toast explains a leftover remainder
- The Save split button no longer silently stays disabled when the parts
  don't add up — tapping it now says exactly what's off, e.g. "Parts total
  $90.00 — $10.00 short of $100.00."

### Budget planner: declutter + Financial goal scrolls with the list
- Removed the "Live income targets…" / "Live budget…" intro paragraphs, the
  Enable all / Disable all buttons, and the "Dimmed rows are suggestions…"
  hints from both planners.
- The Financial goal section now sits at the bottom of the Budget planner's
  scrolling list instead of pinned at the card bottom — scroll through the
  categories to reach it.

### Tab bar and sheets stay above the iOS keyboard
- While the keyboard is open, the footer tab bar rides above it (it was
  getting hidden behind it while typing), and bottom sheets lift so their
  buttons stay reachable.

### Split save is now guaranteed to persist
- Split saving now finishes writing the new rows to the store even if the
  list re-render hits an error, so a split can no longer silently vanish.

### Copy-from shows a spinner
- The Copy button in the "Copy budget / Copy income targets" sheet shows a
  spinner while the copy runs, so it's clear work is happening.

## 2026-10-01

### Budget page: drag-reorder fix, independent column scroll, itemized bills
- Fixed drag-to-reorder: a math bug meant dragged rows could never actually
  change position on drop. Rows now reorder live as you drag and the order
  sticks. The ⋮⋮ grip is a slightly bigger tap target, and both planners
  note "Drag ⋮⋮ to reorder."
- The side-by-side Budget/Income columns now scroll independently — each
  column's row list is capped below the sticky month bar and above the tab
  bar, so a long expense list no longer pushes the income planner away.
- The "Bills due" cash-flow line under the budget planner now lists each
  bill due in the selected month (name, due date, category, amount) with
  overdue / due-soon badges, above the after-bills-and-budget remaining
  figure.

### Planner rows: drag to reorder
- Each Budget and Income planner row now has a ⋮⋮ grip handle beside the
  category name. Drag it (mouse or touch) to move the row; the list
  reorders live as you drag. The order is saved per month, survives
  Recalculate, and newly added categories go to the end once you've set a
  manual order.

### Sticky header: totals centered under the month
- The budget/income and percent values in the sticky header are now
  centered under the month, instead of right-aligned.

### Planner rows: "This month" and "Last month" swapped
- "This month" now sits under the category name (keeping its red/green
  over-budget/target-met coloring); "Last month" moved into the grouped
  stats beside YTD avg, in both the expense and income planners.

### Planner rows: stacked layout everywhere + "This month" label
- The two-line planner row layout (name + padlock on line 1, labeled
  YTD avg + This month stats with amount on line 2) is now the base
  style at every screen width, not just phones — this fixes the padlock
  overlapping the YTD stat seen on Dave's phone, where the phone-only
  rules weren't taking effect.
- "Actual" renamed to "This month" on the grouped stat and the header.
- Sticky bar: month text bumped 15px → 18px; the live totals pill is now
  right-aligned.

### Transactions: drill pill docks to the sticky filter bar
- When a category drill-through pill is active and the filter card has
  scrolled off, the pill now parks itself as an attached section at the
  bottom of the floating sticky filter bar (same docking pattern as the
  bulk-update bar); it returns to the page flow when scrolled back up.

### Planner rows: YTD avg + Actual grouped with labels
- Each planner row now shows YTD avg and the selected month's actual
  side by side as a labeled pair (tiny "YTD AVG" / "ACTUAL" labels),
  instead of the YTD figure sitting alone and the actual tucked under
  the amount field. Over-budget actuals still turn red; income targets
  met still turn green.

### Planner row colors: red expenses, green income
- Enabled expense rows now use a soft red fill and enabled income rows a
  soft green fill (previously both were green), so the two planners are
  instantly distinguishable. Suggestion rows stay dimmed.

### Budget sticky bar: centered month picker, bigger prev/next
- The month stepper (‹ September 2026 ›) is now centered in the sticky
  bar, and the prev/next buttons are bigger tap targets.

### Footer tab bar pinned; planner rows show full category names (phones)
- The footer tab bar gets its own compositing layer so iOS Safari keeps
  it glued to the bottom of the viewport.
- On phones, planner rows are now two lines: ✓ + full category name +
  padlock on the first line, YTD avg + amount + remove on the second,
  slider below. Category names are no longer truncated to a letter or two.

### Budget page: locks, enabled fill, selected-month actuals
- Each planner row now has a padlock button next to the category name.
  Locking fixes the amount: the amount field can't be edited and the
  slider is hidden until you unlock it. Locks are saved per month,
  survive Recalculate (fixed amounts aren't recomputed), travel with
  Copy from…, and clear when the category is removed.
- Enabled categories now get a full accent fill across the row, so it's
  obvious which categories are in the live budget; suggestion rows stay
  dimmed.
- Each row shows the selected month's actual ("actual $312") under the
  budget amount — red when an expense is over budget, green when income
  meets its target — for planning next month's amounts.

### Budget page: iPhone layout fixes (from screenshot review)
- The sticky bar is now two compact rows (month stepper, then the live
  totals pill) and the pill is always a single line — shortened to
  "$11,915 budget · $11,590 income · 103%" with ellipsis instead of
  wrapping mid-phrase over the Copy from…/Recalculate buttons.
- Planner rows can no longer push past the card's right edge on a 390px
  phone: the name column is `minmax(0,1fr)` and every grid child
  (name, amount input, slider) may shrink to zero, so the amount input
  and × button stay on screen and the header labels align with their
  columns.
- Removed the slim actual-vs-budget / received-vs-target bars under each
  row — they read as a double slider track. The slider, YTD avg, and
  "Last month" figures remain.
- Planner intros shortened to one line ("Live budget — every change
  saves instantly.").
- Unchecked (suggestion) rows now get an explanatory hint: "Dimmed rows
  are suggestions — tap ✓ to include one in your budget." The faded
  checkmark means the row isn't part of the live budget yet.

### Budget page: removed the sticky floating totals card
- The floating totals pill near the footer is gone (markup, styles, and
  update logic removed). The per-planner header cards still show planned
  total, % of income, and expected income.
- The values in the sticky totals pill next to the month picker are now
  larger (16px bold values, 14px labels, up from 12.5px).

### Budget page: planners are now the live budget (no more drafts)
- The draft/Save model is gone. The **Budget planner** and **Income
  planner** are the live budget — every check, amount edit, add, and
  remove saves straight to the store the moment it happens (amount
  typing/dragging debounces ~0.6s so slider drags stay smooth).
- The sticky totals pill now follows the live budget: the income target
  is the sum of the checked income categories, updating as you edit.
- **Recalculate** rebuilds fresh year-to-date amounts in place, keeps
  checked states, and writes straight through; it also zeroes any stale
  saved amounts on unchecked rows.
- Opening a month still restores that month's saved budget (checked rows
  with their saved amounts); everything else is an unchecked YTD
  suggestion. Removed categories stay hidden for the month.
- One-time cleanup: old per-month draft keys are swept from localStorage
  on load; removed-category memory is kept.
- **Fix:** restored `incBotCompute`, which a span edit had accidentally
  deleted along with the old draft/save code — the Income planner card
  rendered empty because its loader threw before painting any rows.
## 2026-09-30

### Budget page: planners replace the budget/target cards
- The separate Category budgets and Income targets cards are gone. The
  **Budget planner** and **Income planner** are now the only budget editors.
- Opening a month prefills each planner with that month's saved values
  (checked); **Recalculate** drafts a fresh year-to-date-based proposal
  while keeping checked states, so it never silently wipes the budget.
- Save semantics: checked rows save their amounts, unchecked rows save as
  $0, and categories removed from a planner (✕) revert to $0 — removed
  rows stay hidden for the month and the Add menu lists only categories
  not currently shown, so it's the way to bring one back.
- Each planner has its own **Copy from…** (budgets and income targets copy
  independently).
- Row reference lines now show last month's actual (no more 3-month
  average) next to the YTD monthly-average column, plus a slim
  actual-vs-draft bar for the selected month.
- The sticky totals pill now reflects saved totals for the selected month.

## 2026-09-30

### Budget page: expenses and income side by side on large desktop
- Category budgets and Income targets cards now sit side by side on
  desktop (1200px and up); stacked everywhere else.

### Sticky % of income now actually turns red/green
- The "% of income" figure in the sticky bar was supposed to go red over
  100% and green otherwise, but a pill style was overriding the colors —
  fixed so the red/green now shows.

### Bot cards: Propose buttons moved up, row fill removed
- "Propose my budget" / "Propose my income" now sit in the card header
  next to the title instead of below the description.
- Removed the green fill from checked bot proposal rows (both bots) —
  checked state still shows via the green checkmark; unchecked rows
  stay dimmed.

### Enable/disable all in both bots
- The Budget Bot and Income Bot proposals each gained "Enable all" /
  "Disable all" buttons above the proposal table (shown only when a
  proposal exists). One tap checks or unchecks every category, updating
  the proposed total and persisting the draft.

### Category panels tinted red/green
- Category budget panels now carry a subtle red tint (expense) and
  income target panels a subtle green tint, so the category type is
  visible at a glance. Works in light and dark mode.

### Copy a budget from another month
- The Category budgets card has a "Copy from…" button. It opens a sheet
  defaulting to the previous month (any month can be picked) and copies
  that month's category budgets and income targets into the month shown
  in the sticky bar, replacing anything already set there. The sheet
  states exactly what will be copied before confirming.

### Category budgets: YTD total + monthly average per category
- Each category panel now shows a reference line under its name, e.g.
  "Jan–Sep YTD $4,320 · avg $480/mo" — the year-to-date total and the
  monthly average for that category. Both follow the month picked in the
  sticky bar (YTD runs Jan 1 through that month; the average divides by
  the months elapsed through it), transfers excluded, same convention
  as the Budget Bot. The selected month's spent-vs-budget stays in the
  panel's top row as before.

### Budget Bot: per-category sliders that auto-enable
- Every category row in a budget proposal now has its own slider under
  the row, with the proposed amount in the middle of its range. Checks
  start off; moving a slider automatically enables that category (check
  mark lights up, row highlights, joins the proposed total) and updates
  the row's amount field live. Typing in the amount field moves that
  row's slider too. Replaces the single bottom-of-card adjust slider.

### Budget Bot: adjust slider for the checked category
- Checking a category's ✓ in a budget proposal now shows an "Adjust"
  slider at the bottom of the proposal for that category. The proposed
  amount sits in the middle of the range ($0 to ~2x proposed) so it can
  be nudged lower or higher; dragging updates the row's amount, the
  proposed total, and the saved draft live, and stays in sync with the
  row's number field both ways. Unchecking (or removing) the category
  hides the slider again.

### Budget page: month stepper in the sticky bar
- The sticky bar's month picker now has ‹ › steppers for flipping through
  months one tap at a time (same pattern as the Bills calendar header);
  the native month field is still there for jumping straight to a month,
  now styled to sit cleanly in the bar.

### Bills page: Edit and Delete buttons on every bill
- Each upcoming bill tile now has explicit Edit and Delete buttons next
  to Paid (editing was previously only discoverable by tapping the bill
  name). Delete asks for confirmation first, as before.

### Budget page: auto-save, no more Save button + clearer category rows
- Budget and income-target amounts now save automatically: pause for a
  moment after dragging/typing and the value persists (a small "Saved ✓"
  note confirms it); releasing the slider saves immediately. The Save
  button is gone.
- Each category row in the Category budgets and Income targets cards is
  now its own bordered panel, so it's easy to tell where one category
  ends and the next begins.

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
  better app name, user documentation, Test CSV import.

### Scanners
- Re-scanning a bill or receipt rolls back what the previous scan set instead
  of leaving stale values; the old payment-info block is replaced, not doubled.
- Bill scanner extracts where-to-pay info and payment instructions into Notes.

### Setup / misc
- Setup → Firebase tab has an "Open Firebase console" link.
- Desktop type ~30% smaller (zoom .56); dropdown menus sized to match.
- Selected footer tab shows an accent-faint rounded pill, not just colored icon.
- Mac desktop icon: rounded squircle with transparency + subtle green gradient.
