---
status: developing
updated: 2026-06-03
type: concept
title: "Review Gate"
aliases: ["Human Gate", "Publish Gate", "per-post approval"]
created: 2026-05-27
tags: [concept, pipeline, security, publishing, human-in-loop]
---

# Review Gate

The non-bypassable human approval gate in the [[ktg-one]] pipeline. Sits at Layer 5 (Publishing) of the [[Five-Layer-Architecture]]. No content can be published — to Vercel, Reddit, LinkedIn, or any channel — without explicit per-post human approval.

## How It Works

1. Content reaches end of the Create → Optimize chain
2. Pipeline stops and waits for a human `YES`
3. Human types `YES` (or `STOP` to cancel)
4. Only then does [[Composio]] fire the publish actions

## Design Properties

- **Non-bypassable**: even `/loop`, scheduled runners, and autonomous agent sessions must stop at the gate
- **Per-post**: no session-wide blanket approval — every post requires its own `YES`
- **Wiki-state**: gate state is written to the wiki, not conversation memory — survives `/clear` and session resets
- **Explicit denial**: typing `STOP` cancels without publishing; no default-publish on timeout

## Security Rationale

The Review Gate exists because:
1. Social posts cannot be recalled cleanly once fired (Reddit/LinkedIn APIs do not guarantee delete)
2. [[Composio]] connectors are permission-to-route, not permission-to-post
3. Autonomous pipelines without a human gate are a liability for a brand identity workspace

## In the Publish Kit

The `review-checklist.md` file inside each [[Publish-Kit-Pattern]] is the human-facing artefact for the gate — a quality checklist the human works through before typing `YES`.

## Relationship to GSD Phase 4.0

In [[GSD-Methodology]], Phase 4.0 is the "Review Gate" phase. Its verification criterion: an autonomous publish attempt is blocked, and per-post `YES` is required before anything fires.

## Cross-References
- [[Five-Layer-Architecture]] — Layer 5 position
- [[Composio]] — the tool the gate controls
- [[Publish-Kit-Pattern]] — contains the `review-checklist.md` gate artefact
- [[GSD-Methodology]] — Phase 4.0
- [[ktg-one]] — the pipeline this gate protects
- [[agents-md-ktg-one]] — security section
