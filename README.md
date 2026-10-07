# BrightPath Consulting: Virtual Assistant Inbox Practice Project

A fictional, portfolio-ready practice project for a Virtual Assistant. You take over the messy inbox of **Sarah Mitchell**
(BrightPath Consulting, a business and marketing consultancy), then organize it and build seven trackers from it.

> All people, companies, emails, amounts and links are fictional. Domains end in `.example`.
> The project's "today" is **Wednesday, October 7, 2026**. VA: **Loren Villas**.

## What is in this repo

| Path | Contents |
|---|---|
| `data/emails.json` | 30 mock emails (id, sender, recipient, subject, timestamp, body, folder, unread) |
| `data/clients.csv` | 12 clients |
| `data/invoices.csv` | 9 invoices |
| `data/tasks.csv` | 15 tasks |
| `data/followups.csv` | 10 follow-ups |
| `data/meetings.csv` | 5 upcoming meetings |
| `answer_key/` | Suggested labels and the list of planted problems. Don't open until you finish |
| `docs/` | Step-by-step guides |
| `tools/` | `validate.py` (checks counts) and `emails_to_csv.py` (JSON to CSV for Google Sheets) |
| `apps_script/` | Optional, untested script to load the emails into a practice Gmail account |

## Gmail label structure

```
BrightPath Consulting
├── 01 - Action Required
├── 02 - Client Information
├── 03 - Invoices & Payments
├── 04 - Follow-Up
├── 05 - Meetings & Calendar
├── 06 - Waiting for Client
├── 07 - Completed
└── 08 - Reference
```

## The task

Review every email and decide the label, priority, owner, deadline, follow-up date, whether a reply is needed and whether
Sarah must approve. Then build:

1. Client Tracker
2. Invoice Tracker
3. Email Action List
4. Task Tracker
5. Follow-Up Tracker
6. Weekly Priority List
7. Simple Executive Dashboard

The data deliberately contains duplicates, missing details, inconsistent names, conflicting figures and unclear statuses.
Finding and flagging these is part of the work.

## How to follow it

1. [Publish this repo on GitHub](docs/01-publish-on-github.md)
2. [Set up the practice inbox and labels](docs/02-set-up-practice-inbox.md)
3. [Triage method: decide label, priority and action](docs/03-triage-method.md)
4. [Build the seven trackers](docs/04-build-the-trackers.md)
5. [Present it in your portfolio](docs/05-portfolio-tips.md)

## Quick check

```bash
python tools/validate.py
```

## License

MIT. See `LICENSE`.
