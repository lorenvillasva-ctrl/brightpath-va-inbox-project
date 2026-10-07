"""Convert data/emails.json to data/emails.csv so it can be imported into Google Sheets.
Run: python tools/emails_to_csv.py
"""
import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
emails = json.loads((root / "data" / "emails.json").read_text(encoding="utf-8"))

fields = ["id", "sender", "recipient", "subject", "timestamp", "folder", "unread", "body",
          "label", "priority", "action", "owner", "deadline", "followup_date"]
with open(root / "data" / "emails.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.DictWriter(f, fieldnames=fields)
    w.writeheader()
    for e in emails:
        row = {k: e.get(k, "") for k in fields}
        row["body"] = e["body"].replace("\n", " ")
        w.writerow(row)
print(f"Wrote {len(emails)} rows to data/emails.csv")
