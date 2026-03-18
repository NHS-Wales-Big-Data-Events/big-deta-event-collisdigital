# 📖 Workshop Guide

## From Repo to Dashboard: Hands-on GitHub, Codespaces & Copilot

> **"I tried this, and I didn't even break anything!"**
>
> Welcome! This guide walks you through the entire workshop step by step. There's nothing to install. No admin rights needed. Just a browser and a GitHub account.

---

## ⏱️ Workshop at a Glance

| Module | Topic                                    | Time    |
| ------ | ---------------------------------------- | ------- |
| 1      | GitHub Fundamentals                      | ~25 min |
| 2      | Codespaces — Your Cloud Environment      | ~15 min |
| 3      | GitHub Copilot — Your AI Pair Programmer | ~10 min |
| 4      | Run the Notebook & Make It Yours         | ~15 min |
| 5      | Publishing Your Dashboard                | ~15 min |
| 6      | Share Your Work!                         | ~5 min  |

**Total: ~85 minutes** (plus questions and exploration time)

---

## 🎯 What You'll Build

By the end of this workshop you'll have:

- A **GitHub repository** with your data analysis code
- A **live public dashboard** showing real Welsh statistics
- Experience with **Git, Codespaces, and Copilot** that you can use every day

> 💡 **This workshop is about GitHub skills, not coding.** The notebook is pre-built — you just run it, customise small things (like a chart title), and focus on practising version control.

Here's what the finished dashboard looks like: open `docs/index.html` in your browser or visit your GitHub Pages URL.

---

## Module 1 — GitHub Fundamentals

### What is GitHub, and why does it matter?

GitHub is the world's most widely used platform for version control and collaboration. Think of it as a combination of:

- A **backup system** that never forgets any version of your code
- A **collaboration tool** where colleagues can review and suggest changes
- A **publishing platform** for sharing your work with the world

This isn't just a new tool — it's international best practice used by NASA, the NHS, the UK Government and data teams across the globe. You're joining millions of analysts who use this every day.

---

### 1.1 — Create your repository from this template

1. Click the green **"Use this template"** button at the top of this repository
2. Choose **"Create a new repository"**
3. Give it a name like `my-stats-wales-dashboard` (no spaces — use hyphens)
4. Set visibility to **Public** (needed for GitHub Pages later)
5. Click **"Create repository from template"**

🎉 You now have your own copy of the workshop template!

---

### 1.2 — Understand the repository structure

Look at the files in your new repository:

```
README.md              ← The welcome page everyone sees
WORKSHOP_GUIDE.md      ← This guide
.devcontainer/         ← Codespaces configuration
workshop/              ← Your Jupyter notebooks go here
docs/                  ← Your dashboard (GitHub Pages serves this)
```

> 💡 **Best practice:** A good `README.md` is the front door to your project. It should explain what the project does, how to use it, and who it's for. GitHub Copilot can help you write one!

---

### 1.3 — Git concepts you'll use today

| Term                  | What it means                    | Real-world analogy                         |
| --------------------- | -------------------------------- | ------------------------------------------ |
| **Repository (repo)** | A folder tracked by Git          | A project folder with full version history |
| **Commit**            | A saved snapshot of your changes | Ctrl+S, but you can go back to _any_ save  |
| **Branch**            | A separate line of development   | A copy of the project to try something new |
| **Pull Request (PR)** | A request to merge your branch   | Asking a colleague to review your changes  |
| **Merge**             | Combining branches               | Accepting the reviewed changes             |
| **Push**              | Sending commits to GitHub        | Uploading your saves to the cloud          |
| **Pull**              | Getting the latest changes       | Downloading the latest version             |

---

### 1.4 — Make your first commit

Once you've made changes in Codespaces (in Module 2), you'll commit them like this:

**Using the VS Code Source Control panel (recommended for beginners):**

1. Click the **Source Control icon** in the left sidebar (looks like a branch)
2. You'll see your changed files listed under "Changes"
3. Hover over a file and click **+** to "stage" it (prepare it for saving)
4. Type a message in the box at the top — e.g., `"Add Stats Wales data and chart"`
5. Click the **✓ Commit** button
6. Click **Sync Changes** (or the cloud/upload icon) to push to GitHub

**Using the terminal (for the curious):**

```bash
git add .                          # Stage all changes
git commit -m "Add my chart"       # Save with a message
git push                           # Upload to GitHub
```

