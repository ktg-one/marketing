---
type: meta
title: "Hot Cache"
updated: 2026-06-03T20:00:00+08:00
tags: [meta, hot-cache]
---

# Recent Context

## Last Updated
2026-06-03. **Catch-up ingest after a neglected session** (the wiki was not touched for most of the work; this ingest closes the gap). Three big shifts captured: (1) the content pipeline engine migrated Ollama → **Google/Gemini**; (2) a self-contained **ktg-hub plugin** was built (dual Claude Code + Cowork packaging); (3) Kevin's **actual content flow** was corrected — Claude writes the blog, Gemini only does images + repurpose.

## Total wiki state
| Domain | Count | Δ this session |
|---|---|---|
| Sources | 33 | 0 |
| Entities | 17 | +1 ([[ktg-hub-Plugin]]) |
| Concepts | 33 | +3 ([[Google-Gemini-Engine]], [[Content-Production-Flow]], [[Agent-SDK-Orchestration]]) |
| Intel | 6 | 2 updated ([[model-registry]], [[hybrid-models-guide]] → Gemini supersede) |
| Playbooks | 3 | 1 updated ([[runtime-config]] → Claude Code) |

## Key facts (2026-06-03 session)
- **Engine = Google/Gemini** (`pipeline/ktg_pipeline/`): text `gemini-3.5-flash` (hero `gemini-3-pro-preview`), images Nano Banana `gemini-3.1-flash-image-preview`, driver `GEMINI_API_KEY`. House voice → 6 prose stages only. Parallel (ThreadPoolExecutor, 8 stages, ~20s). Verified live. Branch `feat/pipeline-google-voice-parallel`. Ollama = `--local` fallback only.
- **Gemini is NOT the writer.** Actual flow: Research→NotebookLM → **write in Claude (in-session)** → images via banana → repurpose (Gemini) → review gate → Composio publish. Ads + videography = Gemini's domain, out of content-hub scope.
- **ktg-hub plugin**: Claude Code plugin (`./plugins/ktg-hub`) + Cowork `.plugin` (`dist/ktg-hub.plugin`). Skills `hub`/`publish`; 3 agents; fail-closed `PreToolUse` gate hook (`hooks/review-gate.sh`, blocks path-traversal/unapproved slugs, exit 2); bundles nanobanana MCP + pipeline + voice.
- **Publish path**: Composio (key `COMPOSIO_API_KEY` in `.env`, gitignored) → Vercel + LinkedIn + Reddit, behind non-bypassable per-post gate. X/Meta/Medium MANUAL.
- **SDK split**: orchestration+publish = Claude Agent SDK (Python) + Composio MCP; Gemini = generation only. **NEVER `permission_mode="bypassPermissions"` on publish** — it defeats the gate.

## ⛔ Trust State: PROBATION
Read `wiki/meta/agent-trust-state.md` FIRST. Status still `probation` (set 2026-05-27, Kevin-owned). This session: the wiki was neglected most of the way through — exactly the drift the Karpathy canon exists to prevent. Only Kevin promotes the status.

## Active Threads
- **Publish Mirage**: still awaiting per-post green-light (Vercel → URL → Reddit + LinkedIn via Composio).
- **Pipeline E2E verify**: Gemini engine returns "PIPELINE OK" but full /hub Phase 2.0–6.0 + Composio auto-post path still untested end-to-end.
- **ktg-hub plugin**: built + gate hook verified; needs a real publish dry-run through the gate.

## Carry-forward
- `COMPOSIO_API_KEY` + `GEMINI_API_KEY` live in `.env` (gitignored) — don't commit; WP Basic auth still in `README.md.txt` (security flag).
- Gemini owns ads + videography; do not pull those into the content hub.
- Vercel AI SDK (TS) only relevant if a streaming web UI is built later.
- Branch `feat/pipeline-google-voice-parallel` pushed; repo reorg (`templates/`) committed `387b109`.
