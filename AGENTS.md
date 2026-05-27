# AGENTS.md — ktg.one

> This file is the single source of truth for AI coding agents working on this project.
> Last updated: 2026-05-26

---

## 1. Project Overview

**ktg.one** is a plugin-driven AI content creation hub. It is NOT a traditional software application with a web server or compiled binary. Instead, it is an **agent-orchestrated content pipeline** that runs inside AI coding environments (Claude Code, OpenCode, Gemini CLI, Cursor, Codex CLI) to automate the full content marketing lifecycle:

1. **Capture** — ingest ideas, files, or URLs into a structured wiki
2. **Plan** — generate campaign briefs from wiki state
3. **Create** — draft blog posts and generate images in parallel
4. **Optimize** — run GEO, SEO audits, and schema markup sequentially
5. **Review** — mandatory human gate before any publish action
6. **Publish** — deploy to Vercel and fire social variants via Composio

The project is the personal workspace of Kevin Tan (kevin.pl.tan@gmail.com), operating under the brand **Good AI** (`goodai.au`). Content is produced in a distinctive voice called **Myth-Hilarity** — a two-layer writing stack where brand voice defines *what tone* and a Writing Discipline Ruleset defines *how not to collapse into formula*.

---

## 2. Technology Stack

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Runtime** | Python 3.12+ | Minimal Python shell (`main.py` is a stub) |
| **Package Manager** | `uv` | Fast Python package resolution (lockfile: `uv.lock`) |
| **AI CLI Host** | OpenCode (primary), Claude Code, Gemini CLI, Codex CLI | Agent runtime environment |
| **Skills System** | OpenCode / Claude Code Skills (YAML frontmatter + Markdown) | ~80 skills across 7 plugins |
| **Wiki Engine** | Custom Obsidian-style markdown vault in `wiki/` | Persistent state, knowledge graph, hot cache |
| **Image Generation** | Gemini Nano Banana models via `banana-claude` plugin | Hero images, inline visuals, ad creatives |
| **SEO Data** | DataForSEO API (extension), Firecrawl (extension) | Live SERP, keyword, backlink data |
| **Publishing** | Composio MCP (Reddit, LinkedIn, Vercel, Gmail, Google Drive, Discord, YouTube, GitHub) | Social outbound and deploy |
| **WordPress** | `wp-mcp-ultimate` MCP server (`https://ktg.one/wp-json/mcp/wp-mcp-ultimate`) | WordPress gateway with Basic auth |
| **Browser Automation** | Chrome DevTools MCP | DOM inspection, console capture, screenshots |
| **Project Planning** | GSD (Go-to-Market Software Development) methodology in `.planning/` | Roadmaps, phases, requirements, audits |

### Key Dependencies (`pyproject.toml`)
```toml
[project]
name = "ktg-one"
version = "0.1.0"
requires-python = ">=3.12"
dependencies = [
    "kimi-cli>=1.44.0",
    "tool>=0.8.0",
]
```

The Python dependencies are minimal because the project's real "code" is the skill orchestration layer, not a traditional application.

---

## 3. Directory Structure

