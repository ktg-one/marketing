# ⛔ STOP — THIS IS A STALE FORK. READ BEFORE ANYTHING.

This repo (`ktg-one/marketing`) is **behind** the real project. The current repo is
**`github.com/ktg-one/content-hub`** — it has `Runtime.md`, the GSD plan (`.multica/plan/`),
the `claude-socials` plugin, finished publish-kits, and the current `wiki/hot.md`. None of
that is here.

**Do this first:**
```
multica repo checkout https://github.com/ktg-one/content-hub
```
Then read `content-hub/Runtime.md` + `content-hub/wiki/hot.md` (the SESSION HANDOFF block).
The plan is on Multica issues **GOO-34** (epic) + **GOO-35..39** — already written. **Do NOT
re-plan, scaffold `.planning/phases/`, or write new PLAN.md files here.** That re-planning
loop has burned 4+ sessions. The work is a blog-post repurpose, not an engineering epic.

---

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
5. `wiki/modules/index.md` — plugin ecosystem map (7 plugins · 84 skills · 39 agents)

**Karpathy LLM Wiki Pattern (canon):** agents that don't load the wiki have no user context. Reading the wiki INTO context is load-bearing, not optional.

**No-babysitting protocol:** resolve ambiguity from project docs before asking. Multi-option `AskUserQuestion` blocks are the relapse signal. Terse corrections mean "go figure it out."

## Architecture — five layers

```
Layer 5  PUBLISHING       Vercel · Composio (Reddit/LinkedIn) · WordPress
                          ⛔ Non-bypassable per-post REVIEW GATE
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

Cross-cutting: `.planning/` (GSD methodology — 6-phase roadmap), `.agents/skills/` (84 canonical skills), `.claude/agents/` (39 specialist agents).

## Pipeline readiness state

| Layer | Status |
|-------|--------|
| `pipeline/run.sh` bash template | ✅ **Production-ready** — 2s, 8-file publish-kit, $0 |
| Wiki vault | ✅ **Usable** — 33 sources, 16 entities, 30 concepts |
| Skill registry | ✅ **Installed** — 84 skills + 39 agents in `.agents/skills/` + `.claude/agents/` |
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
| `bash pipeline/run.sh <input.md>` | ✅ Working production pipeline (2s, 8-file publish-kit) |
| `uv sync` | Sync Python deps |
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

## Local-first LLM routing

Hub uses **Ollama** for text tasks by default:
- `Ministral:latest` (13.5B) — repurpose, SEO, GEO, schema
- `Qwopus:latest` (9B) — shorter content tasks

Cloud (Gemini, Claude API) only for: image generation, live SERP data, Composio publishing. Pass `--cloud` to override local routing.

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

## Sister projects (outside this vault)

- `C:/Users/kevin/knowledge2026/` — parent wiki vault (separate repo).
- `C:/Users/kevin/Desktop/ktg-one/` and `C:/Users/kevin/projects2026/06-projects-code/goodai-mate/` — Next.js sites (separate build systems).
