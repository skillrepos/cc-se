# Changelog

## v6.1 — 06/11/26 — Right-sized to 7 labs per session

### Changed
- **Trimmed 27 labs → 21 labs (7 per 4.5-hr session, warm-ups included)** to fit each session realistically. No topics dropped — six lab pairs were merged and tightened so every lab is ≤12 steps and ≤12 minutes:
  - Day 2: Agent SDK I+II → **Lab 11** (read-only loop + unattended runs; both skeleton/diff-merge pairs retained); /loop + cloud Routines → **Lab 13**; background agents + Claude Code on the web/teleport → **Lab 14**
  - Day 3: artifacts basics + AI-powered artifacts → **Lab 16**; Cowork folder task + Cowork skills/plugins → **Lab 17**; Capstone I + II → **Lab 21**
- Renumbered Day 2 to Labs 8–14 and Day 3 to Labs 15–21; updated all cross-references (warm-up "where we're going" map, Day 2 wrap table, Day 3 concept map, connector/scheduling/artifact callbacks)
- README agenda, course-spec lab plan + consistency checks updated to 21 labs

### Deck (workshop-claude-code_v6.pptx — 108 slides)
- Built v6 from the v5.6 base (the v6 deck had not actually been generated): +31 new on-theme slides — Lab 6/7 dividers, a "What's New in 2026" summary, and full Day 2 (Labs 8–14) and Day 3 (Labs 15–21) concept + lab-divider sections
- Applied all 10 modernization items to existing Day 1 slides (models → Opus 4.8/Fable 5; Auto mode + supervised/plan/auto/bypass terminology; headless → Agent SDK + Jun 15 metering; /rewind "Summarize up to here"; /model persistence + /usage per-category; command renames; MCP connectors/.mcpb/unified directory; teleport; Agent Teams off-by-default + 5-level subagent nesting; plugin init/auto-load/`/plugin list`)
- Audit trail: per-slide `[Update - 2026-06-11]` speaker notes + a "Modernization Audit" slide at deck end; `workshop-claude-code_v5.pptx` retained as the full pre-modernization backup
- Known cosmetic: 3-digit slide numbers (100+) wrap in the page-number box (pre-existing template constraint, now visible because the deck exceeds 100 slides)

### Removed
- Stale intermediate fragments `labs-day1-new.md`, `labs-day2.md`, `labs-day3.md` (superseded by the assembled `labs.md`); `labs-v5.7-backup.md` kept as the pre-extension backup

### Note
- Root cause of the earlier "plugins not available" error: the installed `course-forge` plugin ships only the `course-interviewer` skill — the `lab-forge`/`slide-forge` generators its spec references aren't in the bundle. This pass used the installed `training-course-builder` + `pptx` skills instead. To make `course-forge` work end-to-end, add the two generator skills back into the plugin and reinstall.

## v6.0 — 06/11/26 — Extension to 1.5 days (3 x 4.5-hour sessions)

### Added
- 22 new labs (6-27): hooks, MCP, headless pipelines, /goal, Agent SDK (2 diff-merge labs), GitHub Actions, /loop, cloud Routines, background agents (agent view), Claude Code on the web + teleport, artifacts, AI-powered artifacts, Cowork (folder tasks, skills/plugins, scheduled tasks), connectors, Live Artifacts, two-part capstone
- Day 2 and Day 3 divider sections with environment banners (Day 3 runs in claude.ai / Claude Desktop, outside the Codespace)
- Code files: `sdk/agent_loop.py` + `extra/agent_loop.txt`, `sdk/auto_agent.py` + `extra/auto_agent.txt` (skeleton/complete pairs, diff-verified, py_compile-clean)
- README: 3-day agenda + Day 3 pre-class setup (Claude Desktop install)
- `course-spec.md` (course-forge spec, source of truth for this extension)
- Screenshot placeholders ccode301-399 — **need capture**

### Changed (modernization, Claude Code 2.1.116 → 2.1.173)
- Lab 2: new step 9 "Check Out Auto Mode"; official mode terminology (supervised editing/plan/auto/bypass); steps 9-11 renumbered to 10-12; summary updated
- Lab 3: /rewind "Summarize up to here" note; headless step gains Day 2 forward-pointer + June 15, 2026 separate-metering warning
- Lab 5: plugin lab notes `claude plugin init`, auto-load from `.claude/skills` (no marketplace), `/plugin list`, `defaultEnabled`; Agent Teams note updated (still experimental/disabled by default; subagents now nest 5 levels per 2.1.172); docs link fixed to code.claude.com
- Preamble: /model selection now persists as default (press `s` for session-only)
- Copyright footer added (2026)

### Still to do
- Deck v6 (in progress): new slide sections + 10 modernization fixes + backups + speaker notes
- Capture screenshots ccode301-399
- Add `claude-agent-sdk` to the course repo's requirements.txt (Labs 11-12)
- Lab Verification Pass via live Codespace run (codespace-lab-tester skill) before shipping
- `labs-v5.7-backup.md` = pre-extension labs.md; `labs-day*.md` fragments can be deleted
