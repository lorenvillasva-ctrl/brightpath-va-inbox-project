"""Check that the dataset matches the project brief.  Run: python tools/validate.py"""
import csv
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
data = root / "data"

emails = json.loads((data / "emails.json").read_text(encoding="utf-8"))
required = {"id", "sender", "recipient", "subject", "timestamp", "body", "folder", "unread"}

problems = []
for e in emails:
    missing = required - e.keys()
    if missing:
        problems.append(f"{e.get('id')}: missing {sorted(missing)}")
    if not isinstance(e.get("unread"), bool):
        problems.append(f"{e.get('id')}: unread must be true/false")

ids = [e["id"] for e in emails]
if len(ids) != len(set(ids)):
    problems.append("duplicate email ids")


def count(name):
    with open(data / name, newline="", encoding="utf-8") as f:
        return len(list(csv.DictReader(f)))


with open(root / "answer_key" / "answer_key.csv", newline="", encoding="utf-8") as f:
    key_ids = {r["email_id"] for r in csv.DictReader(f)}
if key_ids != set(ids):
    problems.append("answer key ids do not match emails")

expected = {"clients.csv": 12, "invoices.csv": 9, "tasks.csv": 15, "followups.csv": 10, "meetings.csv": 5}
print(f"emails: {len(emails)}")
for name, want in expected.items():
    got = count(name)
    print(f"{name}: {got}")
    if got != want:
        problems.append(f"{name}: expected {want}, found {got}")

if problems:
    print("\nProblems:")
    print("\n".join(" - " + p for p in problems))
    sys.exit(1)
print("\nAll checks passed.")
