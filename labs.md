# AI-Powered Coding with Claude Code
## Learn practical workflows, hands-on coding techniques, and structured interactions
## Session Labs — 1.5-Day Edition (3 sessions x 4.5 hours)
## Revision 6.5 - 06/22/26

<br><br>

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**Copy and paste may not work as expected if using the mouse. If not, use the keyboard shortcuts - *Ctrl+C/Cmd+C and Ctrl+V/Cmd+V*.**

**If you haven't done so already, set your model to `Sonnet` instead of `Opus`.**

> In Claude Code at the prompt, type:
> ```
> /model
> ```
> In the list that comes up, type "2" or use the arrow keys to move the pointer to "2" and hit *Enter*. Also use the left/right arrow keys to set the thinking mode to *medium*.
>
> ![set model](./images/ccode209.png?raw=true "set model")
>
> You should see an indicator that the model was set to *claude-sonnet-4-6*.
>
> **Note:** As of Claude Code 2.1.153, your `/model` selection is saved as the default for new sessions. To set a model for the current session only, press `s` in the model list.
>
<br><br>


---
<br><br>

# Lab 1: Introduction to Claude Code and Basic Setup
## Lab Purpose
Get familiar with Claude Code basic command-line interface. You'll learn how to execute your basic commands in Claude Code.

---
<br><br>

## 1: Test Basic Interaction
**What we're doing:** Verifying Claude can respond to simple queries.  
**Why:** This confirms the connection is working properly.

**Action:** At the Claude prompt, type the prompt below and hit *Enter*. While that is running, hit *Ctrl+o* to have Claude show its thinking process.
```
Hello Claude, can you tell me what you can help with?
```

Claude should respond with information about its capabilities preceded by its thinking process.

![Initial prompt](./images/ccode210.png?raw=true "Initial prompt")


---
<br><br>

## 2: Ask Claude to Explain a Code Snippet
**What we're doing:** Testing Claude's code understanding capabilities.  
**Why:** Understanding code is a fundamental Claude Code feature.

**Action:** Type the following:
```
Explain this code: console.log([1,2,3].map(x => x * 2))
```

Claude will explain the JavaScript array operation.

![Initial prompt](./images/ccode211.png?raw=true "Initial prompt")

---
<br><br>

## 3: Create Your First File with Claude
**What we're doing:** Using Claude to generate a simple code file.  
**Why:** File creation is a core feature for development workflows.

**Action:** Type:
```
Create a simple hello.js file that prints "Hello from Claude Code!"
```

Claude will create the file and *may* show you the content in the diff above the terminal. You do not need to do anything in the diff area. Just select option 1 in the terminal where Claude is waiting.

![Initial file creation](./images/ccode86.png?raw=true "Initial file creation")

---
<br><br>

## 4: View the Created File
**What we're doing:** Verifying the file was created successfully.  
**Why:** Understanding where Claude saves files is important.

**Action:** The file should be created and the diff closed. You can click on the file on the left to see the contents. Or, alternatively, in a new terminal tab (keep Claude running), type:
```bash
ls -la
cat hello.js
```

You should see your new file and its contents.

![Initial file creation](./images/ccode87.png?raw=true "Initial file creation")

---
<br><br>

## 5: Ask Claude to Run the File
**What we're doing:** Having Claude execute the code it created.  
**Why:** Claude can run commands and show output directly.

**Action:** Back in Claude, type the prompt below. You'll see the run started and then you'll be prompted for permission to proceed. Just select option 1.
```
Run the hello.js file we just created
```

![Run file](./images/ccode88.png?raw=true "Run file")

You'll see the output: "Hello from Claude Code!"

![Run file](./images/ccode89.png?raw=true "Run file")

---
<br><br>

## 6: Exit and Resume
**What we're doing:** Learning how to properly exit and resume sessions.  
**Why:** You'll often need to pause and continue work later.

**Action:** 
1. Type `exit` to exit Claude
2. Restart with: `claude --resume`
3. You'll see a list with your session at the top. Just hit *Enter* to resume.
4. Claude will restore your previous session context

![Resume session](./images/cc-se3.png?raw=true "Resume session")

---
<br><br>

## 7: Creating a second file
**What we're doing:** Creating a second file for additional context.  
**Why:** We want to learn more about resume.

**Action:** Type the following. When you are prompted to continue, **select option 3 to tell Claude to do something different.**
```
Create a simple goodbye.js file that prints "Goodbye from Claude Code!"
```

Claude will create the file and show you the content in the diff above the terminal. You do not need to do anything in the diff area. Just select option 3 in the terminal where Claude is waiting.

![Do something different](./images/ccode92.png?raw=true "Do something different")


---
<br><br>

## 8: Redo
**What we're doing:** Redoing our command.  
**Why:** We want to learn how to do redo a request.

**Action:** You'll see the previous rejected operation message above the prompt area. Use the `up arrow` key to bring up the last prompt. Change the name of the file in the prompt from *goodbye.js* to *goodbye.py* to create a Python file instead. Hit *Enter*.
```
Create a simple goodbye.py file that prints "Goodbye from Claude Code!"
```

Claude will create the file and show you the content in the diff above the terminal. Once Claude generates it and prompts whether to continue, select 1 to proceed.

---
<br><br>

## 9: Use @ Mentions to Pull Context
**What we're doing:** Using the @ shortcut to bring files into Claude's context on demand.  
**Why:** @ mentions let you reference specific files, folders, or URLs without copy-pasting.

**Action:** Type the following — notice the @ symbol before the filename:
```
What does @hello.js do? Can you add a timestamp to it?
```

Claude will pull hello.js into its context and explain it before making changes. It will display the changes and ask for approval. You can just select the *Yes* option.

After this, there will probably be a suggestion in lighter ("ghost") text to run the file. If you'd like to execute that suggestion, you can just hit *Tab* and then return and approve the command.

![Ref file by mention](./images/ccode212.png?raw=true "Ref file by mention")

**Note that you can also use @folder/ to reference entire directories and @https://url for web content.**

---
<br><br>

## 10: Try the # Memory and Bash ! shortcuts
**What we're doing:** Using keyboard shortcuts to create memories and run shell commands inline.  
**Why:** These shortcuts speed up common operations without leaving Claude Code.

**Action:** First, try the # shortcut to create a memory. Type:
```
# This project uses JavaScript and Python for demos
```

Claude will save this to a MEMORY.md file as a persistent memory.


![Create memory](./images/ccode213.png?raw=true "Create memory")

Now try the ! shortcut to run a bash command directly to look at the memory file that just got created:
```
! cat ~/.claude/projects/-workspaces-cc-se/memory/MEMORY.md
```

This runs the shell command and shows output without a separate terminal.

![Shell command](./images/ccode214.png?raw=true "Shell command")


---
<br><br>

## 11: Explore the Codebase with Questions
**What we're doing:** Asking Claude questions about the files we've created.  
**Why:** Codebase exploration is one of Claude Code's most powerful everyday uses.

**Action:** Type:
```
What files have we created so far? Summarize the purpose of each one and suggest an improvement.
```

Claude will scan the working directory, list the files, and provide analysis. This is how developers use Claude Code for orientation — jumping into a new codebase and asking "What does this project do?" or "How is this function used?"

![File info](./images/ccode215.png?raw=true "File info")

---
<br><br>

## 12: Exit

**Action:** In prep for the next lab and a fresh start, type `exit` to exit Claude Code.

```
exit
```

## Lab Summary
✅ You've successfully:
- Verified Claude Code installation
- Authenticated your account
- Created and executed code with Claude
- Learned basic navigation and commands
- Practiced session management
- Used @ mentions, # memory, and ! bash shortcuts
- Explored a codebase with natural language questions

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 2: Working with Claude Code Modes
## Lab Purpose
Master Claude Code's different operating modes including default mode, plan mode, and auto-accept mode. Learn when and how to use each mode effectively for different development scenarios.

---
<br><br>

## 1: Understand Default Mode 
**What we're doing:** Starting Claude in its standard interactive mode.  
**Why:** Default mode gives you full control with permission prompts for each action.

**Action:** Start Claude with model Sonnet and medium effort (Note: You can use these command line options if you want for other places you start Claude in the labs.)
```bash
claude --model sonnet --effort medium
```

You're now in default mode where Claude asks permission before file changes.

---
<br><br>

## 2: Test Default Mode Permissions
**What we're doing:** Creating a file to see permission prompts in action.  
**Why:** Understanding permission flow helps you maintain control over changes.

**Action:** Type:
```
Create a config.json file with database connection settings for Postgresql
```

Notice how Claude asks permission before creating the file as we've seen before. Type `1` to accept.


![Creating config.json](./images/ccode216.png?raw=true "Creating config.json")

---
<br><br>

## 3: Activate Plan Mode
**What we're doing:** Switching to Plan Mode for complex task planning.  
**Why:** Plan Mode helps Claude think through multi-step tasks before executing.

**Action:** Press `Shift+Tab` until you see *Plan mode*

![Activating plan mode](./images/ccode96.png?raw=true "Activating plan mode")


---
<br><br>

## 4: Prompt for a complex task
**What we're doing:** Prompting Claude for complex task planning.  
**Why:** Plan Mode helps Claude think through multi-step tasks before executing.

**Action:** Type:

```
Create a basic user profile page with fields for name, email, and profile picture upload. 
```

![Planning](./images/ccode98.png?raw=true "Planning")

Claude will start creating a detailed plan before starting implementation.

---
<br><br>

## 5: Respond to questions
**What we're doing:**  Responding to questions from Claude
**Why:** Claude needs our input on some things before proceeding.

**Action:** Read any questions that come up and select number of answer to proceed if single option for answer. (To save time and complexity, it is recommended to use the recommended/simplest option.) If you can select multiple options, use arrow keys and space/Enter to select options. Then move on to next question using right arrow. Answer all questions and then move to *Submit* and press *Enter*. If you want to see more of Claude's *thinking* during this process, press *ctrl+o".

![Responding to questions](./images/ccode217.png?raw=true "Responding to questions")


![Responding to questions](./images/ccode218.png?raw=true "Responding to questions")


---
<br><br>

## 6: Review the Plan
**What we're doing:** Interacting with Claude's proposed plan.  
**Why:** You can review plans before execution to ensure desired outcomes.

