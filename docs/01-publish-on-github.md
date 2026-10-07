# Step 1: Publish the project on GitHub

Two routes. Route A needs no tools. Route B uses Git.

## Route A: Browser only (easiest)

1. Go to <https://github.com> and sign in (or **Sign up**, free).
2. Click the **+** at the top right, then **New repository**.
3. Fill in:
   - **Repository name:** `brightpath-va-inbox-project`
   - **Description:** `Virtual Assistant practice project: inbox triage, labels and trackers (fictional data)`
   - **Public** (so recruiters can see it)
   - Leave "Add a README" **unchecked** because this project already has one.
4. Click **Create repository**.
5. On the new empty page, click **uploading an existing file**.
6. Unzip the project on your computer, open the folder, and drag **the contents** (the `data`, `docs`, `answer_key`,
   `tools`, `apps_script` folders plus `README.md`, `LICENSE`, `.gitignore`) into the browser window.
   Dragging folders works in Chrome and Edge.
7. In **Commit changes**, type `Add BrightPath VA practice project` and click **Commit changes**.
8. Refresh the page. You should see `README.md` displayed under the file list.

## Route B: Git on your computer

1. Install Git from <https://git-scm.com/downloads>, then confirm: `git --version`.
2. Set your identity once:
   ```bash
   git config --global user.name "Loren Villas"
   git config --global user.email "your-email@example.com"
   ```
3. Create the empty repository on GitHub as in Route A steps 1-4.
4. In a terminal, go into the unzipped folder and run:
   ```bash
   cd brightpath-va-inbox-project
   git init -b main
   git add .
   git commit -m "Add BrightPath VA practice project"
   git remote add origin https://github.com/YOUR-USERNAME/brightpath-va-inbox-project.git
   git push -u origin main
   ```
5. If asked to sign in, use a browser login or a personal access token (GitHub no longer accepts account passwords for Git).
6. Refresh the repository page to confirm the files are there.

## Make the repo look professional

1. Click the gear icon beside **About** (right side of the repo page).
2. Add a description and topics: `virtual-assistant`, `gmail`, `project-management`, `portfolio`, `mock-data`.
3. Check the README renders its tables and the label tree correctly.

## Optional: hide the answer key

Because the repo is public, anyone can read `answer_key/`. If you want it hidden, delete that folder before publishing or
keep it in a separate private repository. For a portfolio, leaving it public is fine because it shows your thinking.

## Keep it updated

Each time you add a finished tracker, repeat Route A's upload (**Add file > Upload files**) or run:
```bash
git add .
git commit -m "Add invoice tracker"
git push
```

## Before you publish: privacy check

- Use only the fictional data in this repo.
- Never upload a real client's emails, invoices or contact details.
- Do not include your personal passwords or tokens in any file.
