<!-- refreshed: 2026-05-27 -->
# Architecture

**Analysis Date:** 2026-05-27

## System Overview

`ktg-one` is not a compiled application — it is an **agent-orchestrated content production system** whose runtime is an AI CLI (Claude Code / OpenCode / Gemini CLI / Codex / Kimi). The "binary" is a stack of Markdown skill files; the "database" is an Obsidian-style wiki. Five layers, strictly ordered, with state at the bottom and a non-bypassable human gate near the top.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│ LAYER 5 — PUBLISHING                                                        │
│   Vercel (deploy)  ·  Composio MCP (reddit/linkedin/gmail/discord/youtube)  │
│   wp-mcp-ultimate (WordPress gateway)                                       │
│   ⛔ Non-bypassable per-post REVIEW GATE                                    │
│      Gate state persisted in `wiki/` so it survives /clear and /loop        │
└──────────────────────────────▲──────────────────────────────────────────────┘
                               │ (only fires after explicit per-post YES)
┌──────────────────────────────┴──────────────────────────────────────────────┐
│ LAYER 4 — RUNTIME                                                           │
│   `pipeline/run.sh`         (2s bash, working production path)              │
│   `pipeline/ktg_pipeline/`  (Python AI orchestrator, ~70% untested)         │
│   `pipeline/publish-kit/<slug>/`  (8-file output package per post)          │
└──────────────────────────────▲──────────────────────────────────────────────┘
                               │ (skills shell out to runtime, or write kits)
┌──────────────────────────────┴──────────────────────────────────────────────┐
│ LAYER 3 — ORCHESTRATION (skills)                                            │
│   `.claude/skills/hub/`     →  `/hub <slug>`     (top-level orchestrator)   │
│   Per-domain sub-orchestrators:                                             │
│     `/blog`   `/ads`   `/seo`   `/canvas`   `/wiki`   `/wiki-ingest`        │
│   `.agents/skills/`          (60+ community + custom skills, agent-scoped)  │
└──────────────────────────────▲──────────────────────────────────────────────┘
                               │ (orchestrators dispatch into plugin skills)
┌──────────────────────────────┴──────────────────────────────────────────────┐
│ LAYER 2 — PLUGINS (`.claude/plugins/` — 7 plugins, ~80 skills)              │
│   claude-blog-main (22)  ·  claude-ads (22)  ·  claude-seo (25)             │
│   banana-claude (image engine)  ·  claude-canvas (8)                        │
│   best-practices-main  ·  wordpress-mcp-ultimate (WP gateway)               │
└──────────────────────────────▲──────────────────────────────────────────────┘
                               │ (every plugin reads wiki; many write back)
┌──────────────────────────────┴──────────────────────────────────────────────┐
│ LAYER 1 — STATE (`wiki/` — Karpathy LLM Wiki Pattern)                       │
│   `hot.md` (≤500 tok cache) → `index.md` (catalog) → `log.md` (append-only) │
│   `sources/` `entities/` `concepts/` `intel/` `playbooks/` `modules/`       │
│   `content/<slug>/` (per-post campaign dirs — canonical persistence)        │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| Wiki state | Persistent knowledge graph; survives `/clear`; load-bearing for every agent invocation | `wiki/` |
| Hot cache | <500-token rolling continuity packet read at session start | `wiki/hot.md` |
| Vault catalog | Master index of every wiki page (read after `hot.md`) | `wiki/index.md` |
| Activity log | Append-only chronological operations log | `wiki/log.md` |
| Plugin registry | Map of 7 plugins, ~80 skills, 40 agents | `wiki/modules/index.md` |
| Pipeline shape map | Sequential + parallel dependency diagrams across plugins | `wiki/modules/pipeline-signals.md` |
| Top-level orchestrator | `/hub <slug>` — fans out across blog/ads/seo/banana/wp | `.claude/skills/hub/SKILL.md` |
| Image engine | Gemini Nano Banana — sole image producer for ads/blog/seo/canvas | `.claude/plugins/banana-claude/` |
| WordPress gateway | MCP server bridging skills to `ktg.one/wp-json/...` | `.claude/plugins/wordpress-mcp-ultimate/` |
| Production runtime (stable) | 2-second bash pipeline that builds 8-file publish-kits | `pipeline/run.sh` |
| Production runtime (AI) | Python AI orchestrator, partially exercised | `pipeline/ktg_pipeline/` |
| Publish kits | Frozen, per-post output bundle ready for review gate | `pipeline/publish-kit/<slug>/` |
| GSD methodology | 6-phase roadmap, requirements, phase verification criteria (no automated tests) | `.planning/` |
| SCCD model | Functional Self-Consciousness-Choice-Decide model (~1.6k lines math + Python + insights) | `sccd/` |
| Canonical agent doc | Single source of truth for AI coding agents (authoritative when in conflict) | `AGENTS.md` |
| Human onboarding | Behavioral guidelines and architecture summary | `CLAUDE.md` |

