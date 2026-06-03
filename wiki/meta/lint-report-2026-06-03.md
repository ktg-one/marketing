---
type: meta
title: "Lint Report 2026-06-03"
created: 2026-06-03
updated: 2026-06-03
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-06-03

Run via a 4-agent swarm (link-graph, frontmatter+fix, content gaps, session-ingest). Trust state: `probation`.

## Summary
- Pages scanned: ~151
- Frontmatter auto-fixed: **76 pages** (added missing `status`/`created`/`updated`; never overwrote existing values)
- Stale intel corrected (via callouts, nothing deleted): **4 pages** — [[runtime-config]] (OpenCode → Claude Code), [[model-registry]] + [[hybrid-models-guide]] (local lineup → Google/Gemini), [[Composio]] (.env key + publish path)
- New pages ingested: **4** — [[Google-Gemini-Engine]], [[Content-Production-Flow]], [[Agent-SDK-Orchestration]], [[ktg-hub-Plugin]]
- Link fixes applied: index stale entries ([[Good-AI]], [[Writing-Discipline-Ruleset]]) + body-page name-mismatch sweep + `.md`-suffix orphan fix
- Needs human review: orphan deletions, missing satire-character pages, plugin-count drift

## Orphan Pages (11 → fixed at source)
Root cause: `content/the-mirage-of-ethical-ai/_index.md` linked its 7 sub-pages with a `.md` extension (`[[social-medium.md]]`), which Obsidian does not resolve. Fixed by stripping the extension → the 7 content pages ([[post]], [[publish-checklist]], [[social-ig-caption]], [[social-linkedin]], [[social-medium]], [[social-reddit]], [[social-x-thread]]) now resolve.
Remaining intentional orphans (intel/playbooks/modules hub pages): [[hybrid-models-guide]], [[model-registry]], [[pipeline-signals]], [[runtime-config]] — reachable via their `_index`/`modules/index`; low priority.

## Dead Links (71 distinct)
- **Fixed (name-vs-slug mismatch):** `[[Good AI]]`→`[[Good-AI]]`, `[[Writing Discipline Ruleset]]`→`[[Writing-Discipline-Ruleset]]`, `[[Myth-Hilarity Tech Anthropology]]`→`[[myth-hilarity-tech-anthropology]]`, `[[Prompt God]]`→`[[Prompt-God]]`, `[[LLM Council]]`→`[[Team LLM Orchestration Roster|LLM Council]]`.
- **By-design (left as-is):** in-universe satire references in the Mirage essays + BotB results with no backing page — `[[Conway]]`, `[[BUDDY]]`, `[[QuitGPT]]`, `[[OpenCode]]`, `[[AMD]]`, `[[FreeBSD]]`, `[[Claude Mythos]]`, `[[Anti-Distillation]]`, the TEAM-EAST/WEST judging links. Not errors.

## Missing Pages (needs review — create or leave)
- "Claude Mythos", "Anti-Distillation" — Mirage-universe entities at the same tier as KAIROS/autoDream (which got pages). Asymmetry worth closing if you want them paged.
- `modules/index.md` links to non-existent `[[playbooks/karpathy-llm-wiki]]`, `[[modules/cross-plugin-dependencies]]`, `[[modules/agent-roster]]` — stubs to create.
- "Shane", "Josh" (Kismet principals) — currently inline in [[Kismet]]; person pages optional.

## Stale Claims (corrected this session)
- [[runtime-config]]: "Active Runtime: OpenCode" → corrected to Claude Code (`[!contradiction]` callout).
- [[model-registry]] / [[hybrid-models-guide]]: Qwen/kimi/Ministral lineup → superseded by Google/Gemini (`[!update]`/`[!contradiction]`).
- `modules/index.md`: "79 skills, 40 agents" vs CLAUDE.md "84 skills · 39 agents" vs on-disk ~128 project + ~100 canonical skills / 10 agents — **count drift, NOT yet reconciled** (flagged for a follow-up pass).

## Empty Sections / Style
- None of consequence. Naive scans flagged code-fence/list/subsection content as false positives; first-person "I think" in social copy and in-character dialogue are house style, not violations.

## Not run
- **DragonScale address validation** — skipped (no `scripts/allocate-address.sh` / `.vault-meta/address-counter.txt`; vault not on DragonScale).
- **Semantic tiling** — not run this pass.
