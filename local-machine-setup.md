# Local Machine Setup (No Codespace)

This guide sets up the supporting infrastructure to run the workshop labs on **your own
computer**, instead of in a GitHub Codespace. The Codespace does all of this for you
automatically; if you use it, you don't need this file.

Follow the steps in order. Total time is about 15–20 minutes. Commands are grouped by
operating system where they differ — run the block that matches your machine.

> **Windows users:** do everything inside **WSL2** (Ubuntu). Install WSL2 first
> (`wsl --install` in an Administrator PowerShell, then reboot), open the **Ubuntu**
> terminal, and follow the **Linux** instructions below. Running these labs directly in
> PowerShell or CMD is not supported.

---

## What you'll install

| Tool | Why | Labs |
|---|---|---|
| Node.js 20+ & npm | Runs the Claude Code CLI (and the Lab 1–5 / Lab 14 `npm test` demo) | All |
| Claude Code CLI | The tool the whole course is about | All |
| Python 3.10+ & venv | Runs the Lab 10 to-do API and the Lab 11 Agent SDK | 10, 11 |
| Project Python deps | `flask` (Lab 10) and `claude-agent-sdk` (Lab 11) | 10, 11 |

You also need **git** and a **paid Claude account**.

---

## Step 1 — Install Node.js 20+ and the Claude Code CLI

**macOS** (using [Homebrew](https://brew.sh)):
```bash
brew install node git
```

**Linux / WSL2 (Ubuntu/Debian):**
```bash
sudo apt-get update
sudo apt-get install -y git curl
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Then install Claude Code (same on every platform):
```bash
npm install -g @anthropic-ai/claude-code
claude --version          # confirm it prints a version (need v2.1.139+ for /goal)
```

> If `npm install -g` fails with a permissions error, configure a user-level npm prefix
> (`npm config set prefix ~/.npm-global` and add `~/.npm-global/bin` to your `PATH`), or use
> a Node version manager like `nvm`. Avoid `sudo npm install -g`.

---

## Step 2 — Install Python 3.10+

**macOS:**
```bash
brew install python@3.12
```

**Linux / WSL2 (Ubuntu/Debian):**
```bash
sudo apt-get install -y python3 python3-venv python3-pip
```

Confirm:
```bash
python3 --version         # 3.10 or newer
```

> The `python3-venv` and `python3-pip` packages are what provide the `venv` module and
> `pip`. If `python3 -m venv` or `pip` later report "not found," it's almost always because
> one of these isn't installed — re-run the apt line above.

---

## Step 3 — Clone the course repo

```bash
git clone https://github.com/skillrepos/cc-se.git
cd cc-se
```

(Replace the URL if your instructor gives you a different repo.) **Run every remaining
command from inside this `cc-se` directory.**

---

## Step 4 — Create and activate a Python virtual environment

A virtual env keeps the course's Python packages isolated from the rest of your system
(and avoids the "externally-managed-environment" error that newer Python installs raise on
a bare `pip install`).

```bash
python3 -m venv .venv
source .venv/bin/activate
```

After activating, your prompt shows `(.venv)`. **You must re-run `source .venv/bin/activate`
in every new terminal** you open for the labs. To deactivate, run `deactivate`.

> **macOS/Linux note:** the activate command is `source .venv/bin/activate`. (Only relevant
> if you're on native Windows PowerShell, which this course doesn't support — use WSL2.)

---

## Step 5 — Install the Python dependencies

With the venv activated:
```bash
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

This installs `flask` (Lab 10) and `claude-agent-sdk` (Lab 11). Verify:
```bash
python3 -c "import flask, claude_agent_sdk; print('Python deps OK')"
```

---

## Step 6 — Authenticate Claude Code

```bash
claude            # launches the Claude Code TUI
/login            # choose "Log in with Claude account" and complete the browser flow
```

Your credentials are saved to `~/.claude/` and are reused by the Agent SDK in Lab 11 — no
separate auth needed there.

> If `/schedule` (Lab 13 Routines) later prints "Unknown command," you're authenticated with
> an API key instead of a Claude account. Run `unset ANTHROPIC_API_KEY`, restart `claude`,
> and `/login` again.

---

## Step 7 — Verify each lab's supporting infrastructure

Run these from the repo root, with the venv activated, to confirm everything works before
class:

```bash
# Lab 10 — the to-do API tests should run and report failures (that's expected;
# the /goal lab is what fixes them):
python3 app/test_app.py            # expect "10 passed, 4 failed"

# Lab 11 — the Agent SDK imports:
python3 -c "import claude_agent_sdk; print('Agent SDK OK')"

# Lab 7 — the MCP reference server is fetchable via npx (Ctrl+C to stop it):
npx -y @modelcontextprotocol/server-everything --help
```

If all three run, your machine is ready.

---

## Keeping the repo clean

The virtual env and a couple of lab artifacts should not be committed. If they aren't
already in `.gitignore`, add them:

```bash
printf '.venv/\nbuild-status.txt\n__pycache__/\n' >> .gitignore
```

---

## Troubleshooting

**`pip: command not found`** — Use `python3 -m pip ...` instead of a bare `pip`, and make
sure `python3-pip` is installed (Step 2). Inside an activated venv, `pip` is available
directly.

**`error: externally-managed-environment`** — You're installing into the system Python.
Activate the venv (Step 4) and reinstall; the venv is exactly what avoids this.

**`ModuleNotFoundError: No module named 'flask'`** — The venv isn't activated, or deps
aren't installed. Run `source .venv/bin/activate` then `python3 -m pip install -r
requirements.txt`.

**`claude: command not found`** — npm's global bin directory isn't on your `PATH`. Run
`npm bin -g` to find it and add that directory to your `PATH`.

**A new terminal "forgot" the environment** — venvs are per-shell. Re-run
`source .venv/bin/activate` in each new terminal used for the labs.
