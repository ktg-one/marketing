# Codebase Structure

**Analysis Date:** 2026-05-27

## Directory Layout

```text
ktg-one/
├── wiki/                              # STATE LAYER — Karpathy LLM Wiki (Markdown vault)
├── .claude/                           # Claude Code config + plugin/skill ecosystem
│   ├── plugins/                       # Layer 2: 7 plugins, ~80 skills
│   └── skills/                        # Layer 3: project-local orchestrators (hub, wiki-ingest, …)
├── .agents/                           # Agent-scoped skills (60+ community + custom)
│   └── skills/
├── pipeline/                          # Layer 4: runtime — bash + Python + publish-kits
│   ├── run.sh                         #   stable 2s production path
│   ├── ktg_pipeline/                  #   Python AI orchestrator (~70% untested)
│   └── publish-kit/<slug>/            #   per-post 8-file output bundles (review-gate input)
├── .planning/                         # GSD methodology: roadmap, requirements, audits, research
│   └── codebase/                      #   this analysis pack
├── sccd/                              # Self-Consciousness-Choice-Decide functional model
├── blog/                              # Long-form drafts + battle-of-the-bots subprojects
├── videography/                       # Team-LLM animated series production
├── design/                            # Brand design assets and reference material
├── notebooklm-infographic-designs/    # Static-site template (NotebookLM infographics)
├── notebooklm-slide-templates/        # 14 Korean slide templates (NotebookLM)
├── awesome-notebookLM-prompts/        # NotebookLM prompt template repo (vendored)
├── awesome-notebooklm-prompts-raprealai/ # Alt NotebookLM prompt template repo (vendored)
├── data/                              # Runtime data stores (state_store.db/, stream_store/)
├── .raw/                              # Raw article sources awaiting wiki ingestion
├── .understand-anything/              # Auto-generated codebase knowledge graph (read-only)
├── .kimi/                             # Kimi CLI configuration (minimal)
├── .antigravitycli/                   # Antigravity CLI config (minimal)
├── AGENTS.md                          # AUTHORITATIVE big-doc for AI agents
├── CLAUDE.md                          # Human-readable architecture + behavioral guidelines
├── PROJECT_STATE.md                   # Current pipeline status (what works, what's untested)
├── README.md                          # Empty by design — human docs live in CLAUDE.md
├── README.md.txt                      # MCP config fragment — holds WP Basic auth (do not commit)
├── main.py                            # Python stub (prints "Hello from ktg-one!")
├── pyproject.toml                     # Python project metadata (kimi-cli, tool)
├── uv.lock                            # Locked Python deps
├── skills-lock.json                   # Skill integrity hashes (~400 entries)
└── .python-version                    # uv-managed Python version pin
```

Excluded from this map (noise / generated / out-of-scope):
`.venv/`, `D:packagesnpm/`, `iii console/`, `in-memoria.db`, `new 5.txt`, `STATE.txt`, `.git/`.

## Directory Purposes

**`wiki/` — STATE (Layer 1):**
- Purpose: Persistent project memory. The Karpathy LLM Wiki Pattern — load INTO model context before doing work.
- Contains: Obsidian-flavoured Markdown with wikilinks and YAML frontmatter.
- Key files: `wiki/hot.md` (≤500-tok continuity cache), `wiki/index.md` (master catalog), `wiki/log.md` (append-only ops log), `wiki/modules/index.md` (plugin ecosystem map), `wiki/modules/pipeline-signals.md` (sequential + parallel pipeline shapes), `wiki/voice/myth-hilarity-tech-anthropology.md` (locked house voice), `wiki/voice/cast/` (locked LLM character canon), `wiki/content/<slug>/` (per-post campaigns).

**`.claude/plugins/` — PLUGINS (Layer 2):**
- Purpose: Domain toolkits. Capability surface area.
- Contains: 7 plugins, ~80 skills total.
- Key subdirs: `banana-claude/` (image engine — sole image producer, hard dep for ads, soft dep for blog/seo/canvas), `claude-blog-main/` (22 blog skills: write, repurpose, geo, seo-check, schema, strategy), `claude-ads/` (22 ad skills: Google/Meta/LinkedIn/TikTok/YouTube/Amazon), `claude-seo/` (25 SEO skills: audit, geo, schema, technical, cluster, briefs), `claude-canvas/` (8 canvas skills), `best-practices-main/`, `wordpress-mcp-ultimate/` (WordPress gateway → `https://ktg.one/wp-json/mcp/wp-mcp-ultimate`).

