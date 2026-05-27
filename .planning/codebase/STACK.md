# Technology Stack

**Analysis Date:** 2026-05-27

> This is NOT a traditional code project. `ktg-one` is an agent-orchestrated content creation hub. The "stack" is overwhelmingly skill orchestration + MCP servers + bash glue, with Python as a deliberately minimal shell. Architecturally significant components are captured below; the long tail of skill markdown is intentionally omitted.

## Languages

**Primary:**
- Bash - production content pipeline (`pipeline/run.sh`, ~2s end-to-end, 8-file publish kit)
- Markdown (Obsidian-flavoured, YAML frontmatter) - the actual "source code" — skills, wiki state, content packages, voice canon

**Secondary:**
- Python 3.12+ - thin runtime shell. `main.py` is a Hello-World stub. AI pipeline at `pipeline/ktg_pipeline/` (~2,000 lines / 10 modules) is ~70% untested per `PROJECT_STATE.md`.
- HTML/CSS/JS - self-contained battle mini-sites under `blog/battlle-of-the-bots/round-N/` (each subproject is its own static site with a `deploy.sh`)
- YAML - skill frontmatter, `pipeline/config.yaml`, `.planning/config.json`-adjacent configs

## Runtime

**AI CLI Hosts** (this *is* the runtime — there is no traditional process):
- **OpenCode** - primary skill host; all 7 plugins load as skills here
- **Claude Code** - sidecar for `wordpress-mcp-ultimate` and for `claude-flow` swarm orchestration
- **Gemini CLI** - research/web-grounded queries
- **Codex CLI** - bulk mechanical edits
- **Kimi CLI** (`kimi-cli>=1.44.0`) - declared Python dependency; deep-research specialist
- **Jules CLI** - async background tasks

**Python Environment:**
- Python `>=3.12`
- `.venv/` managed by `uv`

## Package Managers

- **`uv`** - Python package manager. Lockfile: `uv.lock` (present). Commands: `uv sync`, `uv run main.py`, `uv add <pkg>`.
- **No npm / no pnpm / no yarn at root.** Battle subprojects under `blog/battlle-of-the-bots/round-N/*/` are self-contained — no monorepo tooling.

## Frameworks

**Orchestration Layer:**
- Custom **Skills System** (OpenCode / Claude Code skills format) - ~80 skills across 7 plugins; YAML frontmatter + Markdown body; progressive disclosure via `Skill` tool invocation (never `Read`)
- **GSD (Go-to-Market Software Development)** methodology in `.planning/` - 6-phase roadmap with verification criteria in lieu of unit tests
- **Karpathy LLM Wiki Pattern** - `wiki/` is load-bearing persistent state; agents that skip it have no user context

**No conventional web framework, no test framework, no build system.**

## Key Dependencies

**Python (from `pyproject.toml`):**
- `kimi-cli>=1.44.0` - Kimi AI CLI runtime
- `numpy>=2.4.6` - numerical (likely used by sccd/ math models)
- `psutil>=7.2.2` - process/system inspection
- `tool>=0.8.0` - generic tooling shim

The Python dependency list is deliberately minimal because the project's real "code" is skill orchestration, not application logic.

**Plugin Ecosystem** (`.claude/plugins/`, 7 plugins):
| Plugin | Role |
|--------|------|
| `banana-claude` | **Image engine** — Gemini Nano Banana via `nanobanana-mcp`. Cross-plugin dep for ads/blog/seo/canvas. |
| `claude-blog-main` | 22 blog skills (write, repurpose, seo-check, schema, geo) |
| `claude-ads` | 22 ad skills (Google, Meta, LinkedIn, TikTok, photoshoot branch) |
| `claude-seo` | 25 SEO skills (8+ parallel audit specialists → Health Score) |
| `claude-canvas` | 8 visual planning skills (12 archetypes, node graphs) |
| `best-practices-main` | Development conventions |
| `wordpress-mcp-ultimate` | WordPress gateway MCP server |

**Skill registry:** `wiki/modules/index.md` (79 skills / 40 agents); integrity hashes in `skills-lock.json` (400+ entries).