> 💡 **Good commit messages** are short but specific. "Add population chart for Wales 2020" is much better than "update stuff".

---

### 1.5 — Create a branch and pull request

Branches let you experiment without affecting the main version of your code.

1. In the VS Code bottom bar, click the branch name (probably `main`)
2. Select **"Create new branch…"** and call it `feature/my-chart`
3. Make some changes (e.g., update the dashboard title in `docs/index.html`)
4. Commit and push the branch
5. On GitHub, you'll see a prompt to **"Compare & pull request"** — click it
6. Write a description of your changes and click **"Create pull request"**
7. Review the diff (the green/red changes), then click **"Merge pull request"**

> 💡 Pull requests are how teams review each other's work. Even if you're working alone, PRs give you a record of _why_ you made each change.

---

### 1.6 — GitHub Projects (lightweight tracking)

You can use **GitHub Projects** to track your workshop tasks like a Kanban board:

1. Click the **"Projects"** tab in your repository
2. Click **"New project"** → **"Board"**
3. Create cards for tasks: "Fetch data", "Create chart", "Publish dashboard"
4. Move them through To Do → In Progress → Done as you work

---

## Module 2 — Codespaces: Your Cloud Development Environment

### Why Codespaces?

> **The single biggest barrier to data collaboration in Wales is software differences.**
>
> One analyst has Python 3.9. Another has 3.11. One has Jupyter. Another has Spyder. Nothing is configured the same, and sharing code between organisations is a nightmare.
>
> Codespaces solves this completely. Every analyst in Wales runs the **exact same environment** — the same Python version, the same libraries, the same VS Code extensions. No local IT configuration. No admin rights. No "it works on my machine".

---

### 2.1 — Launch your Codespace

1. In your repository, click the green **"Code"** button
2. Click the **"Codespaces"** tab
3. Click **"Create codespace on main"**
4. Wait ~1 minute while the environment sets up ☕
5. VS Code opens in your browser — you're now running in the cloud!

Everything is configured automatically by the `.devcontainer/devcontainer.json` file in this repo. It installs Python, Jupyter, and all required libraries.

---

### 2.2 — Explore the Codespace

Take a look around:

