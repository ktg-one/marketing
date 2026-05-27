# Coding Conventions

**Analysis Date:** 2026-05-27

This is a **content-and-skills repo**, not a software application. "Code style" here is dominated by Obsidian markdown conventions and Claude Code skill conventions, with a thin Python shell at the root. Every convention below was confirmed by sampling real files in the repo.

## Naming Patterns

**Files (Obsidian / wiki):**
- `kebab-case.md` for most pages (e.g. `myth-hilarity-tech-anthropology.md`, `writing-ruleset.md`)
- `Title Case.md` allowed for concept pages where the title is the natural slug (e.g. `wiki/concepts/AI Anthropology Framing.md`, `Bugs as Personality Traits.md`)
- `_index.md` for per-directory landing pages
- `hot.md`, `index.md`, `log.md`, `overview.md` reserved at the wiki root
- **Leading `-` prefix** intentionally used to control Obsidian sort order (e.g. `videography/-Chat/`, `-claude/`, `-media/`) — **keep the prefix on rename**

**Files (skills):**
- `SKILL.md` — fixed name for every skill entry file
- `kebab-case/` for skill directory names (e.g. `blog-write/`, `seo-schema/`, `wiki-ingest/`)
- Per-plugin `CLAUDE.md` documents the plugin itself (e.g. `.claude/plugins/claude-blog-main/CLAUDE.md`)
- Reference docs live under `<skill>/references/*.md`, kept under ~200 lines each
- Scripts under `<skill>/scripts/` with CLI interface and JSON output

**Files (planning):**
- `.planning/*.md` in UPPERCASE (`ROADMAP.md`, `REQUIREMENTS.md`, `PROJECT.md`)
- `.planning/codebase/*.md` in UPPERCASE (`STACK.md`, `CONVENTIONS.md`, `TESTING.md`)

**Files (blog posts):**
- `POST-<title>.md` or descriptive slugs (e.g. `the-mirage-of-ethical-ai-final.md`)
- Battle posts in `blog/battlle-of-the-bots/round-N/` keep the misspelled `battlle` directory — do not "fix"

**Functions / variables (Python):**
- `snake_case` for functions and variables
- `UPPER_SNAKE` for module-level constants
- Python is minimal here — `main.py` is a stub. No house Python conventions beyond stdlib idiom.

## Obsidian Markdown Conventions

**YAML frontmatter on every wiki page** — confirmed across `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`, `wiki/concepts/AI Anthropology Framing.md`. Required fields vary by page type but always include `type`, `tags`, and timestamps.

Standard frontmatter shape:
```yaml
---
type: meta | concept | source | entity | playbook | intel | content
title: "Human Readable Title"           # optional for concept pages
status: developing | stable | archived   # for concepts
created: 2026-05-16
updated: 2026-05-26
tags: [concept, ai-anthropology, framework]
---
```

**Wikilinks (`[[name]]`) are valid markdown** — they MUST be preserved on every edit. They are load-bearing for `/wiki-lint` orphan detection and `/wiki-query` graph traversal. Aliased form `[[slug|Display Text]]` is used in `wiki/index.md`. Example from `wiki/concepts/AI Anthropology Framing.md`:

```markdown
Established empirically by [[battle-of-the-bots|Battle of the Bots]] (2025)
and codified in [[botb-round-2-prematch|the agents.md pre-match]].
```

**`wiki/hot.md` — rolling continuity cache:**
- Hard cap **~500 tokens** (NFR-2.2). Read on every session start; bloating it breaks the Karpathy LLM wiki pattern.
- Always update at session end via the `/session-end` hook (FR-1.3).
- Structure: `## Last Updated` → `## Total wiki state` table → `## Key Recent Facts` → `## Active Threads`.

**`wiki/log.md` — append-only operations log:**
- **Newest entries at the TOP** (header comment in file: *"Append-only. **Newest entries at the TOP.** Never edit past entries."*)
- One `## YYYY-MM-DD — <action> | <summary>` heading per entry
- Sub-bullets list created sources, pages, cross-references — never edit historical entries

