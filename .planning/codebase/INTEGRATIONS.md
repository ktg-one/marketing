# External Integrations

**Analysis Date:** 2026-05-27

> Integrations are routed through MCP servers, not direct SDKs. The local MCP gateway at `D:\projects\.mcp\gateway.py` proxies most calls. Composio is the **default** outbound publishing route; n8n is wired but currently unreliable.

## MCP Gateway (Cross-Cutting)

**Local gateway:**
- Path: `D:\projects\.mcp\gateway.py` (outside the repo)
- Declared in `.claude/config.json` as `gateway` MCP server
- Command: `cmd python3 D:\projects\.mcp\gateway.py`
- **Role:** Proxies MCP tool calls to downstream services; modifying it has downstream effects on all connected services.
- **Status:** Active

## Publishing — Composio MCP Routes (DEFAULT)

One Composio connector per channel. Channel list = permission to use the route, **NOT** permission to post. Per-post explicit user `YES` required at the Review Gate (non-bypassable, state persisted in `wiki/` to survive `/clear`).

| Channel | Composio Connector | Auth | Status | Notes |
|---------|--------------------|------|--------|-------|
| **Reddit** | `reddit` | OAuth via Composio | Wired, needs per-post green-light | Discussion post variant from `reddit.txt` |
| **LinkedIn** | `linkedin` | OAuth via Composio | Wired, needs per-post green-light | Professional article from `linkedin.txt` |
| **Vercel** | `vercel` | Token via Composio | Wired | Long-form deploy → captures canonical URL → injected into social variants |
| **Gmail** | `gmail` | OAuth via Composio | Wired | Outbound email |
| **Google Drive** | `googledrive` | OAuth via Composio | Wired | Asset storage / sharing |
| **Discord** | `discord` | Bot token via Composio | Wired | Notification / community posting |
| **YouTube** | `youtube` | OAuth via Composio | Wired | Video upload (videography stream) |
| **Facebook** | `facebook` | OAuth via Composio | Wired | Casual variant from `meta.txt` |
| **Slack** | `slack` | OAuth via Composio | Wired | Notifications |
| **GitHub** | `github` (Composio) + local `gh` CLI | Token | Active | Battle subproject `deploy.sh` scripts run `gh repo create` + GitHub Pages publish |

**Auth storage:** Composio manages all credentials internally. No tokens in repo. Connect/disconnect via Composio dashboard.

**Hard limits (per `PROJECT_STATE.md`):**
- X (Twitter) auto-post: **not possible** — API $5K/month. Manual copy-paste from `x-thread.txt` only.
- Meta business auto-post: blocked by verification requirement. Copy-paste from `meta.txt`.
- Medium: API mostly read-only. Manual import of `medium.md`.

## WordPress Integration

- **MCP Server:** `wp-mcp-ultimate` (custom plugin under `.claude/plugins/wordpress-mcp-ultimate/`)
- **Endpoint:** `https://ktg.one/wp-json/mcp/wp-mcp-ultimate`
- **Runtime:** Claude Code sidecar (not OpenCode)
- **Auth:** **Basic auth, base64 string stored in `README.md.txt`** (NOT `.env`). Flag any attempt to commit credential-bearing files.
- **Status:** Configured; consumer plugin `claude-blog` integration planned (not yet wired)
- **Purpose:** WordPress REST API gateway — post create/update/list, media upload, schema injection

## Image Generation — Gemini Nano Banana

- **MCP Server:** `nanobanana-mcp`
- **Consumer Plugin:** `banana-claude` (`.claude/plugins/banana-claude/`)
- **Invocation:** `/banana <prompt>` skill
- **Auth:** Google AI Studio API key, injected via MCP server env
- **Status:** Active — primary image engine
- **Used by:** `claude-blog` (hero + inline), `claude-ads` (creatives), `claude-seo` (visual audit), `claude-canvas` (exports)
- **Output:** Hero images, 3 crops, ad variants, canvas archetypes
- **Backup path (unwired):** Local RTX 5070 via ComfyUI (`localhost:8188`) or Automatic1111 (`localhost:7860` with `--api`)

## SEO Data — DataForSEO

