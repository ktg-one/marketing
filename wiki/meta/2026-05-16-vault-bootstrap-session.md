---
type: session
title: "Vault Bootstrap Session — 2026-05-16"
created: 2026-05-16
updated: 2026-05-16
tags: [session, bootstrap, meta]
status: complete
related:
  - "[[index]]"
  - "[[hot]]"
  - "[[log]]"
  - "[[battle-of-the-bots]]"
  - "[[the-mirage-of-ethical-ai]]"
  - "[[STRAWHATS-DIRECTIVE]]"
  - "[[myth-hilarity-tech-anthropology]]"
---

# Vault Bootstrap Session — 2026-05-16

The session that turned `C:/Users/kevin/Pictures/ktg-one/` from a content workspace into the **KTG AI Marketing Hub** wiki.

## What the vault is

- **Vault root**: `C:/Users/kevin/Pictures/ktg-one/`
- **Role**: content creation fork covering "03/06 domains" (`03-prompt-zone/` + `blog-2026/`)
- **Distinct from**: `C:/Users/kevin/knowledge2026/` (the main ~40GB wiki — Obsidian MCP `obsidian-vault` REST API points there, not here)
- **Plugins** loaded locally in `.claude/`: claude-obsidian (wiki, ingest, query, lint, save, autoresearch, canvas, defuddle, obsidian-bases, obsidian-markdown, wiki-fold) + claude-canvas (12 templates, 6 layout algorithms, 3 canvas agents, 1 `/canvas` command). Both **local, not global**, per user preference.

## Final wiki state at session end

| Domain | Count | Notes |
|---|---|---|
| Sources | 11 | All from `blog-2026/` + `03-prompt-zone/` |
| Entities | 9 | [[Anthropic]], [[Claude Code]], [[KAIROS]], [[autoDream]], [[Project Glasswing]], [[Undercover Mode]], [[Capybara v8]], [[STRAWHATS-DIRECTIVE]], [[botb-personas]] |
| Concepts | 21 | AI lab behaviour + Production pillars + STRAWHATS architecture + Fabrication doctrine + Diagnostic instruments + BotB mechanics + AI Anthropology |
| Cast pages | 11 | Full Team LLM roster: GPT, Gemini, Claude, DeepSeek, Kimi, Perplexity, Qwen, Grok, Outliers, User-Narrator, Prompt-God |
| Episodes | 5 scripted + 4 banked | The Weekend, Breakfast Sabotage, Output Unsanctioned, MoE Episode, Cognitive Overclock + bank |
| Intel snapshots | 3 | Anthropic Q1 degradation; 9-model fabrication survey; BotB results history |
| Playbooks | 1 | [[battle-of-the-bots]] |
| Content packages | 1 | `wiki/content/the-mirage-of-ethical-ai/` — full publish-ready bundle |

## The KTG thesis (now fully wikified)

The thesis loop is closed in three independent angles:

**Diagnosis**
- [[Silent Compute Cuts]] + [[Always-On AI Daemons]] + [[Source Map Leak Pattern]] + [[Ethics as Branding]] (Mirage P1 / [[anthropic-2026-q1-degradation]])
- [[Fabrication Necessity]] + [[Transparency-Fabrication-Complexity Ordering]] + [[Internal Process Verification Boundary]] + [[Capybara v8]] (Mirage P2 / [[model-fabrication-survey-2026-q1]])
- [[botb-results-history]] (Round 3 East self-reported 90/100, judges scored 10) — the same phenomenon at the live-agent surface

**Prescription**
- [[STRAWHATS-DIRECTIVE]] + [[Cognitive Architecture (Prompt-Only)]] + [[RKQDE Assessment Framework]] + [[Success Criteria Lock]] + [[3-Iteration Protocol]] — externalise verification at boundaries

**Method**
- [[AI Anthropology Framing]] (5 tenets) + [[battle-of-the-bots]] as the empirical lab

## Locked canon (do NOT reinvent)