**`wiki/index.md` — master catalog:**
- Update after every ingest or new note
- Groups pages by domain (Campaigns / Channels / Audiences / Content / Voice / Intel / Calendar / Playbooks / Performance)

## Skill Conventions (Claude Code / OpenCode)

These are non-negotiable per AGENTS.md §5 and the per-plugin `CLAUDE.md` files (e.g. `.claude/plugins/claude-blog-main/CLAUDE.md`, `.claude/plugins/claude-seo/CLAUDE.md`).

**Mandatory YAML frontmatter on every `SKILL.md`:**
```yaml
---
name: skill-name
description: >
  One-line description for discovery. This is what model-routing sees;
  keep it dense with trigger keywords.
user-invokable: true
argument-hint: "[command] [arg]"
license: MIT
metadata:
  author: <name>
  version: "1.9.9"
---
```

Valid frontmatter fields (from `.claude/plugins/claude-blog-main/CLAUDE.md`): `name`, `description`, `user-invokable`, `argument-hint`, `compatibility`, `license`, `metadata`, `disable-model-invocation`. **Do NOT use `allowed-tools`** — it is not a Claude Code spec field.

**Progressive disclosure (FR-7.2):**
- Entry skill (e.g. `claude-blog-main/skills/blog/SKILL.md`) loads first and routes
- Sub-skills load **on demand** via the `Skill` tool (e.g. `Skill("blog-write")`)
- Reference files in `<skill>/references/` load on demand, not on entry

**`Skill` tool only — never `Read` on skill files** (architecture decision 3.3, AGENTS.md §5):
- Reading skill files directly breaks evolution — cached reads go stale when skills update
- Bypasses the harness's skill metadata and version awareness
- Inflates main-context budget past the 30% ceiling (NFR-2.1)

**Orchestrator size budget (NFR-2.1):**
- Orchestrator skills MUST stay under **~4k tokens** after loading
- SKILL.md files under **500 lines / 5000 tokens**
- Reference files under **~200 lines** (exemption: existing comprehensive references like `platform-guides`, `schema-stack`, `content-templates`, `distribution-playbook`)
- Over-budget orchestrators get refactored into entry + delegation pattern (Phase 6.0)

**Three-layer architecture (architecture decision 3.1):**
- **Directive** — STRAWHATS-DIRECTIVE, CLAUDE.md, user-voice → posture and non-negotiables
- **Orchestration** — pipeline skills (`blog`, `ads`, `seo` entry skills) → decide *what*
- **Execution** — leaf sub-skills (`blog-write`, `seo-schema`, `banana`) → do the work, know nothing about pipeline

**Cross-plugin signals** are documented in `wiki/modules/pipeline-signals.md`. Orchestrators MUST consult `wiki/modules/index.md` and `wiki/modules/pipeline-signals.md` before chaining (FR-7.1).

**Agents invoked via Task / Agent tool, never via Bash.**

## Python Conventions

Python is intentionally minimal — most logic lives in skill Markdown files.

- **Python 3.12+** (`pyproject.toml` declares `requires-python = ">=3.12"`)
- **`uv` is the package manager** — lockfile is `uv.lock`. Use `uv sync`, `uv add <pkg>`, `uv run main.py`.
- **Prefer stdlib** — current dependencies are only `kimi-cli` and `tool`
- Scripts inside skills (e.g. `claude-seo/scripts/*.py`) must have docstrings, CLI interface, and JSON output
- Strict mode is not enforced (this is not a TypeScript project) — but follow the user's global rules: minimum code, no speculative abstractions, no flexibility that wasn't requested

## Battle Post / Episode Conventions

