#!/usr/bin/env python3
"""Lab 12: Unattended agent runs that never hang.

Three layers keep an unattended run both safe and unblocked:
  1. allowed_tools   -- pre-approve the tools we expect Claude to use
  2. permission_mode -- "acceptEdits" auto-approves file edits
  3. can_use_tool    -- a programmatic gatekeeper that decides everything
                        else, so no human prompt can ever hang the run

[Lab 12 - AI-Powered Coding with Claude Code - Rev 6.0 - 06/11/26]
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
    # TODO 1: If tool_name is "Bash" and the command contains "rm " or "sudo",
    #         return PermissionResultDeny with a short message. Otherwise
    #         print a "[gatekeeper] auto-approving: <tool_name>" note and
    #         return PermissionResultAllow(updated_input=input_data).
    return PermissionResultDeny(message="gatekeeper not implemented yet")


# Required workaround: a PreToolUse hook keeps the stream open for can_use_tool
async def keep_alive(input_data, tool_use_id, context):
    return {"continue_": True}


async def prompt_stream():
    yield {"type": "user", "message": {"role": "user", "content": TASK}}


async def main() -> None:
    raise SystemExit("auto_agent.py: merge the completed code from extra/auto_agent.txt first")
    # TODO 2: Build ClaudeAgentOptions with the three safety layers plus a
    #         hard stop: allowed_tools=["Read", "Glob", "Grep", "Write"],
    #         permission_mode="acceptEdits", max_turns=10,
    #         can_use_tool=gatekeeper, and
    #         hooks={"PreToolUse": [HookMatcher(matcher=None, hooks=[keep_alive])]}
    options = ClaudeAgentOptions()

    # TODO 3: Iterate query(prompt=prompt_stream(), options=options) and when
    #         the ResultMessage arrives print num_turns and result.
    async for message in query(prompt=prompt_stream(), options=options):
        pass


asyncio.run(main())
