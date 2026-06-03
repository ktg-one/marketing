---
status: developing
type: concept
title: "Content Production Flow"
aliases: ["content flow", "Kevin's content flow", "production flow", "actual content flow"]
created: 2026-06-03
updated: 2026-06-03
tags: [concept, workflow, pipeline, content, notebooklm, claude, banana, composio, review-gate]
---

# Content Production Flow

Kevin's **actual** end-to-end content flow, corrected and locked in the **2026-06-03** session. This supersedes earlier descriptions that implied Gemini writes the blog post.

## The flow

```
1. Research        → NotebookLM (Kevin does research there)
2. WRITE blog post → Claude (in-session)        ← NOT Gemini
3. Images          → banana / Nano Banana (in-session)
4. Repurpose       → Gemini pipeline → platform variants
5. Review Gate     → non-bypassable per-post YES
6. Publish         → Composio (Vercel + LinkedIn + Reddit)
```

## Step detail

1. **Research → NotebookLM.** Kevin does his research in [[NotebookLM]]-style source-grounded notebooks. (See the `notebooklm` skill.)
2. **Write → Claude, in-session.** The blog post is **written in Claude during the session**, in the KTG house voice ([[myth-hilarity-tech-anthropology]]). This is a Claude task, not a Gemini task.
3. **Images → banana.** Image assets are generated in-session via **banana / Nano Banana** ([[banana-claude]]).
4. **Repurpose → Gemini.** The finished post is fed to the [[Google-Gemini-Engine]] pipeline to produce platform variants (the repurposing stage).
5. **Review Gate.** Output stops at the non-bypassable [[Review-Gate]] — explicit per-post `YES` required.
6. **Publish → Composio.** [[Composio]] deploys to Vercel and fires LinkedIn + Reddit. X / Meta / Medium remain **manual** (platform APIs block auto-posting).

## Critical clarification — Gemini is NOT the writer

> [!important] Gemini's role is the **image model + repurposer**, NOT the blog writer.
> The blog post is authored in **Claude**, in-session. Gemini comes in afterward for images (Nano Banana) and for turning the finished post into platform variants. Do not route the primary draft through Gemini.

## Scope boundary

**Ads and videography are Gemini's domain** and are **out of scope** for the content hub. The content hub covers blog → images → repurpose → publish only.

## Cross-References
- [[Google-Gemini-Engine]] — the repurpose/image engine (steps 3–4)
- [[banana-claude]] — image generation (step 3)
- [[Review-Gate]] — step 5 gate
- [[Composio]] — step 6 publishing
- [[ktg-hub-Plugin]] — the plugin that orchestrates this flow
- [[Agent-SDK-Orchestration]] — how steps 5–6 are orchestrated
- [[Five-Layer-Architecture]] — the layers this flow traverses
- [[Publish-Kit-Pattern]] — the artifacts produced
- [[myth-hilarity-tech-anthropology]] — voice used in the Claude write step