```
ktg-one/
├── .agents/                    # Agent-scoped skills (community + custom)
│   └── skills/                 # 60+ skills: next-best-practices, copywriting, council, etc.
├── .claude/                    # Claude Code configuration and plugin ecosystem
│   ├── plugins/                # 7 plugins with ~80 skills total
│   │   ├── banana-claude/      # Image generation (Gemini Nano Banana)
│   │   ├── claude-ads/         # 22 ad skills (Google, Meta, LinkedIn, TikTok, etc.)
│   │   ├── claude-blog-main/   # 22 blog skills (write, repurpose, seo-check, schema, etc.)
│   │   ├── claude-canvas/      # 8 canvas skills (visual planning, node graphs)
│   │   ├── claude-seo/         # 25 SEO skills (audit, geo, schema, technical, etc.)
│   │   ├── best-practices-main/# Development best practices
│   │   └── wordpress-mcp-ultimate/  # WordPress MCP gateway
│   ├── skills/                 # Project-local skills (hub, wiki-ingest, banana, canvas, etc.)
│   ├── config.json             # Claude Code config (permissions, MCP servers, theme)
│   └── ...
├── .kimi/                      # Kimi CLI configuration (minimal)
├── .planning/                  # GSD project management
│   ├── PROJECT.md              # Project scope, requirements, decisions
│   ├── ROADMAP.md              # 6-phase sequential roadmap (v1.0.0)
│   ├── REQUIREMENTS.md         # Functional + non-functional requirements
│   ├── config.json             # GSD mode: yolo, parallelization, model profiles
│   └── research/               # Research artifacts
├── .raw/                       # Raw article sources before wiki ingestion
│   └── articles/
├── .understand-anything/       # Codebase knowledge graph (auto-generated)
├── .venv/                      # Python virtual environment (uv-managed)
├── blog/                       # Blog content workspace (Obsidian vault)
│   ├── posted/                 # Published posts archive
│   ├── assets/                 # Images and media
│   ├── WRITING.md-main/        # Writing rulesets and voice docs
│   └── *.md                    # Draft posts and strategic deliverables
├── data/                       # Runtime data stores
│   ├── state_store.db/         # Application state database
│   └── stream_store/           # Stream data
├── design/                     # Design artifacts
├── notebooklm-infographic-designs/  # Static site for NotebookLM infographic prompts
├── notebooklm-slide-templates/      # 14 Korean slide design templates for NotebookLM
├── videography/                # Video production scripts, characters, episode bibles
├── wiki/                       # Obsidian-style knowledge vault (THE STATE LAYER)
│   ├── hot.md                  # <500 token session continuity cache
│   ├── index.md                # Vault master index
│   ├── log.md                  # Activity log
│   ├── concepts/               # Concept pages (Writing Discipline Ruleset, etc.)
│   ├── content/                # Content campaigns (one dir per post)
│   ├── entities/               # Named entities (Kismet, Good AI, STRAWHATS-DIRECTIVE, etc.)
│   ├── intel/                  # Intelligence snapshots (model degradation, benchmark results)
│   ├── meta/                   # Meta pages (vault bootstrap, config)
│   ├── modules/                # Plugin documentation and pipeline signals
│   ├── playbooks/              # Operational playbooks (Battle of the Bots, recovery)
│   └── ...
├── main.py                     # Python entry stub (prints "Hello from ktg-one!")
├── pyproject.toml              # Python project metadata
├── uv.lock                     # Locked dependency resolution
├── skills-lock.json            # Skill integrity hashes (400+ entries)
├── README.md                   # Empty (intentional — human docs are in CLAUDE.md)
├── README.md.txt               # MCP config fragment (WP auth credentials)
└── CLAUDE.md                   # Human-readable project overview and behavioral guidelines
```

---

## 4. Build and Test Commands

This project has **no traditional build system** and **no test suite** in the conventional software engineering sense. The "build" is skill orchestration; the "tests" are pipeline verification criteria defined in `.planning/ROADMAP.md`.

### Available Commands

| Command | Purpose |
|---------|---------|
| `uv run main.py` | Run the Python stub (does nothing meaningful) |
| `uv sync` | Sync Python dependencies from `uv.lock` |
| `uv add <pkg>` | Add a Python dependency |
| `/hub <post-file.md>` | **Primary workflow** — run the full content pipeline |
| `/wiki` | Check wiki setup, scaffold, or continue session |
| `/wiki-ingest [file]` | Ingest a source into the wiki (creates 8-15 pages) |
| `/wiki-query <topic>` | Query accumulated wiki knowledge |
| `/wiki-lint` | Health check: orphans, dead links, gaps |
| `/banana <prompt>` | Generate images via Gemini Nano Banana |
| `claude -p '<prompt>'` | Spawn Claude Code sidecar for parallel work |
| `gemini` | Spawn Gemini CLI for research tasks |
| `codex` | Spawn Codex CLI for execution tasks |

### Pipeline Verification (from ROADMAP.md)

Each phase has explicit verification criteria rather than unit tests:

- **Phase 1.0 (Foundation)**: 3 seeds → 3 briefs; hot cache reflects state on fresh session start
- **Phase 2.0 (Creation)**: Brief → draft + 3 images in one orchestration; main context <30% budget
- **Phase 3.0 (Optimization)**: 3 drafts through pipeline → valid JSON-LD each; GEO score present
- **Phase 4.0 (Review Gate)**: Autonomous publish attempt blocked; per-post YES required
- **Phase 5.0 (Publish)**: Deploy → URL → 2 variants → 2 fires → wiki log
- **Phase 6.0 (Hardening)**: Full pipeline <10 min end-to-end; wiki-lint zero orphans

---

## 5. Code Style Guidelines

### For Skill Authors (SKILL.md files)

- **YAML frontmatter** is mandatory:
  ```yaml
  ---
  name: skill-name
  description: >
    One-line description for discovery.
  user-invokable: true
  argument-hint: "<file-path>"
  ---
  ```
- **Progressive disclosure**: Entry skill loads first; sub-skills load on-demand via `Skill` tool only
- **Never use `Read` on skill files** — always invoke via `Skill` tool to stay under context budget
- **Orchestrator skills must stay under ~4k tokens** after loading
- **Cross-plugin dependencies** are documented in `wiki/modules/pipeline-signals.md`

### For Wiki Content

- **Obsidian-style markdown** with YAML frontmatter on every page
- **Wikilinks** for cross-references: `[[page-name]]`
- **Tags** in frontmatter: `tags: [concept, seo, pipeline]`
- **Hot cache** (`wiki/hot.md`) must stay under ~500 tokens — update at end of every session

### For Python Code

- Python 3.12+ syntax
- Minimal dependencies — prefer stdlib
- This project rarely writes Python; most logic lives in skill Markdown files