## Pattern Overview

**Overall:** Five-layer agent-orchestrated content pipeline anchored on the **Karpathy LLM Wiki Pattern** — agents that don't load the wiki have no user context, so reading wiki state INTO the model is load-bearing, not optional.

**Key Characteristics:**
- State is Markdown in `wiki/`, not a database. Persistence == git + filesystem.
- Skills are Markdown files with YAML frontmatter discovered by the CLI host. There is no compile step.
- Cross-plugin coupling happens through (a) the wiki, (b) shared MCP servers (banana, wp), and (c) `pipeline/publish-kit/<slug>/` artifacts — never direct skill-to-skill calls.
- Every publish path terminates in a **non-bypassable Review Gate** whose state is persisted to the wiki so even `/loop`, scheduled runners, or fresh sessions cannot bypass it.
- Quality is enforced by **phase verification criteria** in `.planning/ROADMAP.md` plus `/wiki-lint`, not by `pytest`/`jest`/CI.

## Layers

**Layer 1 — State (`wiki/`):**
- Purpose: Single source of project truth. Knowledge graph + rolling hot cache + append-only log.
- Location: `wiki/`
- Contains: Obsidian-flavoured Markdown with wikilinks, YAML frontmatter, tags.
- Depends on: nothing (it IS the dependency).
- Used by: every layer above. No skill should run without loading `wiki/hot.md` and the relevant `wiki/modules/*` entries.

**Layer 2 — Plugins (`.claude/plugins/`):**
- Purpose: Domain-specific operational toolkits. The capability surface area.
- Location: `.claude/plugins/<plugin>/skills/<skill>/SKILL.md`
- Contains: 7 plugins, ~80 skills total. Two cross-cutting plugins (`banana-claude`, `wordpress-mcp-ultimate`) act as service buses.
- Depends on: wiki (read), MCP servers (banana for images, wp-mcp for WordPress, gateway at `D:\projects\.mcp\gateway.py`).
- Used by: Layer 3 orchestrators.

**Layer 3 — Orchestration (skills):**
- Purpose: Compose plugin skills into end-to-end pipelines. Decide what runs when.
- Location: `.claude/skills/` (project-local: `hub/`, `wiki-ingest/`, `banana/`, `canvas/`, etc.) and `.agents/skills/` (60+ community + custom, agent-scoped).
- Contains: SKILL.md entry files (must stay <~4k tokens loaded), references/ loaded on-demand.
- Depends on: Layer 2 plugins.
- Used by: User commands (`/hub`, `/blog`, `/ads`, `/seo`, `/wiki`, `/canvas`, `/banana`).

**Layer 4 — Runtime (`pipeline/`):**
- Purpose: Mechanical pipeline execution. Build publish-kits. The only "code" in the traditional sense.
- Location: `pipeline/run.sh` (production), `pipeline/ktg_pipeline/` (Python AI), `pipeline/publish-kit/<slug>/` (output bundles).
- Contains: Bash that produces an 8-file kit in ~2s; Python AI orchestrator (~70% untested per `PROJECT_STATE.md`).
- Depends on: wiki content (input), `.claude/plugins/banana-claude` and `.claude/plugins/wordpress-mcp-ultimate` via MCP.
- Used by: Layer 3 orchestrators (`/hub` shells into `pipeline/run.sh`), Layer 5 publishers (read finished kits).

