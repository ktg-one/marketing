# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

**ktg-one** is not a traditional software repo. It is an agent-orchestrated content creation hub for the Good AI / KTG brand. The "code" is skill orchestration + wiki state + pipeline scripts — not a compiled application. Personal workspace of Kevin Tan (`goodai.au`). Content voice: **Myth-Hilarity + Tech Anthropology** (locked — see `wiki/voice/myth-hilarity-tech-anthropology.md`).

## Read first, every session

0. **`wiki/meta/agent-trust-state.md`** — **mandatory.** The trust contract with Kevin. Check the `status:` field before doing anything. If it says `probation` or `wipe-pending`, you are not at a normal trust baseline.
1. `wiki/hot.md` — rolling ~500-token context cache (active threads, recent deltas)
2. `wiki/index.md` — master catalog of every wiki page
3. `AGENTS.md` — authoritative big-doc (~300 lines, declared canonical when in conflict with this file)
4. `PROJECT_STATE.md` — current pipeline status (what works, what's untested)
5. `wiki/modules/index.md` — plugin ecosystem map (7 plugins; registry claims differ from disk — see Skill/agent inventory below)

**Karpathy LLM Wiki Pattern (canon):** agents that don't load the wiki have no user context. Reading the wiki INTO context is load-bearing, not optional.

**No-babysitting protocol:** resolve ambiguity from project docs before asking. Multi-option `AskUserQuestion` blocks are the relapse signal. Terse corrections mean "go figure it out."

## Architecture — five layers

```
Layer 5  PUBLISHING       Vercel · Composio (Reddit/LinkedIn) · WordPress
                          ⛔ Non-bypassable per-post REVIEW GATE
─────────────────────────────────────────────────────────────────────────
Layer 4  RUNTIME          pipeline/run.sh (bash, working production)
                          pipeline/run.py + ktg_pipeline/ (Python AI orch, Google/Gemini-driven)
                          pipeline/swarm-run.py (parallel agent swarm variant)
                          pipeline/publish-kit/<slug>/ — 13 files per /hub run
                          pipeline/HUB-PIPELINE.md — the operations manual (read this)
─────────────────────────────────────────────────────────────────────────
Layer 3  ORCHESTRATION    .claude/skills/hub/  →  /hub <slug>
                          Per-domain sub-orchestrators: /blog /ads /seo /canvas
─────────────────────────────────────────────────────────────────────────
Layer 2  PLUGINS          .claude/plugins/ — 7 plugins
                          claude-blog · claude-seo · claude-ads
                          banana-claude (image engine) · claude-canvas
                          best-practices · wp-mcp-ultimate (WP gateway)
─────────────────────────────────────────────────────────────────────────
Layer 1  STATE (wiki/)    hot.md → index.md → sources/entities/concepts/
                          intel/ playbooks/ modules/ log.md (append-only)
```

Cross-cutting: `.planning/` (GSD methodology — 6-phase roadmap), `.agents/skills/` and `.claude/skills/` (skills), `.claude/agents/` + plugin agents (agents). See inventory below for on-disk counts.

### Skill / agent inventory (on-disk, verified this clone)

| What | Location | Count |
|---|---|---|
| Project skills | `.claude/skills/*/SKILL.md` | ~128 |
| Canonical skills | `.agents/skills/*/SKILL.md` | ~100 |
| Project agents | `.claude/agents/*.md` | 6 (brief-constructor, canvas-composer/layout/media, wiki-ingest, wiki-lint) |
| Plugin agents | `.claude/plugins/*/agents/*.md` | 4 |
| Plugins | `.claude/plugins/` | 7 |

> Older docs (`AGENTS.md`, `wiki/modules/index.md`, root `README.md`) cite "84 skills / 39–40 agents" — that's a registry/aspirational figure, not what's on disk. Trust `find` over the prose.

## Pipeline readiness state

| Layer | Status |
|-------|--------|
| `pipeline/run.sh` bash template | ✅ **Production-ready** — 2s, 8-file publish-kit, $0 |
| Wiki vault | ✅ **Usable** — 33 sources, 16 entities, 30 concepts |
| Skill registry | ✅ **Installed** — ~128 project + ~100 canonical skills; 6 project agents (+4 plugin) |
| `/hub` Phase 1.0 Foundation | ✅ **CLOSED** — campaign-brief.md template exists, wiki-ingest stable |
| `/hub` Phase 2.0–6.0 | ❌ **NOT VERIFIED** — skills wired but E2E untested |
| Python AI pipeline | 🚧 **70% built** — framework exists, LLM calls untested |
| Composio auto-post | 🚧 **Wired, not tested** — LinkedIn/Reddit routes active, no E2E run |
| Review Gate skill | 🚧 **Designed** — not implemented as discrete skill yet |
| X/Meta/Medium auto-post | ❌ **Impossible** — platform APIs block it |

**Current practical path:** `bash pipeline/run.sh <post.md>` → copy-paste publish. Use `/hub` for LLM-orchestrated drafting; expect manual steps at publish.

## Commands

| Command | Purpose |
|---|---|
| `bash pipeline/run.sh <input.md>` | ✅ Working production bash pipeline (fast, publish-kit, $0) |
| `uv run pipeline/run.py <post.md>` | Python AI orchestrator — drives Ollama for the /hub steps |
| `uv run pipeline/swarm-run.py <post.md>` | Parallel agent-swarm variant of the pipeline |
| `curl http://localhost:11434/api/tags` | Verify Ollama is up **before** /hub or run.py (text gen depends on it) |
| `uv sync` | Sync Python deps (run on every fresh clone) |
| `uv run main.py` | Python stub — does nothing meaningful |
| `/hub <slug>` | LLM-orchestrated content pipeline (blog + ads + image + SEO) |
| `/wiki` | Bootstrap or continue wiki session |
| `/wiki-ingest <file\|url>` | Add source, extract entities & concepts |
| `/wiki-query <topic>` | Synthesize answer from wiki state |
| `/wiki-lint` | Health check: orphans, dead links, frontmatter gaps |
| `/canvas` | Visual planning (12 archetypes) |
| `/banana <prompt>` | Image generation via Gemini Nano Banana |
| `/seo-audit <url>` | 8+ parallel SEO agents → Health Score 0–100 |
| `/ads dna <url>` | Brand profile JSON for ad generation |

**No `npm` / `pytest` / `make`.** Quality gates are pipeline verification criteria per phase in `.planning/ROADMAP.md`.

## Fresh clone / multi-machine setup

This repo is synced across machines via git. **`.claude/` and `.agents/` ARE committed** (900 + 504 tracked files) — skills/plugins/agents travel with the clone. What does **not** travel (gitignored) and must be rebuilt/re-set locally:

| Missing on fresh clone | Restore with |
|---|---|
| `.venv/` | `uv sync` |
| `.env*` (Gemini/xAI keys) | re-set `$env:GEMINI_API_KEY`, `$env:XAI_API_KEY` in shell profile |
| `.raw/` (raw article sources) | re-drop sources before `/wiki-ingest` |
| `data/` (state_store.db, stream_store) | regenerated at runtime |
| `*.png` (all hero/banana images) | regenerate via `/banana` or the hub image step |
| Ollama models (`Ministral:latest`, `Qwopus:latest`) | `ollama pull <model>`; confirm `ollama serve` is running |

If text generation fails on a new machine, the cause is almost always **Ollama not running** or a **missing model** — not the pipeline. ImageMagick is needed for crop variants (`winget install ImageMagick.ImageMagick`).

## Skill invocation rules (critical)

1. **Never `Read` skill files directly** — always invoke via `Skill` tool. Reading a skill file raw burns context without activating its logic.
2. **Orchestrator skills stay under ~4k tokens** after loading — use entry skill + on-demand sub-skill loading.
3. **Skill name = exact `name:` from YAML frontmatter** — no aliases. Scope is explicit: User (`.agents/skills/`) vs Project (`.claude/skills/`).
4. **For parallel work** — dispatch via `Agent` tool. Each agent loads its target skill via `Skill` tool independently.
5. **Progressive disclosure** — entry `SKILL.md` first; `references/` loaded on-demand by the invoked skill.

## Plugin pipeline shapes

Full diagrams: `wiki/modules/pipeline-signals.md`.

- **Blog** — `notebooklm → brief → outline → write` with **parallel** factcheck + image at write step, then `seo-check → schema → geo → repurpose`.
- **SEO audit** — 8+ specialist agents in parallel → aggregated Health Score (0–100) → prioritized action plan.
- **Ads** — `dna → create → generate`, `photoshoot` as branch.
- **Canvas** — `create → populate → layout → export`, or `/generate <desc>` for full AI orchestration.
- **Hub orchestrator** — `campaign-brief.md` is the Phase 1→2 handoff artifact. Template: `wiki/templates/campaign-brief.md`.

## LLM routing — Google-first

The engine is **Google (Gemini)**, not local models. `GEMINI_API_KEY` drives the whole stack; config lives in `pipeline/config.yaml`.

| Task | Model |
|---|---|
| Repurpose / SEO / GEO / schema (workhorse) | `gemini-3.5-flash` |
| Hero draft / hard reasoning | `gemini-3-pro-preview` |
| Hero + crops (Nano Banana) | `gemini-3.1-flash-image-preview` / `nano-banana-pro-preview` |
| Research / grounding | `deep-research-pro-preview`, NotebookLM |
| Episode audio (videography/) | `gemini-2.5-flash-tts`, `lyria-3-pro-preview` |

Ollama/LM Studio remain in `config.yaml` as **offline fallback only** — the pipeline does not depend on them. Override per-run with `--provider ollama`. Cost: Flash ≈ fractions of a cent/post, Pro a few cents.

**Voice guard:** cloud models default to generic register. Inject `blog/user_voice.md` (Myth-Hilarity) into every generation prompt, and keep the non-bypassable review gate — quality means nothing if it sounds like every other AI blog.

## Publishing & security

- Composio MCP routes: `reddit`, `linkedin`, `vercel`, `gmail`, `discord`, `slack`, `youtube`, `facebook`, `googledrive`.
- **Always get explicit per-post green-light before firing any social send**, even on pre-approved channels. Channel list ≠ publish permission.
- **Credentials:** WP Basic auth in `README.md.txt` (NOT `.env`). MCP gateway at `D:\projects\.mcp\gateway.py`.
- **Review Gate is non-bypassable** — even `/loop` and scheduled runners must stop. Gate state written to wiki (survives `/clear`). Per-post `YES` required — no session-wide blanket approval.

## Working conventions

- Obsidian-flavoured markdown — wikilinks `[[name]]` are valid and must be preserved on edit.
- Filenames starting with `-` control Obsidian sort order — keep the prefix on rename.
- Battle posts and episode briefs use heavy emoji + headed sections — intentional KTG style, not noise to clean up.
- `blog/battlle-of-the-bots/round-N/` battle sub-projects are the **only** dirs with executable scripts (`deploy.sh` runs `gh repo create` and publishes a public repo — confirm before running).
- Hot cache (`wiki/hot.md`) must stay under ~500 tokens — update at session end.

## Locked canon (do not reinvent)

- **Cast** (GPT, Claude, Gemini, DeepSeek, Kimi, Perplexity, Qwen, Grok, Outliers, User-Narrator, Prompt-God) — sprites, palettes, voice direction, personality flaws. Source: `videography/TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md` + `wiki/voice/cast/`.
- **House voice:** "Myth-Hilarity + Tech Systems mixed with Anthropology" — full spec in `blog/user_voice.md` and `wiki/voice/myth-hilarity-tech-anthropology.md`.
- **Copyright evasion:** chibi designs, shape language, palettes — **never logos**.

## Other top-level dirs (not in the 5-layer map)

- `videography/` — Team-LLM production bibles, episode scripts, the **Cast canon source** (see Locked canon).
- `sccd/` — SCCD-Model: `code/ guide/ insights/ math/`. Shipped by Kimi/DeepSeek (~1,608 lines); the SCCD ↔ wiki theorem treats `wiki/` as the agent-layer substrate.
- `notebooklm-slide-templates/`, `notebooklm-infographic-designs/`, `awesome-notebookLM-prompts*/` — NotebookLM design/prompt asset libraries.
- `blog/` — content workspace; `blog/battlle-of-the-bots/round-N/` are the **only** dirs with executable deploy scripts.
- `iii console/` — small console asset set.

## Sister projects (outside this vault)

- `C:/Users/kevin/knowledge2026/` — parent wiki vault (separate repo).
- `C:/Users/kevin/Desktop/ktg-one/` and `C:/Users/kevin/projects2026/06-projects-code/goodai-mate/` — Next.js sites (separate build systems).
