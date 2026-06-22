# AI Powered Coding with Claude Code

## Learn practical workflows, hands-on coding techniques, and structured interactions

This 1.5-day hands-on workshop (3 sessions x 4.5 hours) teaches you how to leverage Claude Code's AI features to build applications faster and more efficiently — and how to go beyond single prompts into loops, automation, managed agents, and the broader Claude platform (artifacts, Cowork, and connectors). You'll learn through 21 short guided labs (10-12 minutes each), 7 per session.

**Course agenda:**

- **Day 1 — Foundations (Labs 1-7):** Claude Code basics, modes, context management, skills, subagents, plugins, hooks, and MCP. Runs in a GitHub Codespace.
- **Day 2 — Loops, automation, and managed agents (Labs 8-14):** Day 2 warm-up, headless pipelines, /goal, the Agent SDK (programmatic + unattended), GitHub Actions, scheduled tasks (/loop and cloud Routines), and managed agents (background, cloud, and web). Runs in the Codespace + claude.ai.
- **Day 3 — The Claude platform (Labs 15-21):** Day 3 warm-up, artifacts (interactive + AI-powered), Cowork in the Claude Desktop app, connectors, Cowork scheduled tasks, Live Artifacts, and a build-to-present capstone. Runs in claude.ai and Claude Desktop on your own machine.

Prerequisites: Claude paid account (any paid plan — Pro, Max, Team, or Enterprise).

**Pre-class setup for Day 3 (do before the Day 3 session):**

1. Install the Claude Desktop app on your laptop from [claude.com/download](https://claude.com/download) and sign in with your paid Claude account.
2. Open the app and confirm you can see the **Chat**, **Cowork**, and **Code** tabs.
3. (Optional, for the GitHub Actions and web labs on Day 2) Have a personal GitHub repo you can push to.

These instructions will guide you through configuring a Claude Code environment that you can use to do the labs.

## 1. If you don't already have a paid Claude account, sign up for one at [claude.ai](https://claude.ai). 

You **must** have a paid Claude account to use Claude Code.

![Claude signup](./images/ccode76.png?raw=true "Claude signup")

<br><br>

## 2. Choose where you want to run Claude Code. 
**Important note: Lab commands and screenshots reflect using terminal integration in Codespace/VS Code integration. Steps and functionality in other environments may vary!**

If you would like to use the GitHub Codespace zero-install option that runs in a browser, skip to step 6.  Otherwise, continue with step 3.

<br><br>


## 3. Clone down the training repo locally from GitHub.

```
git clone https://github.com/skillrepos/ccode
```

<br><br>

## 4. If you want to install Claude Code on your local system (and are allowed to):

Go to [Get Started](https://code.claude.com/docs/en/overview#get-started), choose the **Terminal** tab and proceed with installation for your desired platform.

![Claude terminal setup](./images/ccode208.png?raw=true "Claude terminal setup")

<br><br>



## 5. Go to the cloned repo, start Claude and authenticate as appropriate.

If in the terminal integration, change into your cloned directory and you can likely follow the directions in  [STARTUP.md](./STARTUP.md) to complete this task. Otherwise, consult the online documentation.

 <br><br>

---
> **STOP HERE if NOT using the GitHub Codespace environment.**

> **Directions for GitHub Codespace environment setup follow.**
---
<br><br>

## 6. Set codespace timeout

While logged in to GitHub, go to https://github.com/settings/codespaces.

Scroll down and find the section on the page labeled *Default idle timeout*. 

Increase the default timeout value to 90 minutes and then select the *Save* button.

![Increasing default timeout](./images/ccode77.png?raw=true "Increasing default timeout")

(**NOTE**: If your codespace does time out at some point in the course, there should be a button to restart it. In that case, you will need to run the *minikube start* command again.)

<br><br>

## 7. Create your own codespace to run the labs by clicking on the button below.
<br/><br/>

Click here ------> [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/skillrepos/cc-se?quickstart=1)

<br/><br/>

Then click on the option to create a new codespace.

![Creating new codespace from button](./images/ccode2.png?raw=true "Creating new codespace from button")

**This will run for several minutes while it gets everything ready.**

<br/><br/>


## 8. Complete the startup/authentication steps in the file [STARTUP.md](./STARTUP.md). 

Once the codespace is running, you will need to authenticate Claude Code in the codespace using your Claude account. Follow the steps in [STARTUP.md](./STARTUP.md) to complete this task.