**`.claude/skills/` — ORCHESTRATION (Layer 3, project-local):**
- Purpose: Compose plugin skills into end-to-end pipelines.
- Contains: top-level orchestrators discovered as `/commands` in the CLI host.
- Key skills: `hub/` (→ `/hub <slug>`, the top-level multi-plugin orchestrator), `wiki-ingest/`, `banana/`, `canvas/`, plus the `/wiki`, `/wiki-query`, `/wiki-lint` family.

**`.agents/skills/` — ORCHESTRATION (Layer 3, agent-scoped):**
- Purpose: Community + custom skills usable by named agents (per `CLAUDE.md` SendMessage coordination model).
- Contains: 60+ skills (`next-best-practices`, `copywriting`, `council`, etc.).
- Key files: each skill is its own `<name>/SKILL.md`.

**`pipeline/` — RUNTIME (Layer 4):**
- Purpose: The only "real code" in the traditional sense — mechanical pipeline execution + publish-kit assembly.
- Contains: `run.sh` (stable 2-second bash production path), `ktg_pipeline/` (Python AI orchestrator, ~70% untested per `PROJECT_STATE.md`), `publish-kit/<slug>/` (8-file per-post output bundles ready for the Review Gate).
- Key files: `pipeline/run.sh`, `pipeline/ktg_pipeline/*.py`, `pipeline/publish-kit/<slug>/{post.md, social-*.md, hero.png, schema.json, publish-checklist.md}`.

**`.planning/` — GSD METHODOLOGY (cross-cutting):**
- Purpose: Project management without traditional CI. Roadmap, requirements, phase verification criteria.
- Contains: `PROJECT.md` (scope + decisions), `ROADMAP.md` (6-phase sequential roadmap with verification criteria instead of tests), `REQUIREMENTS.md`, `config.json` (GSD mode + parallelization), `research/` (research artifacts), `codebase/` (this analysis pack — `ARCHITECTURE.md`, `STRUCTURE.md`, future `STACK.md`/`CONVENTIONS.md`/etc.).

**`sccd/` — THEORETICAL MODEL LAYER:**
- Purpose: Self-Consciousness-Choice-Decide functional model. ~1,600 lines of math + Python + insights. Provides the theoretical scaffold cited by `CLAUDE.md` self-token and downstream agent design.
- Contains: math derivations, Python reference implementation, flow/install/use-case guides.

**`blog/` — CONTENT PRODUCTION (long-form):**
- Purpose: Long-form writing pipeline (Reddit/Medium) and "Battle of the Bots" series.
- Contains: `posted/` (published archive), `assets/`, `WRITING.md-main/` (rulesets and voice docs), `*.md` drafts, `battlle-of-the-bots/round-N/` (per-round self-contained mini-sites — **the only directories with executable scripts**: `deploy.sh` runs `gh repo create` and publishes a public repo; confirm before running).

**`videography/` — CONTENT PRODUCTION (Team-LLM series):**
- Purpose: Animated series production. Locked cast canon.
- Contains: `-<character>/` sprite folders (leading `-` is intentional Obsidian sort-order), `-media/`, `-together/` (ensemble assets), `Episodes--<TITLE>.md` scripts, `TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md` (canon source of truth), `PROMPT-ZONE-OVERVIEW.md`, `PROMPT-ZONE-STATUS.md`.

**`design/` — CONTENT PRODUCTION (brand assets):**
- Purpose: Design artifacts and reference material for the KTG brand.

**`notebooklm-infographic-designs/`, `notebooklm-slide-templates/` — TEMPLATE REPOS:**
- Purpose: Static-site / slide-template scaffolds for NotebookLM-driven outputs. Self-contained vendored repos; treat as read-only inputs unless actively editing.
- Contains: HTML/CSS/JS for infographics; 14 Korean slide design templates.

**`awesome-notebookLM-prompts/`, `awesome-notebooklm-prompts-raprealai/` — VENDORED PROMPT LIBRARIES:**
- Purpose: Reference prompt template collections for NotebookLM. Vendored, read-mostly.

**`data/` — RUNTIME DATA STORES:**
- Purpose: Application state for runtime tooling (not the wiki — durable knowledge belongs in `wiki/`).
- Contains: `state_store.db/`, `stream_store/`.