**Layer 5 — Publishing:**
- Purpose: Move approved content to the world. Always gated.
- Location: Composio MCP routes (reddit/linkedin/vercel/gmail/discord/youtube/facebook/googledrive), `wp-mcp-ultimate`, Vercel.
- Contains: No project files — pure external service surface.
- Depends on: a YES from the human at the Review Gate (state stored in wiki).
- Used by: nothing downstream — terminal layer.

## Data Flow

### Primary Request Path — Idea → Publish

1. **Idea ingress** — user drops a source via `/wiki-ingest <file|url>` (`.claude/skills/wiki-ingest/SKILL.md`).
2. **Wiki state update** — entities/concepts extracted, cross-referenced into `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`; `wiki/index.md` updated; `wiki/log.md` appended; `wiki/hot.md` refreshed.
3. **Campaign init** — user runs `/hub <slug>` (`.claude/skills/hub/SKILL.md`); orchestrator loads `wiki/hot.md` + `wiki/modules/pipeline-signals.md` to decide plugin routing.
4. **Sub-orchestrator dispatch** — `/hub` invokes `/blog`, `/ads`, `/seo`, `/banana` in the shape defined by `wiki/modules/pipeline-signals.md`.
5. **Plugin execution** — sequential creative chain (`brief → outline → write`) with parallel branches (`factcheck` + `image` via `banana-claude`) at the write step, then `seo-check → schema → geo → repurpose`.
6. **Kit assembly** — `pipeline/run.sh` (or AI runtime) writes an 8-file `pipeline/publish-kit/<slug>/` bundle (post + 4 social variants + hero + crops + schema + checklist).
7. **REVIEW GATE** — gate state written to `wiki/`; runtime stops; pipeline awaits per-post YES. No session-wide blanket approval is allowed.
8. **Publishing** — on YES: Vercel deploy → capture canonical URL → URL substituted into social variants → Composio fires `reddit` + `linkedin` (+ others per policy) → WP via `wp-mcp-ultimate` if applicable.
9. **Log close-out** — publish event appended to `wiki/log.md`; `wiki/hot.md` cache rotated.

### Secondary Flow — SEO Audit

1. `/seo-audit <url>` → detect business type.
2. Spawn 8+ specialist agents in parallel via Task tool with `context: fork` (technical / content / schema / sitemap / performance / visual / geo + conditional google/local/maps/backlinks/cluster/ecommerce/drift/sxo).
3. Each agent emits validated JSON scores.
4. Aggregate → SEO Health Score (0-100) → prioritized action plan (Critical → High → Medium → Low).
5. Optional PDF report; findings written back to `wiki/intel/`.

### Secondary Flow — Image Generation

1. `/banana <prompt>` or upstream skill calls into `banana-claude`.
2. Banana is the **sole image producer** for ads/blog/seo/canvas — hard dependency for `ads-generate`, `ads-photoshoot`, `ads/visual-designer`; soft (graceful-fallback) for `blog-image`, `seo-image-gen`, `canvas-generate`.
3. Output written under the consuming plugin's working dir (e.g. `pipeline/publish-kit/<slug>/hero.png`).

**State Management:**
- All durable state lives in `wiki/` as Markdown. The wiki survives `/clear`, model swaps, and CLI host swaps.
- Runtime state (publish kits) lives in `pipeline/publish-kit/<slug>/` and is the artifact under review at the gate.
- Conversation memory is treated as ephemeral. Anything that must outlive a session is written to `wiki/`.
- The Review Gate's "open / pending / approved" status is itself persisted in `wiki/` so it cannot be lost by `/clear`.

## Key Abstractions

**Karpathy LLM Wiki Pattern:**
- Purpose: A Markdown wiki used as durable LLM working memory; entities/concepts/sources cross-reference via wikilinks; new sources are ingested only after existing state is loaded (or the graph breaks).
- Examples: `wiki/hot.md`, `wiki/index.md`, `wiki/log.md`, `wiki/entities/`, `wiki/concepts/`, `wiki/sources/`.
- Pattern: load → ingest → cross-link → cache → log.

**Plugin:**
- Purpose: A self-contained domain toolkit (blog, ads, seo, canvas, image, WP gateway).
- Examples: `.claude/plugins/claude-blog-main/`, `.claude/plugins/claude-ads/`, `.claude/plugins/banana-claude/`.
- Pattern: directory with one or more `skills/<name>/SKILL.md` plus `references/` and assets. Discovered by CLI host via skill registry.