- **Explorer** (left sidebar, file icon) — your repository files
- **Source Control** (left sidebar, branch icon) — Git integration
- **Extensions** (left sidebar, puzzle piece) — GitHub Copilot is already installed
- **Terminal** (bottom panel, or `Ctrl+` `` ` ``) — run Python, pip, git commands

> 💡 **Ports panel:** When you run a Jupyter notebook server or a local web server, the Ports panel (bottom) shows you a clickable URL to open it in your browser.

---

### 2.3 — Understanding devcontainers

The `.devcontainer/devcontainer.json` file tells Codespaces:

- Which Docker image to use (Python 3.12)
- Which VS Code extensions to install (Copilot, Jupyter, etc.)
- Which Python packages to install (`requests`, `pandas`, `matplotlib`, etc.)
- Which ports to forward (8888 for Jupyter)

You can customise this file to add any tools your team needs. Once committed, every teammate gets the same setup automatically.

---

## Module 3 — GitHub Copilot: Your AI Pair Programmer

### What is Copilot?

GitHub Copilot is an AI assistant built into VS Code. It can:

- **Complete your code** as you type
- **Generate functions** from a comment describing what you want
- **Explain code** you don't understand
- **Debug errors** by reading your error messages
- **Write documentation** for your functions

> ⚠️ **Important:** Copilot is a pair of hands, not a replacement for your brain — and definitely not a way to bypass data governance. You are responsible for reviewing, understanding, and validating everything Copilot suggests. Treat it like a fast junior colleague who needs supervision.

---

### 3.1 — Using Copilot Chat

Press `Ctrl+I` (or `Cmd+I` on Mac) anywhere in VS Code to open Copilot Chat inline, or click the **Copilot icon** in the sidebar for a full chat panel.

**Try these prompts:**

| Task             | Copilot prompt                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Understand code  | `"Explain what this function does in plain English"`                                        |
| Fix an error     | Paste the error message: `"I'm getting this error: [paste error]. How do I fix it?"`        |
| Generate a chart | `"Write Python code to create a bar chart comparing England and Wales from this dataframe"` |
| Clean data       | `"How do I remove rows where the Value column is empty?"`                                   |
| Document code    | `"Add docstrings to all functions in this file"`                                            |
| Improve README   | `"Write a README section explaining what this dashboard shows"`                             |

---

### 3.2 — Prompt engineering tips

Getting useful responses from Copilot is a skill. Here's what works:

1. **Be specific** — "Create a bar chart" is vague. "Create a horizontal bar chart showing `Data` values grouped by `Area`, with green bars and a title 'Wales Health Data 2020'" is much better.

2. **Give context** — Tell Copilot what your dataframe looks like: "I have a dataframe with columns: Area, Year, Measure, Data"

3. **Iterate** — If the first answer isn't right, refine: "That's good but can you also add data labels on each bar?"

4. **Ask for explanations** — "Can you explain what `pd.to_numeric` does in that code?"

---

## Module 4 — Run the Notebook & Make It Yours

The notebook does the heavy lifting — you just need to **pick a dataset** and **paste its ID**. The real learning here is practising Git!

### 4.1 — Open the notebook and browse datasets

1. In Codespaces, open `workshop/fetch_data.ipynb`
2. VS Code will ask you to select a kernel — choose **Python 3 (ipykernel)**
3. Run **Step 1** (loads libraries) and **Step 2** (lists all available datasets)
4. Scroll through the dataset list and **find one that interests you**
5. Copy its `id` value (a long string like `0ff18b56-0a4f-4ac3-a198-197aa48cc9e1`)

> 💡 Pick something relevant to your work — health, population, education, economics.

---

### 4.2 — Paste your Dataset ID and fetch the data

In **Step 3** of the notebook, you'll see this line:

```python
DATASET_ID = "PASTE_YOUR_DATASET_ID_HERE"
```

1. Delete `PASTE_YOUR_DATASET_ID_HERE` and paste the `id` you copied (keep the quotes!)
2. Run the cell — it will fetch your chosen data from the Stats Wales API

If you get an error, check that:

- The ID is pasted correctly (no extra spaces)
- The quotes are still there around the ID

---

### 4.3 — Customise your chart (the fun part!)

In **Step 4** of the notebook, you'll see some clearly marked lines you can edit:

```python
# ✏️ CUSTOMISE THESE — change the title, colours, or labels!
CHART_TITLE = "My Stats Wales Chart"
Y_LABEL = "Value"
BAR_COLOURS = ["#007C45", "#D40000"]  # Welsh green and red
```

Try changing:

- The **chart title** to something meaningful for your data
- The **colours** — try `"#1f77b4"` (blue) or `"#ff7f0e"` (orange)
- The **Y-axis label** to describe what's being measured

After editing, re-run that cell (`Shift+Enter`) to see your changes!

> 💡 **Copilot tip:** Highlight the chart code and press `Ctrl+I`. Try: _"Change this to a horizontal bar chart"_ or _"Add a legend"_

---

### 4.4 — Commit your changes (this is the key skill!)

Now practise the Git workflow:

1. Open the **Source Control panel** (branch icon in the left sidebar)
2. You'll see your changed files listed
3. Click **+** next to each file to stage it
4. Type a commit message: `"Add Stats Wales chart for [your dataset]"`
5. Click **✓ Commit**, then **Sync Changes**

> 💡 **Try this cycle:** customise something small → re-run the cell → commit with a descriptive message. Repeat! Each commit is a snapshot you can always go back to.

---

## Module 5 — Publishing Your Dashboard

### 5.1 — How the dashboard works

The `docs/index.html` file is a self-contained HTML dashboard that:

- Lets users enter a Dataset ID and filters
- Calls the Stats Wales API directly from the browser
- Renders the data as a chart (bar, line, or doughnut)
- Shows the data in a table

The notebook you ran in Module 4 also exported a `chart.png` and `data.json` into the `docs/` folder. These are ready for GitHub Pages.

Because it runs entirely in the browser, it works as a static file — perfect for GitHub Pages.

---

### 5.2 — Customise your dashboard

Open `docs/index.html` and make it yours! Some easy changes:

1. **Change the title** — Find `Stats Wales Open Data Dashboard` and update it
2. **Change the default Dataset ID** — Find the `value="0ff18b56-..."` attribute and replace it with your dataset's ID
3. **Change colours** — The Welsh Government green is `#007C45` and red is `#D40000`. Try other colours!
4. **Add a description** — Add a `<p>` tag under the header to describe what your dashboard shows

> 💡 **Copilot tip:** Highlight a section of the HTML and press `Ctrl+I`. Try "Add a footer with today's date and a link to the Stats Wales website."

---

### 5.3 — Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **"Settings"** (top menu)
3. Click **"Pages"** (left sidebar)
4. Under **"Source"**, select **"Deploy from a branch"**
5. Set branch to `main` and folder to `/docs`
6. Click **"Save"**

Wait ~2 minutes, then GitHub will show you your live URL:
`https://YOUR-USERNAME.github.io/YOUR-REPO-NAME/`

🎉 **Your dashboard is now live on the internet!**

---

### 5.4 — Commit and deploy your changes

After customising the dashboard:

1. In Codespaces, open the Source Control panel
2. Stage your changes (notebook files, `docs/index.html`, `docs/chart.png`, `docs/data.json`)
3. Commit with a message like `"Customise dashboard for Welsh health data"`
4. Push to GitHub
5. GitHub Pages will automatically redeploy — give it ~1 minute

---

## Module 6 — Share Your Work! 🎉

You've built something real. Share it!

### Sharing options

**Teams or Slack:**

> "Just completed the Big Data Does GitHub workshop! Built a live dashboard showing [your data topic] from the Stats Wales API. Check it out: [your GitHub Pages URL]"

**LinkedIn:**

> "Excited to share my first GitHub-hosted data dashboard, built using GitHub Codespaces and GitHub Copilot!
>
> Queried the #StatsWales API, visualised the data, and published it as a live page — all without installing anything locally.
>
> Big thanks to the #NHSWales Big Data team for the workshop.
>
> 🔗 [link to dashboard]  
> 🔗 [link to repo]
>
> #DataWales #GitHubCopilot #OpenData #PublicSector"

**Email to your manager:**
Subject: _"New skill + live data dashboard from today's workshop"_

> Hi [Name],
>
> I attended the Big Data Does GitHub workshop today and built a live data dashboard using the Stats Wales API.
>
> The dashboard is hosted here: [your GitHub Pages URL]
> The code is here: [your GitHub repo URL]
>
> I've learned how to use GitHub for version-controlled data analysis and GitHub Codespaces for consistent, zero-setup Python environments. Happy to show you more if useful.

---

## 🔧 Troubleshooting

| Problem                   | Solution                                                                 |
| ------------------------- | ------------------------------------------------------------------------ |
| Codespace won't start     | Try a different browser (Chrome/Edge recommended)                        |
| Notebook kernel not found | Click "Select Kernel" → "Python Environments" → "Python 3"               |
| API returns an error      | Check the Dataset ID — copy it exactly from the API browser              |
| Dashboard shows no data   | Check the browser console (F12) for error messages                       |
| GitHub Pages shows 404    | Wait 2–3 minutes and try again; check Settings → Pages is set to `/docs` |
| `requests` not found      | Run `pip install requests pandas matplotlib` in the terminal             |

---

## 🚀 What Next?

Now that you have the basics, here are some ideas to take this further:

- **Add more datasets** — Fetch multiple Stats Wales datasets and compare them
- **Schedule updates** — Use GitHub Actions to refresh your data automatically every day
- **Add Welsh language support** — Change `lang=en-gb` to `lang=cy-gb` in the API calls
- **Collaborate** — Invite a colleague to your repository and work on it together
- **Go deeper with Python** — Ask Copilot to help you add statistical analysis
- **R users** — The same API works with R's `httr` package!

---

## 📚 Useful Links

| Resource                      | URL                                                                    |
| ----------------------------- | ---------------------------------------------------------------------- |
| Stats Wales API documentation | https://api.stats.gov.wales                                            |
| Browse all datasets           | https://api.stats.gov.wales/v1/?lang=en-gb&page_number=1&page_size=100 |
| GitHub Docs                   | https://docs.github.com                                                |
| GitHub Codespaces Docs        | https://docs.github.com/codespaces                                     |
| GitHub Copilot Docs           | https://docs.github.com/copilot                                        |
| Pandas documentation          | https://pandas.pydata.org/docs                                         |
| Matplotlib gallery            | https://matplotlib.org/stable/gallery                                  |

---

_Built with ❤️ for data professionals across Wales. Zero installs. Zero barriers. Just data._
