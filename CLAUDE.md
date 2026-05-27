# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

**ktg-one** is not a traditional software repo. It is an agent-orchestrated content creation hub for the Good AI / KTG brand. The "code" is skill orchestration + wiki state + pipeline scripts — not a compiled application. Personal workspace of Kevin Tan (`goodai.au`). Content voice: **Myth-Hilarity + Tech Anthropology** (locked — see `wiki/voice/myth-hilarity-tech-anthropology.md`).

## Read first, every session

0. **`wiki/meta/agent-trust-state.md`** — **mandatory.** The trust contract with Kevin. Check the `status:` field before doing anything. If it says `probation` or `wipe-pending`, you are not at a normal trust baseline. The file documents what behaviors earn trust back and what relapses are.
1. `wiki/hot.md` — rolling ~500-token context cache (active threads, recent deltas)
2. `wiki/index.md` — master catalog of every wiki page
3. `AGENTS.md` — authoritative big-doc (~300 lines, declared canonical when in conflict with this file)
4. `PROJECT_STATE.md` — current pipeline status (what works, what's untested)
5. `wiki/modules/index.md` — plugin ecosystem map (7 plugins · 79 skills · 40 agents)

**Karpathy LLM Wiki Pattern (canon):** agents that don't load the wiki have no user context. Reading the wiki INTO context is load-bearing, not optional. Ingesting new sources without first loading existing state breaks the graph.

**No-babysitting protocol (from `agent-trust-state.md`):** resolve ambiguity from project docs before asking. Multi-option `AskUserQuestion` blocks are the relapse signal. Terse user corrections mean "go figure it out", not "give me more dropdowns."

## Architecture — five layers

```
Layer 5  PUBLISHING       Vercel · Composio (Reddit/LinkedIn) · WordPress
                          ⛔ Non-bypassable per-post REVIEW GATE
                             (state lives in wiki, survives /clear)
─────────────────────────────────────────────────────────────────────────
Layer 4  RUNTIME          pipeline/run.sh (2s bash, working production)
                          pipeline/ktg_pipeline/ (Python AI, ~70% untested)
                          pipeline/publish-kit/<slug>/ — 8 files per post
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

Cross-cutting: `.planning/` (GSD methodology — 6-phase roadmap, no automated tests, phase verification criteria instead), `sccd/` (Self-Consciousness-Choice-Decide functional model, ~1,600 lines of math + Python + insights), multi-CLI roster (`~/.claude/rules/ai-orchestration.md`).

## Commands

| Command | Purpose |
|---|---|
| `bash pipeline/run.sh <input.md>` | Working production pipeline (2s, produces 8-file publish-kit) |
| `uv sync` / `uv run main.py` | Python deps (minimal — `main.py` is a stub) |
| `/hub <slug>` | Full LLM-orchestrated content pipeline (blog + ads + image + SEO) |
| `/wiki` | Bootstrap or continue wiki session |
| `/wiki-ingest <file\|url>` | Add source, extract entities & concepts, cross-reference into graph |
| `/wiki-query <topic>` | Synthesize answer from accumulated wiki state |
| `/wiki-lint` | Health check: orphans, dead links, frontmatter gaps |
| `/canvas` | Visual planning (12 archetypes) |
| `/banana <prompt>` | Image generation via Gemini Nano Banana |
| `/seo-audit <url>` | 8+ parallel SEO agents → Health Score 0-100 |
| `/ads dna <url>` | Brand profile JSON for ad generation |

**No `npm` / `pytest` / `make`.** Quality gates are pipeline verification criteria per phase in `.planning/ROADMAP.md`, plus `/wiki-lint` for state integrity and voice audit against `[[user-voice]]`.

## Plugin pipeline shapes

Full diagrams in `wiki/modules/pipeline-signals.md`. High level:

- **Blog** — sequential `brief → outline → write` with **parallel** factcheck + image at the write step, then `seo-check → schema → geo → repurpose`.
- **SEO audit** — 8+ specialist agents in parallel (technical/content/schema/sitemap/performance/visual/geo + conditional google/local/maps/backlinks/cluster/ecommerce/drift/sxo) → aggregated Health Score → prioritized action plan.
- **Ads** — `dna → create → generate`, `photoshoot` as branch.
- **Canvas** — `create → populate → layout → export`, or `/generate <desc>` for full AI orchestration.

Cross-plugin dependencies: `banana-claude` is the image engine for ads/blog/seo/canvas. `wp-mcp-ultimate` is the WordPress gateway.

## Locked canon (do not reinvent)

- **Cast** (GPT, Claude, Gemini, DeepSeek, Kimi, Perplexity, Qwen, Grok, Outliers, User-Narrator, Prompt-God) — sprites, palettes, voice direction, personality flaws. Source: `videography/TEAM-LLM-PRODUCTION-BIBLE-EXTRACT.md` + `wiki/voice/cast/`.
- **Creative engine:** technical LLM flaws = character flaws (e.g. context-window limit = anxiety disorder).
- **Copyright evasion:** chibi designs, shape language, palettes — **never logos**.
- **House voice:** "Myth-Hilarity + Tech Systems mixed with Anthropology" — full spec with examples in `blog/user_voice.md` and `wiki/voice/myth-hilarity-tech-anthropology.md`.
- **LLM orchestration roster:** Claude=spine, Gemini=research, Codex=mechanical execution, Jules=async — see `videography/PROMPT-ZONE-OVERVIEW.md`.

## Publishing & security

- Composio MCP routes: `reddit`, `linkedin`, `vercel`, `gmail`, `discord`, `slack`, `youtube`, `facebook`, `googledrive`. n8n is wired but `list_workflows` auth is flaky — Composio is the default.
- **Always get explicit per-post green-light from the user before firing any social send**, even on pre-approved channels. The channel list is permission to use the route, not permission to post.
- **Credentials:** WP Basic auth lives in `README.md.txt` (NOT `.env`). Flag if anything attempts to commit credential-bearing files.

## Working conventions

- Obsidian-flavoured markdown — wikilinks `[[name]]` are valid and must be preserved on edit.
- Filenames frequently start with `-` to control Obsidian sort order. Keep the prefix on rename.
- Battle posts and episode briefs use heavy emoji + headed sections — intentional KTG style, not noise to clean up.
- Heavy assets (PDFs, MP4, ZIPs, multi-MB PNGs) live alongside the posts they support — don't move to a central assets dir.
- `blog/battlle-of-the-bots/round-N/` battle sub-projects are the **only** dirs with executable scripts (`deploy.sh` runs `gh repo create` and publishes a public repo — confirm before running).

## Sister projects (outside this vault)

- `C:/Users/kevin/knowledge2026/` — parent wiki vault. This fork (`Pictures/ktg-one`) is the marketing/content production fork.
- `C:/Users/kevin/Desktop/ktg-one/` and `C:/Users/kevin/projects2026/06-projects-code/goodai-mate/` — Next.js sites (separate repos, separate build systems).
- `LEGIO/`, `Recursive-Council/` — referenced from prompt-zone docs, live under `C:/Users/kevin/knowledge2026/Projects-Coding/`.
