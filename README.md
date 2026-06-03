# ktg.one — AI Content Hub

> Plugin-driven content creation and publishing pipeline.  
> Blog · SEO · Ads · Image Generation · Wiki · Analytics

---

## Start Here

**→ [Marketing Hub](./marketing/)** — Your command center for content creation.

New? Read the [Quick Start Guide](./marketing/QUICKSTART.md).

---

## What's Inside

| Layer | What | Where |
|-------|------|-------|
| **Marketing** | 84 skills, 39 agents | [`marketing/`](./marketing/) |
| **Wiki** | Knowledge vault, hot cache | [`wiki/`](./wiki/) |
| **Design** | Landing pages, assets | [`design/`](./design/) |
| **Blog** | Drafts, published posts | [`blog/`](./blog/) |
| **Pipeline** | Input/output, logs | [`pipeline/`](./pipeline/) |

---

## One-Command Operations

```
/blog write <topic>        # Write a blog post
/seo audit [url]           # Full SEO audit
/ads audit                 # Multi-platform ad audit
/hub <file.md>             # Run full publishing pipeline
/wiki-ingest <source>      # Add source to knowledge vault
/banana <prompt>           # Generate images
```

---

## Project Structure

```
ktg-one/
├── marketing/              ← Start here. Hub docs + commands.
├── .agents/skills/         ← Canonical skill source (84 marketing skills)
├── .kimi/skills/           ← Kimi-accessible skills
├── .claude/skills/         ← Claude Code skills (hub, canvas, wiki)
├── .claude/plugins/        ← Full plugin repos (blog, seo, ads, banana)
├── .claude/agents/         ← 39 specialist agents
├── wiki/                   ← Obsidian-style knowledge vault
├── blog/                   ← Content workspace
├── design/                 ← Landing pages, visuals
├── pipeline/               ← I/O, logs, publish kit
└── .planning/              ← GSD project management
```

---

## Session Handoff

Picking this up in a new session?

1. Read `wiki/hot.md` — active threads, trust state, carry-forward
2. Run `/wiki-lint` — health check the vault
3. Navigate to [`marketing/`](./marketing/) for your tools

---

*ktg.one — AI content, human voice.*