### General Behavioral Rules (from CLAUDE.md)

1. **Think Before Coding** — State assumptions explicitly. Ask when uncertain.
2. **Simplicity First** — Minimum code that solves the problem. No speculative abstractions.
3. **Surgical Changes** — Touch only what you must. Match existing style. Don't refactor unrelated code.
4. **Goal-Driven Execution** — Transform tasks into verifiable goals with success criteria.

---

## 6. Testing Instructions

There is **no automated test suite** (no pytest, no jest, no CI). Quality is ensured through:

1. **Pipeline verification** — Run the full `/hub` pipeline on a test post and check outputs
2. **Wiki lint** — Run `/wiki-lint` to detect orphans, dead links, and structural gaps
3. **Voice audit** — Sample drafts against the `[[user-voice]]` (Myth-Hilarity) ruleset
4. **Schema validation** — Verify JSON-LD output against Schema.org using `seo-schema` skill
5. **Token audit** — Ensure orchestrator skills stay under 4k tokens after loading

### Manual Test: Full Pipeline

```
1. Create a test post in wiki/content/test-post/post.md
2. Run `/hub wiki/content/test-post/post.md`
3. Verify: 4 social variants generated, hero + 3 crops, GEO score, schema.json
4. Verify: Review gate stops and waits for YES
5. Type STOP to cancel (do not publish test content)
6. Run `/wiki-lint` — confirm zero orphans
```

---

## 7. Security Considerations

### Credential Storage

- **WordPress MCP auth** is stored in `README.md.txt` (Basic auth base64 string)
- **Composio connections** are managed via MCP gateway at `D:\projects\.mcp\gateway.py`
- **No `.env` file** in the repo — API keys are injected via MCP server environment or CLI config
- **Sensitive files** are NOT in `.gitignore` by default — be careful what you commit

### MCP Gateway

The `.claude/config.json` references a local MCP gateway:
```json
"gateway": {
  "command": "cmd",
  "args": ["python3 D:\\projects\\.mcp\\gateway.py"]
}
```

This gateway proxies MCP tool calls. Do not modify gateway configuration without understanding the downstream effects on all connected services.

### Review Gate Security

- The Review Gate is **non-bypassable by design** — even `/loop` and scheduled autonomous runners must stop
- Per-post approval is required — **no session-wide blanket YES**
- Gate state is written to wiki (not conversation memory) so it survives `/clear`

### Platform Constraints

- **Windows / PowerShell** — all shell commands must use PowerShell syntax
- **No n8n** — n8n auth is broken; all automation routes through OpenCode/CLI/Composio
- **No sudo/root operations** — this is a user-level content tool

---

## 8. Deployment Process

### Content Deployment (Vercel)

1. Post is approved at Review Gate → user types `YES`
2. Composio deploys to Vercel → captures canonical URL
3. Canonical URL is injected into social variants
4. Composio fires Reddit + LinkedIn posts
5. Wiki log entry written to `wiki/log/publish.md`

### Rollback

- **Vercel**: `vercel rollback <deploymentId>`
- **Composio posts**: Use Composio delete endpoint per platform
- **Wiki**: Revert `wiki/log.md` and relevant content pages

### Skill Deployment

- Skills are loaded dynamically by the AI CLI — no compile or deploy step
- New skills: create `SKILL.md` with proper YAML frontmatter in `.claude/skills/` or `.agents/skills/`
- Register in `wiki/modules/index.md` and `wiki/modules/pipeline-signals.md`

---

## 9. Key Files for Agent Onboarding

When starting work on this project, read these in order:

1. **`wiki/modules/index.md`** — Master index of all plugins (79 skills, 40 agents)
2. **`wiki/modules/pipeline-signals.md`** — How sequential pipelines chain between plugins
3. **`wiki/hot.md`** — Current session state and active threads (<500 tokens)
4. **`.planning/PROJECT.md`** — Project scope, requirements, and architecture decisions
5. **`.planning/ROADMAP.md`** — Current phase and verification criteria
6. **`CLAUDE.md`** — Behavioral guidelines and MCP configuration
7. **`wiki/playbooks/runtime-config.md`** — MCP server setup and runtime mapping

---

## 10. Active Workstreams (as of 2026-05-26)

| Workstream | Status | Next Action |
|-----------|--------|-------------|
| Publish "Mirage" post | Awaiting green-light | Vercel → URL → Reddit + LinkedIn via Composio |
| Kismet/Good AI strategy | Wikified | Define Training + Dashboard phase |
| Phase 1.0 Foundation | In progress | Audit `wiki-ingest` for all 3 input modes |
| Plugin registration | 13 of 79 skills registered | Continue registering blog + ads sub-skills |

---

*This AGENTS.md is authoritative. When it conflicts with other documentation, this file takes precedence for AI agents. Keep it updated when project structure, conventions, or security posture changes.*
