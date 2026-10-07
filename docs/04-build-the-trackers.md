# Step 4: Build the seven trackers

Create one Google Sheets workbook named `BrightPath - VA Trackers`. Each tracker is a tab. Clean data before you build:
fix inconsistent names, mark duplicates, and put "UNKNOWN" (not a blank) where information is missing.

## General setup (do once)

1. Import each CSV from `data/` into its own tab.
2. Format dates: select a date column, **Format > Number > Date**.
3. Turn on filters: select the header row, **Data > Create a filter**.
4. Freeze the header row: **View > Freeze > 1 row**.
5. Add data validation drop-downs for status columns (**Data > Data validation**).

## 1. Client Tracker

Columns: `client_id`, `contact`, `company`, `email`, `phone`, `service`, `status`, `open_items`, `last_contact`, `next_step`, `flag`.

1. Start from `clients.csv`.
2. Merge duplicates: C004 and C012. Keep one, note the other in `flag`.
3. Add Dana Whitaker as a new lead.
4. Fill `open_items` with a formula: `=COUNTIFS(Tasks!C:C, C2, Tasks!G:G, "<>Done")` after matching names (see the note below).
5. Conditional formatting: **Format > Conditional formatting**, colour rows red where `status = "At Risk"`.

*Name matching:* tasks use company names, so create a consistent `company` value and use it in every tab.

## 2. Invoice Tracker

Columns: `invoice_no`, `client`, `amount`, `issue_date`, `due_date`, `status`, `days_overdue`, `payment_date`, `next_action`, `flag`.

1. Start from `invoices.csv`.
2. Clean names (Thomas Hargrove, Greenleaf Landscape).
3. Days overdue: `=IF(AND(F2<>"Paid", E2<DATE(2026,10,7)), DATE(2026,10,7)-E2, 0)`
4. Add a total row: outstanding = `=SUMIFS(C:C, F:F, "<>Paid")`
5. Status drop-down: Draft, Sent, Paid, Overdue, Disputed.
6. Flag INV-1041 (paid or overdue?), INV-1043 (dispute), INV-1047 (hours mismatch), INV-1049 (missing due date).

## 3. Email Action List

Columns: `email_id`, `from`, `subject`, `label`, `priority`, `action`, `owner`, `deadline`, `response_needed`, `approval_needed`, `done`.

1. Use only emails that need an action.
2. Sort by `priority`, then `deadline`.
3. Use a checkbox in `done`: **Insert > Checkbox**.
4. Strike through finished rows with conditional formatting: custom formula `=$K2=TRUE`, style: strikethrough and grey text.

## 4. Task Tracker

Columns: `task_id`, `task`, `client`, `owner`, `due_date`, `priority`, `status`, `source_email`, `notes`.

1. Start from `tasks.csv`.
2. Remove the duplicate (T010 / T014) and assign an owner to T005.
3. Add a due date to T013 or mark it `UNKNOWN`.
4. Status drop-down: Not Started, In Progress, Waiting, Done, Overdue.
5. Highlight overdue: custom formula `=AND($E2<DATE(2026,10,7), $G2<>"Done")`.

## 5. Follow-Up Tracker

Columns: `followup_id`, `client`, `subject`, `last_contact`, `followup_date`, `owner`, `status`, `days_waiting`, `message_to_send`.

1. Start from `followups.csv`.
2. Merge F005 and F010 (the same Daniel Brooks call).
3. Days waiting: `=DATE(2026,10,7)-D2`
4. Draft the next message in `message_to_send` for every overdue row.

## 6. Weekly Priority List (week of Oct 5-11, 2026)

Layout: one table with `rank`, `item`, `why_it_matters`, `owner`, `due`, `next_step`.

1. Pull rows where priority is Urgent or High and the deadline is before Oct 12.
2. Rank by deadline, then by money or relationship risk.
3. Keep to **10 items maximum**. Put the rest under "Next week".
4. Add "Decisions needed from Sarah" as a separate short list.

Suggested order of attention: Brooks call, price confirmation for Delgado proposal, meeting clash on Oct 8,
DesignDeck renewal before Oct 10, Hargrove contract, Mendez invoice dispute.

## 7. Simple Executive Dashboard

Make a tab called `Dashboard` with summary tiles and two charts.

Tiles (use formulas that read from your other tabs):
- Outstanding invoices: `=SUMIFS(Invoices!C:C, Invoices!F:F, "<>Paid")`
- Overdue invoices: `=COUNTIF(Invoices!F:F, "Overdue")`
- Open tasks: `=COUNTIF(Tasks!G:G, "<>Done")-1`
- Overdue follow-ups: `=COUNTIF(FollowUps!G:G, "Overdue")`
- Meetings this week: `=COUNTIFS(Meetings!D:D, ">="&DATE(2026,10,5), Meetings!D:D, "<="&DATE(2026,10,11))`
- Emails still unlabeled: `=COUNTBLANK(Inbox!K2:K31)`

Charts (**Insert > Chart**):
1. Invoices by status (column or bar chart).
2. Tasks by owner (column chart).

Layout tip: tiles across the top, charts below, and a "Top 5 priorities" list at the right. Avoid decoration; limit to two
or three colours.

## Final quality check

- [ ] No duplicate clients, tasks or follow-ups remain
- [ ] Every task has an owner and a due date, or is flagged
- [ ] Every invoice has a status and amount
- [ ] Names match across all tabs
- [ ] The Issues Log lists every conflict you found
- [ ] The dashboard numbers match the underlying tabs
- [ ] Export a PDF copy: **File > Download > PDF**