**Skill (orchestrator vs leaf):**
- Purpose: Single addressable unit of agent behavior, discovered via `/command-name`.
- Examples: `.claude/skills/hub/SKILL.md` (orchestrator), `.claude/plugins/claude-blog-main/skills/seo-check/SKILL.md` (leaf).
- Pattern: YAML frontmatter (`name`, `description`, `user-invokable`, `argument-hint`) + Markdown body; progressive disclosure — entry SKILL.md must be <~4k tokens loaded; deeper files invoked only via the `Skill` tool, never via `Read`.

**Publish Kit:**
- Purpose: Frozen 8-file bundle that represents the reviewable artifact for one post.
- Examples: `pipeline/publish-kit/<slug>/{post.md, social-reddit.md, social-linkedin.md, social-x-thread.md, social-medium.md, hero.png, schema.json, publish-checklist.md}`.
- Pattern: produced by `pipeline/run.sh` or AI runtime; consumed by Review Gate, then by Composio publishers.

**Review Gate:**
- Purpose: Mandatory human checkpoint between Layer 4 and Layer 5.
- Examples: state persisted in `wiki/` (no in-memory gate state), runtime blocks until YES.
- Pattern: per-post approval only — no session-wide YES; survives `/clear`, `/loop`, and scheduled autonomous runners by design.

## Entry Points

**`/hub <slug>` — top-level orchestrator:**
- Location: `.claude/skills/hub/SKILL.md`
- Triggers: user command in CLI host (Claude Code / OpenCode / Gemini CLI).
- Responsibilities: load wiki context → route through blog/ads/seo/banana pipelines → assemble publish-kit → halt at Review Gate.

