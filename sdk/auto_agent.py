#!/usr/bin/env python3
"""Lab 11 (Part 2): Unattended agent runs that never hang.

Three layers keep an unattended run both safe and unblocked:
  1. allowed_tools   -- pre-approve the tools we expect Claude to use
  2. permission_mode -- "acceptEdits" auto-approves file edits
  3. can_use_tool    -- a programmatic gatekeeper that decides everything
                        else, so no human prompt can ever hang the run

[Lab 11 - AI-Powered Coding with Claude Code - Rev 6.10 - 06/29/26]
"""
import asyncio

from claude_agent_sdk import ClaudeAgentOptions, HookMatcher, ResultMessage, query
from claude_agent_sdk.types import (
    PermissionResultAllow,
    PermissionResultDeny,
    ToolPermissionContext,
)

TASK = (
    "Create a file named agent_report.md that lists every .js file in this "
    "directory with a one-line description of each. Then say DONE."
)


async def gatekeeper(
    tool_name: str, input_data: dict, context: ToolPermissionContext
):
    """Decide any tool call not already pre-approved. Never asks a human."""
    # GATEKEEPER (TODO 1) -- merge this body from extra/auto_agent.txt:
    #   block Bash commands containing "rm " or "sudo" (print a DENIED note,
    #   then return a Deny); otherwise print an "auto-approving" note and
    #   return an Allow.
    raise NotImplementedError("gatekeeper: merge extra/auto_agent.txt, then save")


# Required workaround: a PreToolUse hook keeps the stream open for can_use_tool
async def keep_alive(input_data, tool_use_id, context):
    return {"continue_": True}


async def prompt_stream():
    yield {"type": "user", "message": {"role": "user", "content": TASK}}


async def main() -> None:
    # ------------------------------------------------------------------
    # SKELETON BODY (TODO 2 + 3) -- merge this whole body from
    # extra/auto_agent.txt, then SAVE. It builds ClaudeAgentOptions with
    # the three safety layers plus max_turns, then reads the result.
    # ------------------------------------------------------------------
    raise SystemExit("auto_agent.py is still the skeleton -- merge BOTH highlighted regions from the left (the finished file) into the right, SAVE, then run again.")


asyncio.run(main())