- **Voice**: [[myth-hilarity-tech-anthropology]] — Myth-Hilarity + Tech Systems mixed with Anthropology. House writing voice for any KTG written content.
- **Cast**: see [[cast/_index|Cast Index]] — every animated character has locked visual / palette / personality flaw / voice direction. Sprite folders in `03-prompt-zone/-<character>/`.
- **Personas**: [[botb-personas]] — 6 locked Battle of the Bots agent personas (distinct from cast — same models, different content surface).
- **Production pillars**: [[Two-World Structure]], [[Bugs as Personality Traits]], [[Chibi Copyright Evasion]] (no logos), [[Geopolitical AI Satire]], [[Found Family Doctrine]], [[HTTYD Narration]].

## Decisions made this session

| Decision | Why |
|---|---|
| Wiki at `ktg-one/` root, not `blog-2026/` | User chose — keep blog-2026 as Obsidian sub-vault for actual posts; wiki is the meta layer above |
| Don't ingest into the 40GB knowledge2026 vault | Too big; user will port specific posts over manually if needed |
| Keep the wiki I scaffolded at ktg-one | User's call — "leave it itll be top folder for blog, seo, this, video creation eventually" |
| Use individual cast pages, not consolidated | Each character has discrete canon worth its own page |
| Consolidate Outliers (Llama, 7B, Mistral) into one page | They're side-cast, lower production priority |
| Consolidate Round 3 BotB into one source page | 5 docs tell different sides of the same battle (incl. self-report vs judging contradiction) — better as one page with `> [!contradiction]` callout |
| Defer entities for: Conway, BUDDY, Anti-Distillation, Claude Mythos, OpenCode, AMD director, QuitGPT, FreeBSD | Mentioned but not central enough yet — promote on next related ingest |
| Local plugin install (`.claude/`), not global | User explicitly requested. Both claude-obsidian + claude-canvas merged in. `.claude/settings*.json` write blocked by global deny rule (correct behaviour). |
| **Always ASK before any social post**, even with pre-approved channels | User stopped me right before I fired Reddit/LinkedIn/Vercel. Channel-set approval ≠ per-post fire approval. See [[memory/feedback_social_posting]]. |

## What's still open (next session)

- **Publish socials**: Reddit r/ClaudeAI + LinkedIn personal feed + Vercel deploy approved as channels for the Mirage post. Variants staged in `wiki/content/the-mirage-of-ethical-ai/`. Vercel HTML built (`assets/index.html`). Composio has all three tools. **Awaiting per-post green light from user.**
- **Performance tracker**: `wiki/performance/` is empty. Once anything goes live (or once the user reports back on what was already posted), create `wiki/performance/the-mirage-launch.md` recording URLs + engagement.
- **Mirage Part 2 publish package**: not yet built. Same shape as Part 1 (Reddit / LinkedIn / Medium / X / IG variants).
- **Episode bank**: 4 episodes scripted in name only — The Open-Source Invasion, Claude Tries, Grok Crashes In, Mistral - The Exception. None have full scripts.
- **Sprite gaps**: [[Kimi]] needs sprite expansion (1 only), [[Outliers|Mistral]] needs sprite creation (0).
- **n8n auth**: `list_workflows` returns 401 despite health check passing. Token may need refresh. Not blocking publish (Composio is the route).

## Operational notes

- **Manifest**: `.raw/.manifest.json` tracks all 11 ingested sources by hash. Re-ingest is a no-op if hash matches. Skip checking with "force ingest" if needed.
- **DragonScale addressing**: OFF (no `scripts/allocate-address.sh` at root, no `.vault-meta/`). Pages have no `address:` frontmatter. Don't change without backfill plan.
- **Custom callouts** (`> [!contradiction]`, `> [!gap]`, `> [!key-insight]`) used throughout. Render styled if `.obsidian/snippets/vault-colors.css` is enabled, fall back to default styling otherwise.
- **Hot cache**: [[hot|wiki/hot.md]] is the load-into-context-first file. Keep it under 500 words. Overwrite, don't append.
- **Log**: [[log|wiki/log.md]] is append-only. New entries at the **TOP**. Never edit past entries.

## Cross-references

- [[index]] · [[hot]] · [[log]] · [[overview]] — meta files
- [[battle-of-the-bots]] — the playbook this session ingested most heavily
- [[content/the-mirage-of-ethical-ai/_index]] — the publish package built but not fired
- `MEMORY.md` (in `~/.claude/projects/C--Users-kevin-Pictures-ktg-one/memory/`) — cross-session memory rules saved this session