**`/wiki`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint`, `/canvas`, `/banana`, `/seo-audit`, `/ads`:**
- Location: `.claude/skills/<command>/SKILL.md` and `.claude/plugins/<plugin>/skills/...`
- Triggers: direct user invocation.
- Responsibilities: domain-specific entry points; each loads wiki state first, then dispatches.

**`bash pipeline/run.sh <input.md>`:**
- Location: `pipeline/run.sh`
- Triggers: shelled out from `/hub` or run manually.
- Responsibilities: produce 8-file publish-kit in ~2s. The proven path while `pipeline/ktg_pipeline/` (AI runtime) is still being hardened.

**`uv run main.py`:**
- Location: `main.py`
- Triggers: rarely — Python stub that prints "Hello from ktg-one!".
- Responsibilities: keep `pyproject.toml` honest. Not a real entry point.

## Architectural Constraints

- **Platform:** Windows / PowerShell. Shell commands must use PowerShell syntax (`$null`, `$env:VAR`, backtick continuation). Bash is available via the Bash tool for POSIX scripts.
- **No test suite:** No pytest, no jest, no CI. Quality gates are phase verification criteria in `.planning/ROADMAP.md` + `/wiki-lint` for state integrity + voice audit against `[[user-voice]]`.
- **No n8n at runtime:** n8n is wired but `list_workflows` auth is flaky — Composio is the default publishing route.
- **MCP gateway is shared infrastructure:** all MCP calls funnel through `D:\projects\.mcp\gateway.py` (referenced from `.claude/config.json`). Do not modify without understanding downstream effects.
- **Skill token budget:** orchestrator SKILL.md files must stay under ~4k tokens after loading. Use progressive disclosure (`references/` loaded only when invoked via the `Skill` tool, never via `Read`).
- **Sensitive files:** `README.md.txt` holds WP Basic auth (NOT a `.env`). No `.env` is present. Be careful what is committed.
- **Cross-plugin coupling:** plugins do not call each other directly. They coordinate through (a) the wiki, (b) MCP services (banana, wp-mcp), and (c) publish-kit artifacts.
- **Wiki edits must preserve wikilinks** (`[[name]]`) and Obsidian sort-order filename prefixes (leading `-`).

## Anti-Patterns

### Skipping the wiki load on a new session

**What happens:** Agent answers questions or starts work without first reading `wiki/hot.md`, `wiki/index.md`, and the relevant `wiki/modules/*` entries.
**Why it's wrong:** This project's entire persistence model is the Karpathy LLM Wiki Pattern. An agent without the wiki has no user context, will hallucinate canon (cast, voice, palettes), and will desync the knowledge graph if it then ingests new sources.
**Do this instead:** Always read `wiki/hot.md` → `wiki/index.md` → relevant module pages before performing work. See `AGENTS.md` §9 "Key Files for Agent Onboarding".

### Reading SKILL.md files with the `Read` tool

**What happens:** Agent uses `Read` on `.claude/skills/<x>/SKILL.md` or `.claude/plugins/.../SKILL.md` to inspect a skill.
**Why it's wrong:** Blows the orchestrator token budget (>4k loaded), defeats progressive disclosure, and bypasses the skill registry's discovery semantics.
**Do this instead:** Invoke via the `Skill` tool (or the `/command` form). Reserve `Read` for non-skill source files.

### Bypassing the Review Gate

**What happens:** A `/loop`, scheduled runner, or "all variants pre-approved" shortcut fires a publish without per-post YES.
**Why it's wrong:** The channel list is permission to use the *route*, not permission to *post*. Gate state lives in `wiki/` precisely so that no session/loop/script can short-circuit it.
**Do this instead:** Stop at the gate. Ask for per-post YES. Honour STOP. See `AGENTS.md` §7 "Review Gate Security".

### Direct skill-to-skill calls

**What happens:** A skill tries to call another skill's internals directly instead of going through the orchestrator or the documented dependency surface.
**Why it's wrong:** Skills cannot reliably call each other (`.planning/PROJECT.md` Constraints). Hidden coupling breaks the publish-kit contract and bypasses pipeline-signals routing.
**Do this instead:** Use the `Skill` tool, CLI delegation, or coordinate through shared artifacts (wiki state, publish-kit files, MCP services). Document the dependency in `wiki/modules/pipeline-signals.md`.

### Moving heavy assets into a central `assets/` dir

**What happens:** Refactor consolidates PDFs/MP4/ZIPs/multi-MB PNGs into a shared assets folder.
**Why it's wrong:** Project convention is that heavy assets live alongside the post they support, so the post stays self-contained when archived/forked.
**Do this instead:** Leave assets next to their consuming post (e.g. inside `wiki/content/<slug>/` or the matching `blog/` subdir).

### Renaming files to drop the leading `-`

**What happens:** "Cleanup" renames `-Chat/`, `-claude/`, `Episodes--*.md` etc. to remove the leading dash.
**Why it's wrong:** The leading `-` is intentional Obsidian sort-order control. Renaming breaks vault navigation and any existing wikilinks.
**Do this instead:** Preserve the prefix on rename. Update wikilinks atomically when a rename is unavoidable.

## Error Handling

**Strategy:** Soft-failure with graceful degradation, because the system is interactive and human-supervised.

**Patterns:**
- **Image generation:** hard dependency on `banana-claude` for ads; soft (with explicit fallback message) for blog/seo/canvas.
- **MCP transport failures:** surfaced to the user — no silent retries that would mask credential or gateway issues.
- **Wiki integrity errors:** `/wiki-lint` runs proactively after edits; reports orphans, dead links, and frontmatter gaps rather than auto-fixing.
- **Publish failures:** post-publish errors are appended to `wiki/log.md` and the publish-kit is left in place for retry.

## Cross-Cutting Concerns

**Logging:** Append-only to `wiki/log.md`. Significant pipeline runs and publish events MUST log.
**Validation:** `/wiki-lint` for state integrity, JSON-LD validation in the `seo-schema` skill, voice audit against `[[user-voice]]` for drafts.
**Authentication:** WP Basic auth in `README.md.txt`. Composio handles its own connection auth. MCP gateway at `D:\projects\.mcp\gateway.py` proxies all MCP tool calls — single chokepoint for credential review.
**Voice & canon:** "Myth-Hilarity + Tech Anthropology" is locked. Cast visuals/palettes/personality flaws are locked. Sources of truth: `wiki/voice/myth-hilarity-tech-anthropology.md`, `wiki/voice/cast/`, `videography/TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md`. Do not reinvent.
**Multi-CLI orchestration:** Claude = spine, Gemini = research, Codex = mechanical execution, Jules = async; KIMI/Qwen for second opinions. See `~/.claude/rules/ai-orchestration.md`.

---

*Architecture analysis: 2026-05-27*