**`.raw/` — INGESTION STAGING:**
- Purpose: Raw article sources awaiting processing by `/wiki-ingest`.
- Contains: `articles/`.

**`.understand-anything/` — AUTO-GENERATED:**
- Purpose: Codebase knowledge graph generated by tooling. Read-only output.

**`.kimi/`, `.antigravitycli/` — CLI CONFIGS:**
- Purpose: Per-CLI configuration for the multi-CLI roster. Minimal contents.

## Key File Locations

**Entry Points:**
- `/hub <slug>` → `.claude/skills/hub/SKILL.md`
- `/wiki`, `/wiki-ingest`, `/wiki-query`, `/wiki-lint` → `.claude/skills/wiki*/SKILL.md`
- `/banana`, `/canvas`, `/seo-audit`, `/ads`, `/blog` → `.claude/skills/<command>/SKILL.md` or `.claude/plugins/<plugin>/skills/...`
- `bash pipeline/run.sh <input.md>` → `pipeline/run.sh`
- `uv run main.py` → `main.py` (stub, not a real entry point)

**Configuration:**
- `.claude/config.json` — Claude Code permissions, MCP servers, theme; references MCP gateway at `D:\projects\.mcp\gateway.py`
- `pyproject.toml` — Python project metadata
- `uv.lock` — locked Python deps
- `.python-version` — Python version pin
- `skills-lock.json` — skill integrity hashes (~400 entries)
- `.planning/config.json` — GSD mode + parallelization + model profiles

