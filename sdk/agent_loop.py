#!/usr/bin/env python3
"""Lab 11: Your first programmatic agent loop.

This is the SAME agent loop that powers the Claude Code CLI --
we are just driving it from Python instead of a terminal.

[Lab 11 - AI-Powered Coding with Claude Code - Rev 6.10 - 06/29/26]
"""
import asyncio
import sys

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ResultMessage,
    TextBlock,
    query,
)


async def run_agent(prompt: str) -> None:
    """Send one prompt through the agent loop and print what happens."""
    # ------------------------------------------------------------------
    # SKELETON BODY -- replace everything between these dashed lines by
    # merging from extra/agent_loop.txt (see the lab's diff-merge step),
    # then SAVE this file. Two pieces turn this script into an agent:
    #   1. the OPTIONS -- which tools are pre-approved, plus a turn cap
    #   2. the LOOP    -- read each message that query() streams back
    # ------------------------------------------------------------------
    raise SystemExit("agent_loop.py is still the skeleton -- merge the right side of the diff over this body, SAVE, then run again.")


if __name__ == "__main__":
    user_prompt = " ".join(sys.argv[1:]) or (
        "What files are in this directory? Answer in one sentence."
    )
    asyncio.run(run_agent(user_prompt))