## Image Generation

- **Gemini Nano Banana** via `banana-claude` plugin + `nanobanana-mcp` MCP server
- Invoked via `/banana <prompt>` skill
- Used for: hero images, inline blog visuals, ad creatives, canvas exports
- Future option: local GPU (RTX 5070, ComfyUI / Automatic1111) — not wired yet

## Publishing Toolchain

- **Composio MCP gateway** - default route for all outbound social (one connector per channel: `reddit`, `linkedin`, `vercel`, `gmail`, `discord`, `slack`, `youtube`, `facebook`, `googledrive`, `github`)
- **Vercel** (via Composio) - long-form deploy; canonical URL injected into social variants
- **WordPress MCP** (`wp-mcp-ultimate`) - REST API gateway at `https://ktg.one/wp-json/mcp/wp-mcp-ultimate`
- **Bash pipeline** (`pipeline/run.sh`) - emits the 8-file publish-kit (`linkedin.txt`, `reddit.txt`, `x-thread.txt`, `meta.txt`, `medium.md`, `buffer.csv`, `review-checklist.md`, `all-image-prompts.md`)
- **GitHub** (`gh` CLI) - battle subproject `deploy.sh` scripts create public repos + GitHub Pages

## MCP Servers (architecturally significant)

| Server | Consumer | Purpose |
|--------|----------|---------|
| `gateway` (`D:\projects\.mcp\gateway.py`) | All Claude Code MCP calls | Local Python proxy for downstream MCP services |
| `nanobanana-mcp` | `banana-claude` | Gemini image generation |
| `wp-mcp-ultimate` | `claude-blog` (planned) | WordPress REST API |
| `chrome-devtools` MCP | `claude-seo` | DOM inspection, screenshots, rendering checks |
| Composio MCP | Publishing layer | Reddit/LinkedIn/Vercel/Gmail/Drive/Discord/YouTube/Facebook routes |
| DataForSEO (extension) | `claude-seo` | Live SERP/keyword/backlink data |
| Firecrawl (extension) | `claude-seo` | Full-site crawling |

## Configuration

**Project config files (present):**
- `pyproject.toml` - Python metadata + minimal deps
- `uv.lock` - locked Python resolution
- `skills-lock.json` - skill integrity hashes
- `.claude/config.json` - Claude Code permissions + MCP server registry + theme
- `.planning/config.json` - GSD mode (yolo, parallelization, model profiles)
- `pipeline/config.yaml` - Python pipeline provider config
- `.kimi/` - Kimi CLI config (minimal)

**Environment / secrets:**
- **No `.env` file in repo** by design
- WordPress Basic auth lives in `README.md.txt` (NOT `.env`) — base64 string
- Composio credentials managed inside the MCP gateway, not local config
- API keys injected via MCP server env or per-CLI config
- `.gitignore` does **not** broadly cover secrets — credential hygiene is manual

## Platform Requirements

**Development:**
- Windows / PowerShell (all shell commands assume PowerShell syntax)
- Bash available via the Bash tool / Git Bash for `pipeline/run.sh`
- Obsidian (optional, but markdown is Obsidian-flavoured — wikilinks `[[name]]`, leading `-` in filenames for sort order)

**Production:**
- No production server. Output artifacts publish to: Vercel (long-form), WordPress (`ktg.one`), social channels via Composio.

## Local AI Inference (optional, untested)

Python pipeline supports four providers, none load-tested:
- Ollama (local)
- LM Studio (local)
- Google AI Studio (API, ~$0.02–0.05/post)
- OpenRouter (API)

## Sister Stacks (out of scope, referenced)

- `C:/Users/kevin/knowledge2026/` - parent wiki vault
- `C:/Users/kevin/Desktop/ktg-one/`, `goodai-mate/` - Next.js sites (separate repos)
- `LEGIO/`, `Recursive-Council/` - agentic framework + multi-agent reasoning (under `Projects-Coding/`)

---

*Stack analysis: 2026-05-27*
