---
status: developing
type: entity
subtype: plugin
title: "ktg-hub Plugin"
aliases: ["ktg-hub", "ktg-hub plugin", "hub plugin"]
created: 2026-06-03
updated: 2026-06-03
tags: [entity, plugin, hub, orchestration, review-gate, mcp, packaging]
---

# ktg-hub Plugin

A self-contained content-hub plugin built in the **2026-06-03** session. It packages the [[ktg-one]] pipeline (run → review gate → publish) into a single installable unit with **dual packaging**: it works as a **Claude Code** plugin AND is repackaged as a **Claude Cowork** `.plugin`.

## Dual packaging

| Target | Form | Location |
|---|---|---|
| Claude Code | Plugin via marketplace `ktg-one` | repo `./plugins/ktg-hub` |
| Claude Cowork | `.plugin` bundle | `dist/ktg-hub.plugin` |

## Components

### Skills
- **`hub`** — run the pipeline, then stop at the [[Review-Gate]].
- **`publish`** — deploy/distribute *after* approval (post-gate only).

### Agents
- **`content-repurposer`** — repurposes the post into platform variants.
- **`seo-geo-optimizer`** — SEO + GEO optimization.
- **`publish-reviewer`** — reviews content before the publish step.

### Review-gate hook
- A **fail-closed `PreToolUse` hook** at `hooks/review-gate.sh`.
- Verified this session to **block path-traversal and unapproved slugs**, exiting with **code 2** (deny).
- This is the enforcement mechanism behind the non-bypassable [[Review-Gate]].

### Bundled assets
- Bundled **nanobanana MCP** (image generation — see [[banana-claude]]).
- Bundled **pipeline** (the [[Google-Gemini-Engine]] runtime).
- Bundled **voice** (`blog/user_voice.md` → [[myth-hilarity-tech-anthropology]]).

## Design intent

Self-contained: a single install carries the orchestration skills, the specialist agents, the image MCP, the generation pipeline, the voice spec, and — critically — the **fail-closed review-gate hook** so the gate travels with the plugin rather than depending on host config.

## Cross-References
- [[Five-Layer-Architecture]] — packages Layers 3–5 into one unit
- [[Review-Gate]] — enforced by the `review-gate.sh` PreToolUse hook
- [[Publish-Kit-Pattern]] — the artifacts the hub produces
- [[Skill-Progressive-Disclosure]] — `hub` (entry) + on-demand sub-skills
- [[banana-claude]] — bundled nanobanana MCP
- [[Google-Gemini-Engine]] — bundled generation pipeline
- [[Content-Production-Flow]] — the flow the hub orchestrates
- [[Agent-SDK-Orchestration]] — SDK that can drive the hub/publish step
- [[ktg-one]] — the parent workspace