**Heavy emoji + headed sections are intentional KTG style — not noise to clean up.** This applies to:
- `blog/battlle-of-the-bots/round-N/` — round READMEs, judging reports, agent `AGENTS.md` pitches
- `videography/Episodes--*.md` — episode briefs and scripts
- `wiki/playbooks/battle-of-the-bots.md`

Battle sub-projects are also the **only** directories with executable scripts. The pattern in `blog/battlle-of-the-bots/round-2/02-saas-landing/`:
- `deploy.sh` runs `gh repo create` and publishes a public GitHub Pages repo — **side-effects are real, confirm before running**
- Each battle project is self-contained (no monorepo tooling, no shared `package.json`)

## Voice Conventions

**Two-layer writing stack** (NFR-5.1) is mandatory for all long-form prose:
1. **`[[user-voice]]`** (Myth-Hilarity + Tech Anthropology) — brand register, *what tone*
2. **`[[Writing Discipline Ruleset]]`** — technical prose layer, *how not to collapse into formula*

Source-of-truth files:
- `wiki/voice/myth-hilarity-tech-anthropology.md`
- `blog/user_voice.md`
- `blog/WRITING.md-main/WRITING.md`
- `wiki/voice/cast/` — 11-character Team LLM canon (locked)

**Creative engine:** "technical LLM flaws = character flaws" (e.g. context-window limit = anxiety disorder). Never reinvent cast visuals, palettes, or personality traits.

**Copyright evasion** in cast art: chibi designs, shape language, palettes — **never logos**.

## Import / Module Organization

**Not applicable in the traditional sense** — this is not a code monorepo. The closest equivalent is:

- **Skill orchestration order:** Entry skill → routing → `Skill("sub-skill")` invocations → sub-skill's own references load on demand
- **Wiki cross-reference order:** Page → `[[wikilinks]]` → backlinks discoverable via `/wiki-lint` and `/wiki-query`
- **Pipeline order:** documented in `wiki/modules/pipeline-signals.md` (Capture → Plan → Create → Optimize → Review → Publish)

## Error Handling

- Wiki state errors: caught by `/wiki-lint` (orphans, dead wikilinks, frontmatter gaps)
- Skill loading errors: surfaced by the Claude Code / OpenCode harness — do not write defensive wrappers around `Skill()`
- Composio / Vercel failures: documented recovery in `wiki/playbooks/hub-recovery.md` (Phase 6.0 deliverable)
- Review Gate is non-bypassable — a failed gate is not an error, it is the design

## Comments

- Wiki pages: prose is the documentation; HTML comments are rare. Use prose under a `## Notes` heading instead.
- Skill files: keep the Markdown human-readable. Comment with `<!-- ... -->` only for tooling hints.
- Python scripts: docstrings on every CLI entry point (enforced by per-plugin `CLAUDE.md` development rules).

## Function / Module Design

**Skill design (the primary unit of "function" here):**
- One responsibility per skill (write, audit, repurpose, schema, geo — never combined)
- Entry skill routes; sub-skills execute. Sub-skills MUST NOT know about the pipeline they live in.
- Heavy steps (>5 file reads or >2k token output) MUST be forked to Task subagents (architecture decision 3.4 / NFR-2.3) so context dies with the task

**Cross-cutting state:**
- All cross-skill state lives in the wiki, never in conversation memory or local scratch files (NFR-3.2, architecture decision 3.5)
- The wiki survives `/clear`, model swaps, and session resets — design every skill assuming a fresh context

## Security Conventions

- **No `.env` file** in the repo — credentials live in `README.md.txt` (WP Basic auth) or are injected via MCP server env
- Sensitive files are NOT in `.gitignore` by default — be deliberate about every `git add`
- Never commit Composio tokens, Vercel tokens, WP credentials, or OAuth `client_secret*.json`
- WordPress Basic auth lives in `README.md.txt` (intentionally outside `.env` flow) — flag any change that moves it
- All social outbound goes through Composio MCP; per-post explicit `YES` is required even on pre-approved channels

---

*Convention analysis: 2026-05-27*
