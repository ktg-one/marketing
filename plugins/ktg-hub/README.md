# ktg-hub

A self-contained Claude Code plugin for the **KTG / Good AI** content marketing hub. It drives a Gemini-powered pipeline that takes one blog post and produces a multi-platform publish-kit — platform variants (Medium, Reddit, X, LinkedIn, Meta), SEO/GEO optimization, JSON-LD schema, and an image — then stops at a non-bypassable human review gate before anything ships.

Content voice is **Myth-Hilarity + Tech Anthropology** (locked), sourced from `blog/user_voice.md`.

## What's inside

- **Commands** — `/ktg-hub:hub` (run pipeline -> review gate) and `/ktg-hub:publish` (deploy after approval).
- **Agents** — `content-repurposer` (voiced platform variants), `seo-geo-optimizer` (SEO + GEO score + JSON-LD), `publish-reviewer` (the review-gate keeper).
- **Hook** — a `PreToolUse` review gate that fail-closed blocks any publish (Composio reddit/linkedin, Vercel deploy) without a per-post approval marker.
- **MCP** — bundles the nanobanana (Gemini image) MCP server. (Composio is remote/OAuth and is referenced, not bundled.)
- **Pipeline** — the runnable Gemini engine (`pipeline/run.py` + `ktg_pipeline/`) plus a sample input.

## Install

```
/plugin marketplace add ktg-one/marketing
/plugin install ktg-hub@ktg-one
```

## Usage

1. **Run the pipeline:** `/ktg-hub:hub <post.md>` — generates the publish-kit and STOPS at the review gate.
2. **Review:** inspect the variants, SEO/GEO, and schema. Reply `YES` to the reviewer to approve **this specific post**.
3. **Publish:** `/ktg-hub:publish <slug>` — deploys to Vercel and posts LinkedIn + Reddit via Composio.

X, Meta, and Medium stay **manual** — their platform APIs block reliable auto-posting; the kit gives you ready-to-paste copy.

## Engine & requirements

- **Engine is Gemini** (Google AI Studio). Set `GEMINI_API_KEY` in your environment. The nanobanana image MCP also uses it.
- Runs via `uv` (`uv run --no-project --with pyyaml --with requests ...`) — no project venv required.

## Non-negotiables

- **Voice is locked** — Myth-Hilarity + Tech Anthropology, from `blog/user_voice.md`. Applied to narrative copy only, never to JSON/structured outputs.
- **The review gate is non-bypassable and fail-closed.** Approval is **per-post only** (one `YES` = one slug), never session-wide. The `PreToolUse` hook independently re-checks the `.approved` marker and blocks publish calls that lack it.
