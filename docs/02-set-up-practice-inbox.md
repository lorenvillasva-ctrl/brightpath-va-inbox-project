# Step 2: Set up the practice inbox and labels

Pick **one** option. Option A is simplest and is enough for the portfolio.

## Option A: Google Sheets inbox (no setup risk)

1. Run `python tools/emails_to_csv.py` to create `data/emails.csv`. If you don't use Python, open `emails.json` in any
   JSON-to-CSV converter online.
2. Open <https://sheets.google.com> and create a blank spreadsheet named `BrightPath - Inbox`.
3. **File > Import > Upload**, choose `emails.csv`, then **Replace current sheet** and **Import data**.
4. Freeze the header row: **View > Freeze > 1 row**.
5. Add a drop-down for the `label` column: select the column cells, **Data > Data validation > Add rule > Dropdown**,
   and type these items:
   - 01 - Action Required
   - 02 - Client Information
   - 03 - Invoices & Payments
   - 04 - Follow-Up
   - 05 - Meetings & Calendar
   - 06 - Waiting for Client
   - 07 - Completed
   - 08 - Reference
6. Import the five other CSVs from `data/` as extra tabs: **File > Import > Insert new sheet(s)**.

## Option B: A real Gmail practice account

Use a **new** account created only for this exercise. Never use your personal or a real client's account.

### B1. Create the account
1. Go to <https://accounts.google.com/signup> and create e.g. `brightpath.practice.inbox@gmail.com`.

### B2. Create the labels
1. In Gmail, click the gear icon, then **See all settings > Labels**.
2. Click **Create new label**, name it `BrightPath Consulting`, and **Create**.
3. Create each of these, ticking **Nest label under: BrightPath Consulting** each time:
   `01 - Action Required`, `02 - Client Information`, `03 - Invoices & Payments`, `04 - Follow-Up`,
   `05 - Meetings & Calendar`, `06 - Waiting for Client`, `07 - Completed`, `08 - Reference`.
4. In the left sidebar you should now see the parent label with eight sub-labels.

### B3. Get the emails in
- **Easy way:** open `data/emails.json`, and for each email, compose a message from a second account (or your own
  address) with the same subject and body. It's slow, but it works for 30 emails.
- **Script way (optional, untested):** follow the comments in `apps_script/import_emails.gs`. If it errors, switch to the
  easy way or Option A.

### B4. Useful Gmail features to turn on
1. **Stars:** gear > **See all settings > General > Stars**, drag the red "!" and yellow star into the in-use list.
2. **Multiple Inboxes** (optional): **Inbox** tab > **Inbox type > Multiple inboxes**.
3. **Filters:** search for a sender, click the search-options icon, **Create filter**, apply a label. Try it for `no-reply`
   senders after you have decided where they belong.

## Important rule for both options

Do **not** open `answer_key/` until you have labeled everything yourself.
