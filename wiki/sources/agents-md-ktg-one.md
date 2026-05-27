---
type: source
title: "AGENTS.md — ktg-one (Authoritative Agent Onboarding Doc)"
slug: agents-md-ktg-one
source_path: "AGENTS.md"
source_type: project-config
ingested_at: 2026-05-27
tags: [source, project-config, pipeline, agents, architecture, security]
hash: md5:a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6
---

# AGENTS.md — ktg-one

> Canonical onboarding document for AI coding agents working on [[ktg-one]]. Last updated 2026-05-26. Authoritative — conflicts with other docs resolve in favour of this file.

## Summary

`AGENTS.md` is the single source of truth for AI agents entering the ktg-one workspace. It covers project overview, tech stack, directory structure, build commands, code style, testing philosophy, security posture, deployment, and active workstreams. At ~300 lines it is the most detailed single document in the project.

## Key Facts Extracted

### Project Identity
- [[ktg-one]] is a **plugin-driven, agent-orchestrated content creation hub** — not a traditional software application.
- Pipeline: Capture → Plan → Create → Optimize → Review → Publish (6-stage lifecycle).
- Owner: Kevin Tan (`kevin.pl.tan@gmail.com`), brand: **[[Good-AI]]** (`goodai.au`).
- Voice: **Myth-Hilarity** — two-layer writing stack (brand voice + [[Writing-Discipline-Ruleset]]).

### Technology Stack
| Layer | Technology |
|---|---|
| Runtime | Python 3.12+ (`uv`) |
| AI CLI Host | OpenCode (primary), [[Claude Code]], Gemini CLI, Codex CLI |
| Skills System | OpenCode / Claude Code skills (YAML frontmatter + Markdown) |
| Wiki Engine | Custom Obsidian-style vault (`wiki/`) |
| Image Generation | Gemini Nano Banana models (`banana-claude` plugin) |
| SEO Data | DataForSEO API, Firecrawl |
| Publishing | [[Composio]] MCP (Reddit, LinkedIn, Vercel, Gmail, Drive, Discord, YouTube, GitHub) |
| WordPress | `wp-mcp-ultimate` at `https://ktg.one/wp-json/mcp/wp-mcp-ultimate` |
| Browser | Chrome DevTools MCP |
| Planning | [[GSD-Methodology]] (`.planning/`) |

### Plugin Ecosystem (7 plugins, ~80 skills)
- `banana-claude` — image generation
- `claude-ads` — 22 ad skills
- `claude-blog-main` — 22 blog skills
- `claude-canvas` — 8 canvas skills
- `claude-seo` — 25 SEO skills
- `best-practices-main` — development best practices (upstream: [[Best-Practices-Kernel]])
- `wordpress-mcp-ultimate` — WordPress MCP gateway

### Skills Count
- ~80 skills across 7 plugins
- 60+ skills in `.agents/skills/`
- `skills-lock.json` — 400+ integrity hash entries

### Build / Test Philosophy
- **No traditional build system** — no pytest, no jest, no CI
- Quality via [[Pipeline-Verification-Criteria]] (phase-by-phase verification gates)
- Primary test: `/wiki-lint` for structural integrity, voice audit against `[[user-voice]]`
- Manual test: run `/hub` on a test post, check 4 social variants, hero + 3 crops, GEO score, schema.json, then [[Review-Gate]] stops

### Key Commands
| Command | Purpose |
|---|---|
| `bash pipeline/run.sh <input.md>` | Working 2s template pipeline |
| `/hub <slug>` | Full LLM-orchestrated pipeline |
| `/wiki-ingest [file]` | Add source to wiki |
| `/wiki-lint` | Health check |
| `/banana <prompt>` | Image gen |

### Security
- WordPress MCP auth stored in `README.md.txt` (Basic auth base64) — NOT `.env`
- Composio connections via MCP gateway at `D:\projects\.mcp\gateway.py`
- No `.env` file — API keys injected via MCP server environment or CLI config
- [[Review-Gate]] is **non-bypassable by design** — even `/loop` and scheduled runners must stop
- Per-post approval required — no session-wide blanket YES
- Gate state written to wiki (survives `/clear`)

### Active Workstreams (2026-05-26)
| Workstream | Status |
|---|---|
| Publish "Mirage" post | Awaiting green-light → Vercel + Reddit + LinkedIn |
| Kismet/Good AI strategy | Wikified → Training + Dashboard phase |
| Phase 1.0 Foundation | In progress — audit wiki-ingest input modes |
| Plugin registration | 13 of 79 skills registered |

## Plugin Duplication Note

The behavioral rules in section 5 ("Think Before Coding", "Simplicity First", "Surgical Changes", "Goal-Driven Execution") directly mirror the upstream [[Best-Practices-Kernel]] (`best-practices-main/best-practices.md`). AGENTS.md encodes these at project scope; the plugin is the canonical upstream. Treat the plugin as the authoritative definition; AGENTS.md is a project-scoped re-statement.

## Cross-References
- [[ktg-one]] — project entity
- [[Good-AI]] — brand
- [[Claude Code]] — primary AI CLI
- [[GSD-Methodology]] — planning framework
- [[Composio]] — publishing layer
- [[Review-Gate]] — publish security concept
- [[Pipeline-Verification-Criteria]] — quality gates
- [[Best-Practices-Kernel]] — upstream engineering principles
- [[Five-Layer-Architecture]] — the stack model
- [[Skill-Progressive-Disclosure]] — skill loading pattern
- [[Writing-Discipline-Ruleset]] — voice complement