**Authoritative Docs:**
- `AGENTS.md` — single source of truth for AI coding agents (takes precedence in conflict)
- `CLAUDE.md` — behavioral guidelines, architecture summary, MCP/publishing rules
- `PROJECT_STATE.md` — current pipeline status (what works, what's untested)
- `wiki/hot.md` — read FIRST every session
- `wiki/index.md` — master catalog
- `wiki/modules/index.md` — plugin ecosystem map (7 plugins · 79 skills · 40 agents)
- `wiki/modules/pipeline-signals.md` — pipeline shapes + cross-plugin dependency graph

**Core Logic:**
- Orchestration: `.claude/skills/hub/SKILL.md`
- Runtime: `pipeline/run.sh`, `pipeline/ktg_pipeline/`
- State engine: `wiki/` (Markdown — no code)

**Locked Canon (do not reinvent):**
- House voice: `wiki/voice/myth-hilarity-tech-anthropology.md`, `blog/user_voice.md`
- Cast canon: `wiki/voice/cast/`, `videography/TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md`
- LLM orchestration roster: `videography/PROMPT-ZONE-OVERVIEW.md`

**Sensitive (do NOT commit):**
- `README.md.txt` — WP Basic auth fragment
- `data/state_store.db/`, `data/stream_store/` — runtime stores
- Anything containing tokens for Composio routes

## Naming Conventions

**Files:**
- Markdown is the primary medium. YAML frontmatter required on every wiki page (`type`, `title`, `created`, `updated`, `tags`).
- Wikilinks `[[name]]` are valid Obsidian markdown — preserve on edit.
- Battle posts: `blog/battlle-of-the-bots/round-N/` (note: original misspelling "battlle" is intentional — do not "fix").
- Episode scripts: `videography/Episodes--<TITLE>.md` (double-dash separator).
- Posts: `POST-<title>.md` or descriptive slugs.

**Directories:**
- Leading `-` (e.g. `-Chat/`, `-claude/`, `-gem/`, `-media/`, `-together/`) — intentional Obsidian sort-order control. Keep on rename.
- `-main` suffix on a few plugin/skill dirs (e.g. `claude-blog-main`, `best-practices-main`, `WRITING.md-main`) — preserved historical naming.
- Per-post campaign dir: `wiki/content/<slug>/`.
- Per-post publish kit: `pipeline/publish-kit/<slug>/`.

**Skills:**
- `name: skill-name` in YAML frontmatter is the canonical handle.
- File path: `.claude/(plugins/<plugin>/)?skills/<name>/SKILL.md`.

## Where to Add New Code

**New content campaign (post / drop / launch):**
- Wiki state: `wiki/content/<slug>/` (canonical post + per-channel variants + `publish-checklist.md`).
- Runtime output: `pipeline/publish-kit/<slug>/` (produced by `pipeline/run.sh` — do not author by hand).
- Log: append to `wiki/log.md`; refresh `wiki/hot.md`.

**New skill:**
- Project-local orchestrator: `.claude/skills/<name>/SKILL.md`
- Plugin-scoped skill: `.claude/plugins/<plugin>/skills/<name>/SKILL.md`
- Agent-scoped skill: `.agents/skills/<name>/SKILL.md`
- Register in `wiki/modules/index.md` and (if it participates in a pipeline) `wiki/modules/pipeline-signals.md`.
- Keep entry SKILL.md under ~4k tokens loaded; push detail into `references/` invoked via the `Skill` tool.

**New plugin:**
- `.claude/plugins/<plugin>/` with one or more `skills/<skill>/SKILL.md`, optional `references/`, optional MCP server.
- Document cross-plugin dependencies in `wiki/modules/pipeline-signals.md` (hard vs soft).

**New runtime/pipeline logic:**
- Bash production path: edit `pipeline/run.sh` only if behavior change is required by an approved roadmap phase.
- Python AI runtime: `pipeline/ktg_pipeline/` (still hardening — see `PROJECT_STATE.md`).
- Never reach into `pipeline/publish-kit/<slug>/` from outside the runtime — those are immutable per-post outputs.

**New wiki source (idea / file / URL):**
- Stage raw in `.raw/articles/` then run `/wiki-ingest <file|url>`.
- Ingestion writes into `wiki/sources/`, extracts to `wiki/entities/`, `wiki/concepts/`, cross-references via wikilinks, updates `wiki/index.md`, appends `wiki/log.md`, refreshes `wiki/hot.md`.
- Never ingest without first loading existing wiki state — it breaks the graph.

**New planning artifact:**
- Roadmap phase: edit `.planning/ROADMAP.md`.
- Requirement: edit `.planning/REQUIREMENTS.md`.
- Research output: `.planning/research/`.
- Codebase analysis: `.planning/codebase/<NAME>.md`.

**New blog post (long-form, outside `/hub`):**
- Draft at `blog/<slug>.md` or `blog/POST-<title>.md`.
- Assets alongside the post — do NOT move to a central assets dir.
- For Battle of the Bots: `blog/battlle-of-the-bots/round-N/<NN>-<project>/` (self-contained mini-site with `index.html`, `style.css`, `app.js`, `dataset.json`, and `deploy.sh` — confirm before running `deploy.sh` since it creates a public GitHub repo).

**New episode / sprite:**
- Sprite: `videography/-<character>/` (matching character folder, preserve leading `-`).
- Episode: `videography/Episodes--<TITLE>.md`.
- Update `videography/PROMPT-ZONE-STATUS.md`.

**New design asset:** `design/` — direct drop, organize as needed for the brand.

**Utilities / shared helpers:** This project does not have a shared util layer. Resist the urge to invent one — most "utilities" should be skills, not code modules.

## Special Directories

**`.understand-anything/`:**
- Purpose: Auto-generated codebase knowledge graph.
- Generated: Yes.
- Committed: Treat as read-only; do not hand-edit.

**`.venv/`:**
- Purpose: uv-managed Python virtual environment.
- Generated: Yes.
- Committed: No (excluded from this map).

**`pipeline/publish-kit/<slug>/`:**
- Purpose: Immutable per-post output bundle. The artifact under review at the gate.
- Generated: Yes — by `pipeline/run.sh` or the Python AI runtime.
- Committed: Yes (acts as audit trail for what was published).

**`data/state_store.db/`, `data/stream_store/`:**
- Purpose: Runtime stores for tooling.
- Generated: Yes.
- Committed: Avoid — runtime state.

**`.raw/articles/`:**
- Purpose: Ingestion staging only. Files here are not canon until processed by `/wiki-ingest`.
- Generated: No (human-curated drops).
- Committed: Optional — the canonical form is the resulting `wiki/sources/` page.

**`blog/battlle-of-the-bots/round-N/<project>/`:**
- Purpose: Self-contained static mini-sites — the **only** directories with executable scripts in the repo.
- Generated: No (per-agent author).
- Committed: Yes.
- Side-effect warning: `deploy.sh` invokes `gh repo create` and publishes a public repo to the user's GitHub account. Confirm before running.

**`.archive/` (under `blog/`):**
- Purpose: Historical content, keep but don't touch unless asked.
- Committed: Yes.

---

*Structure analysis: 2026-05-27*
