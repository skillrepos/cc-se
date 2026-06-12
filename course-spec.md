---
spec_version: "1.0"
course_title: "AI-Powered Coding with Claude Code (1.5-Day Edition)"
course_version: "6.1"
created: "2026-06-11"
updated: "2026-06-11"
status: complete
interview_rounds_complete: [1, 2, 3, 4]
revision_note: "v6.1 — trimmed from 27 to 21 labs (max 7 per 4.5-hr session) by merging Agent SDK I+II, /loop+Routines, background+web agents, artifacts basics+AI-powered, the two Cowork labs, and the two-part capstone. Each lab ≤12 steps / ≤12 min."
---

# Course Spec: AI-Powered Coding with Claude Code (1.5-Day Edition)

**Pitch:** Learn practical workflows, hands-on coding techniques, and structured interactions — extended from the half-day workshop to cover agentic loops, automation, managed agents, and the broader Claude platform (Cowork, connectors, artifacts).
**Type:** extension of skillrepos/ccode (local folder: ccode-long)

## Existing Course Inventory

- Source: skillrepos/ccode @ labs.md Revision 5.7 - 05/18/26; deck workshop-claude-code_v5.pptx (v5.6, 76 slides)
- Current duration: half-day (~3 hrs); target duration: 13.5 hrs (3 × 4.5-hr days); added capacity: ~10.5 hrs ≈ 10–13 new labs + lecture
- Sections & labs:
  - Lab 1 — Intro & basics (CLI, file create/run, resume, @ mentions, # memory, ! bash) — run-and-observe, ~30 min
  - Lab 2 — Modes (default, plan, accept-edits, YOLO) — run-and-observe, ~25 min
  - Lab 3 — Commands & context (/help, /context, /compact, /rewind, CLAUDE.md, /memory, git, headless -p) — run-and-observe, ~30 min
  - Lab 4 — Skills + subagents (api-checker skill, planner + test-runner agents) — build, ~30 min
  - Lab 5 — Supervised delegation + plugin packaging + VS Code ext — build, ~30 min
- Topic coverage: CLI/modes/context/skills/subagents/commands/plugins = hands-on; MCP, hooks, agent teams, remote control, web, cost = awareness (slides only)
- Versions found: deck references Claude Code v2.1.116 (current: 2.1.173 — outdated items identified, see Modernization)
- Day-boundary plan: Day 1 ends after new MCP depth lab; Days 2 and 3 each open with a 10-min recap/warm-up
- Renumbering map: existing labs 1–5 keep numbers; new labs append 6+

## Audience

- Who: beginners + intermediate developers (mixed general technical)
- Prerequisites: paid Claude account; basic terminal comfort; no prior Claude Code experience required
- Class size / context: instructor-led workshop, 3 sessions × 4.5 hrs

## Schedule

- Duration: 1.5 days as 3 × 4.5-hr sessions
- Lab budget: 21 labs total, 7 per session (client-confirmed ceiling)
- Sections:
  - Day 1 — Foundations (Labs 1–7): existing Labs 1–5 (modernized) + Hooks hands-on + MCP hands-on
  - Day 2 — Loops & automation (Labs 8–14): recap, headless/loops (/goal), Agent SDK (programmatic + unattended), GitHub Actions, scheduled tasks (/loop + Routines), managed agents (background + cloud/web)
  - Day 3 — Claude platform (Labs 15–21): recap, artifacts (interactive + AI-powered), Cowork (folder task + skills/plugins), connectors, Cowork scheduled tasks, Live Artifacts, capstone
- Suggested break points: mid-session break each day after ~2 hrs

## Topic Map

<!-- PENDING: gap-proposal accept/reject -->

| # | Topic | Depth | Priority | Source | Notes |
|---|-------|-------|----------|--------|-------|
| 1 | Claude Code fundamentals (CLI, modes, context) | hands-on | must-cover | existing | modernize: auto mode, /model persistence |
| 2 | Skills, subagents, commands, plugins | hands-on | must-cover | existing | modernize: plugin init flow |
| 3 | Hooks | hands-on (new) | must-cover | user (was slides-only) | Day 1 |
| 4 | MCP | hands-on (new) | must-cover | user (was slides-only) | Day 1; leads into Day 3 connectors |
| 5 | Loops instead of prompts (headless -p, /goal, Agent SDK) | hands-on | must-cover | user | Day 2 |
| 6 | CI automation (GitHub Actions claude-code-action@v1) | hands-on | proposed (Important) | research-gap | Day 2 |
| 7 | Scheduled tasks (/loop, Desktop tasks, Routines) | hands-on | must-cover | user + research | 3-way comparison table |
| 8 | Managed agents (claude agents view, --bg, Claude Code on the web, Desktop Code tab) | hands-on | must-cover | user + research-gap(Critical) | local + cloud story |
| 9 | Artifacts (claude.ai, AI-powered artifacts) | hands-on | must-cover | user | Day 3 |
| 10 | Cowork (Claude Desktop) | hands-on | must-cover | user | Day 3 |
| 11 | Connectors (directory, custom connectors, MCPB awareness) | hands-on | must-cover | user | Day 3 |
| 12 | Live Artifacts + Cowork scheduled tasks | hands-on | proposed (Nice-to-have) | research-gap | Day 3 |
| 13 | Permissions/sandboxing for unattended runs | awareness→hands-on element | proposed (Critical) | research-gap | embedded in Day 2 |
| 14 | Capstone: Code + agents + scheduling + Cowork | mastery | must-cover | user | Day 3 finale |

Accepted gap proposals (2026-06-11): ALL — Critical: local background agents, Routines + 3-way scheduling comparison, auto-mode/permissions refresh, June 15 headless metering. Important: /goal, GitHub Actions lab, sandboxing, channels (awareness in scheduled-tasks section), cross-surface skills story, MCPB packaging. Nice-to-have: Live Artifacts lab, teleport/Remote Control demo, dynamic workflows (ultracode) slides, agent teams status update, /usage walkthrough.
Rejected gap proposals: none
Obsolete topics flagged: see Modernization items (all 10 fixes approved, with audit trail)

## Lab Plan

**Lab format constraint (confirmed 2026-06-11): every lab ≤10–12 minutes, 10–12 steps.** Existing labs 1–5 already fit (10–12 steps each). Larger topics split into multiple micro-labs.

**v6.1 lab plan — 21 labs, 7 per session (each ≤12 steps / ≤12 min).** Six v6.0 labs were merged to hit the 7-per-session ceiling; merges are noted below.

| Lab | Status | Topic(s) | Style | Est. time | Day |
|-----|--------|----------|-------|-----------|-----|
| 1–5 | existing/modernize | fundamentals → plugins | as today | 5 × 10–12 min | 1 |
| 6 | new | Hooks: PreToolUse/PostToolUse policy enforcement | build | 10–12 min | 1 |
| 7 | new | MCP: claude mcp add, /mcp, .mcp.json | guided | 10–12 min | 1 |
| 8 | new | Day 2 recap warm-up | run-and-observe | 5–8 min | 2 |
| 9 | new | Headless mode: -p patterns, piping, JSON output | guided | 10–12 min | 2 |
| 10 | new | /goal: condition-driven loops | guided | 10–12 min | 2 |
| 11 | new | **Agent SDK (merge of v6.0 11+12):** read-only query() loop + unattended runs (allowed_tools, permission_mode, can_use_tool, max_turns) | skeleton + diff-merge (both sdk/*.py → extra/*.txt) | 10–12 min | 2 |
| 12 | new | GitHub Actions: claude-code-action@v1 | guided | 10–12 min | 2 |
| 13 | new | **Scheduled tasks (merge of v6.0 14+15):** /loop session cron + cloud Routines via /schedule, with the 3-way comparison | guided | 10–12 min | 2 |
| 14 | new | **Managed agents (merge of v6.0 16+17):** background `claude agents` view + Claude Code on the web + teleport | guided | 10–12 min | 2 |
| 15 | new | Day 3 recap warm-up | run-and-observe | 5–8 min | 3 |
| 16 | new | **Artifacts (merge of v6.0 19+20):** interactive artifact + AI-powered artifact (artifact calls Claude) | build | 10–12 min | 3 |
| 17 | new | **Cowork (merge of v6.0 21+22):** first folder task + skills/plugins in Customize (cross-surface story) | guided | 10–12 min | 3 |
| 18 | new | Connectors: directory, add + use one | guided | 10–12 min | 3 |
| 19 | new | Cowork scheduled task | guided | 10–12 min | 3 |
| 20 | new | Live Artifact dashboard (connector-fed) | build | 10–12 min | 3 |
| 21 | new | **Capstone (merge of v6.0 26+27):** build + automate (Code, agent, /loop) → monitor + present (Cowork, Live Artifact, share) | build | 10–12 min | 3 |

- Lab time per day: each session = 7 labs; warm-up ≈ 6–8 min, others 10–12 min → D1 ≈ 78 min, D2 ≈ 72 min, D3 ≈ 74 min of lab time — the balance of each 4.5-hr session is lecture, demos (teleport/Remote Control mobile, dynamic workflows), Q&A, and breaks
- Capstone: Lab 21 combines Claude Code build + background agent + scheduled task + Cowork/connector Live Artifact + shareable artifact in one brisk recall lab
- Reuse sources: skillrepos/ccode (all existing labs, images, devcontainer, STARTUP.md flow)
- Merge rationale: the merged labs reuse the same assets (e.g., both Agent SDK skeleton/diff-merge pairs remain in Lab 11) — no content was dropped, only consolidated and tightened to ≤12 steps each

## Slide Plan

<!-- PENDING: Round 4 visuals confirmation -->

| Section | Status | Slide count (est.) | Precedes lab(s) | Visuals needed |
|---------|--------|--------------------|-----------------|----------------|
| Existing 76 slides | modernize (targeted) | 76 | 1–5 | per modernization list |
| Hooks (expanded) | new | 4–6 | 6 | hook lifecycle diagram |
| MCP (expanded) | new | 4–6 | 7 | MCP architecture diagram |
| Loops & headless & SDK | new | 8–10 | 9–10 | prompt-vs-loop diagram |
| CI automation | new | 4–5 | 11 | Actions flow |
| Scheduled tasks | new | 5–6 | 12 | 3-tier comparison table |
| Managed/background agents | new | 6–8 | 13 | local↔cloud agent map |
| Artifacts | new | 4–5 | 15 | — |
| Cowork | new | 6–8 | 16 | Chat/Cowork/Code surface map |
| Connectors | new | 5–6 | 17 | connector/MCP relationship |
| Capstone + wrap | new | 4–5 | 19 | capstone architecture |

- Theme source deck: workshop-claude-code_v5.pptx (inherited)
- Visual density: balanced (confirmed 2026-06-11)
- Animated build-ups (all 7 confirmed 2026-06-11): prompt-vs-loop agentic loop; local-vs-cloud managed-agents map; scheduled-tasks 3-tier comparison; hook lifecycle; MCP/connector architecture; Cowork Chat/Cowork/Code surface map; capstone architecture
- Speaker script: notes only (confirmed)

## Environment

- Delivery: GitHub Codespaces (Days 1–2 CLI labs) + student claude.ai account + Claude Desktop installed locally (Day 3) — confirmed "hands-on everywhere"
- hostRequirements: 4 CPU / 16gb / 32gb (inherited)
- Ollama model(s): n/a (course uses Claude models)
- Key dependencies: claude-agent-sdk (Python) for Lab 10; @anthropic-ai/claude-code current
- Services/ports: GitHub repo w/ Actions enabled for Lab 11

## Conventions

Standard TechUpSkills conventions apply (repo structure, labs.md format, skeleton/diff-merge rules, devcontainer template, slide master rules, copyright). Deviations: (1) Day 3 labs run outside Codespace (claude.ai + Claude Desktop) — labs.md carries environment banners per lab; (2) micro-lab format: every lab ≤10–12 min and 10–12 steps (course total 21 labs, 7 per session — within the per-session ceiling confirmed by the client).

## Assumptions Log

- Existing content disposition: modernize — all 10 fixes with audit trail — confirmed 2026-06-11
- All new topics hands-on (channels = awareness slides within scheduled-tasks section) — confirmed by default 2026-06-11
- Visual density: balanced — confirmed 2026-06-11
- Day structure: foundations → automation → platform — confirmed 2026-06-11
- Delivery env: students' own claude.ai + Claude Desktop — confirmed 2026-06-11
- Capstone: yes — confirmed 2026-06-11
- Speaker support: notes only — confirmed 2026-06-11

## Modernization Items (all approved, audit trail required)

1. Modes lab + slides: add auto mode; terminology → supervised editing / plan / auto / bypass
2. Plugin lab: `claude plugin init`, auto-load from `.claude/skills` (no marketplace), `experimental` key, `defaultEnabled`, `/plugin list`
3. Headless slide: reframe under Agent SDK; June 15 metering; `claude ultrareview`
4. `/model` now persists as default (session-only = `s`)
5. Command renames: `/simplify`→`/code-review` (+cleanup-only `/simplify`), `/extra-usage`→`/usage-credits`, workflow→`ultracode`
6. Model slides: Opus 4.8, Fable 5 (1M context)
7. Agent teams slide: still experimental/disabled by default; subagents now nest 5 levels
8. Context module: `/rewind` "Summarize up to here", auto memory, `/usage` per-category
9. Web slides: research preview + teleport (one-way cloud→terminal) + Remote Control
10. MCP slides: connectors surface in Claude Code; `.mcpb` naming; unified directory

Audit trail per conventions: code comments, `[Update - 2026-06-11]` speaker notes, slide backups at deck end, CHANGELOG.md entry.

## Consistency Checks (run 2026-06-11 — all pass)

1. Lab budget: D1 = 7 labs, D2 = 7 labs (8–14), D3 = 7 labs (15–21) — exactly at the client-confirmed ceiling of 7 labs/session; warm-ups (Labs 8, 15) count toward the 7 ✓
2. Every must-cover topic mapped to ≥1 lab (channels intentionally awareness-only) ✓
3. Every lab preceded by its concept slide section ✓
4. Diff-merge lab (10) has skeleton/complete pair assigned ✓
5. No multi-process labs requiring port documentation ✓
6. Timing warnings: Day 3 Cowork task runs can take minutes — labs 16/18/19 flagged for inline timing notes ✓
7. Theme source deck exists in folder ✓
8. No unconfirmed assumptions remain on must-cover topics or environment ✓

Extension-specific: new material fits added 10.5 hrs ✓; hooks/MCP are depth increases, not duplicates ✓; Day 3 prerequisite (Claude Desktop installed) handled via new pre-class setup section in README ✓; day boundaries at natural breaks, Days 2–3 open with recap labs ✓; no labs dropped ✓; requirements.txt addition (claude-agent-sdk) doesn't affect kept labs — flag regeneration test ✓.

## Open Items (deferred to generation)

- README update: pre-class setup for Day 3 (Claude Desktop install + claude.ai login check), Day-2 GitHub repo with Actions enabled
- Lab 11 needs a disposable GitHub repo per student (or fork pattern) — decide at lab-forge time
- June 15 metering: verify final wording against Anthropic announcement at deck-generation time
- Verify Cowork features against current build at QA time (product is moving fast)
