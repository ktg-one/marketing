---
type: entity
subtype: project
title: "ktg-one"
aliases: ["KTG Content Hub", "ktg.one workspace"]
created: 2026-05-27
tags: [entity, project, pipeline, content, agent-orchestration]
---

# ktg-one

Plugin-driven, agent-orchestrated content creation hub. Personal workspace of Kevin Tan (`kevin.pl.tan@gmail.com`), operating under the **[[Good-AI]]** brand (`goodai.au`).

## What It Is

ktg-one is **not** a traditional software application. There is no web server, no compiled binary, no traditional build pipeline. The "code" is:
- Skill orchestration (Markdown + YAML frontmatter skills loaded by AI CLIs)
- Wiki state (Obsidian-style knowledge graph — the persistent memory layer)
- Pipeline scripts (`pipeline/run.sh` — 2s bash; `pipeline/ktg_pipeline/` — Python AI, untested)

## Six-Stage Pipeline

1. **Capture** — ingest ideas, files, or URLs into the wiki
2. **Plan** — generate campaign briefs from wiki state
3. **Create** — draft blog posts and generate images (parallel at write step)
4. **Optimize** — GEO, SEO audits, schema markup (sequential)
5. **Review** — mandatory human gate ([[Review-Gate]]) before any publish action
6. **Publish** — deploy to Vercel, fire social variants via [[Composio]]

## Architecture

See [[Five-Layer-Architecture]] for the full stack diagram.

| Layer | What it is |
|---|---|
| 5 — Publishing | Vercel + [[Composio]] (Reddit/LinkedIn) + WordPress |
| 4 — Runtime | `pipeline/run.sh` + `pipeline/ktg_pipeline/` |
| 3 — Orchestration | `.claude/skills/hub/` → `/hub <slug>` |
| 2 — Plugins | 7 plugins, ~80 skills (blog, seo, ads, canvas, image, best-practices, wp) |
| 1 — State | `wiki/` — the knowledge graph |

## Technology Stack

- **Python 3.12+** managed by `uv` (lockfile: `uv.lock`)
- **AI CLI Host**: OpenCode (primary), [[Claude Code]], Gemini CLI, Codex CLI
- **Publishing**: [[Composio]] MCP
- **Planning**: [[GSD-Methodology]] in `.planning/` (6-phase roadmap)
- **Skills**: 400+ skill hashes in `skills-lock.json`
- **Python deps**: minimal — `kimi-cli>=1.44.0`, `tool>=0.8.0`

## Current Status (2026-05-26)

- **MVP**: Complete — bash pipeline ships content in 2 seconds at $0
- **Python AI pipeline**: ~70% — framework built, untested against real LLMs
- **Auto-publish**: Blocked — X/Meta/Medium APIs unavailable; LinkedIn/Reddit possible via [[Composio]]
- Phase 1.0 Foundation: in progress

See [[project-state]] and [[state-txt]] for current snapshot.

## Content Voice

**[[myth-hilarity-tech-anthropology]]** — "Myth-Hilarity + Tech Systems mixed with Anthropology." Two-layer writing stack: brand voice defines the tone, [[Writing-Discipline-Ruleset]] defines how not to collapse into formula.

## Key Files for Agent Onboarding

1. `wiki/modules/index.md` — master plugin map
2. `wiki/modules/pipeline-signals.md` — sequential pipeline chaining
3. `wiki/hot.md` — current session state
4. `.planning/PROJECT.md` — scope + architecture decisions
5. `.planning/ROADMAP.md` — current phase + verification criteria
6. `AGENTS.md` — authoritative agent doc (overrides other docs in conflict)

## Related Entities
- [[Good-AI]] — the brand this workspace produces content for
- [[Kismet]] — sales/engagement operation, separate but related
- [[Claude Code]] — primary AI CLI runtime
- [[Composio]] — publishing MCP connector
- [[GSD-Methodology]] — project management framework
- [[SCCD-Model]] — functional self-model built inside this workspace

## Sources
- [[agents-md-ktg-one]] — AGENTS.md (authoritative)
- [[claude-md-ktg-one]] — CLAUDE.md (5-layer architecture)
- [[project-state]] — PROJECT_STATE.md (pipeline status)
- [[state-txt]] — STATE.txt (quick-state card)