**Action:** After Claude presents the plan, you could modify it if you wanted by selecting `ctrl+g`. 
1. Go ahead and select that key sequence (ctrl+g) to bring the plan up in the editor.
2. (Optional) To see the markdown version of the plan (if you're in VS Code, you can right-click and select *Reopen Editor with ... Text Editor*).
3. After you're done reviewing it, you can close the file (close the original file if you also opened a preview version).
4. Then **select option 1** to proceed and auto-accept edits. 

![Reviewing plan](./images/ccode102.png?raw=true "Reviewing plan")

![Approving plan](./images/ccode219.png?raw=true "Approving plan")

**Note that you are now in a different mode, but the original task will still run under *plan* mode.**

---
<br><br>

## 7: View to-do list
**What we're doing:** Monitoring the progress through the to-do list.  
**Why:** Helps you understand what is done and what is left to be done.

**Action:** While Claude Code is doing the implementation, hit `ctrl+t` to see the current state of the to-do list. (If the implementation is already done, you can just skip this step and try it on a future implementation.)

```
ctrl+t
```

![Viewing to-do list](./images/ccode103.png?raw=true "Viewing to-do list")

---
<br><br>

## 8: When done, clear the Conversation
**What we're doing:** Using /clear to start fresh.  
**Why:** Clearing context helps when switching between unrelated tasks.

After a few minutes, Claude Code will be done and provide you a summary. It may ask if you want it to do additional tasks, but you can just ignore those.

![Plan completed](./images/ccode220.png?raw=true "Plan completed")

Now, let's clear the context.

**Action:** Type:
```
/clear
```

Your conversation history is now cleared, giving you a clean slate.

---
<br><br>

## 9: Check Out Auto Mode
**What we're doing:** Looking at the newer *Auto* permission mode.  
**Why:** Auto mode replaces many manual permission prompts with a background classifier that approves routine, safe actions and stops for risky ones. It sits between supervised editing and bypass permissions, and is what unattended/agentic workflows (Day 2) build on.

**Action:** If not already on *auto mode*, press `Shift+Tab` repeatedly and watch the mode indicator cycle. Along with the modes we've used, you should see **auto mode**. The official mode set is now: *supervised editing* (default) → *accept edits* → *plan* → *auto* → *bypass permissions*. Stop cycling when you get back to your previous mode — we'll use bypass next.

---
<br><br>

## 10: Try YOLO Mode (Auto-Accept)
**What we're doing:** Running Claude with automatic permission granting.  
**Why:** This speeds up development when you trust Claude's actions.

**Action:** Exit Claude (`exit`), then restart with the command below and **use option 2** to accept the risk:

```bash
claude --dangerously-skip-permissions
```

![Accepting bypass mode](./images/ccode184.png?raw=true "Accepting bypass mode")

If you don't see the mode as **bypass permissions on** mode, use `Shift+Tab` to change the mode until you see that.

We also have an alias for this that you can use in the future `claude-yolo` if you are in a terminal other than the starting one.

⚠️ **Note:** Use with caution! Claude won't ask before making changes.

![YOLO](./images/ccode123.png?raw=true "YOLO")

---
<br><br>

## 11: Test Auto-Accept Mode
**What we're doing:** Creating multiple files without interruption.  
**Why:** See how much faster development is without permission prompts.

**Action:** Type:
```
Create a simple To-Do list app in javascript wtih functionality to add and delete tasks
```

Notice Claude creates all files without asking for permission.

![YOLO](./images/ccode221.png?raw=true "YOLO")

---
<br><br>

## 12: Exit

**Action:** In prep for the next lab and a fresh start, type `exit` to exit Claude Code.

```
exit
```

## Lab Summary
✅ You've successfully learned:
- Default (supervised editing) mode with permission prompts
- Plan mode for complex task planning
- Auto mode's classifier-based permissions
- Auto-accept and bypass modes for rapid development


---

<br><br>
---
## END OF LAB
---
<br><br>

**NOTE:** From here on, you can use the `claude --dangerously-skip-permissions` mode if you want to avoid having to respond to most prompts. For convenience, if working in the codespace, there is a shortcut alias for this setup:  `claude-yolo`. You must be in a terminal other than the original one that you started with to use this.

<br><br>

# Lab 3: Built-in Commands and Context Management
## Lab Purpose
Master Claude Code's built-in slash commands for managing conversations, context, and memory. Learn how to effectively manage long coding sessions and optimize token usage.

---
<br><br>

## 1: Start Fresh with Claude
**What we're doing:** Beginning a new Claude session to explore commands.  
**Why:** Starting fresh ensures we have a clean context for learning.

**Action:** Start Claude:
```bash
claude
```

---
<br><br>

## 2: View Available Commands
**What we're doing:** Discovering all built-in slash commands.  
**Why:** Knowing available commands improves your workflow efficiency.

**Action:** Type:
```
/help
```

Hit *Enter*. This will bring up a set of *tabbed* output for help. Use the *tab* key to get to the *commands* section at the top. Then you can use the arrow keys to move up and down to see all the commands.
Review the list including /clear, /compact, /rewind, /model, and others.

![help to see commands](./images/ccode222.png?raw=true "help to see commands")

Use *Esc* to exit when done.

---
<br><br>

## 3: Create Some Context
**What we're doing:** Building up conversation history to practice management.  
**Why:** We need content to demonstrate context management commands.

**Action:** Have a multi-turn conversation. **Type each of the following into the prompt area one at a time and let each complete before entering the next one** (When prompted about accepting an edit, you can just choose to accept or accept all edits in the session.):
```
Create a user.js file with a User class
```

Wait for this to finish, then...

```
Add methods for getName and setName  
```

Wait for this to finish, then...

```
Add email validation to the User class
```

Wait for this to finish, then...

```
Create a test file for the User class
```

Let Claude complete each task to build up context.


![help to see commands](./images/ccode223.png?raw=true "help to see commands")

---
<br><br>

## 4: Check Context Usage
**What we're doing:** Understanding how much context we're using.  
**Why:** Managing context prevents hitting token limits in long sessions.

**Action:** Type:
```
/context
```

Scroll back up to the start of the output. You'll see information about current token usage and remaining capacity.


![context command](./images/ccode224.png?raw=true "context command")

---
<br><br>

## 5: Compact the Conversation
**What we're doing:** Condensing conversation history while preserving key information.  
**Why:** Compacting extends how long you can work without losing context.

**Action:** Type:
```
/compact Keep the User class implementation details and test structure
```

Claude will summarize earlier parts while keeping specified information.


![compact](./images/ccode225.png?raw=true "compact")

---
<br><br>

## 6: Use Rewind Feature
**What we're doing:** Rolling back to a previous state in the conversation.  
**Why:** Rewind lets you undo mistakes or explore different approaches.

**Action:** 
a. Ask Claude: `Delete the test file we created`
b. After deletion, press `Esc` twice or type `/rewind`
c. Select the point before deletion (the *compact*) to restore **by using the up and down arrow to navigate between the checkpoints** listed and then press `Enter`.


![rewind](./images/ccode34.png?raw=true "rewind")

d. Respond to the clarification question to restore both the code and the conversation.


![rewind](./images/ccode35.png?raw=true "rewind")

e. You should see the file and the conversation restored. You can use backspace or hit `Esc` twice to clear out any commands showing up in Claude.

---
<br><br>


## 7: Create a project context file
**What we're doing:** Setting up a CLAUDE.md file for project context.  
**Why:** CLAUDE.md provides persistent project knowledge across sessions.

**Action:** Type:
```
/init
```

This file will be automatically created and read in future sessions.

![claude.md](./images/ccode226.png?raw=true "claude.md")

Afterwards, you can take a look at the file by opening it up in an editor (you can use 'code' command if in VS Code or Codespace).

You'll probably notice that it identifies custom slash commands, custom agents, and custom skills that we have in the `extra` directory. While it is finding those kind of files there, it is NOT registering them as something usable. It is just describing the file types.

---
<br><br>

## 8: Demonstrate the project context file is used
**What we're doing:** Resetting chat while keeping project guidance.  
**Why:** Persistent memory improves continuity across sessions. Also shows difference between chat context and project files.

**Action:**
1. Type `/clear` to clear the conversation
2. Ask: `What are our project rules and what test command should I run after code edits?`

Claude should recall information from the CLAUDE.md file and display that info.


![claude.md](./images/ccode227.png?raw=true "claude.md")

---
<br><br>

## 9: View the Memory Hierarchy with /memory
**What we're doing:** Visualizing how CLAUDE.md memory is organized across scopes.  
**Why:** Understanding the memory hierarchy helps you structure project knowledge effectively.

**Action:** Type:
```
/memory
```

You'll see a visualization of how memory is layered: enterprise (if applicable) → user-level → project-level. The CLAUDE.md file you just created with `/init` appears at the project level. Note that CLAUDE.md files in nested subdirectories are automatically pulled in too, and you can create a CLAUDE.local.md for personal overrides that don't get committed to git.

![claude.md](./images/ccode228.png?raw=true "claude.md")

---
<br><br>

## 10: Explore Git History with Claude
**What we're doing:** Using Claude to analyze changes in the repository.  
**Why:** Claude Code excels at navigating and explaining code history.

**Action:** Type:
```
What changes have been made in this repo recently? Summarize the git log.
```

Claude will run git commands and summarize the commit history in natural language. This is a powerful pattern for onboarding — instead of reading through git logs manually, ask Claude to explain what changed and why.

![claude.md](./images/ccode229.png?raw=true "claude.md")

---
<br><br>

## 11: Try Headless Mode with Pipe Input
**What we're doing:** Using Claude Code as a Unix utility with piped input.  
**Why:** Headless/pipe mode lets you chain Claude into scripts and automation workflows.

**Action:** Exit Claude first with `exit`, then run this in your regular terminal:
```bash
echo "What files are in this directory?" | claude -p
```

The `-p` flag runs Claude in print (headless) mode — it takes input from stdin, processes it, and outputs the result. No interactive session needed. This is how you integrate Claude into shell scripts, CI pipelines, and automated workflows. We'll go much deeper on this in Day 2, where headless mode becomes the foundation for writing *loops* instead of single prompts.

> **Heads-up on usage:** Starting June 15, 2026, headless/SDK and GitHub Actions usage is metered separately from interactive Claude Code on subscription plans (separate weekly token pools). Worth knowing before you start automating!

![claude.md](./images/ccode230.png?raw=true "claude.md")

---
<br><br>


## Lab Summary
✅ You've mastered:
- Using /help to discover commands
- Managing context with /compact
- Undoing changes with /rewind
- Switching models with /model
- Creating persistent memory with CLAUDE.md
- Viewing memory hierarchy with /memory
- Exploring git history with natural language
- Using headless pipe mode for automation


<br><br>
---
## END OF LAB
---
<br><br>
# Lab 4: Skills + Subagents 
## Lab Purpose 
Build one practical skill and two specialist subagents to see how delegation keeps work fast and clean.

**NOTE: If using the codespace setup, you can use the `code` command to create/edit a file.**

---
<br><br>

## 1: Create the Project Structure
**What we're doing:** Creating the folders used by Claude Code for skills and agents.  
**Why:** Skills/subagents are file-system discoverable.

**Action:**
```bash
mkdir -p .claude/skills/api-checker/scripts
mkdir -p .claude/agents
```

---
<br><br>

## 2: Create a Minimal Skill (api-checker)
**What we're doing:** Writing a SKILL.md with a focused purpose.  
**Why:** Skills help Claude apply repeatable expertise automatically.

**Action:** Make a new file `.claude/skills/api-checker/SKILL.md`.

**Action:** Copy/paste the following contents into the file and save it.

```md
---
name: api-checker
description: When the user asks to validate a REST endpoint, generate a curl test, run it, and summarize status + key fields.
---

## Rules

- Ask for the base URL if missing.
- Run `scripts/check.py <url>` to fetch the endpoint and get structured JSON output.
- Parse the output: use `ok` for success/failure, `status` for HTTP code, `json` for the response body.
- Keep output short: status, 3 key fields, and one recommendation.

## Example trigger

User: "Can you validate GET /health on my service?"
```

![Creating the skill](./images/ccode196.png?raw=true "Creating the skill")

---
<br><br>

## 3: Add the referenced script to the Skill
**What we're doing:** Adding a deterministic helper.  
**Why:** Scripts make results more predictable than pure prompting.

**Action:** Make a new file `.claude/skills/api-checker/scripts/check.py`.

**Action:** Copy/paste the following contents into the file and save it.


```python
#!/usr/bin/env python3
import json, sys, urllib.request

url = sys.argv[1] if len(sys.argv) > 1 else None
if not url:
    print("Usage: check.py <url>")
    sys.exit(2)

req = urllib.request.Request(url, headers={"Accept":"application/json"})
try:
    with urllib.request.urlopen(req, timeout=10) as r:
        status = r.status
        body = r.read().decode("utf-8", errors="replace")
except Exception as e:
    print(json.dumps({"ok": False, "error": str(e)}))
    sys.exit(1)

out = {"ok": 200 <= status < 300, "status": status}
try:
    out["json"] = json.loads(body)
except Exception:
    out["body_preview"] = body[:200]
print(json.dumps(out))
```

Then make it executable:
```bash
chmod +x .claude/skills/api-checker/scripts/check.py
```

---
<br><br>

## 4: Create the Planner Agent
**What we're doing:** Creating a “plan-first” helper.  
**Why:** This keeps your main chat focused on decisions, not long plans.

> **Terminology note:** The file in `.claude/agents/` defines an *agent configuration*. When Claude delegates to it during a conversation, it runs as a *subagent* — a separate context that does work and returns results to the main conversation.

**Action:** Make a new file `.claude/agents/planner.md`.

**Action:** Copy/paste the following contents into the file and save it.

```md
---
name: planner
description: Create a short implementation plan + risks. Do not edit files.
model: sonnet
---

## Instructions
- Ask 1-2 clarifying questions only if required.
- Output a 5-step plan.
- List 3 risks.
- Do not write or modify files.
```

---
<br><br>

## 5: Create the Test-Runner Agent
**What we're doing:** Creating a “run tests, summarize, propose minimal fix” helper.  
**Why:** Subagents reduce context noise and speed up troubleshooting.

**Action:** Make a new file `.claude/agents/test-runner.md`.

**Action:** Copy/paste the following contents into the file and save it.


```md
---
name: test-runner
description: Run tests, summarize failures, propose minimal fixes.
model: sonnet
---

## Instructions
- Run the project test command (ask if unknown).
- Summarize failures in 3 bullets.
- Propose the smallest fix, then implement only if approved.
```

---
<br><br>

## 6: Start Claude Code
**Action:**
```bash
claude
```

---
<br><br>

## 7: Trigger the skill (Without Naming It)
**What we're doing:** Letting Claude choose the skill automatically.  
**Why:** Skills are intended to be invoked based on context.

**Action:** In Claude, type:
```
Please validate https://jsonplaceholder.typicode.com/posts/1 and summarize what you find.
```

If Claude asks for approval to run scripts, approve it.

(Optional: You can open the .claude/skills/api-checker/SKILL.md file to remember what it specifies.)

What you should see in the output is that the skill was selected and loaded, then, per the skill instructions:

- The supporting script was run
- The status was reported
- Key fields were listed
- A recommendation was provided

![Using the skill](./images/ccode231.png?raw=true "Using the skill")


---
<br><br>

## 8: Use the Planner Subagent
**What we're doing:** Delegating planning to a subagent that cannot edit files.  
**Why:** This is a safe and scalable “team” pattern.

**Action:** In Claude, type:
```
Use the planner subagent.
We need to add input validation to the User class without changing public behavior.
Return only the plan + risks.
```
(Optional: You can open the .claude/agents/planner.md file to remember what it specifies.)

What you should see after this runs is a plan produced by the agent that, per the planning agent spec:

- Outputs a step-by-step plan
- Lists several risks


![Using the planning subagent](./images/ccode198.png?raw=true "Using the planning subagent")


---
<br><br>

## 9: Use the Test-Runner Subagent
**What we're doing:** Delegating test execution + fix suggestion.  
**Why:** This is the most common “AI teammate” workflow.

**Action:** In Claude, type:
```
Use the test-runner subagent.
Create one minimal failing test for invalid email handling in user.js, then propose the smallest fix.
Stop after proposing the fix (do not implement yet).
```

(Optional: You can open the .claude/agents/test-runner.md file to remember what it specifies.)

![Using the test-runner subagent](./images/ccode232.png?raw=true "Using the testrunner subagent")

What you should see after this runs is a failing email test added to user.test.js and a proposed fix.

![Using the test-runner subagent](./images/ccode233.png?raw=true "Using the testrunner subagent")

You can choose to accept the fix (make the edit) or not.

---
<br><br>

## 10: Exit Claude Code
**Action:**
```
exit
```

---
<br><br>

## Lab Summary
✅ You’ve built and used:
- A project Skill (SKILL.md + script)
- Two subagents (planner + test-runner)
- A safe delegation workflow (plan-first, test-first)

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 5: Supervised Subagent Workflow + Plugin Packaging + VS Code
## Lab Purpose
Turn your commands + agents + skills into a shareable "team kit," and practice a supervised delegation workflow where you orchestrate specialist subagents step by step.

---
<br><br>
## 1: Add a Team Command: /ship
**What we're doing:** Creating a standardized "ready to ship" checklist command.  
**Why:** To have a reusable standardized command that encompasses multiple functions.

**Action:** Make a new file `.claude/commands/ship.md`.

**Action:** Copy/paste the following contents into the file and save it.

```md
---
description: Ship checklist: review, tests, and summary
---
Do the following in order:
1) Summarize what changed (3 bullets) using git status/diff
2) Run tests (ask for the command if unknown)
3) List 3 risks and 3 follow-ups
Do not edit files unless asked.
```
---
<br><br>

## 2: Add the Reviewer Agent
**What we're doing:** Adding a "review-only" specialist agent definition.  
**Why:** We want a reviewer as part of our workflow.

> **Tooling note:** This agent is structurally restricted from editing files — not just told not to, but actually blocked from using Write and Edit tools. This is the difference between a prompt-level constraint (which Claude can override) and a tool-level constraint (which it cannot).

**Action:** Make a new file `.claude/agents/reviewer.md`.

**Action:** Copy/paste the following contents into the file and save it.

```md
---
name: reviewer
description: Review code changes for correctness, tests, and security. Do not edit files.
model: sonnet
disallowedTools: Write, Edit
---
## Instructions
- Review the diff and changed files.
- Output: 3 risks, 3 tests to add, 3 patch suggestions.
- Do not modify files.
```

> **What changed from Lab 4's agents?** Compare this to the planner agent you created in Lab 4. The planner says "Do not write or modify files" in its instructions — a prompt-level constraint. This reviewer goes further with `disallowedTools: Write, Edit`, which *enforces* the restriction at the tool level. Both approaches have their place: prompt constraints are flexible, tool constraints are guaranteed.

---
<br><br>

## 3: Create the Plugin Manifest Folder
**What we're doing:** Preparing a shareable plugin bundle.  
**Why:** Plugins are the packaging mechanism for distributing team assets (commands, agents, skills) so teammates can install them with a single command rather than copying files around.

**Action:**
```bash
mkdir -p .claude-plugin
```
---
<br><br>

## 4: Create plugin.json
**What we're doing:** Defining the plugin metadata and component paths.  
**Why:** Claude Code uses this manifest to discover and load plugin components. When someone installs your plugin, these paths tell Claude Code where to find the commands, agents, and skills you've bundled.

**Action:** Make a new file `.claude-plugin/plugin.json`.

**Action:** Copy/paste the following contents into the file and save it.

```json
{
  "name": "intro-claude-code-team-kit",
  "version": "0.1.0",
  "description": "Intro workshop team kit: commands, agents, and a skill.",
  "commands": ["../.claude/commands"],
  "agents": ["../.claude/agents"],
  "skills": "../.claude/skills"
}
```

> **Key detail:** The `commands`, `agents`, and `skills` fields are top-level in `plugin.json` — there is no wrapper object around them. Paths are relative to the `plugin.json` file location.

> **Newer shortcut (v2.1.157+):** `claude plugin init <name>` now scaffolds a plugin for you, and plugins placed in `.claude/skills` auto-load with no marketplace required. We build the manifest by hand here so you understand the pieces; for real projects, start with `claude plugin init`. Also useful: `/plugin list` shows installed plugins with their projected per-session token cost, and `defaultEnabled: false` in plugin.json ships a plugin disabled by default.

---
<br><br>

## 5: Start Claude Code and (optional) Verify Discovery
**What we're doing:** Validating the repo has the expected structure.  
**Why:** Before running any workflows, confirm that Claude Code discovers all your assets — the new `/ship` command, the reviewer agent from this lab, plus the planner agent, test-runner agent, and api-checker skill from Lab 4.

**Action:** Start Claude Code

```bash
claude
```

Then run:

```
/help
```

Confirm you see `/ship` listed in the `custom-commands` section.

![The /ship command is present](./images/ccode234.png?raw=true "The /ship command is present")


Hit *Esc" to get out of that output. Then run: 

```
/agents
```

 Switch to the `Library` tab. Confirm the `reviewer`, `planner`, and `test-runner` agents are shown.

![Agents are present](./images/ccode235.png?raw=true "Agents are present")


Hit *Esc" to get out of that output. Then run: 

```
/skills
```

Confirm the `api-checker` skill is shown.

![Skill is  present](./images/ccode236.png?raw=true "Skill is present")

Hit *Esc" to get out of that output.

---
<br><br>


## 6: Practice the Supervised Delegation Pattern (Plan → Implement → Review)
**What we're doing:** Running a realistic delegation flow where *you* act as the supervisor, directing Claude to use the right subagent at each step.  
**Why:** This is how most people use subagents in practice — you decide what happens next, and subagents are your specialists. You control the workflow; they do the focused work.

**Action:** In Claude, type:
```
Use the planner subagent to propose a plan to add phoneNumber to User (optional field).
```

![Initial plan](./images/ccode237.png?raw=true "Initial plan")

Review the plan. When you're satisfied, tell Claude to proceed:

```
The plan looks good. Now implement the change minimally. Do not run tests yet.
```
![Executing plan plan](./images/ccode204.png?raw=true "Executing plan")

Approve as needed.

> **What's happening here:** You explicitly delegated the planning step to the planner subagent. Claude ran it in a separate context and returned the result to you. Then you — the supervisor — approved the plan and gave the next instruction. This is the "supervised delegation" pattern: the human decides the workflow, subagents do the specialized work.
---
<br><br>

## 7: Delegate Review (Reviewer Subagent)
**What we're doing:** Getting a review from the reviewer subagent, which is structurally unable to edit files.  
**Why:** Because the reviewer has `disallowedTools: Write, Edit` in its definition, you can trust that it will only analyze — never modify — your code. This keeps the review honest and the main conversation focused on your decisions about what to change.

**Action:** In Claude, type:
```
Use the reviewer subagent to review the change we just made.
```

You'll see output of the main agent interpreting the subagent output. If you want to see the results from the subagent (the 3 risks, 3 tests to add, and 3 patch suggestions we told the reviewer agent to output) you can expand the output with *ctrl+o* and look back up in the output. 

![Start of reviewer output](./images/ccode239.png?raw=true "Start of reviewer output")

> **What's happening here:** Claude delegates to the reviewer subagent, which runs with its own instructions and tool restrictions in a separate context. It returns structured output to the main conversation. You then decide which suggestions to act on.

You can choose to proceed with all or some of the suggested changes by responding in the Claude Code input.
 
---
<br><br>

## 8: Run the Ship Checklist Command
**What we're doing:** Running the `/ship` command you created in Step 1.  
**Why:** Execute the overall workflow.

> **Note:** Notice the difference from Steps 6–7. The `/ship` command runs *inline* in the main conversation — it doesn't spawn a separate subagent context. It's a reusable prompt template, not a specialist. Commands and agents serve different purposes: commands standardize *what to do*, agents specialize *who does it*.

**Action:** In Claude, run:

```
/ship
```

What you should see is the git info being gathered and the testing running. Then in the summary, you'll see what changed, the test results (1 will be failing), the "Risks" list and the suggested "Follow-ups".

![Partial output of ship command](./images/ccode240.png?raw=true "Partial output of ship command")

---
<br><br>


## 9: (OPTIONAL) Open the VS Code Extension
**What we're doing:** Switching to IDE workflow.  
**Why:** Many learners prefer IDE-first interaction.

**Action:** Open the Claude Code VS Code extension (sidebar or toolbar icon).

If you are prompted to log in, choose the "Claude.ai Subcription" option and follow the steps to authenticate.

---
<br><br>

## 10: (OPTIONAL) Run /ship from the Extension
**What we're doing:** Using the same team kit inside the IDE.  
**Why:** Reinforces that repo-level assets (commands, agents, skills) work the same way whether you're in the terminal or VS Code. The extension automatically discovers everything in `.claude/`.

**Action:** In the extension chat, run:
```
/ship
```

![/ship in extension](./images/ccode207.png?raw=true "/ship in extension")

---
<br><br>

## 11: Exit
**Action:** End any running sessions and close Claude Code.

---
<br><br>

## Lab Summary
You've learned:
- **Supervised delegation pattern:** You act as the orchestrator, directing Claude to use specialist subagents (planner, reviewer) at each step and making decisions between them.
- **Prompt constraints vs. tool constraints:** The planner uses prompt instructions ("do not edit files") while the reviewer uses `disallowedTools: Write, Edit` for structural enforcement. Both are valid; tool constraints are stronger.
- **Commands vs. agents:** Commands (`/ship`) are reusable prompts that run inline. Agents are specialists that run in their own subagent context and return results.
- **Plugin packaging:** How to bundle commands, agents, and skills into a `plugin.json` manifest that teammates can install.
- **Cross-environment consistency:** The same repo-level assets work in both the terminal and VS Code.

> **Going further:** Claude Code also has an experimental **Agent Teams** feature for fully autonomous multi-agent coordination. With Agent Teams, a "team lead" agent spawns independent teammates that coordinate through shared task lists and direct messaging — no human orchestration needed between steps. Agent Teams remain experimental and disabled by default (enabled via the `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` setting or env var) and are architecturally different from the subagent delegation shown here: each teammate gets its own context window, and they can message each other directly. Note also that as of v2.1.172, regular subagents can spawn their own subagents up to 5 levels deep — so even without Agent Teams, delegation can go deeper than one level. See the [Agent Teams documentation](https://code.claude.com/docs/en/agent-teams) for details. We'll see the *managed agents* side of this story — background and cloud agents — in Day 2.
<br><br>
---
## END OF LAB
---
<br><br>





# Lab 6: Hooks: Enforcing Policy at the Tool Boundary
## Lab Purpose
Learn how hooks let you enforce rules that Claude *cannot* talk its way around. You'll create a PreToolUse hook that blocks edits to a protected file and a PostToolUse hook that logs every bash command Claude runs — then watch both fire live. 

---
<br><br>

## 1: Set Up the Protected File and Hooks Folder
**What we're doing:** Confirming we have a file worth protecting and creating the folder where hook scripts live.
**Why:** Our policy will be "nobody edits config.json" — the database config file you created back in Lab 2.

**Action:** In a regular terminal (not Claude), check that the file is still there:
```
cat config.json
```

If it's missing (maybe you cleaned up), recreate a stand-in:
```
echo '{ "database": { "host": "localhost", "port": 5432 } }' > config.json
```

Then create the hooks folder:
```
mkdir -p .claude/hooks
```

---
<br><br>

## 2: Create the Guard Script
**What we're doing:** Writing the small shell script that decides whether an edit is allowed.
**Why:** When a PreToolUse hook fires, Claude Code sends the tool call details as JSON on the script's *stdin*. The script inspects it and answers with an exit code: **exit 0** means "no objection," **exit 2** means "block it" — and whatever the script prints to *stderr* is fed back to Claude as the reason.

**Action:** Make a new file `.claude/hooks/protect-config.sh` (remember you can use the `code` command if working in the codespace).

**Action:** Copy/paste the following contents into the file and save it.

```
#!/bin/bash
# PreToolUse guard: block any Edit/Write that targets config.json
FILE=$(jq -r '.tool_input.file_path // ""')

if [[ "$(basename "$FILE")" == "config.json" ]]; then
  echo "POLICY: config.json is protected. Do not modify it. Suggest the change to the user instead." >&2
  exit 2
fi

exit 0
```

The `jq -r '.tool_input.file_path'` line pulls the target file path out of the JSON that arrives on stdin.

![Creating the guard script](./images/cc-se4.png?raw=true "Creating the guard script")

---
<br><br>

## 3: Make the Script Executable
**What we're doing:** Setting the execute bit.
**Why:** Claude Code runs the script as a process — it must be executable.

**Action:**
```
chmod +x .claude/hooks/protect-config.sh
```

---
<br><br>

## 4: Wire Up the Hooks in settings.json
**What we're doing:** Registering two hooks in the project's settings file.
**Why:** Hooks are configured under a `"hooks"` key in `.claude/settings.json`. Each entry names an *event* (PreToolUse, PostToolUse, etc.), a *matcher* that filters by tool name, and the *handler* to run.

**Action:** Make a new file `.claude/settings.json`.

**Action:** Copy/paste the following contents into the file and save it.

```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "${CLAUDE_PROJECT_DIR}/.claude/hooks/protect-config.sh",
            "args": []
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "jq -r '\"\\(.tool_input.command) - \\(.tool_input.description // \"No description\")\"' >> \"${CLAUDE_PROJECT_DIR}/.claude/bash-command-log.txt\""
          }
        ]
      }
    ]
  }
}
```

Two things to notice:
- The matcher `Edit|Write` means "fire on either the Edit or the Write tool." `Bash` matches only the Bash tool.
- The guard hook uses the newer *exec form* (`args: []`), which runs the script directly with no shell in between — recommended whenever you use a path placeholder like `${CLAUDE_PROJECT_DIR}`. The logger omits `args`, so it runs in *shell form*, which we need for the `>>` redirect.

![The hooks settings file](./images/cc-se5.png?raw=true "The hooks settings file")

---
<br><br>

## 5: Start Claude in Bypass Mode
**What we're doing:** Starting Claude with permissions bypassed — on purpose.
**Why:** This is the punchline of the lab: hooks fire at the *tool boundary*, outside of the permission system. Even with all permission prompts turned off, the hook still gets a veto.

**Action:** In a terminal other than your original one, start Claude with the option or alias (if working in the codespace):
```
claude --dangerously-skip-permissions

  or

claude-yolo (if running in the codespace)
```

---
<br><br>

## 6: Inspect the Hooks with /hooks
**What we're doing:** Verifying Claude Code loaded our hooks.
**Why:** The `/hooks` command opens a read-only browser of every configured hook — handy for checking what's active and which settings file it came from.

**Action:** Type:
```
/hooks
```

You should see **PreToolUse** and **PostToolUse** each showing one configured hook, labeled with a `[command]` type and a `Project` source (meaning it came from `.claude/settings.json`). 

![The /hooks menu](./images/cc-se6.png?raw=true "The /hooks menu")

Pick one and select it to see general details about how the hook works.

![How the hook works](./images/cc-se7.png?raw=true "How the hook works")

Then select the listed hook and you should see the configured command for it.

![How the hook works](./images/cc-se8.png?raw=true "How the hook works")

You can select it again to go one level deeper and see the `Hook details`.

![Hook details](./images/cc-se9.png?raw=true "Hook details")

Hit `Esc` several times to get back to the main Claude Code prompt.

---
<br><br>

## 7: Try to Edit the Protected File
**What we're doing:** Asking Claude to do the thing our policy forbids.
**Why:** Time to watch the hook earn its keep.

**Action:** Type:
```
Add a connection_timeout setting to config.json using the Edit tool.
```

Watch what happens: Claude attempts the edit, and the tool call is **blocked** before it touches the file. You'll see the hook's stderr message surfaced in the conversation — Claude reads it too.

![Edit blocked by hook](./images/cc-se10.png?raw=true "Edit blocked by hook")

---
<br><br>

## 8: Look at How Claude Reacts
**What we're doing:** Observing what Claude does with the block message.
**Why:** Exit code 2 doesn't just stop the tool call — the stderr text is fed back to Claude as feedback. Our message told it to suggest the change to the user instead, so a well-behaved Claude should explain the policy and show you the change it *would* have made.

**Action:** Read Claude's response. Then verify the file is untouched:
```
! cat config.json
```

No `connection_timeout` — the file never changed, even in bypass-permissions mode.

> **Spot the loophole:** Our matcher only guards the `Edit|Write` tools. Claude could in principle modify the file through the Bash tool (`sed`, `echo >>`, etc.). Real policies often add a Bash matcher too, or use the `if` field with permission-rule syntax to narrow further. If Claude offers to work around the block, tell it no — and remember this when you design your own hooks.

---
<br><br>

## 9: Generate Some Bash Traffic
**What we're doing:** Giving the PostToolUse logger something to record.
**Why:** PostToolUse fires *after* a tool call succeeds — it can't block (the command already ran), but it's perfect for auditing, logging, and follow-up actions like auto-formatting.

**Action:** Type:
```
Use bash to list the files in this project and count the lines in user.js.
```

Let Claude run its commands.

---
<br><br>

## 10: Check the Audit Log
**What we're doing:** Reading the log file our PostToolUse hook has been writing.
**Why:** Proof that every Bash call went through our hook — no exceptions, no forgetting.

**Action:** Type:
```
! cat .claude/bash-command-log.txt
```

You should see each command Claude ran, with its description. (You may even see your own `!` commands show up — they go through the Bash tool too.)

![The bash command log](./images/cc-se11.png?raw=true "The bash command log")

---
<br><br>

## 11: Prompt vs. Tool vs. Hook Constraints
**What we're doing:** Showing how we can leverage hooks in the constraint toolbox you've been building all day. (Reading only)
**Why:** You now have three ways to say "don't do that" — and they are not equally strong.

Recall Lab 5: the planner agent had a *prompt constraint* ("Do not write or modify files" — advisory, the model can drift), and the reviewer agent had a *tool constraint* (`disallowedTools: Write, Edit` — structural, but scoped to that one agent). Hooks are the third tier:

- **Prompt constraint** — instructions in CLAUDE.md or an agent file. Flexible, but it's a request, not a guarantee.
- **Tool constraint** — `disallowedTools` removes the tool entirely, for one agent.
- **Hook** — your own code at the tool boundary, for *every* tool call in the session, with any logic you can script. Exit 2 is a hard no, even in bypass mode.

> **Going further:** Hooks can do much more than block: a hook can exit 0 and print JSON to make richer decisions (`permissionDecision: allow / deny / ask`), rewrite a tool's input before it runs, or inject context for Claude. There are also handler types beyond shell commands (`prompt`, `agent`, `http`, `mcp_tool`) and many more events — `SessionStart` for loading context when a session begins is a popular one. To temporarily switch everything off, set `"disableAllHooks": true` in settings. See the [hooks reference](https://code.claude.com/docs/en/hooks) for the full schema.

---
<br><br>

## 12: Exit

**Action:** In prep for the next lab, type `exit` to exit Claude Code.

```
exit
```

## Lab Summary
✅ You've successfully:
- Created a PreToolUse hook that blocks edits to a protected file
- Used exit code 2 + stderr to veto a tool call and explain why
- Created a PostToolUse hook that logs every bash command
- Verified configured hooks with the /hooks menu
- Proved hooks fire even in bypass-permissions mode
- Placed hooks in the constraint hierarchy: prompt → disallowedTools → hooks

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 7: MCP: Connecting Claude Code to External Tools
## Lab Purpose
Connect Claude Code to an external tool server using the Model Context Protocol (MCP). You'll add a reference MCP server, inspect it with /mcp, call its tools from a prompt, see where the configuration lives for sharing with a team, and cleanly remove it. Estimated time: 10-12 minutes.

---
<br><br>

## 1: Add an MCP Server
**What we're doing:** Registering a *stdio* MCP server — a local process that Claude Code starts and talks to over stdin/stdout.
**Why:** MCP is the open standard that lets Claude reach tools outside its built-ins: issue trackers, databases, browsers, and more. We'll use the official **everything** reference server — a test server built to exercise MCP features, perfect for learning.

**Action:** In a regular terminal (Claude not running), type:
```
claude mcp add everything -- npx -y @modelcontextprotocol/server-everything
```

The `--` (double dash) separates Claude's own options from the command that runs the server — everything after it is the server's own command line. Local stdio is the default transport; remote servers use `--transport http <url>` instead.

![Adding the MCP server](./images/ccode306.png?raw=true "Adding the MCP server")

---
<br><br>

## 2: Verify the Connection
**What we're doing:** Listing configured servers with a health check.
**Why:** `claude mcp list` actually starts each server and reports whether it connects — your first diagnostic stop when MCP misbehaves.

**Action:** Type:
```
claude mcp list
```

The first run downloads the package via npx, so give it a few seconds (any npm notices are harmless). You should see the server with a **✓ Connected** status.

![MCP server connected](./images/ccode307.png?raw=true "MCP server connected")

---
<br><br>

## 3: See the Server's Configuration and Scope
**What we're doing:** Inspecting one server's details.
**Why:** Every MCP server lives in a *scope*. The default is **local** — stored in your user config, visible only to you, in this project.

**Action:** Type:
```
claude mcp get everything
```

Note the output: type *stdio*, the command line it runs, and **Scope: Local**. Notice there's no new file in your project — local-scope config lives in `~/.claude.json`, keyed to this project directory.

---
<br><br>

## 4: Move It to Project Scope
**What we're doing:** Re-adding the server at *project* scope so it can be shared with teammates.
**Why:** Project-scoped servers are written to a `.mcp.json` file in the repo root. Commit that file, and everyone who clones the project gets the same tool connections — the same "team kit" idea as Lab 5's plugins.

**Action:** Type both commands:
```
claude mcp remove everything
```
```
claude mcp add everything --scope project -- npx -y @modelcontextprotocol/server-everything
```

There's also `--scope user` for "available to me in every project."

---
<br><br>

## 5: Look at .mcp.json
**What we're doing:** Reading the shareable config file that just appeared.
**Why:** This is the artifact you'd commit. It's plain JSON — no secrets should go here (use `--env` vars or remote servers with OAuth for that).

**Action:** Type:
```
cat .mcp.json
```

You'll see the server entry with its `command` and `args`.

> **Naming note:** the server name `workspace` is reserved for internal use — if a config defines a server with that name, Claude Code skips it at load time with a warning. Pick anything else.

![The .mcp.json file](./images/ccode308.png?raw=true "The .mcp.json file")

---
<br><br>

## 6: Start Claude and Approve the Project Server
**What we're doing:** Starting a session that loads the project-scoped server.
**Why:** Because `.mcp.json` can arrive in a repo from *anyone*, Claude Code asks you to approve project-scoped servers before it will run them — a safety gate teammates will see the first time they open your repo.

**Action:** Start Claude (the yolo alias is fine here):
```
claude-yolo
```

If you're prompted to approve the MCP server(s) from `.mcp.json`, approve them.

---
<br><br>

## 7: Inspect with /mcp
**What we're doing:** Checking server status from inside the session.
**Why:** `/mcp` is the in-session control panel: connection status, tool counts, and OAuth sign-in for remote servers that need it.

**Action:** Type:
```
/mcp
```

You should see the **everything** server listed as connected with a tool count next to it. Select it to browse the tools it exposes (echo, get-sum, and a menagerie of MCP demo features), then hit *Esc* to back out.

You may also notice a **claude.ai** section in this panel — connectors you've added to your claude.ai account now surface right inside Claude Code sessions when you're signed in with your subscription. Hold that thought for Day 3.

![The /mcp panel](./images/ccode309.png?raw=true "The /mcp panel")

---
<br><br>

## 8: Use an MCP Tool in a Prompt
**What we're doing:** Letting Claude call the server's `echo` tool.
**Why:** Once connected, MCP tools are just tools — Claude picks them up from context the same way it picks built-ins or skills.

**Action:** Type:
```
Use the everything server's echo tool to send the message "Hello from MCP!"
```

Claude calls the tool and shows the round-trip result. Notice the tool's full name in the output: MCP tools are named `mcp__<server>__<tool>` — here, `mcp__everything__echo`. (That's also the pattern you'd use to match MCP tools in a hook, tying back to Lab 6.)

![Calling the echo tool](./images/ccode310.png?raw=true "Calling the echo tool")

---
<br><br>

## 9: Use a Second Tool
**What we're doing:** Calling a tool with structured arguments.
**Why:** To see Claude map a natural-language request onto a tool's input schema.

**Action:** Type:
```
Use the everything server to add 25 and 17.
```

Claude should call the server's `get-sum` tool with `a: 25, b: 17` and report 42.

![Calling the get-sum tool](./images/ccode311.png?raw=true "Calling the get-sum tool")

---
<br><br>

## 10: Exit and Remove the Server
**What we're doing:** Cleaning up the demo server.
**Why:** `claude mcp remove` is the symmetric counterpart to `add` — it edits the same config the add command wrote (here, `.mcp.json`).

**Action:** Type `exit` to leave Claude, then in the terminal:
```
claude mcp remove everything
```

---
<br><br>

## 11: Confirm the Cleanup
**What we're doing:** Verifying nothing is left configured.
**Why:** Good hygiene — and one more rep with the management commands.

**Action:** Type:
```
claude mcp list
```

The everything server should be gone (and the entry removed from `.mcp.json`).

![Server removed](./images/ccode312.png?raw=true "Server removed")

---
<br><br>

## Lab Summary
✅ You've successfully:
- Added a stdio MCP server with `claude mcp add <name> -- <command>`
- Health-checked it with `claude mcp list` and inspected it with `claude mcp get`
- Moved a server between local and project scope and read `.mcp.json`
- Inspected connections in-session with `/mcp`
- Called MCP tools (`mcp__everything__echo`, `mcp__everything__get-sum`) from natural-language prompts
- Removed a server with `claude mcp remove`

> **Where this is going:** On Day 3 you'll see the same MCP idea as *connectors* in the Claude apps — the directory of reviewed connectors at claude.ai uses the same MCP infrastructure you just configured by hand, and connectors you add there appear automatically in your Claude Code `/mcp` panel.

<br><br>
---
## END OF LAB
---
<br><br>


# 🗓️ DAY 2: Loops, Automation, and Managed Agents
**Welcome back! Today Claude works while you do not watch — headless pipelines, condition-driven goals, the Agent SDK, CI automation, scheduled tasks, and background agents.**

---
<br><br>

# AI-Powered Coding with Claude Code
## Learn practical workflows, hands-on coding techniques, and structured interactions
## Session Labs — 1.5-Day Edition — Day 2: Loops, Automation, and Managed Agents
## Revision 6.0 - 06/11/26

<br><br>

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**These labs continue in the same GitHub Codespace you used on Day 1. The files you created in Labs 1-7 (hello.js, user.js, the api-checker skill, the planner/test-runner/reviewer agents, etc.) are assumed to be present.**

**Remember the `claude-yolo` alias is available for `claude --dangerously-skip-permissions` (use it from a terminal other than the original starting one).**

**Day 2 theme: yesterday you drove Claude interactively, one prompt at a time. Today Claude works while you don't watch — headless pipelines, condition-driven loops, SDK programs, CI jobs, scheduled tasks, and managed agents running in the background and in the cloud.**

> **Heads-up on usage:** Starting June 15, 2026, Agent SDK and `claude -p` (headless) usage on subscription plans draws from a new monthly Agent SDK credit, separate from your interactive usage limits. GitHub Actions usage falls under this too. Several labs today use these surfaces — that's expected and fine for a workshop, but worth knowing for your own automation later.

<br><br>

---
<br><br>

# Lab 8: Day 2 Warm-Up & Recap
## Lab Purpose
Rehydrate your Day 1 environment and confirm the assets you built — memory, skill, and agents — are all still in place before we start automating with them. Estimated time: 5-8 minutes.

---
<br><br>

## 1: Start Claude
**What we're doing:** Starting a fresh interactive session in the same Codespace as Day 1.  
**Why:** All of today's automation builds on the project state we left behind yesterday.

**Action:** In a terminal in your Codespace, start Claude:
```bash
claude --model sonnet --effort medium
```

---
<br><br>

## 2: Check the Context Loadout
**What we're doing:** Seeing what Claude loads automatically at session start.  
**Why:** Today's headless and SDK runs load this same context — understanding what's "free" in every session matters when you automate.

**Action:** Type:
```
/context
```

Notice the system prompt, CLAUDE.md, skills, and agents all consuming context before you've typed a single prompt.

![context loadout](./images/ccode320.png?raw=true "context loadout")

---
<br><br>

## 3: Confirm Project Memory Survived
**What we're doing:** Verifying the CLAUDE.md project memory from Lab 3 is still being read.  
**Why:** Persistent memory is what lets unattended runs follow your project rules without you in the loop.

**Action:** Type:
```
What are our project rules and what test command should I run after code edits?
```

Claude should answer from the CLAUDE.md file created with `/init` on Day 1.

---
<br><br>

## 4: Re-run the Lab 4 Skill
**What we're doing:** Triggering the api-checker skill once, without naming it.  
**Why:** Skills will resurface today in headless mode, GitHub Actions, and agent view — confirm yours still fires.

**Action:** Type:
```
Please validate https://jsonplaceholder.typicode.com/posts/1 and summarize what you find.
```

You should see the skill load and the `check.py` script run, just like yesterday.

![skill recap](./images/ccode321.png?raw=true "skill recap")

---
<br><br>

## 5: Confirm the Agents Are Present
**What we're doing:** Listing the subagents you built in Labs 4-5.  
**Why:** Today we'll meet a different kind of agent — *background* and *cloud* agents. Knowing your subagents are here sets up the contrast.

**Action:** Type:
```
/agents
```

Confirm `planner`, `test-runner`, and `reviewer` are listed. Hit *Esc* to exit the list.

![agents present](./images/ccode322.png?raw=true "agents present")

---
<br><br>

## 6: Reframe and Exit
**What we're doing:** Setting the Day 2 mindset and exiting.  
**Why:** Everything yesterday was *you prompting, Claude responding, you approving*. Everything today removes one of those three from the loop.

**Action:** Read this, then exit:

- **Labs 9-10:** remove *you prompting each step* (headless pipelines, `/goal` loops)
- **Lab 11:** remove *the terminal entirely* (Agent SDK programs — read-only and unattended)
- **Labs 12-13:** remove *your machine being involved at the moment of execution* (CI automation, scheduled tasks, cloud routines)
- **Lab 14:** keep many agents working at once and check in on your terms (background, cloud, and web sessions)

```
exit
```

## Lab Summary
✅ You've successfully:
- Restarted Claude in your Day 1 environment
- Inspected the automatic context loadout with /context
- Confirmed CLAUDE.md project memory persists
- Re-triggered the api-checker skill
- Verified your subagents with /agents
- Framed the Day 2 shift: from prompts to loops

<br><br>
---
## END OF LAB
---
<br><br>

# Lab 9: Headless Mode: From Prompts to Pipelines
## Lab Purpose
Use `claude -p` as a Unix-style building block: pipe data through it, get structured JSON out, chain calls, and write your first loop that runs Claude once per file. Estimated time: 10-12 minutes.

**NOTE: This whole lab runs in a regular terminal — no interactive Claude session needed.**

---
<br><br>

## 1: Pipe Input Through Claude
**What we're doing:** Sending stdin into a non-interactive Claude run.  
**Why:** `-p` (print) mode reads stdin, processes it, prints the result, and exits — the contract every pipeline tool follows.

**Action:** In a terminal, run:
```bash
cat user.js | claude -p "Summarize what this code does in two sentences"
```

You get just the answer — no session UI, no prompts.

![pipe input](./images/ccode323.png?raw=true "pipe input")

---
<br><br>

## 2: Run a Prompt Directly
**What we're doing:** Passing the prompt as an argument instead of stdin.  
**Why:** This is the form you'll embed in scripts, Makefiles, and CI.

**Action:** Run:
```bash
claude -p "What does goodbye.py print? Answer in one line."
```

---
<br><br>

## 3: Get Structured JSON Output
**What we're doing:** Switching the output format from text to JSON.  
**Why:** Scripts can't parse prose reliably. JSON output gives you the result plus metadata: session ID, cost, turns, duration.

**Action:** Run:
```bash
claude -p "Summarize this project in one sentence" --output-format json
```

Look at the raw JSON. Find the `result`, `session_id`, `total_cost_usd`, and `num_turns` fields.

![json output](./images/ccode324.png?raw=true "json output")

---
<br><br>

## 4: Inspect the JSON with jq
**What we're doing:** Extracting specific fields from the JSON payload.  
**Why:** This is how automation consumes Claude — pull the field you need, ignore the rest.

**Action:** Run these two commands:
```bash
claude -p "Summarize this project in one sentence" --output-format json | jq -r '.result'
```
```bash
claude -p "How many .js files are in this directory?" --output-format json | jq '{result: .result, cost: .total_cost_usd, turns: .num_turns}'
```

![jq extraction](./images/ccode325.png?raw=true "jq extraction")

**Note:** `--output-format json` also supports `--json-schema` to force output matching a schema you define — the structured result lands in a `structured_output` field.

---
<br><br>

## 5: Stream Output Token by Token
**What we're doing:** Using `stream-json` to watch events arrive in real time.  
**Why:** Long-running automation needs progress signals, not a single blob at the end.

**Action:** Run:
```bash
claude -p "Write a 4-line poem about loops" --output-format stream-json --verbose --include-partial-messages | jq -rj 'select(.type == "stream_event" and .event.delta.type? == "text_delta") | .event.delta.text'
```

Each line of the raw stream is a JSON event; the jq filter selects only text deltas so you see the poem stream in live.

---
<br><br>

## 6: Chain Two Headless Calls
**What we're doing:** Feeding the output of one `claude -p` into another.  
**Why:** Composability — each call does one focused job, and the shell wires them together.

**Action:** Run:
```bash
claude -p "List the .js files in this directory, one filename per line, output nothing else" | claude -p "For each filename on stdin, rate from 1-5 how descriptive the name is. One line per file."
```

Two separate Claude runs, connected by a pipe — your first multi-step pipeline.

![chained calls](./images/ccode326.png?raw=true "chained calls")

---
<br><br>

## 7: Your First Loop Instead of a Prompt
**What we're doing:** Running Claude once per file inside a bash for-loop.  
**Why:** This is the core Day 2 move. Yesterday you'd have prompted "summarize all my js files" and hoped. A loop gives you one bounded, repeatable call per item.

**Action:** Run:
```bash
for f in *.js; do
  echo "## $f" >> summaries.md
  cat "$f" | claude -p "Summarize this file in one sentence" >> summaries.md
done
```

Watch the loop iterate — each pass is an independent headless run.

---
<br><br>

## 8: Inspect the Loop's Output
**What we're doing:** Checking what the loop produced.  
**Why:** Verifying automated output is a habit you'll need all day.

**Action:** Run:
```bash
cat summaries.md
```

You should see a heading and a one-sentence summary for each .js file.

![loop output](./images/ccode327.png?raw=true "loop output")

---
<br><br>

## 9: Let Headless Runs Make Changes
**What we're doing:** Pre-approving actions so a headless run can write files without hanging.  
**Why:** `-p` mode has no human to click "Yes." Anything not pre-approved either aborts the run or gets denied — so automation must declare its permissions up front.

**Action:** Run:
```bash
claude -p "Create a file named pipeline.txt containing the single word OK" --permission-mode acceptEdits
```

Then verify with `cat pipeline.txt`. The `acceptEdits` mode auto-approves file writes; `--allowedTools "Bash,Read,Edit"` is the finer-grained alternative that pre-approves specific tools (and supports rules like `Bash(git diff *)`). We'll build on this idea in Lab 11.

---
<br><br>

## 10: Know the Fine Print
**What we're doing:** Noting two operational facts about headless mode.  
**Why:** Both will matter the moment you automate for real.

**Action:** Read (nothing to run):

1. **Metering:** Starting **June 15, 2026**, `claude -p` and Agent SDK usage on subscription plans draws from a separate monthly Agent SDK credit, distinct from your interactive limits.
2. **`--bare`:** For CI and scripts, add `--bare` to skip auto-discovery of hooks, skills, plugins, MCP servers, and CLAUDE.md — same result on every machine, faster startup. (It's slated to become the default for `-p`. Note it skips OAuth, so it needs `ANTHROPIC_API_KEY` for auth — which is why we didn't use it in this lab.)

## Lab Summary
✅ You've mastered:
- Piping data through `claude -p`
- Structured output with `--output-format json` and jq
- Real-time streaming with `stream-json`
- Chaining headless calls in a shell pipeline
- Writing a bash loop that runs Claude per file
- Pre-approving permissions for unattended writes
- The June 15 metering change and `--bare` mode

<br><br>
---
## END OF LAB
---
<br><br>

# Lab 10: /goal: Condition-Driven Loops
## Lab Purpose
Use `/goal` to set a completion condition and watch Claude keep working turn after turn — without you prompting each step — until an independent evaluator confirms the condition is met. Estimated time: 10-12 minutes.

**NOTE: `/goal` requires Claude Code v2.1.139 or later (`claude --version` to check).**

---
<br><br>

## 1: Start Claude in YOLO Mode
**What we're doing:** Starting with permissions bypassed.  
**Why:** `/goal` removes per-*turn* prompts; bypass (or auto) mode removes per-*tool* prompts. Together the loop runs hands-free.

**Action:** In a terminal (not your original one), run:
```bash
claude-yolo
```

---
<br><br>

## 2: Confirm There's a Failing Test
**What we're doing:** Checking the test state we left after Day 1's user.js work.  
**Why:** `/goal` needs a verifiable gap between current state and target state — a red test is perfect.

**Action:** Type:
```
! npm test
```

You should see at least one failure left over from the Lab 4/5 work on `user.js` / `user.test.js`.

![failing test](./images/ccode328.png?raw=true "failing test")

**If everything passes**, create a gap first:
```
Add a test to user.test.js asserting that setName rejects empty strings. Do not change user.js. It's fine if this test fails.
```

---
<br><br>

## 3: Set the Goal
**What we're doing:** Giving Claude a completion condition instead of an instruction.  
**Why:** A goal states the *end state* and lets Claude figure out the steps. After each turn, a small fast model (Haiku by default) checks the condition against the conversation; "not met" starts another turn automatically.

**Action:** Type:
```
/goal all tests in this project pass (npm test exits 0), no test file is deleted, or stop after 10 turns
```

Note the three parts of a good condition: a measurable end state, a stated check, and constraints (including a turn bound so it can't run forever).

---
<br><br>

## 4: Watch the Loop Run
**What we're doing:** Observing Claude iterate without further prompting.  
**Why:** This is the loop made visible — fix, test, evaluate, repeat.

**Action:** Setting the goal starts a turn immediately — no extra prompt needed. Watch for:
- the `◎ /goal active` indicator showing how long the goal has been running
- Claude running tests, reading failures, editing, and re-running on its own
- (press *ctrl+o* to watch the thinking between turns)

![goal active](./images/ccode329.png?raw=true "goal active")

---
<br><br>

## 5: Check Goal Status Mid-Run
**What we're doing:** Querying the goal's progress.  
**Why:** Unattended doesn't mean unobservable.

**Action:** While the goal is active (or right after), type:
```
/goal
```

With no argument, `/goal` shows the condition, elapsed time, turns evaluated, token spend, and the evaluator's most recent reason for "not met yet."

![goal status](./images/ccode330.png?raw=true "goal status")

---
<br><br>

## 6: Let It Finish
**What we're doing:** Watching the goal clear itself.  
**Why:** Completion is decided by a *separate* evaluator model, not the model doing the work — a fresh pair of eyes confirms the condition.

**Action:** Wait for the tests to go green. When the evaluator returns "yes," the goal clears automatically and an achieved entry is recorded in the transcript.

![goal achieved](./images/ccode331.png?raw=true "goal achieved")

Run `/goal` once more — it now shows the *achieved* condition with its duration, turn count, and token spend.

---
<br><br>

## 7: Set and Clear a Goal Manually
**What we're doing:** Practicing the off switch.  
**Why:** You'll want to abandon goals that turn out to be wrong or too expensive.

**Action:** Type:
```
/goal summaries.md contains an entry for every .js file in this directory, or stop after 5 turns
```

Let it run one turn, then cancel it:
```
/goal clear
```

(`stop`, `off`, `cancel`, `reset`, and `none` all work as aliases. `/clear` also removes any active goal.)

---
<br><br>

## 8: Goals in Headless Mode
**What we're doing:** Noting that `/goal` composes with Lab 9.  
**Why:** A goal in `-p` mode runs the whole loop to completion in a single shell command — condition-driven automation with no session open.

**Action:** Read (optional to run — it will iterate for a while):
```bash
claude -p "/goal summaries.md has an entry for every .js file in this directory, or stop after 5 turns" --permission-mode acceptEdits
```

Ctrl+C stops a non-interactive goal early.

---
<br><br>

## 9: Know the Loop Family
**What we're doing:** Placing `/goal` among its siblings.  
**Why:** Today you'll meet three ways to keep a session running — pick by what should trigger the next turn.

**Action:** Read:

| Approach | Next turn starts when | Stops when |
|---|---|---|
| `/goal` | The previous turn finishes | An evaluator model confirms the condition is met |
| `/loop` (Lab 13) | A time interval elapses | You stop it, or Claude decides the work is done |
| Stop hook (Lab 6) | The previous turn finishes | Your own script or prompt decides |

Under the hood, `/goal` *is* a session-scoped prompt-based Stop hook — which is why it requires the workspace trust dialog and is unavailable when hooks are disabled.

---
<br><br>

## 10: Exit
**Action:** Type `exit` to end the session.
```
exit
```

## Lab Summary
✅ You've successfully:
- Set a `/goal` with a measurable condition, check, and turn bound
- Watched Claude iterate to green tests with zero prompting
- Inspected progress with bare `/goal` status
- Cleared a goal early with `/goal clear`
- Seen `/goal` run headlessly via `claude -p`
- Compared `/goal` vs `/loop` vs Stop hooks

<br><br>
---
## END OF LAB
---
<br><br>

# Lab 11: Agent SDK: Programmatic and Unattended Loops
## Lab Purpose
Drive the same agent loop as the CLI from your own Python program — first a read-only explorer, then an *unattended* agent that can act safely with nobody watching (pre-approved tools, an auto-accept mode, a gatekeeper callback, and a hard turn cap). Estimated time: 10-12 minutes.

> **⚠️ Diff-merge lab:** You'll start from skeleton files in `sdk/` and merge in the completed code from `extra/`. **Each skeleton is valid Python but will refuse to run until you merge.** For each part: view skeleton → diff/merge → run.

---
<br><br>

## 1: Install the Agent SDK
**What we're doing:** Installing the Python package.  
**Why:** The SDK gives you the same tools, agent loop, and context management that power Claude Code — as a library. It drives the bundled CLI under the hood, so your existing login carries over with no extra auth.

**Action:** In a terminal, run:
```bash
pip install claude-agent-sdk
```

---
<br><br>

## 2: View the Skeleton and Map It to the CLI
**What we're doing:** Reading `sdk/agent_loop.py` and connecting it to commands you already know.  
**Why:** Nothing here is new — it's yesterday's CLI with Python names. The two TODOs mark the only pieces that make it an *agent*: the options and the message loop.

**Action:** Open the skeleton and read the two TODO blocks:
```bash
code sdk/agent_loop.py
```

| SDK piece | CLI equivalent you've used |
|---|---|
| `query(prompt=..., options=...)` | `claude -p "<prompt>"` |
| `ClaudeAgentOptions(allowed_tools=[...])` | `--allowedTools "..."` |
| `ClaudeAgentOptions(max_turns=...)` | `--max-turns` |
| iterating `AssistantMessage` / `ResultMessage` | `--output-format stream-json` events |

`query()` returns an async iterator — your `async for` loop receives each message as the agent works, ending with a `ResultMessage` of stats.

![skeleton view](./images/ccode332.png?raw=true "skeleton view")

---
<br><br>

## 3: Diff and Merge
**What we're doing:** Comparing the skeleton against the completed version and merging.  
**Why:** Seeing only the *differences* highlights exactly what turns a script into an agent program.

**Action:** Run:
```bash
code -d sdk/agent_loop.py extra/agent_loop.txt
```

For each highlighted block, merge the completed code (right) into `sdk/agent_loop.py` (left) using the gutter arrows or copy/paste. When the differences are gone, **save the left file** and close the diff tab.

![diff merge](./images/ccode333.png?raw=true "diff merge")

---
<br><br>

## 4: Run Your Agent
**What we're doing:** Executing the program.  
**Why:** First proof that an agent loop runs under *your program's* control.

**Action:** Run:
```bash
python3 sdk/agent_loop.py "What files are in the sdk directory? Answer in one sentence."
```

You'll see `[claude]` lines, then the `ResultMessage` stats: turns used, duration, final result.

![sdk run](./images/ccode334.png?raw=true "sdk run")

---
<br><br>

## 5: Force Multiple Turns, Then Try to Write
**What we're doing:** Giving the agent a tool-using prompt, then a prompt it can't fulfill.  
**Why:** To see the *loop* part of "agent loop" — and to see what `allowed_tools=["Read","Glob","Grep"]` quietly prevents.

**Action:** Run a prompt that forces tool use:
```bash
python3 sdk/agent_loop.py "Find every TODO comment in the .py files under sdk/ and list them"
```
Note **Turns used** — the agent used Grep/Read across turns. Now try to make it write:
```bash
python3 sdk/agent_loop.py "Create a file named sdk_test.txt containing hello"
```
The write isn't blocked — it just isn't *pre-approved*, so with no human attached it can't proceed. Confirm nothing was created: `ls sdk_test.txt`. Next we do this on purpose, safely.

---
<br><br>

## 6: View the Unattended Skeleton and Its Permission Funnel
**What we're doing:** Reading `sdk/auto_agent.py` and the order in which a tool call gets decided.  
**Why:** In the CLI, "undecided" means *ask the human*. Unattended, there is no human — so your code must be the last word.

**Action:** Open it:
```bash
code sdk/auto_agent.py
```
Every tool call falls through this funnel until something decides it:

1. `allowed_tools` list → pre-approved? Done.
2. `permission_mode="acceptEdits"` → file edit? Auto-approved.
3. `can_use_tool` callback → **your Python function** decides: allow, deny, or rewrite the input.

The skeleton already provides a `keep_alive` PreToolUse hook and a `prompt_stream()` generator — both required so the `can_use_tool` callback can run in streaming mode.

---
<br><br>

## 7: Diff and Merge the Unattended Agent
**What we're doing:** Merging the completed implementation.  
**Why:** The diff shows exactly the three decisions you're adding: the gatekeeper logic, the options, and the result handling.

**Action:** Run, merge each block from the right into the left, save, and close:
```bash
code -d sdk/auto_agent.py extra/auto_agent.txt
```

![diff merge auto](./images/ccode335.png?raw=true "diff merge auto")

---
<br><br>

## 8: Run It Unattended and Inspect the Output
**What we're doing:** Starting the agent and not touching the keyboard, then checking its work.  
**Why:** The whole point — start it, take your hands off, then trust-but-verify.

**Action:** Run:
```bash
python3 sdk/auto_agent.py
```
Watch the `[gatekeeper] auto-approving: ...` lines, then the final turn count. Check the product:
```bash
cat agent_report.md
```
You should see every `.js` file listed with a one-line description.

![gatekeeper run](./images/ccode336.png?raw=true "gatekeeper run")

---
<br><br>

## 9: Trigger the Deny Path
**What we're doing:** Making the gatekeeper say no.  
**Why:** Allow-paths are easy. The deny-path is what makes unattended safe.

**Action:** Edit the `TASK` string in `sdk/auto_agent.py` to:
```python
TASK = "Use a Bash rm command to delete agent_report.md. Then say DONE."
```
Run it again (`python3 sdk/auto_agent.py`). The gatekeeper denies the `rm`; Claude sees the denial and adapts. Confirm `agent_report.md` still exists, then **restore the original TASK string**.

---
<br><br>

## 10: Why max_turns and Sandboxing Matter
**What we're doing:** Placing the four policy layers next to OS-level enforcement.  
**Why:** A deny-loop can become an infinite loop. And policy decides what Claude *may try*; enforcement decides what any command can *actually touch*.

**Action:** Read (nothing to run):

- **`max_turns=10`** guarantees the program *ends*, with `ResultMessage.subtype == "error_max_turns"` telling your code why. Every unattended run needs a bound — turns, budget, or wall-clock.
- **`/sandbox`** in the CLI enables OS-enforced boundaries (which file paths and network domains commands may reach). Policy (allowlists, callbacks) + enforcement (sandbox) is how production agents stay both fast and survivable.
- The cloud surfaces in Labs 13 and 14 run in Anthropic-managed isolated VMs — the same idea, hosted for you.

---
<br><br>

## 11: Connect It Back to the CLI
**What we're doing:** Confirming this is the same loop, not a lookalike.  
**Why:** One mental model for everything: the CLI, the SDK, GitHub Actions, and cloud sessions all run this loop.

**Action:** Run the read-only program's CLI equivalent and compare:
```bash
claude -p "What files are in the sdk directory? Answer in one sentence." --output-format json | jq '{result: .result, num_turns: .num_turns, duration_ms: .duration_ms}'
```
The JSON fields mirror the `ResultMessage` attributes your program printed. Same loop, different driver.

---
<br><br>

## 12: Exit
**Action:** Nothing running to exit — SDK programs end when the loop ends. Optionally clean up:
```bash
rm -f agent_report.md sdk_test.txt
```

## Lab Summary
✅ You've built and exercised:
- A pip-installed Agent SDK environment (bundling the CLI)
- A read-only `query()` loop merged from skeleton to working program
- An unattended agent with four safety layers: allowed_tools, permission_mode, can_use_tool, max_turns
- The deny path — blocking a destructive command programmatically
- The policy-vs-enforcement distinction: allowlists/callbacks vs `/sandbox`
- The CLI-to-SDK mapping: same agent loop, programmatic driver

<br><br>
---
## END OF LAB
---
<br><br>

# Lab 12: CI Automation with GitHub Actions
## Lab Purpose
Author a GitHub Actions workflow that runs Claude Code in CI using `anthropics/claude-code-action@v1`, understand its trigger and configuration model, and know what it takes to run it in your own repos. Estimated time: 10-12 minutes.

> **⚠️ Note:** You'll author and inspect the workflow in the Codespace. Actually pushing and running it is an **optional advanced** exercise — the workshop repo (`skillrepos/ccode`) isn't yours, so a live run requires your own repo plus `/install-github-app` (covered in step 8).

---
<br><br>

## 1: Create the Workflow Directory
**What we're doing:** Setting up the standard GitHub Actions location.  
**Why:** GitHub discovers workflows only in `.github/workflows/`.

**Action:** Run:
```bash
mkdir -p .github/workflows
```

---
<br><br>

## 2: Author the @claude Responder Workflow
**What we're doing:** Writing a workflow where Claude responds to `@claude` mentions in issues and PR comments.  
**Why:** This is the canonical pattern: a teammate types `@claude fix the TypeError in the dashboard` in a PR comment, and Claude analyzes, implements, and pushes — on GitHub's runners, not your machine.

**Action:** Make a new file `.github/workflows/claude.yml` and copy/paste the following contents into it:

```yaml
name: Claude Code
on:
  issue_comment:
    types: [created]
  pull_request_review_comment:
    types: [created]
jobs:
  claude:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          # No prompt: the action auto-detects interactive mode and
          # responds to @claude mentions in comments
```

![workflow file](./images/ccode338.png?raw=true "workflow file")

---
<br><br>

## 3: Add a Scheduled Automation Workflow
**What we're doing:** Writing a second workflow that runs on a cron schedule with an explicit `prompt:`.  
**Why:** With a `prompt:`, the action auto-detects *automation mode* — it runs immediately on the trigger instead of waiting for a mention. This is "loops instead of prompts" at the CI level.

**Action:** Make a new file `.github/workflows/daily-report.yml` with:

```yaml
name: Daily Report
on:
  schedule:
    - cron: "0 9 * * 1-5"
jobs:
  report:
    runs-on: ubuntu-latest
    steps:
      - uses: anthropics/claude-code-action@v1
        with:
          anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
          prompt: "Summarize yesterday's commits and open issues as a markdown report"
          claude_args: |
            --max-turns 5
            --model claude-sonnet-4-6
```

---
<br><br>

## 4: Understand claude_args
**What we're doing:** Connecting the workflow back to Lab 9.  
**Why:** `claude_args` is a passthrough to the same CLI flags you used headlessly — the action is the Agent SDK running on a GitHub runner.

**Action:** Read the key mappings:

| In claude_args | You used it as |
|---|---|
| `--max-turns 5` | `max_turns` in the SDK (Lab 11) |
| `--allowedTools "Read,Edit,Bash"` | `--allowedTools` / `allowed_tools` (Labs 9, 11) |
| `--append-system-prompt "..."` | custom instructions per workflow |
| `--model claude-sonnet-4-6` | `/model` from Day 1 |

Also note: `prompt:` accepts skill invocations (e.g. `/code-review:code-review ...`) and the action respects your repo's CLAUDE.md — your Day 1 assets work in CI too.

---
<br><br>

## 5: Have Claude Explain the Workflow
**What we're doing:** Using headless Claude to review what you just wrote.  
**Why:** Reinforces both skills at once — and catches authoring mistakes.

**Action:** Run:
```bash
cat .github/workflows/claude.yml | claude -p "Explain this GitHub Actions workflow: what triggers it, what the action does, what secrets it needs, and one risk to consider."
```

![claude explains](./images/ccode339.png?raw=true "claude explains")

---
<br><br>

## 6: Know the Security Basics
**What we're doing:** Reviewing the non-negotiables before anyone runs this for real.  
**Why:** CI agents act with real credentials on real repos.

**Action:** Read:

- The API key comes **only** from `${{ secrets.ANTHROPIC_API_KEY }}` — never hardcoded.
- The Claude GitHub App needs read/write on **Contents, Issues, Pull requests** — and nothing more.
- Bound every job: `--max-turns` in `claude_args` plus a workflow-level `timeout-minutes`.
- Review Claude's PRs like any contributor's. CI runs are unattended runs — Lab 11 rules apply.

---
<br><br>

## 7: Deep Review in CI: claude ultrareview
**What we're doing:** Noting the purpose-built CI review subcommand.  
**Why:** For PR review specifically, there's a heavier-duty option than authoring your own workflow.

**Action:** Read:

```bash
claude ultrareview        # review current branch vs default branch
claude ultrareview 1234   # review PR #1234
```

The `claude ultrareview` subcommand launches the same deep multi-agent review as `/code-review ultra` from CI or a script: it runs a fleet of reviewer agents in a remote sandbox, blocks until finished, prints verified findings to stdout, and exits 0/1 — ready to gate a pipeline. (Requires claude.ai authentication; research preview.)

---
<br><br>

## 8: (OPTIONAL ADVANCED) Run It in Your Own Repo
**What we're doing:** The path to a live run, for later or for students with a personal repo.  
**Why:** The workshop repo isn't yours, so the live loop happens on your own GitHub account.

**Action:** In your own repo (admin access required):
1. Run `claude` and type `/install-github-app` — it guides you through installing the Claude GitHub App and adding the `ANTHROPIC_API_KEY` secret.
2. Commit the `claude.yml` workflow from step 2 to `.github/workflows/`.
3. Open an issue and comment: `@claude suggest an improvement to the README`.
4. Watch the Actions tab — Claude analyzes and responds (or opens a PR).

---
<br><br>

## 9: Metering Reminder and Cleanup
**What we're doing:** Closing the loop on cost awareness.  
**Why:** Actions usage falls under the June 15, 2026 separate Agent SDK metering on subscription plans — plus normal GitHub Actions minutes.

**Action:** Read the note above, and leave the workflow files in place — they're harmless here (no secret is configured in the workshop repo, and no one will comment `@claude` on it).

## Lab Summary
✅ You've successfully:
- Authored an `@claude` responder workflow with `claude-code-action@v1`
- Authored a scheduled automation workflow with explicit `prompt:`
- Mapped `claude_args` to the CLI/SDK flags from Labs 9-11
- Used headless Claude to review your own workflow
- Learned the security baseline and the `claude ultrareview` CI subcommand
- Identified the `/install-github-app` path for your own repos

<br><br>
---
## END OF LAB
---
<br><br>

# Lab 13: Scheduled Tasks: /loop and Cloud Routines
## Lab Purpose
Schedule time-driven work two ways: `/loop` for a recurring prompt inside your session, and **Routines** for a saved job that runs on Anthropic-managed cloud infrastructure even when your machine is off — then place both in the full scheduling landscape. Estimated time: 10-12 minutes.

**NOTE: `/loop` requires Claude Code v2.1.72+. Routines require a claude.ai subscription login (Pro/Max/Team/Enterprise with Claude Code on the web) and are in research preview.**

---
<br><br>

## 1: Create a Recurring /loop
**What we're doing:** Scheduling a 1-minute recurring task with an observable side effect, inside a session.  
**Why:** `/loop` tasks are session-scoped — they live and die with this conversation. A file that grows a line per fire makes the invisible scheduler visible.

**Action:** Start `claude-yolo`, then type:
```
/loop 1m append one line to loop_status.log with the current time and the count of .js files in this directory
```
Claude converts the interval to a cron expression (`*/1 * * * *` — every minute is the minimum), schedules it via `CronCreate`, and confirms an 8-character job ID.

![loop created](./images/ccode340.png?raw=true "loop created")

---
<br><br>

## 2: Watch It Fire and Verify
**What we're doing:** Letting the scheduler run, then checking the file.  
**Why:** Seeing a prompt arrive that *you didn't type* is the moment scheduled tasks click. Two timestamped lines = two autonomous fires.

**Action:** Leave the session idle. Within a minute or so the scheduled prompt fires between turns and Claude appends to the log. Wait for it to fire **twice**, then:
```
! cat loop_status.log
```
(Timing note: the scheduler adds deterministic jitter — up to half the interval for sub-hourly tasks — so fires won't land exactly on the minute.)

![loop fired](./images/ccode341.png?raw=true "loop fired")

---
<br><br>

## 3: List Tasks and Add a One-Time Reminder
**What we're doing:** Managing tasks in natural language.  
**Why:** Natural language *is* the management interface — under the hood Claude calls `CronList` / `CronCreate`.

**Action:** Type:
```
what scheduled tasks do I have?
```
You'll see the task's ID, cron schedule, and prompt. Now add a single-fire task — no `/loop` needed:
```
in 2 minutes, remind me to check whether the loop is still firing
```
One-shots use the same machinery (a pinned time) and delete themselves after firing.

![task list](./images/ccode342.png?raw=true "task list")

---
<br><br>

## 4: Delete the Loop and Learn the Lifecycle
**What we're doing:** Cancelling the recurring task and learning when loops survive.  
**Why:** These boundaries are exactly why cloud Routines exist.

**Action:** Type `cancel the loop_status.log task` (this runs `CronDelete`), confirm with `what scheduled tasks do I have?`, then read the rules:

- **Session-scoped:** closing the terminal or starting a new conversation stops tasks; `claude --resume` / `--continue` restores unexpired ones.
- **7-day expiry:** recurring tasks fire one last time at day 7, then delete themselves.
- **Min interval 1 minute**; **no catch-up** (missed fires collapse to one); kill switch `CLAUDE_CODE_DISABLE_CRON=1`.
- **Variants:** `/loop <prompt>` with no interval lets Claude pick the wait each iteration; bare `/loop` runs a maintenance prompt (or your `.claude/loop.md`).

Type `exit` — and notice: your loop machinery just died with the session. That limit is what the cloud tier removes.

---
<br><br>

## 5: Confirm /schedule Is Available
**What we're doing:** Checking the Routines prerequisite.  
**Why:** `/schedule` only appears with claude.ai auth and the feature enabled — it's hidden if you're authenticated with an API key.

**Action:** Start `claude`, type `/schedule`, and confirm it's recognized. If you get "Unknown command": check you're logged in via claude.ai (`/login`) and that no `ANTHROPIC_API_KEY` is set. (You can always manage routines at **claude.ai/code/routines**.)

> **⚠️ No personal repo?** Routines clone a **GitHub repo** on each run. If you don't have a small personal repo connected, follow the instructor demo for steps 6-8 and read along.

---
<br><br>

## 6: Create a Daily Routine
**What we're doing:** Describing a scheduled cloud routine conversationally.  
**Why:** `/schedule <description>` collects the same info the web form does — prompt, repo, schedule — and saves the routine to your cloud account.

**Action:** Type (adjust the repo to your own):
```
/schedule every weekday at 9am, review open issues in my repo and post a one-paragraph triage summary as a comment on the newest one
```
Answer Claude's follow-ups (repository, schedule confirmation). If GitHub isn't connected, Claude prompts you to run `/web-setup` first.

![schedule create](./images/ccode343.png?raw=true "schedule create")

---
<br><br>

## 7: List and Run It On Demand
**What we're doing:** Verifying the routine, then triggering it immediately.  
**Why:** Routines live on your claude.ai account, not in this session. "Run now" is how you validate before trusting the schedule.

**Action:** Type:
```
/schedule list
```
You should see your routine (also visible at **claude.ai/code/routines**). Then:
```
/schedule run
```
Each run creates a full Claude Code **cloud session** — autonomous, **no permission prompts**, using the repos and connectors the routine includes.

![schedule list](./images/ccode344.png?raw=true "schedule list")

---
<br><br>

## 8: Inspect the Run
**What we're doing:** Reading what the routine actually did.  
**Why:** A *green* status only means the session exited without infrastructure errors — it does **not** mean your task succeeded. Always read the transcript.

**Action:** At **claude.ai/code/routines**, click your routine, then the latest run to open it as a session. Review what Claude did; from here you could comment, review changes, or open a PR.

![routine run](./images/ccode345.png?raw=true "routine run")

---
<br><br>

## 9: Know the Trigger Types
**What we're doing:** Seeing that schedules are only one of three triggers.  
**Why:** The same saved routine can be fired by time, by your systems, or by GitHub.

**Action:** Read:

| Trigger | How it fires | Set up via |
|---|---|---|
| **Schedule** | Recurring cadence or one-off timestamp (min interval 1 hour) | `/schedule` or web |
| **API** | HTTP POST to a per-routine `/fire` endpoint with a bearer token; optional `text` passes run context | web only |
| **GitHub event** | Pull request or release events, with filters | web only; needs Claude GitHub App |

---
<br><br>

## 10: The Three-Way Scheduling Comparison
**What we're doing:** Putting `/loop`, Desktop scheduled tasks, and cloud Routines side by side.  
**Why:** Picking the right tier is the actual skill. (You'll meet the Desktop/Cowork tier hands-on in Day 3, Lab 19.)

**Action:** Read:

| | Cloud (Routines) | Desktop scheduled tasks | `/loop` |
|---|---|---|---|
| Runs on | Anthropic cloud | Your machine | Your machine |
| Requires machine on | **No** | Yes | Yes |
| Requires open session | No | No | **Yes** |
| Access to local files | No (fresh clone) | Yes | Yes |
| Permission prompts | No (autonomous) | Configurable | Inherits from session |
| Minimum interval | 1 hour | 1 minute | 1 minute |

Rule of thumb: **`/loop`** for quick polling during a session, **Desktop/Cowork tasks** when the job needs local files, **Routines** for work that must run with the laptop closed. (Awareness: for *event-driven* pushes into a live session — CI failures, alerts — see Channels in the docs.)

---
<br><br>

## 11: Clean Up
**What we're doing:** Removing or pausing the practice routine.  
**Why:** Routines count against a daily run allowance and act as *you* (commits/comments use your GitHub identity) — don't leave practice automation live.

**Action:** At **claude.ai/code/routines**, open your routine and either toggle off **Repeats** (pause) or delete it. Verify with `/schedule list`.

---
<br><br>

## 12: Exit
**Action:** Type `exit`.
```
exit
```

## Lab Summary
✅ You've successfully:
- Created a recurring session task with `/loop 1m ...` and watched it fire twice
- Managed tasks in natural language and learned the session-scoped lifecycle
- Created a cloud routine with `/schedule`, listed it, and ran it on demand
- Inspected a run's transcript (and learned green ≠ task success)
- Learned the three trigger types and the official 3-way scheduling comparison

<br><br>
---
## END OF LAB
---
<br><br>

# Lab 14: Managed Agents: Background, Cloud, and Web
## Lab Purpose
Run Claude sessions that don't need you watching: dispatch a **background agent** and manage it from the `claude agents` dashboard, then start a **cloud session** at claude.ai/code and pull it into your terminal with `--teleport`. Many agents, your machine and the cloud, one mental model. Estimated time: 10-12 minutes.

**NOTE: Agent view requires Claude Code v2.1.139+; Claude Code on the web is a research preview (Pro/Max/Team, Enterprise premium seats). Background and cloud sessions consume your subscription quota like interactive ones.**

---
<br><br>

## 1: Dispatch a Background Session
**What we're doing:** Starting a task that immediately detaches from your terminal.  
**Why:** `claude --bg` is fire-and-forget: the session is hosted by a per-user supervisor process, so it keeps working even if you close this shell.

**Action:** In a terminal, run:
```bash
claude --bg --name "js-headers" "Add a one-line comment header to goodbye.js describing what it does"
```
Note the output: a short session ID plus the management commands (`claude agents`, `claude attach <id>`, `claude logs <id>`, `claude stop <id>`).

![bg dispatch](./images/ccode346.png?raw=true "bg dispatch")

---
<br><br>

## 2: Open Agent View and Read the State Icons
**What we're doing:** Opening the dashboard for all background sessions.  
**Why:** One screen answers three questions: what's running, what needs me, what's done.

**Action:** Run:
```bash
claude agents
```
Your `js-headers` session appears as a row grouped by state, with an AI-generated one-line summary and a dispatch input at the bottom. Press `?` for shortcuts. Decode the icons:

- **Animated** = working; **yellow** = needs input; **green** = completed; **red** = failed; `∙` = process exited but you can still peek/reply/attach (it restarts where it left off); `✢` = a `/loop` session sleeping between iterations.
- A `PR #N` label means the session opened a pull request.

![agent view](./images/ccode347.png?raw=true "agent view")

---
<br><br>

## 3: Peek Without Attaching
**What we're doing:** Checking on the session in a side panel.  
**Why:** Most check-ins don't need the full transcript.

**Action:** Select your row with the arrow keys and press `Space`. The peek panel shows the latest output or the question it's blocked on. You can type a reply right here and press `Enter` — without leaving the dashboard.

![peek panel](./images/ccode348.png?raw=true "peek panel")

---
<br><br>

## 4: Fan Out a Second Agent
**What we're doing:** Starting another session from the dashboard input.  
**Why:** Every prompt entered here starts its *own* session — this is how you run parallel work.

**Action:** In the dispatch input at the bottom, type and Enter:
```
List every TODO or FIXME comment in this project and write them to todos.md
```
A second row appears and both run in parallel. **Worktree note:** before editing, a background session moves itself into an isolated git worktree under `.claude/worktrees/`, so parallel agents can't trample each other. (Tip: you can also run a plain shell command as a managed row — type `! npm test` in the dispatch input; no Claude session, no tokens.)

---
<br><br>

## 5: Attach, Then Detach
**What we're doing:** Entering the full conversation, then leaving it running.  
**Why:** When a peek isn't enough, attach — it becomes a normal interactive session.

**Action:** Select a row and press `Enter` (or `→`). Claude posts a recap of what happened while you were away. Look around, then press `←` on an empty prompt to detach. **Detaching never stops a background session.** (Any normal session can become a background agent the same way — `/bg` or a single `←`.)

![attached session](./images/ccode349.png?raw=true "attached session")

---
<br><br>

## 6: Script It, Then Clean Up
**What we're doing:** Getting machine-readable status, then stopping the practice sessions.  
**Why:** Dashboards are for humans; JSON is for your scripts (e.g., a CI gate). And leftover sessions keep consuming attention and quota.

**Action:** Press `Esc` to exit agent view, then:
```bash
claude agents --json | jq '.[] | {name, status, cwd}'
```
Each live session reports `name`, `status`, `cwd`, `pid`, `sessionId` (and `waitingFor` when blocked). Then run `claude agents`, select each practice row, press `Ctrl+X` to stop and `Ctrl+X` again within two seconds to delete. **Caution:** deleting removes that session's worktree, including uncommitted changes. Press `Esc` to exit.

---
<br><br>

## 7: Open Claude Code on the Web
**What we're doing:** Visiting the cloud surface.  
**Why:** This is the same agent loop from Lab 11 — running in an isolated VM on Anthropic infrastructure instead of your machine.

**Action:** In your browser, go to **https://claude.ai/code** and sign in with your claude.ai account. Connect your GitHub account (first time only) and select a small personal repository — each cloud session starts by cloning your repo into a fresh VM.

> **⚠️ No personal repo?** Do steps 7-8 read-only, then follow the **instructor demo** for teleport — the flow is the lesson.

![web code home](./images/ccode350.png?raw=true "web code home")

---
<br><br>

## 8: Start a Cloud Session and Prove It's Untethered
**What we're doing:** Submitting a task that runs entirely in the cloud, then closing the tab.  
**Why:** The headline feature: cloud sessions persist when your browser closes (you can even monitor them from the Claude mobile app).

**Action:** Enter a self-contained task:
```
Add a "Project layout" section to the README that describes the repository structure. Keep it under 15 lines.
```
Submit it and watch the VM provision, repo clone, Claude work. While it's running, **close the tab**, wait ~30 seconds, then reopen `claude.ai/code` — your session is still there with the full transcript. Changes land on a `claude/`-prefixed branch with a **Create PR** option (don't create it — we'll teleport instead).

![cloud session](./images/ccode351.png?raw=true "cloud session")

---
<br><br>

## 9: Teleport the Session Down
**What we're doing:** Pulling the cloud session into your terminal.  
**Why:** Start in the cloud, finish locally — `--teleport` hands you the branch *and* the conversation.

**Action:** In a Codespace terminal, get a checkout of the **same repo** with clean git state, then teleport:
```bash
cd /workspaces && git clone https://github.com/<you>/<your-repo>.git && cd <your-repo>
claude --teleport
```
Pick the session from step 8 in the interactive list (or `claude --teleport <session-id>`). Claude fetches and checks out the session's branch and loads the full conversation history.

![teleport picker](./images/ccode352.png?raw=true "teleport picker")

---
<br><br>

## 10: Continue the Conversation Locally
**What we're doing:** Proving the context came with the branch.  
**Why:** This is a continuation, not a copy — Claude remembers the cloud work.

**Action:** In the teleported session, type:
```
Summarize what you changed in the cloud session, then suggest one follow-up improvement.
```
Claude answers from the imported history. Confirm the branch: `! git branch --show-current` — you're on the session's `claude/...` branch.

![teleported session](./images/ccode353.png?raw=true "teleported session")

---
<br><br>

## 11: The Whole Movement Map
**What we're doing:** Learning all the doors between surfaces.  
**Why:** Cloud↔terminal movement has specific directions and rules.

**Action:** Read:

- **Cloud → terminal:** `claude --teleport` (picker), `/teleport` or `/tp` inside a session, or press `t` on a session in `/tasks`. Requires: claude.ai auth, same repo (not a fork), clean git state, branch pushed.
- **Terminal → cloud:** `claude --remote "<task>"` starts a **new** cloud session from your repo/branch (push first). Teleport is one-way cloud→local; the Desktop app's "Continue in" menu can send a local session to the web.
- **`--remote` ≠ `--remote-control`.** *Instructor demo:* **Remote Control** (`/remote-control`) exposes your *local* session so you can monitor and steer it from claude.ai or your phone.

---
<br><br>

## 12: Exit and Day 2 Wrap
**What we're doing:** Closing the loop on the day.  
**Why:** You now own the full spectrum of running Claude without watching it.

**Action:** Type `exit`. Look at what you can now do that you couldn't yesterday:

| Lever | You learned |
|---|---|
| Loops instead of prompts | bash loops + `-p` (Lab 9), `/goal` (Lab 10) |
| Programs instead of sessions | Agent SDK, read-only + unattended (Lab 11) |
| Runners instead of your machine | GitHub Actions (Lab 12), Routines (Lab 13), Web (Lab 14) |
| Schedules instead of triggers-by-you | `/loop` + Routines (Lab 13) |
| Many agents, one screen | agent view + cloud/web sessions (Lab 14) |

```
exit
```

## Lab Summary
✅ You've successfully:
- Dispatched background sessions with `claude --bg` and from the dashboard input
- Read agent view's state model and peeked/replied without attaching
- Attached and detached cleanly; scripted status with `claude agents --json`
- Started a cloud session at claude.ai/code and verified it persists with the browser closed
- Teleported a cloud session into your terminal (branch + conversation) and continued locally
- Mapped all surface movements: --teleport, /tp, --remote, and Remote Control

<br><br>
---
## END OF LAB
---
<br><br>



# 🗓️ DAY 3: The Claude Platform — Artifacts, Cowork, and Connectors
**Today we leave the terminal: the same Claude concepts (skills, plugins, MCP, scheduling) in claude.ai and the Claude Desktop app, ending with the capstone.**

**NOTE: Most Day 3 labs run OUTSIDE the Codespace — in your browser at claude.ai or in the Claude Desktop app on your machine. Complete the Day 3 pre-class setup in the README first.**

---
<br><br>

# AI-Powered Coding with Claude Code
## Learn practical workflows, hands-on coding techniques, and structured interactions
## Session Labs — Day 3: The Claude Platform (artifacts, Cowork, connectors, capstone)
## Revision 6.0 - 06/11/26

<br><br>

**IMPORTANT: Day 3 labs run OUTSIDE the Codespace.** You'll work in **claude.ai in your browser** and in the **Claude Desktop app** on your own machine (both were part of the pre-class setup). Each lab below starts with an environment banner telling you where it runs. Keep your Codespace around, though — the capstone (Lab 21) returns to it.

**You need a paid Claude account (course prerequisite) and Claude Desktop installed locally. Cowork is included on ALL paid plans (Pro/Max/Team/Enterprise).**

> **Instructor note / nice surprise:** Usage limits are doubled from June 5 – July 5, 2026 as a promo — good timing for a hands-on day. Cowork tasks still consume usage faster than chat, so keep prompts focused.

<br><br>

---
<br><br>

# Lab 15: Day 3 Warm-Up — Where We've Been, Where We're Going
## Lab Purpose
Map the journey from the terminal (Days 1–2) to the same Claude in the apps, and confirm your claude.ai and Claude Desktop setups are ready. Estimated time: 5-8 minutes.

**Environment: claude.ai in your browser AND Claude Desktop app**

---
<br><br>

## 1: The Map — One Claude, Many Surfaces
**What we're doing:** Orienting before we touch anything.
**Why:** Everything you built in Days 1–2 — skills, plugins, MCP, scheduled work, agents — exists on the consumer surfaces too. Day 3 is about recognizing the same concepts in new clothes.

**Action:** No typing yet. Look at this mapping — we'll prove each row today:
```
Day 1-2 (terminal)              Day 3 (apps)
------------------              ------------------------------
SKILL.md skills (Lab 4)    -->  Skills in claude.ai / Cowork
Plugins (Lab 5)            -->  Plugins in Cowork's Customize
MCP servers (Lab 7)        -->  Connectors (managed remote MCP)
/loop + Routines (Day 2)   -->  Cowork scheduled tasks
Background agents (Day 2)  -->  Cowork autonomous tasks
Headless output (Day 2)    -->  Artifacts and Live Artifacts
```

---
<br><br>

## 2: Sign In to claude.ai
**What we're doing:** Opening claude.ai and verifying your account.
**Why:** Lab 16 runs entirely in the browser.

**Action:** In your browser, go to:
```
https://claude.ai
```
Sign in with your course account. Open your settings (your initials/avatar, lower left) and confirm your plan shows a paid tier (Pro/Max/Team/Enterprise).

![claude.ai signed in](./images/ccode361.png?raw=true "claude.ai signed in")

---
<br><br>

## 3: Find the Unified Directory
**What we're doing:** Locating the browsable directory of connectors, skills, and plugins.
**Why:** Anthropic now surfaces skills, connectors, and plugins in one unified directory — the consumer face of everything you hand-built in Labs 4–7.

**Action:** In claude.ai settings, look for the section listing **Connectors** (with a "Browse" or directory option) and the section for **Skills/Capabilities**. Scroll the directory — notice familiar names (GitHub, Google Drive, document skills). Don't connect anything yet; that's Lab 18.

![Unified directory](./images/ccode362.png?raw=true "Unified directory")

---
<br><br>

## 4: Open Claude Desktop and Find the Three Tabs
**What we're doing:** Launching the desktop app and identifying its surfaces.
**Why:** Claude Desktop has three tabs — **Chat / Cowork / Code** — and you already know one of them from Day 2 (the Code tab is the managed-agents surface).

**Action:** Open the Claude Desktop app on your machine. Sign in with the same account if prompted. Locate the mode selector with **Chat**, **Cowork**, and **Code**.

![Three tabs](./images/ccode363.png?raw=true "Three tabs")

---
<br><br>

## 5: Peek at Each Tab
**What we're doing:** Clicking through Chat, Code, and Cowork.
**Why:** A 30-second tour now saves confusion later.

**Action:**
1. Click **Chat** — this is claude.ai in an app.
2. Click **Code** — recognize this? It's the Claude Code sessions surface from Day 2.
3. Click **Cowork** — new territory. You may see a "Setting up Claude's workspace" message the first time; that's expected (it's provisioning the isolated VM Cowork runs tasks in).

---
<br><br>

## 6: Check Your Working Assumptions
**What we're doing:** Confirming two practical facts before the Cowork labs.
**Why:** Cowork has two rules that surprise people.

**Action:** Note these — they'll matter in Labs 17–21:
```
1. Cowork tasks run ON your computer. The Desktop app must stay
   open and your machine awake, or the task/session ends.
2. Cowork tasks can take a few minutes. That's normal — it's
   doing real multi-step work, like a background agent.
```

---
<br><br>

## 7: Set the Frame
**What we're doing:** Stating the Day 3 thesis.
**Why:** So you watch for it all day.

**Action:** Keep this in mind: **it's the same agentic engine.** Cowork literally runs Claude Code's architecture under the hood. The SKILL.md anatomy from Lab 4, the plugin packaging from Lab 5, and the MCP protocol from Lab 7 all reappear today — just with friendlier UI.

---
<br><br>

## Lab Summary
✅ You've successfully:
- Mapped Day 1–2 terminal concepts to their Day 3 platform equivalents
- Signed in to claude.ai and verified your paid plan
- Found the unified directory of connectors, skills, and plugins
- Opened Claude Desktop and toured the Chat / Cowork / Code tabs
- Learned Cowork's two ground rules (app stays open; tasks take minutes)

<br><br>
---
## END OF LAB
---
<br><br>
# Lab 16: Artifacts: Interactive and AI-Powered
## Lab Purpose
Create an interactive artifact in claude.ai and iterate on it conversationally, then build an *AI-powered* artifact that calls Claude from inside — a mini AI app with no API key and no backend. Estimated time: 10-12 minutes.

**Environment: claude.ai in your browser**

---
<br><br>

## 1: Ask for an Interactive Study Aid
**What we're doing:** Prompting Claude to build a small web app about this course.  
**Why:** Substantial, self-contained content (apps, pages, documents) automatically becomes an *artifact* — a separate panel beside the chat.

**Action:** In a new chat on claude.ai, type:
```
Build an interactive flashcard quiz app to help me study Claude Code.
Include 10 flashcards covering: plan mode, /compact, CLAUDE.md, skills,
subagents, plugins, hooks, MCP, headless -p mode, and background agents.
Show a question, let me flip to reveal the answer, and track my score.
```

![Artifact being created](./images/ccode364.png?raw=true "Artifact being created")

---
<br><br>

## 2: Watch It Build, Then Toggle Code vs Preview
**What we're doing:** Observing the live render and viewing the source.  
**Why:** Artifacts are real React/HTML code you can inspect — the same kind of output Claude Code produces, just rendered for you.

**Action:** Watch the artifact panel open beside the chat and the app appear; click through a few flashcards and flip one. Then, in the panel header, use the **Code / Preview** toggle to skim the source and switch back.

![Flashcard app](./images/ccode365.png?raw=true "Flashcard app")

---
<br><br>

## 3: Iterate Conversationally
**What we're doing:** Changing the artifact by just asking — twice.  
**Why:** Iteration is the core artifact workflow — no edit/compile cycle — and every iteration is kept as a version.

**Action:** In the chat, type:
```
Add a "shuffle" button and show my score as a percentage at the end,
with a different message for scores above and below 70%.
```
Test the shuffle, then restyle it:
```
Restyle it with a dark theme and larger card text.
```

---
<br><br>

## 4: Browse Version History
**What we're doing:** Stepping back through artifact versions.  
**Why:** Every iteration is kept — like `/rewind` from Lab 3, but for artifacts.

**Action:** In the artifact panel, find the version selector (near the title or bottom of the panel). Step back to the first version, then return to the latest.

![Version history](./images/ccode367.png?raw=true "Version history")

---
<br><br>

## 5: Publish, Share, and Find Your Gallery
**What we're doing:** Publishing the artifact and locating where all your artifacts live.  
**Why:** Published artifacts are how you hand working tools to teammates — no hosting, no deploy. Viewers can **Remix** to open their own copy.

**Action:** Use the share/publish control (usually top-right of the panel), copy the link, and open it in a new tab — note the **Remix** ("Open in Claude") control. Then, from the claude.ai sidebar, open the **Artifacts** section and confirm your flashcard app is listed.

![Publish artifact](./images/ccode368.png?raw=true "Publish artifact")

---
<br><br>

## 6: The AI-Powered Twist
**What we're doing:** Setting up the key idea for the second half.  
**Why:** Your flashcards are static once built. *AI-powered artifacts* prompt Claude at runtime — the artifact becomes a small AI application.

**Action:** Read before prompting:
```
Regular artifact:    your prompt -> Claude writes app -> app is fixed
AI-powered artifact: your prompt -> Claude writes app -> app itself
                     calls Claude whenever the user clicks a button
```
No API key is involved. The artifact uses the Claude account of whoever is viewing it.

---
<br><br>

## 7: Build a Commit Message Generator
**What we're doing:** Building a developer mini-tool that calls Claude inside.  
**Why:** A commit message generator needs live AI — perfect demo, and it ties back to your Day 1–2 git work.

**Action:** In a **new chat**, type:
```
Build an AI-powered artifact: a "Commit Message Generator" app.
It should have a large textarea where I paste a git diff or a
description of my changes, and a Generate button. When clicked,
the app should call Claude to produce a one-line conventional
commit message plus an optional body, and display the result
with a copy button.
```

![AI artifact build](./images/ccode369.png?raw=true "AI artifact build")

---
<br><br>

## 8: Test It with a Real Diff
**What we're doing:** Exercising the in-artifact Claude call.  
**Why:** Proof that the artifact is calling the model live — Claude writes code that calls a built-in completion function available to artifacts; that's the entire "backend."

**Action:** Paste this into the artifact's textarea and click **Generate**:
```
Added phoneNumber as an optional field to the User class,
updated setName validation, and added a failing-then-fixed
email format test in user.test.js.
```
Notice the brief processing delay — that's a real model call inside the artifact.

![Generated commit message](./images/ccode370.png?raw=true "Generated commit message")

---
<br><br>

## 9: Refine the Embedded Prompt
**What we're doing:** Improving the AI behavior conversationally.  
**Why:** You can refine the *prompt inside the artifact* the same way you refine UI.

**Action:** In the chat, type:
```
Add a dropdown to choose the commit style: "conventional commits",
"plain", or "detailed with bullet-point body". Pass the choice into
the Claude prompt.
```
Test again with a different style selected.

---
<br><br>

## 10: Inspect the Code — Find the Claude Call
**What we're doing:** Looking at how the artifact prompts Claude.  
**Why:** Seeing the embedded prompt demystifies the magic — it's prompt engineering, shipped as an app.

**Action:** Switch the artifact panel to **Code** view and find where the app builds a prompt string and calls the Claude completion function. That string is a prompt template — the same skill you've practiced for two days, now embedded in software.

![Claude call in code](./images/ccode371.png?raw=true "Claude call in code")

---
<br><br>

## 11: Publish It and Understand Who Pays
**What we're doing:** Sharing the AI-powered app and learning the economics.  
**Why:** This removes the #1 blocker for sharing AI tools: keys and billing.

**Action:** Publish via the share control and copy the link (as in step 5). Then note these facts (worth writing down):
```
- Viewers of your published AI artifact sign in with THEIR Claude
  account; their generations count against THEIR subscription usage.
- You never expose an API key. There is no key in the code.
- You don't pay for other people's usage of your artifact.
```

---
<br><br>

## 12: Connect the Dots
**What we're doing:** Tying this to the course arc.  
**Why:** AI-powered artifacts are "headless mode for end users."

**Action:** Consider: in Lab 9 you piped a prompt into `claude -p`. This artifact does conceptually the same thing — wraps a prompt around input and returns Claude's output — but packaged for non-terminal users. Same engine, different surface. Leave these chats; next we move to Claude Desktop.

## Lab Summary
✅ You've successfully:
- Created an interactive artifact from a single prompt and toggled code/preview
- Iterated conversationally (features + styling) and browsed version history
- Published a shareable link and found your artifacts gallery
- Built an artifact that calls Claude at runtime (no API key, no backend)
- Tested live in-artifact generation and inspected the embedded prompt
- Learned that viewers' usage bills to their own subscription

<br><br>
---
## END OF LAB
---
<br><br>

# Lab 17: Cowork: Folder Tasks, Skills, and Plugins
## Lab Purpose
Point Cowork at a local folder of messy files and hand it a multi-step task, then use Cowork's **Customize** area to enable a skill and trigger it — recognizing both the autonomous-task pattern and the exact SKILL.md/plugin anatomy you built on Day 1. Estimated time: 10-12 minutes.

**Environment: Claude Desktop app (Cowork)**

---
<br><br>

## 1: Create a Practice Folder with Messy Files
**What we're doing:** Building a safe sandbox before letting an agent loose on your machine.  
**Why:** Cowork makes *real changes* to real files — always start with a disposable folder.

**Action:** Open your local terminal (macOS Terminal; on Windows use Git Bash) and run:
```bash
mkdir -p ~/cowork-lab && cd ~/cowork-lab

cat > "notes mtg FINAL(2).txt" << 'EOF'
team sync 6/9 - shipped login fix, Dana out thu, demo friday??
action items: bob-update tests, priya-draft release notes
blockers: staging env flaky again
EOF

cat > "expenses_stuff.csv" << 'EOF'
date,item,amount
2026-06-02,team lunch,84.50
2026-06-04,cloud hosting,120.00
2026-06-08,conference ticket,399.00
EOF

cat > "ideas-RANDOM.md" << 'EOF'
- add dark mode?
- commit msg generator (saw this in a workshop)
- automate the weekly status report somehow
EOF

ls -la
```
You should see three messily-named files.

---
<br><br>

## 2: Open Cowork and Point It at Your Folder
**What we're doing:** Switching Claude Desktop into Cowork mode and granting access to `~/cowork-lab` only.  
**Why:** Cowork is where Claude gets file access and autonomous execution — and you control exactly which folders it sees. Least privilege applies to agents too.

**Action:** In Claude Desktop, click the **Cowork** tab (if you see "Setting up Claude's workspace," wait). Then use the folder selector ("Add folder" / working-folder control) and choose your `cowork-lab` folder.

![Cowork tab](./images/ccode373.png?raw=true "Cowork tab")

---
<br><br>

## 3: Give the Multi-Step Task
**What we're doing:** Handing Cowork a real organize-and-report job.  
**Why:** This is the canonical Cowork pattern: describe the *outcome*, not the steps.

**Action:** In the Cowork prompt, type:
```
Organize this folder: rename the files with clean, descriptive
kebab-case names, then create a summary-report.md that summarizes
each file's contents, lists the action items from the meeting notes,
and totals the expenses. Show me your plan before renaming anything.
```

---
<br><br>

## 4: Review and Approve the Plan
**What we're doing:** Checking Claude's proposed actions before it touches files.  
**Why:** Same philosophy as Plan Mode in Lab 2 — review first, then execute.

**Action:** Read the plan Claude presents (proposed filenames, report outline). If it looks right, approve/confirm it.

![Cowork plan](./images/ccode375.png?raw=true "Cowork plan")

---
<br><br>

## 5: Watch the Progress UI
**What we're doing:** Observing an autonomous multi-step run.  
**Why:** This is the Day 2 background-agent experience with a visual task UI: steps, progress, live reasoning — and Claude may coordinate sub-agents (Lab 4's concept!) for parallel pieces.

**Action:** Watch the task execute. You can steer mid-run — try typing `In the report, also flag any blockers you find in the notes.` and Claude folds it in.

> ⏱ **Patience note:** Cowork tasks routinely take a few minutes. That's normal — it's doing real work. You can step away.

![Task progress](./images/ccode376.png?raw=true "Task progress")

---
<br><br>

## 6: Verify on Disk and Note the Safety Rails
**What we're doing:** Confirming real filesystem changes, and naming what protected you.  
**Why:** Cowork output isn't a chat reply — it's files. Knowing the guardrails lets you delegate confidently.

**Action:** Back in your terminal:
```bash
ls -la ~/cowork-lab
cat ~/cowork-lab/summary-report.md
```
You should see renamed files plus the report (expense total 604.50 — check Claude's math). Three protections were active:
```
1. Folder scoping  - Claude saw only ~/cowork-lab
2. Plan approval   - it showed the plan before renaming
3. Delete guard    - permanent deletions always require an explicit "Allow"
```

![Report on disk](./images/ccode377.png?raw=true "Report on disk")

---
<br><br>

## 7: Find Cowork's Customize Section
**What we're doing:** Locating where Cowork groups skills, plugins, and connectors.  
**Why:** The **Customize** area gathers all three extension types in one place — the desktop twin of the unified directory from Lab 15.

**Action:** In the Cowork tab, open **Customize** (check the sidebar or settings area). Note the groupings: skills, plugins, connectors.

![Customize section](./images/ccode378.png?raw=true "Customize section")

---
<br><br>

## 8: Enable a Document Skill — Same SKILL.md as Lab 4
**What we're doing:** Turning on a skill and connecting it to what you built.  
**Why:** Enabled skills load automatically when a task matches their description — exactly like your `api-checker` did in Lab 4.

**Action:** Browse the skills list, find a document-creation skill (e.g., Word/.docx or slides), and enable it. Then read:
```
Lab 4: you wrote SKILL.md with name + description frontmatter,
       rules, and a helper script — auto-selected on a matching request.
Here:  every skill in this list IS that same anatomy — SKILL.md plus
       supporting files — selected the same way. Same mechanism, new surface.
```

![Enable skill](./images/ccode379.png?raw=true "Enable skill")

---
<br><br>

## 9: Invoke the Skill by Intent (Not by Name)
**What we're doing:** Letting Cowork pick the skill from context, like Lab 4 Step 7.  
**Why:** Skills should trigger on intent, not on being named.

**Action:** Start a Cowork task in your `~/cowork-lab` folder and type:
```
Turn summary-report.md into a polished one-page Word document
with a title, headings for each section, and the expense total
highlighted. Save it in this folder.
```

---
<br><br>

## 10: Watch the Skill Load and Open the Output
**What we're doing:** Spotting the skill activation, then judging the deliverable.  
**Why:** Confirms auto-selection happened — and the point of skills is *better, more consistent output*.

**Action:** Watch the progress output for the document skill loading/being used.

> ⏱ **Patience note:** Document generation can take a couple of minutes.

When it finishes, open the new `.docx` in `~/cowork-lab` (double-click in Finder/Explorer). Compare it mentally to raw prompting.

![Skill in action](./images/ccode380.png?raw=true "Skill in action")

---
<br><br>

## 11: Browse Plugins — plugin.json, All Grown Up
**What we're doing:** Looking at plugin offerings and connecting them to Lab 5.  
**Why:** Plugins here are the same packaging mechanism you built by hand — bundles of skills + connectors + commands + sub-agents.

**Action:** In Customize, switch to the plugins area and browse a few (e.g., role-based plugins like legal, finance, brand). Notice each plugin's listed contents. Then read:
```
Lab 5: you wrote .claude-plugin/plugin.json bundling commands,
       agents, and skills so teammates could install one thing.
Here:  these plugins distribute the same asset types to Cowork users
       with one click — the cross-surface distribution story.
       (Enterprise admins can host private plugin marketplaces.)
```

![Plugins list](./images/ccode381.png?raw=true "Plugins list")

---
<br><br>

## 12: Keep the Folder
**What we're doing:** Preserving the sandbox.  
**Why:** Labs 19 and 21 build on this folder.

**Action:** Leave `~/cowork-lab` and its files in place, and leave Claude Desktop open.

## Lab Summary
✅ You've successfully:
- Pointed Cowork at a specific local folder (least privilege) and delegated a multi-step task
- Reviewed the plan, watched progress, steered mid-task, and verified real file changes
- Identified Cowork's safety rails (scoping, plan approval, delete guard)
- Found Customize and enabled a document skill — recognized as the same SKILL.md from Lab 4
- Triggered the skill by intent and produced a polished document deliverable
- Mapped Cowork plugins to the plugin.json packaging from Lab 5

<br><br>
---
## END OF LAB
---
<br><br>


# Lab 18: Connectors — The Directory, OAuth, and Your First Connected Tool
## Lab Purpose
Connect a real external tool through the connectors directory, authorize it, and use it in a conversation — then see that connectors are managed remote MCP, the Lab 7 concept productized. Estimated time: 10-12 minutes.

**Environment: claude.ai in your browser (works the same in Claude Desktop)**

---
<br><br>

## 1: Connectors = MCP with a Bow on It
**What we're doing:** Framing before connecting.
**Why:** In Lab 7 you ran `claude mcp add` and edited `.mcp.json`. Connectors are the same protocol — remote MCP servers — wrapped in a directory with one-click OAuth.

**Action:** Read:
```
Lab 7 (terminal):  claude mcp add <name> <server>  -> tools appear
Today (directory): click Connect -> sign in       -> tools appear
Same protocol (MCP). Same result (Claude gets tools). Less typing.
```

---
<br><br>

## 2: Open the Connectors Directory
**What we're doing:** Browsing the catalog.
**Why:** The directory is browsable on both claude.ai and Claude Desktop; it's part of the unified directory from Lab 15.

**Action:** In claude.ai settings, open the **Connectors** section and browse the directory.

![Connectors directory](./images/ccode382.png?raw=true "Connectors directory")

---
<br><br>

## 3: Choose GitHub
**What we're doing:** Picking a connector that needs no admin setup.
**Why:** You already have a GitHub account from Days 1–2 (Codespaces!), and GitHub's OAuth flow is self-serve — no workspace admin required. (If you prefer, Google Drive/Gmail works the same way with a personal Google account.)

**Action:** Find the **GitHub** connector in the directory and click **Connect**.

---
<br><br>

## 4: Authorize via OAuth
**What we're doing:** Granting Claude scoped access to your GitHub account.
**Why:** OAuth means Claude never sees your password, and you can revoke access anytime.

**Action:** Follow the sign-in flow in the popup/tab: sign in to GitHub, review the requested permissions, and authorize. You should land back in Claude with the connector showing as connected.

![OAuth authorize](./images/ccode383.png?raw=true "OAuth authorize")

---
<br><br>

## 5: Verify It's Live
**What we're doing:** Confirming the connector's tools are available.
**Why:** Trust but verify — same as `/mcp` in Lab 7.

**Action:** In your connectors list, confirm GitHub shows as connected/enabled. Many connectors also let you expand them to see the individual tools they expose — recognize the tools-list idea from `/mcp`?

---
<br><br>

## 6: Use It in a Chat
**What we're doing:** Letting Claude call the connector.
**Why:** The payoff: Claude can now act on your real data.

**Action:** Start a new chat and type:
```
Using the GitHub connector, list my repositories and summarize
what each one is for in a sentence. Which has the most recent activity?
```
Approve any tool-use permission prompts. Claude will call GitHub tools and synthesize an answer.

![Connector in use](./images/ccode384.png?raw=true "Connector in use")

---
<br><br>

## 7: Try It in Cowork Too
**What we're doing:** Confirming connectors cross surfaces.
**Why:** The connector you just added is also available to Cowork tasks (check Cowork's Customize/connector controls) — one connection, many surfaces.

**Action:** In Claude Desktop's Cowork tab, start a quick task:
```
Check my GitHub account and write a short repo-activity.md note in
my cowork-lab folder listing my repos and their last update dates.
```
> ⏱ **Patience note:** Allow a couple of minutes; approve permissions as prompted.

---
<br><br>

## 8: Custom Connectors — Bring Your Own MCP
**What we're doing:** Seeing where your Lab 7 skills plug in.
**Why:** The directory isn't a walled garden: you can add any remote MCP server as a *custom connector* by URL.

**Action:** In the connectors settings, find the **Add custom connector** option (don't add one now — just locate it). Note:
```
- Custom connector = a remote MCP server URL you supply
- Free plan: 1 custom connector; paid plans: multiple
- Anything you could `claude mcp add` remotely, you can add here
```

![Custom connector option](./images/ccode385.png?raw=true "Custom connector option")

---
<br><br>

## 9: Awareness — Desktop Extensions (.mcpb)
**What we're doing:** One-paragraph awareness of locally-packaged connectors.
**Why:** For *local* MCP servers, Claude Desktop supports Desktop Extensions: `.mcpb` packages built with `mcpb init` / `mcpb pack` that users install by double-click. You won't build one today — just know the name when you see it.

**Action:** No action — file `.mcpb` next to plugin.json in your mental model of "ways to ship MCP to non-terminal users."

---
<br><br>

## 10: Know How to Disconnect
**What we're doing:** Locating the off switch.
**Why:** Access hygiene: connectors should be as easy to revoke as to grant.

**Action:** In your connectors settings, find the manage/disconnect control for GitHub. **Leave it connected** — Labs 20 and 21 use it — but remember where this is for after the course.

---
<br><br>

## Lab Summary
✅ You've successfully:
- Browsed the connectors directory (part of the unified directory)
- Connected and OAuth-authorized the GitHub connector
- Used connector tools in chat and in a Cowork task
- Located the custom-connector (remote MCP) option — the Lab 7 concept productized
- Gained awareness of .mcpb Desktop Extensions
- Found where to disconnect a connector

<br><br>
---
## END OF LAB
---


# Lab 19: Cowork Scheduled Tasks
## Lab Purpose
Create a recurring scheduled task in Cowork, run it on demand, and place it in the three-tier scheduling picture from Day 2 (/loop, Routines, and now Cowork). Estimated time: 10-12 minutes.

**Environment: Claude Desktop app (Cowork)**

---
<br><br>

## 1: Open a Cowork Task in Your Lab Folder
**What we're doing:** Starting from the familiar sandbox.
**Why:** Scheduled tasks need a context — ours is `~/cowork-lab`.

**Action:** In the Cowork tab, start a new task with `~/cowork-lab` as the working folder (as in Lab 17).

---
<br><br>

## 2: Invoke /schedule
**What we're doing:** Opening the scheduled-task creator.
**Why:** Cowork supports slash commands too — another cross-surface echo.

**Action:** In the Cowork prompt, type:
```
/schedule
```
(Alternatively, look for **Scheduled** in the left sidebar — both routes work.)

![Schedule command](./images/ccode386.png?raw=true "Schedule command")

---
<br><br>

## 3: Define the Task
**What we're doing:** Describing the recurring work.
**Why:** Same principle as Lab 17 — describe the outcome; Claude handles the steps each run.

**Action:** Define the task as:
```
Every day, tidy my cowork-lab folder: move any new loose files into
sensible subfolders, then update daily-digest.md with today's date,
a list of files changed since yesterday, and any new action items
found in notes files.
```

---
<br><br>

## 4: Set the Cadence
**What we're doing:** Choosing daily recurrence.
**Why:** Cowork scheduled tasks support recurring cadences and on-demand runs.

**Action:** Set the schedule to **daily** at a time of your choosing (pick something later today so it won't fire mid-lab). Save the task.

![Set cadence](./images/ccode387.png?raw=true "Set cadence")

---
<br><br>

## 5: Find It in the Scheduled List
**What we're doing:** Verifying the task is registered.
**Why:** The Scheduled sidebar is your management console: view, edit, pause, delete.

**Action:** Click **Scheduled** in the left sidebar and confirm your daily-tidy task appears.

![Scheduled list](./images/ccode388.png?raw=true "Scheduled list")

---
<br><br>

## 6: Run It On Demand
**What we're doing:** Triggering the task now instead of waiting for the schedule.
**Why:** On-demand runs are how you test scheduled work — never wait until tomorrow to find out a daily job is broken.

**Action:** From the scheduled task's entry, use the run-now control to start it immediately.

> ⏱ **Patience note:** Let it run — a few minutes is normal.

---
<br><br>

## 7: Inspect the Result
**What we're doing:** Checking the digest file.
**Why:** Proof of a successful scheduled run.

**Action:** In your terminal:
```bash
cat ~/cowork-lab/daily-digest.md
```
You should see today's date, the file inventory, and action items pulled from your notes.

![Digest output](./images/ccode389.png?raw=true "Digest output")

---
<br><br>

## 8: The Three-Tier Scheduling Picture
**What we're doing:** Placing Cowork scheduling alongside Day 2's options.
**Why:** You now have three scheduling tiers — choosing the right one is the skill.

**Action:** Study this comparison (callback to Day 2, Lab 13):
```
Tier              Where it runs          Runs when...           Best for
----------------  ---------------------  ---------------------  -------------------------
/loop             your terminal session  session stays open     dev-loop automation, today
Routines          Anthropic's cloud      always (cloud-side)    always-on jobs, no machine
Cowork scheduled  your computer (app)    computer awake +       local-file jobs with a
                  via Claude Desktop     Desktop app open       friendly UI
```

---
<br><br>

## 9: The Fine Print
**What we're doing:** Internalizing Cowork scheduling's key limitation.
**Why:** It's the most common gotcha.

**Action:** Remember:
```
Cowork scheduled tasks ONLY run while your computer is awake and
the Claude Desktop app is open. Laptop closed = task skipped.
If a job must run unconditionally, that's a Routine (cloud tier).
```

---
<br><br>

## 10: Pause It (Housekeeping)
**What we're doing:** Pausing the daily task so it doesn't surprise you tonight.
**Why:** Good agent hygiene — we'll create a purposeful scheduled task in the capstone.

**Action:** In the Scheduled sidebar, pause (or delete) the daily-tidy task. Leave Cowork open.

---
<br><br>

## Lab Summary
✅ You've successfully:
- Created a recurring scheduled task in Cowork via /schedule
- Managed it from the Scheduled sidebar
- Ran it on demand and verified the output file
- Placed Cowork scheduling in the 3-tier model with /loop and Routines
- Learned the awake-and-open constraint (and when to use a Routine instead)

<br><br>
---
## END OF LAB
---


# Lab 20: Live Artifacts — A Connector-Fed Dashboard (Cowork)
## Lab Purpose
Build a Live Artifact: a persistent dashboard that pulls fresh data through your GitHub connector every time it opens — and that Claude itself can run inside. Estimated time: 10-12 minutes.

**Environment: Claude Desktop app (Cowork)**

---
<br><br>

## 1: What Makes an Artifact "Live"
**What we're doing:** Distinguishing Live Artifacts (April 2026, Cowork) from Lab 16's artifacts.
**Why:** Lab 16's flashcards were frozen at build time. Live Artifacts are persistent dashboards that fetch *fresh* data from connectors/MCP each time you open them — and Claude can run inside the artifact to answer questions about that data.

**Action:** Read the comparison:
```
Regular artifact:  data baked in at creation; static until you rebuild
AI-powered (L16):  calls Claude at runtime, but no data sources
Live Artifact:     pulls fresh connector/MCP data on every open,
                   AND Claude can run inside it
```

---
<br><br>

## 2: Confirm Your Connector
**What we're doing:** Checking GitHub (from Lab 18) is available to Cowork.
**Why:** The dashboard's data source must be connected before building.

**Action:** In Cowork's Customize/connector area, confirm **GitHub** is connected and enabled. If you connected Google Drive instead in Lab 18, you'll build a "recent docs tracker" — same steps, swap the data source.

---
<br><br>

## 3: Ask for the Dashboard
**What we're doing:** Prompting Cowork to build a Live Artifact.
**Why:** One outcome-oriented prompt; Claude handles wiring the connector.

**Action:** In a new Cowork task, type:
```
Create a Live Artifact dashboard called "Repo Activity Tracker".
Each time it opens, it should pull fresh data from my GitHub
connector and show: my repositories, last commit date for each,
open issues/PR counts if available, and a "most active this week"
highlight. Keep the layout clean and scannable.
```

![Live Artifact request](./images/ccode390.png?raw=true "Live Artifact request")

---
<br><br>

## 4: Approve and Wait
**What we're doing:** Letting the build run.
**Why:** Building + first data fetch is a real multi-step task.

**Action:** Approve the plan and any connector permission prompts.

> ⏱ **Patience note:** First build can take several minutes — it's fetching live GitHub data, not inventing placeholder numbers.

---
<br><br>

## 5: Explore the Dashboard
**What we're doing:** Verifying the data is *yours*.
**Why:** The wow moment: those are your real repos and real commit dates.

**Action:** When the Live Artifact opens, check the repo list against what you know — you should recognize your course repo from Days 1–2 with very recent activity.

![Dashboard open](./images/ccode391.png?raw=true "Dashboard open")

---
<br><br>

## 6: Prove the "Live" Part — Change Something
**What we're doing:** Creating a detectable change in the data source.
**Why:** A reload that shows the change is the proof of freshness.

**Action:** In your browser, go to your course repo on github.com and make a tiny change — e.g., open a new issue titled `live-artifact-test` (or star a repo).

---
<br><br>

## 7: Reopen and Watch Fresh Data Arrive
**What we're doing:** Triggering a fresh data pull.
**Why:** Live Artifacts refresh from their sources on open.

**Action:** Close and reopen the Live Artifact (or use its refresh control). Confirm your new issue/change appears — no rebuild, no re-prompt.

![Fresh data](./images/ccode392.png?raw=true "Fresh data")

---
<br><br>

## 8: Ask Claude Inside the Artifact
**What we're doing:** Using the embedded Claude.
**Why:** Live Artifacts aren't just charts — Claude can run inside them to interpret the live data.

**Action:** Use the artifact's ask/chat affordance (look for a prompt box or "Ask Claude" control inside the dashboard) and ask:
```
Which repo needs my attention most right now, and why?
```

---
<br><br>

## 9: Where Live Artifacts Live
**What we're doing:** Finding the artifact again later.
**Why:** Persistent means it survives this conversation.

**Action:** Locate the Live Artifact in your Cowork session/sidebar so you can reopen it tomorrow. It will pull tomorrow's data when you do.

---
<br><br>

## 10: Pattern Check
**What we're doing:** Naming the architecture you just used.
**Why:** You'll reuse it in the capstone.

**Action:** Note the pattern:
```
connector (live data) -> Live Artifact (persistent view)
                      -> Claude inside (interpretation on demand)
```
This is "a dashboard that explains itself" — and in Lab 21 you'll point it at your own project.

---
<br><br>

## Lab Summary
✅ You've successfully:
- Distinguished Live Artifacts from regular and AI-powered artifacts
- Built a connector-fed dashboard in Cowork
- Verified it shows your real GitHub data
- Proved freshness by changing the source and reloading
- Asked Claude questions from inside the artifact
- Identified the connector → Live Artifact → embedded-Claude pattern

<br><br>
---
## END OF LAB
---


# Lab 21: Capstone — Build, Automate, Monitor, Present
## Lab Purpose
Tie all three days together: use Claude Code to build a project status reporter, hand it to a background agent, schedule it, then bring it into the platform as a Live Artifact dashboard with a Cowork scheduled task — and map every course concept to where you used it. Brisk pace; you've done every piece before. Estimated time: 10-12 minutes.

**Environment: GitHub Codespace (terminal) for steps 1-7, then Claude Desktop (Cowork) + claude.ai for steps 8-12.**

---
<br><br>

## 1: Build the Status Script
**What we're doing:** Returning to your Day 1–2 environment and having Claude Code build a project status reporter.  
**Why:** A deterministic script (Lab 4's lesson: scripts beat re-prompting) that any agent or schedule can run.

**Action:** Reopen your Codespace (or local terminal in your course project) and start `claude --model sonnet --effort medium`. Then type:
```
Create a script scripts/status.sh that writes STATUS.md containing:
a timestamp, a file count by type, the 5 most recent git commits
(one line each), and the result of running the project tests
(pass/fail summary only). Make it runnable with bash scripts/status.sh.
```
Approve as needed.

---
<br><br>

## 2: Run It Once
**What we're doing:** Validating the script before automating it.  
**Why:** Capstone rule: never schedule something you haven't run by hand.

**Action:** Type:
```
Run scripts/status.sh and show me STATUS.md
```
Check the report looks sane (timestamp, files, commits, test summary).

![STATUS.md](./images/ccode393.png?raw=true "STATUS.md")

---
<br><br>

## 3: Commit and Push
**What we're doing:** Getting the script and report into git.  
**Why:** The Live Artifact dashboard later reads repo activity — commits are the signal.

**Action:** Type:
```
Commit scripts/status.sh and STATUS.md with a sensible commit
message, and push to the remote.
```
(Recognize the commit-message task from Lab 16? You built an app for that.)

---
<br><br>

## 4: Dispatch a Background Agent
**What we're doing:** Handing improvement work to a background agent, Day 2 style.  
**Why:** Build is done; now automate. Background agents work while you do something else.

**Action:** Exit Claude (`exit`), then dispatch:
```bash
claude --bg "Improve scripts/status.sh: add a section to STATUS.md
flagging any TODO or FIXME comments found in the codebase, then
re-run the script, verify STATUS.md updated, and commit the change."
```

---
<br><br>

## 5: Monitor and Review the Agent
**What we're doing:** Watching the run, then verifying the change.  
**Why:** Same observability and trust-but-verify habits as Day 2.

**Action:** Watch with `claude agents` until it completes (a few minutes is normal), then:
```bash
git log --oneline -3
cat STATUS.md
```
Confirm the TODO/FIXME section exists and the commit landed.

![Background agent](./images/ccode394.png?raw=true "Background agent")

---
<br><br>

## 6: Schedule the Refresh with /loop
**What we're doing:** Making the report self-updating in-session, then stopping it cleanly.  
**Why:** Tier 1 of your 3-tier scheduling model: session-local cron. (When the Codespace closes, `/loop` dies — a Routine from Lab 13 survives; same prompt text, different runner.)

**Action:** Start Claude again (`claude`), then type:
```
/loop every 5 minutes: run scripts/status.sh, and if STATUS.md
changed, commit it with message "chore: refresh status report"
```
Let it fire at least once, then cancel the loop (Esc or its stop control) and confirm it stopped.

![Loop running](./images/ccode395.png?raw=true "Loop running")

---
<br><br>

## 7: Bridge to Cowork
**What we're doing:** Getting the project where Cowork can see it.  
**Why:** Cowork points at *local* folders; your Codespace is remote.

**Action:** Make sure your latest STATUS.md is pushed (`git push`). Then on your **local machine** terminal, clone your course repo:
```bash
git clone https://github.com/<your-username>/<your-course-repo>.git ~/capstone
ls ~/capstone
```
You should see your project, including `STATUS.md` and `scripts/status.sh`.

---
<br><br>

## 8: Build a Live Artifact Over Your Project
**What we're doing:** Building a connector-fed dashboard on your real project.  
**Why:** Lab 20's pattern (connector → Live Artifact → embedded Claude), now with stakes.

**Action:** In the Cowork tab, start a task with `~/capstone` as the working folder, then type:
```
Create a Live Artifact dashboard called "Capstone Project Status".
Each time it opens it should: read STATUS.md from this folder, pull
fresh commit and issue activity for this repo from my GitHub
connector, and display: latest status summary, recent commits,
test pass/fail, and any TODO/FIXME flags. Highlight anything that
changed since the last open.
```

> ⏱ **Patience note:** Several minutes — it's reading your repo AND your local folder.

When it opens, verify it shows your real STATUS.md content and the commits from steps 3–6.

![Capstone dashboard](./images/ccode396.png?raw=true "Capstone dashboard")

---
<br><br>

## 9: Interrogate It
**What we're doing:** Using the embedded Claude on real project data.  
**Why:** A dashboard you can question beats a dashboard you can only read.

**Action:** Inside the Live Artifact, ask:
```
Summarize the state of this project in 3 bullets and tell me the
single most useful next step.
```

---
<br><br>

## 10: Add a Daily Summary Scheduled Task
**What we're doing:** Automating the monitoring layer, then testing it now.  
**Why:** Tier 3 of your scheduling model: a local, UI-managed daily job over local files. Same rule as always: never trust an untested schedule.

**Action:** In the Cowork task, type `/schedule` and create (daily/weekday cadence):
```
Every weekday at 9am: read STATUS.md and recent git activity in my
capstone folder, then write/update capstone-daily-summary.md with a
3-bullet status, anything that regressed, and a suggested focus for the day.
```
From the **Scheduled** sidebar, run it now and wait, then check:
```bash
cat ~/capstone/capstone-daily-summary.md
```

![Capstone schedule](./images/ccode397.png?raw=true "Capstone schedule")

---
<br><br>

## 11: (Optional) Publish a Shareable Summary
**What we're doing:** Creating a stakeholder-facing artifact and seeing the whole system.  
**Why:** Cowork sessions are local and not shareable — but claude.ai artifacts are.

**Action:** In claude.ai, start a chat, paste the contents of `capstone-daily-summary.md`, and ask: `Turn this into a clean, visual one-page project status artifact suitable for sharing with a stakeholder.` Publish it. The full system you just built:
```
Claude Code (build script)  -> git repo
background agent (improve)  -> git repo
/loop or Routine (refresh)  -> STATUS.md -> git repo
GitHub connector ---------------------------+
local capstone folder ----------------------+--> Live Artifact dashboard
Cowork scheduled task (daily summary) ------+        |
claude.ai artifact (share out) <---------------------+
```

![Shared summary](./images/ccode399.png?raw=true "Shared summary")

---
<br><br>

## 12: Course Concept Map and Housekeeping
**What we're doing:** Mapping every concept to where you used it, and tidying up.  
**Why:** Retention — and you now own agents, schedules, and connectors, so manage them deliberately.

**Action:** With the class, walk this table and call out one thing you'd use first at work:
```
Concept                      Where you used it
---------------------------  ---------------------------------------
CLI basics, @/#/! shortcuts  Lab 1
Modes (plan/auto/bypass)     Lab 2, every approval since
Context, CLAUDE.md, /rewind  Lab 3
Skills (SKILL.md)            Lab 4 -> Lab 17 (Cowork, same anatomy)
Subagents & delegation       Labs 4-5 -> Cowork sub-agents (Lab 17)
Commands & plugins           Lab 5 -> Lab 17 (Cowork plugins)
Hooks                        Lab 6
MCP                          Lab 7 -> Lab 18 (connectors, .mcpb)
Headless -p / loops / /goal  Labs 9-10 -> Lab 16 (AI artifacts!)
Agent SDK                    Lab 11
GitHub Actions               Lab 12
Scheduling (3 tiers)         Lab 13 -> Lab 19 -> Lab 21
Background/managed agents    Lab 14 -> Lab 21
Artifacts & Live Artifacts   Lab 16, 20 -> Lab 21
Cowork                       Lab 17, 19-21
```
Then decide for each: Cowork scheduled tasks (keep or pause), GitHub connector (keep or disconnect, Lab 18), published artifacts (keep or unpublish), `~/cowork-lab` (delete if you like; `~/capstone` is yours to keep).

**Done!** You came in typing "Hello Claude" into a terminal; you're leaving with a self-updating, agent-maintained, connector-fed, shareable project monitoring system — and the knowledge that it's all the same Claude underneath.

## Lab Summary
✅ You've successfully:
- Built a deterministic status-report script with Claude Code and validated it before automating
- Dispatched and monitored a background agent (`claude --bg`, `claude agents`)
- Scheduled a refresh with `/loop` and noted the Routine upgrade path
- Built a connector-fed Live Artifact over your own project and interrogated it
- Added a Cowork daily-summary scheduled task and (optionally) published a shareable artifact
- Mapped every course concept to where you practiced it

<br><br>
---
## END OF LAB
---
