---
type: meta
title: "Hot Cache"
updated: 2026-05-27T03:00:00+08:00
tags: [meta, hot-cache]
---

# Recent Context

## Last Updated
2026-05-27. **18-source wiki ingest completed across 4 parallel batches.** `.planning/codebase/` map produced (7 files, 1429 lines). `CLAUDE.md` rewritten to the 5-layer architecture. Karpathy LLM Wiki Pattern now load-bearing canon for this repo.

## Total wiki state
| Domain | Count | Δ this session |
|---|---|---|
| Sources | 33 | +9 |
| Entities | 16 | +6 (Composio, GSD-Methodology, ktg-one, SCCD-Model, LTX-Video, Hedra) |
| Concepts | 30 | +7 (Five-Layer-Architecture, Review-Gate, Publish-Kit-Pattern, Skill-Progressive-Disclosure, Pipeline-Verification-Criteria, Best-Practices-Kernel, Level-3-Production-Pipeline) |
| Cast pages | 11 | 4 updated (Grok, DeepSeek, Kimi, Perplexity — voice samples extended) |
| Episodes | 5 scripted + 4 banked | +7 (series-arc-development, benchmarks-episode, prompt-god-scene, digital-backstage-bible, pilot-3in1, 4x-ideas-episode, teamllm-missing-stub) |
| Intel snapshots | 4 | +1 (prompt-zone-status-2026-05-27) |
| Codebase map | 7 docs / 1429 lines | NEW (.planning/codebase/) |

## Key facts (2026-05-27 session)
- **5-layer architecture canonized**: State (wiki) → Plugins (.claude/plugins/) → Orchestration (/hub) → Runtime (pipeline/) → Publishing (Composio + Review Gate)
- **Karpathy LLM Wiki Pattern = canon**: agents that don't load the wiki = no user context = drift. Reading wiki INTO context is load-bearing, not optional. CLAUDE.md and AGENTS.md both encode this.
- **Best-Practices Kernel identified as upstream**: AGENTS.md §5 is downstream restatement of `.claude/plugins/best-practices-main/best-practices.md`. Plugin is the canonical source for engineering + agent discipline.
- **Mirage final = byte-identical** to `.raw/articles/the-mirage-of-ethical-ai-2026-05-16.md` (hash 94d25c…). Finalized-version-of relation captured.
- **6 contradictions flagged** in ingest (all via callouts, never silently overwritten): Gemini voice/visual, Prompt-God framing, CLAUDE role-label, Claude palette, Gemini visual. **Locked cast canon stands** in every case.
- **Two missing source files**: `videography/-11142025-deep-brainstorm.md` and `videography/-TeamLLM.md` (case-variant of `-TEAM-LLM.md`). Logged in manifest as `not_found`.

## SCCD ↔ Wiki theorem (this session insight)
`wiki/` = exterior SELF (anchors that survive `/clear`) · reading wiki = CONSCIOUSNESS pulling state into simulation · `/wiki-ingest` = CHOICE (which entities/concepts collapse into pages) · `wiki/log.md` (newest-on-top append-only) = DECIDE. The vault IS the SCCD substrate for the agent layer.

## ⛔ Trust State: PROBATION
Read `wiki/meta/agent-trust-state.md` FIRST. Kevin set status to `probation` 2026-05-27 after multiple sessions of babysitting overhead. Status field is authoritative; only Kevin can promote it. Behavior is being judged against documented earn-back criteria.

## Active Threads
- **Publish Mirage**: still awaiting per-post green-light. Vercel → URL → Reddit + LinkedIn variants via Composio. The `the-mirage-of-ethical-ai-final.md` ingest confirms zero late edits since 2026-05-16.
- **Kismet/Good AI strategy**: wikified; Training + Dashboard phase still pending.
- **GSD Phase 1.0 Foundation**: the in-flight wiki ingest IS the work for this phase per `.planning/ROADMAP.md`. `.planning/phases/` directory not yet scaffolded; ROADMAP table format isn't parsed by `gsd-sdk` (returns 0 phases). Either reformat ROADMAP or scaffold phase dirs.

## Carry-forward
- Cross-vault drift risk: parent `C:/Users/kevin/knowledge2026/` and Desktop/projects2026 Next.js sites are separate repos.
- WP Basic auth in `README.md.txt` (NOT `.env`) — security flag.
- Plugin registration: 13 of 79 skills registered per `wiki/modules/index.md`.
