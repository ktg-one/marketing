---
status: developing
type: concept
title: "Agent SDK Orchestration"
aliases: ["Claude Agent SDK", "Agent SDK decision", "orchestration SDK", "SDK split"]
created: 2026-06-03
updated: 2026-06-03
tags: [concept, orchestration, sdk, claude-agent-sdk, composio, gemini, publishing, decision]
---

# Agent SDK Orchestration

The **2026-06-03** decision on which SDK orchestrates the [[ktg-one]] content hub's orchestration + publish path, and how that splits from the generation engine.

## The decision

**Orchestration + publish = Claude Agent SDK (Python, `claude_agent_sdk`) + [[Composio]] MCP.**

- Same model family as Claude Code / Claude Cowork → no context-switch, no TypeScript required.
- Composio MCP provides the publish connectors (Vercel + LinkedIn + Reddit).

## The split — Claude orchestrates, Gemini generates

> [!important] Gemini stays the **generation** engine and is **NOT orchestrated by Claude**.
> Claude (via the Agent SDK) runs orchestration and publishing. Gemini ([[Google-Gemini-Engine]]) is the generation/repurpose/image engine, invoked as a tool — it does not drive the agent loop.

## Critical safety rule

> [!warning] Do **NOT** use `permission_mode="bypassPermissions"` on the publish step.
> Bypassing permissions would defeat the non-bypassable [[Review-Gate]]. The gate must remain enforceable. The fail-closed `PreToolUse` hook in [[ktg-hub-Plugin]] (`hooks/review-gate.sh`) is the backstop, but the SDK config must not undermine it.

## Alternatives considered

| Option | When relevant |
|---|---|
| **Vercel AI SDK (TypeScript)** | Only if a **streaming web UI** is built later. Not needed for the CLI/agent path. |
| **LiteLLM / Pydantic AI (Python)** | Provider-agnostic alternative if multi-provider abstraction is wanted. |

## Cross-References
- [[Google-Gemini-Engine]] — the generation engine (NOT orchestrated by Claude)
- [[Composio]] — the MCP publish connector paired with the SDK
- [[Review-Gate]] — must stay enforceable; do not bypass permissions
- [[ktg-hub-Plugin]] — carries the fail-closed gate hook
- [[Content-Production-Flow]] — the flow being orchestrated
- [[Five-Layer-Architecture]] — orchestration (L3) + publishing (L5)
- [[Claude Code]] — same model family as the SDK
