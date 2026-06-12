# Lab Validation Report — Claude Code Course (1.5-Day, 21 labs)

**Date:** 2026-06-11
**Scope:** Static validation of `labs.md` (Revision 6.0) + real sandbox dry-run of the diff-merge labs.
**Note:** A *live* Codespace run was not executed — see "Live test prerequisites" at the end for why and what's needed.

## Summary

| Check | Result |
|-------|--------|
| Lab count / structure | 21 labs, 7 per session ✓ |
| Steps per lab | all ≤ 12 ✓ |
| Cross-references (lab numbers) | no stale refs ✓ |
| Diff-merge ordering (view → merge → run) | correct for the only diff-merge lab (Lab 11) ✓ |
| Skeleton files compile + refuse to run pre-merge | ✓ (valid Python with a `SystemExit` guard) |
| Completed files compile + guard removed | ✓ |
| Referenced files exist (`sdk/`, `extra/`) | ✓ |
| File dependency chain (Day 2/3 reuse Day 1 files) | intact ✓ |
| Day-boundary + per-lab environment banners | present ✓ |

## What was validated (and how)

**1. Execution-plan extraction.** Every fenced terminal command was pulled from `labs.md` and mapped to its lab/step. Commands are well-formed across all 21 labs (claude CLI flags, `jq` filters, `pip`, `cp`, `mkdir`, hook `jq` expressions, GitHub Actions YAML, `/loop` `/goal` `/schedule`).

**2. Diff-merge labs (the highest-risk pattern).** Lab 11 is the only lab using `code -d` skeleton/complete merges. Ordering verified:

- `sdk/agent_loop.py`: view (step 2) → `code -d` merge (step 3) → `python3` run (step 4). ✓
- `sdk/auto_agent.py`: view (step 6) → `code -d` merge (step 7) → `python3` run (step 8). ✓

Sandbox dry-run results:
- Both **skeletons compile** (`py_compile` clean) and each contains a `raise SystemExit("…merge … first")` guard — so they "refuse to run until merged," exactly as the lab text states. Not a bug.
- Both **completed files** (`extra/agent_loop.txt`, `extra/auto_agent.txt`) compile cleanly and have **no** `SystemExit` guard — merging produces runnable programs.
- The skeleton→complete diff is small and intentional (~22 changed lines: the guard line + the two TODO regions).

**3. File dependency chain.** Files that later labs assume (`hello.js`, `goodbye.py`, `user.js`, `user.test.js`, the `api-checker` skill, the planner/test-runner/reviewer agents) are all created in Labs 1–5, and the Day 2 banner explicitly states the Codespace + those files carry forward. No orphaned references.

**4. Day/environment banners.** Day 2 opens "continue in the same Codespace"; Day 3 opens "most labs run OUTSIDE the Codespace," and every Day 3 lab carries an `Environment:` banner (claude.ai / Claude Desktop). Capstone (Lab 21) correctly returns to the terminal then the platform.

## What a live run still needs (and what it could cover)

The `codespace-lab-tester` skill drives Chrome to open a **GitHub repo** in a Codespace and execute steps. Chrome **is** connected. The blockers:

1. **The new labs aren't in a repo.** This folder is not a git repo, and the public `skillrepos/ccode` repo still holds the **old half-day** `labs.md`. Pointing the tester at it would test the wrong content. The updated `labs.md` + `sdk/` + `extra/` must be pushed to a GitHub repo (a fork or a throwaway test repo) first. Pushing needs **your** git credentials — I can't do that autonomously.
2. **Running `claude` needs your account.** The Codespace must authenticate Claude Code via the OAuth flow with your paid account (the `codespace-cc-installer` skill handles this, with you authorizing).
3. **Only part of the course is Codespace-testable.** Day 1 (Labs 1–7) and the terminal portions of Day 2 (Labs 8–10, 12) can be run live. Labs 11 (Agent SDK — needs the SDK credit), 13 (cloud Routines), 14 (cloud/web/teleport), and all of Day 3 (claude.ai artifacts, Cowork, connectors, Live Artifacts) run outside the Codespace and can't be driven by this tester.

**To proceed with a live run:** push the updated files to a GitHub repo you designate (or authorize me to push to a fork using your git auth), confirm your Claude account for the Codespace, and I'll run Labs 1–10 + 12 end-to-end through Chrome and produce a per-step pass/fail report.
