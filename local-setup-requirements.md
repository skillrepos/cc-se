# Local Machine Requirements — Claude Code 1.5-Day Course
### (All 21 Labs, Days 1–3)

Use this if you're running labs **directly on your laptop** rather than in a GitHub Codespace. The Codespace handles all of this for you automatically — if you're using that path, you only need items in the [Account & Subscription](#account--subscription) section.

---

## Account & Subscription

| Requirement | Notes |
|---|---|
| **Claude paid account** | Pro, Max, Team, or Enterprise — any paid plan. Free accounts cannot use Claude Code. |
| **GitHub account** | Required for Lab 12 (GitHub Actions). A free account is sufficient. |

---

## Operating System

| Platform | Status |
|---|---|
| macOS | Fully supported |
| Linux | Fully supported |
| Windows | Requires **WSL2**; run all lab commands inside the WSL2 terminal |

---

## Software to Install

### Core Tools

| Tool | Min Version | Install |
|---|---|---|
| **Node.js** | 20 LTS | [nodejs.org](https://nodejs.org), `brew install node`, or `nvm install 20` |
| **npm** | bundled with Node | Ships with Node — no separate install needed |
| **npx** | bundled with Node | Ships with Node — used in Lab 7 to run the MCP reference server |
| **Python** | 3.10 | [python.org](https://python.org) or `brew install python` |
| **pip** | bundled with Python | Ships with Python 3.10+ |
| **Git** | any recent | [git-scm.com](https://git-scm.com) or `brew install git` |
| **jq** | 1.6 | `brew install jq` / `sudo apt install jq` — required for hook scripts (Lab 6) and JSON extraction (Lab 9) |

### Claude Code CLI

```bash
npm install -g @anthropic-ai/claude-code
```

Verify the install and check the version:

```bash
claude --version
```

**Minimum version: v2.1.72** — required for `/loop` and `/schedule` (Lab 13). If your version is older, update with `npm install -g @anthropic-ai/claude-code` again.

### VS Code

Required for Lab 11's diff-merge steps (`code -d skeleton.py answer.txt`). Recommended for all labs.

1. Install from [code.visualstudio.com](https://code.visualstudio.com)
2. Open VS Code → Command Palette (`Cmd/Ctrl+Shift+P`) → **"Shell Command: Install 'code' command in PATH"**
3. Verify: open a terminal and run `code --version`

Recommended extensions (install from the Extensions panel):
- ESLint (`dbaeumer.vscode-eslint`)
- Prettier (`esbenp.prettier-vscode`)
- Claude Code (`anthropic.claude-code`)

### Claude Desktop App

Required for **Day 3** (Labs 15–21). Cowork mode (Labs 17–21) is only available in the Desktop app.

1. Download from [claude.ai/download](https://claude.ai/download)
2. Install and sign in with the **same paid Claude account** you use for Claude Code

---

## Course Repo Setup

Clone the repo. The root `package.json` ships with the repo and defines `npm test` (used in Lab 10) as `node user.test.js` — no dependency install is required:

```bash
git clone https://github.com/skillrepos/ccode-long.git
cd ccode-long
```

---

## Python Agent SDK (Lab 11)

```bash
pip install claude-agent-sdk
```

---

## First-Time Authentication

On first launch, Claude Code needs to be connected to your Claude subscription:

```bash
claude          # launches Claude Code TUI
/login          # choose "Claude account with subscription" and follow the OAuth flow
```

Your credentials are saved to `~/.claude/` and automatically carry over to the Agent SDK (Lab 11) — no separate auth needed there.

---

## Checklist

- [ ] Paid Claude account (Pro / Max / Team / Enterprise)
- [ ] GitHub account
- [ ] Node.js 20 LTS or later
- [ ] Python 3.10 or later
- [ ] Git
- [ ] jq
- [ ] Claude Code CLI (`npm install -g @anthropic-ai/claude-code`), version ≥ v2.1.72
- [ ] VS Code with `code` command in PATH
- [ ] Claude Desktop app (signed in)
- [ ] Course repo cloned
- [ ] Course repo cloned (ships `package.json` for `npm test` in Lab 10 — no install needed)
- [ ] `pip install claude-agent-sdk`
- [ ] Claude Code authenticated (`claude` → `/login`)
- [ ] *(Windows only)* WSL2 installed and configured

---

## Lab-by-Lab Dependency Reference

| Lab | Day | Extra dependencies |
|---|---|---|
| 1–5 | 1 | Node.js, npm (hello.js, user.js, package.json) |
| 6 | 1 | jq (PreToolUse hook script), bash |
| 7 | 1 | npx (MCP reference server: `@modelcontextprotocol/server-everything`) |
| 8–9 | 2 | jq (JSON extraction from `claude -p --output-format json`) |
| 10 | 2 | npm test (`node user.test.js`; `package.json` ships with repo, no install) |
| 11 | 2 | Python 3.10+, `pip install claude-agent-sdk`, VS Code with `code` in PATH |
| 12 | 2 | GitHub account |
| 13 | 2 | Claude Code v2.1.72+ for `/loop` and `/schedule`; claude.ai subscription for Routines |
| 14 | 2 | claude.ai in browser (for cloud sessions and teleport) |
| 15–21 | 3 | Claude Desktop app; claude.ai in browser; Codespace still needed for capstone (Lab 21) |

> **Note on Routines (Lab 13):** Cloud Routines run on Anthropic infrastructure and require a claude.ai subscription login with Claude Code on the web. They are currently in research preview and may not be available on all accounts.

> **Note for Windows users:** The hook scripts in Lab 6 are bash scripts. They require WSL2 or Git Bash. Running Claude Code itself inside WSL2 is the simplest path — everything works natively there.

