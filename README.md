# From Repo to Dashboard 🏴󠁧󠁢󠁷󠁬󠁳󠁿

## Hands-on GitHub, Codespaces & Copilot for Stats Wales Health Data Analysts

> **"I tried this, and I didn't even break anything!"**

Welcome! 👋 You don't need to be a developer. You don't need to install anything. You just need a browser and a GitHub account. That's it.

This template repository is your starting point for the **Big Data Does GitHub** beginner workshop. The focus is on learning **GitHub, Codespaces, and Copilot** — not coding. The notebook does the heavy lifting for you!

By the end, you'll have:

- ✅ Your own GitHub repository with real data in it
- ✅ A live data dashboard published on GitHub Pages
- ✅ Experience using GitHub Copilot as an AI assistant
- ✅ A working understanding of Git basics (commit, branch, pull request)

---

## 🚀 Quick Start (5 minutes)

### Step 1 — Use this template

Click the green **"Use this template"** button at the top of this page, then choose **"Create a new repository"**. Give it a name like `my-stats-wales-dashboard`.

### Step 2 — Open in Codespaces

In your new repository, click the green **"Code"** button → **"Codespaces"** tab → **"Create codespace on main"**.

A full VS Code environment will open in your browser. No installs. No admin rights needed. ☁️

### Step 3 — Run the notebook

Open `workshop/fetch_data.ipynb` and run each cell from top to bottom. The notebook shows you all the available Stats Wales datasets — **pick one that interests you**, paste its ID, and the notebook does the rest (fetching data, creating a chart, exporting for the dashboard). Then practise committing your changes with Git.

Open [`WORKSHOP_GUIDE.md`](./WORKSHOP_GUIDE.md) for the full walkthrough.

---

## 📋 Workshop Overview

| Topic                   | What you'll learn                                            |
| ----------------------- | ------------------------------------------------------------ |
| 🗂️ **GitHub Basics**    | Repos, commits, branches, pull requests, merging             |
| ☁️ **Codespaces**       | Cloud VS Code, no local setup, same environment for everyone |
| 🤖 **GitHub Copilot**   | AI pair-programming, prompt engineering, explaining code     |
| 📊 **Stats Wales Data** | Run a pre-built notebook to fetch & chart real public data   |
| 🌐 **GitHub Pages**     | Publishing a live HTML dashboard from your repo              |

---

## 📁 Repository Structure

```
.
├── README.md                  ← You are here
├── WORKSHOP_GUIDE.md          ← Step-by-step workshop walkthrough
├── .devcontainer/
│   └── devcontainer.json      ← Codespaces configuration (zero setup!)
├── workshop/
│   └── fetch_data.ipynb       ← Pre-built notebook: just run it to fetch data & create charts
└── docs/
    └── index.html             ← Your live dashboard (published via GitHub Pages)
```

---

## 🛠️ Pre-requisites

- **A GitHub account** (free at [github.com](https://github.com))
- **A browser** — that's genuinely all you need
- Basic familiarity with data is helpful but absolutely not required

> 💡 Codespaces runs entirely in the cloud. There's nothing to install on your laptop, no admin rights needed, and no IT configuration required. Everyone in Wales runs the exact same environment.

---

## 🏴󠁧󠁢󠁷󠁬󠁳󠁿 About the Data

This workshop uses the **Stats Wales API** — a free, open API for official Welsh statistics.

- [Browse all datasets](https://api.stats.gov.wales/v1/?lang=en-gb&page_number=1&page_size=100)
- [Stats Wales website](https://statswales.gov.wales)

---

## 🤝 Share Your Work!

Once you've built your dashboard, share it! Copy your GitHub Pages URL and post it to:

- **Teams** — drop it in your team channel
- **LinkedIn** — tag `#StatsWales #GitHubCopilot #DataWales`
- **Your manager** — this is a real, live, professional output 🎉

---

## 📖 Detailed Instructions

Head to **[WORKSHOP_GUIDE.md](./WORKSHOP_GUIDE.md)** for the full step-by-step guide.