- **MCP Server:** DataForSEO (extension MCP, not in `.claude/plugins/`)
- **Consumer:** `claude-seo` plugin
- **Auth:** API credentials via MCP env
- **Status:** Active extension
- **Purpose:** Live SERP results, keyword research, backlink data, competitor analysis
- **Cost model:** Per-query API charges

## SEO Crawling — Firecrawl

- **MCP Server:** Firecrawl
- **Consumer:** `claude-seo` plugin
- **Auth:** API key via MCP env
- **Status:** Active extension
- **Purpose:** Full-site crawling, page extraction, site-map intake for audits

## Browser Automation — Chrome DevTools MCP

- **MCP Server:** `chrome-devtools`
- **Consumer:** `claude-seo` (rendering checks), general use
- **Auth:** Local Chrome instance — no remote credentials
- **Status:** Active
- **Purpose:** DOM inspection, console capture, screenshots, JS-rendering verification for SEO audits

## n8n Workflows

- **Status:** **Wired but flaky** — `list_workflows` auth currently broken
- **Instance (sister project reference):** `https://ai-yah-old.taile6f11d.ts.net` (per Auto Memory)
- **Auth:** API key via MCP env
- **Decision:** **Composio is the default route** for all automation. n8n is backup only, not relied upon for new pipelines.
- **Use cases (when working):** scheduled triggers, webhook receivers

## Kismet (Sister Integration, External)

- **Reference:** `C:/Users/kevin/projects2026/06-Projects-Coding/kismet` (separate project)
- **Stack:** n8n + Google Workspace automation
- **Relevance here:** Mentioned in `wiki/entities/` and Auto Memory; not directly integrated into this repo's pipeline.

## GitHub (Direct, non-Composio path)

- **CLI:** `gh` (GitHub CLI)
- **Used by:** Battle subproject `deploy.sh` scripts (e.g. `blog/battlle-of-the-bots/round-2/02-saas-landing/deploy.sh`)
- **Side-effects:** Creates **public** repos on the user's account + enables GitHub Pages. Hardcoded `GITHUB_USER="kevin"` and per-project `REPO_NAME`.
- **Confirm before running** — real public artefacts.

## AI CLI Sidecars (Integration Pattern, not Service)

Used for delegated work, not "integrations" in the SaaS sense but they reach external APIs:

| CLI | External Provider | Use |
|-----|-------------------|-----|
| `gemini` | Google Gemini (web-grounded) | Research |
| `codex` | OpenAI (Codex CLI) | Bulk mechanical edits |
| `kimi` (`kimi-cli`) | Moonshot Kimi | Deep research, Eastern advantage |
| `jules` | Google Jules | Async long-running tasks |

Auth: Each CLI manages its own credentials (per-tool config files in `~/.gemini/`, `~/.codex/`, `~/.kimi/`, etc.). None live in this repo.

## Local AI Providers (Python pipeline, untested)

For `pipeline/ktg_pipeline/`:
- **Ollama** — `http://localhost:11434`, no auth (local)
- **LM Studio** — `http://localhost:1234`, no auth (local)
- **Google AI Studio** — API key, ~$0.02–0.05/post
- **OpenRouter** — API key, per-model pricing

All four providers are scaffolded; none have been load-tested against real prompts.

## Webhooks & Callbacks

**Incoming:** None directly to this repo. Any incoming hooks would land on `ktg.one` WordPress or an external n8n instance.

**Outgoing:** Composio handles all outbound webhooks transparently per connector.

## Environment Configuration

**No `.env` file** in repo by design. Credential surfaces:
- `README.md.txt` — WordPress Basic auth base64
- MCP server environments — API keys for Gemini, DataForSEO, Firecrawl, Composio
- Per-CLI config files outside repo (`~/.gemini/`, `~/.codex/`, `~/.kimi/`, `~/.opencode/`)
- Composio dashboard — all OAuth tokens for social channels

**`.gitignore` does not broadly protect secrets** — credential hygiene is manual. Never commit `README.md.txt` (it contains the WP Basic auth string).

## Review Gate (Cross-Cutting Security Boundary)

- Non-bypassable by design — even `/loop` and scheduled runners stop
- Per-post `YES` required; no session-wide blanket approvals
- State written to `wiki/` (not conversation memory) so it survives `/clear`
- Applies to every Composio publish action and every Vercel deploy

---

*Integration audit: 2026-05-27*
