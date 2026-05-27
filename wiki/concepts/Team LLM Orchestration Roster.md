---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, orchestration, multi-agent, team-llm]
---

# Team LLM Orchestration Roster

The KTG operating doctrine for multi-model orchestration. Distinct from the [[cast/_index|animated cast]] — this is the production-side roster used to actually do the work.

## Roster (production)

| Agent | Model | Role | Strengths |
|---|---|---|---|
| Claude (spine) | Claude Sonnet/Opus | Strategy, synthesis, final output | Precision, instruction following |
| Gemini | Gemini | Research, long context, verification | Web-grounded, analytical |
| Codex | Codex CLI | Mechanical execution | Bulk edits, literal compliance |
| Jules | Jules CLI | Async background | GitHub-native, background queue |

## Routing rules (default)

- **Strategy / synthesis / final pass** → Claude (spine).
- **Web research / verification / long-context analysis** → Gemini.
- **Bulk mechanical edits / literal task execution** → Codex.
- **Async background / GitHub-native / overnight queues** → Jules.

(Extended dispatch table — KIMI for deep research, Qwen for additional Eastern advantage, etc. — lives in the global `~/.claude/rules/ai-orchestration.md`.)

## Why these four

- **Claude as spine**: best instruction following, best at maintaining the writing voice + planning loops.
- **Gemini for research**: native web grounding (Google Search), tolerant of long context, stronger on verification.
- **Codex for execution**: literal compliance — does exactly what you say, doesn't editorialise.
- **Jules for async**: background queues so the foreground session stays clean.

## Cross-references

- [[prompt-zone-overview]] — the canonical source
- [[cast/_index|Cast]] — the satirical recast of these (and more) models for the [[team-llm-production-bible|animated series]]
- Sister projects: LEGIO/ (framework), Recursive-Council/ (multi-agent reasoning)
