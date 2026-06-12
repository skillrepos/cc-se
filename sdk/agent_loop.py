#!/usr/bin/env python3
"""Lab 11: Your first programmatic agent loop.

This is the SAME agent loop that powers the Claude Code CLI --
we are just driving it from Python instead of a terminal.

[Lab 11 - AI-Powered Coding with Claude Code - Rev 6.0 - 06/11/26]
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
    raise SystemExit("agent_loop.py: merge the completed code from extra/agent_loop.txt first")
    # TODO 1: Build ClaudeAgentOptions that pre-approves the read-only tools
    #         Read, Glob, and Grep, and caps the loop at 5 turns (max_turns).
    options = ClaudeAgentOptions()

    # TODO 2: Iterate the messages from query(prompt=prompt, options=options).
    #         For each AssistantMessage, print the text of its TextBlocks.
    #         When the ResultMessage arrives, print num_turns, duration_ms,
    #         and result.
    async for message in query(prompt=prompt, options=options):
        pass


if __name__ == "__main__":
    user_prompt = " ".join(sys.argv[1:]) or (
        "What files are in this directory? Answer in one sentence."
    )
    asyncio.run(run_agent(user_prompt))
