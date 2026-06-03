---
status: developing
type: concept
title: "Google/Gemini Engine"
aliases: ["Gemini Engine", "Google engine migration", "Gemini pipeline engine"]
created: 2026-06-03
updated: 2026-06-03
tags: [concept, engine, gemini, google, pipeline, models, image-generation, migration]
---

# Google/Gemini Engine

The content-generation engine for the [[ktg-one]] Python pipeline (`pipeline/ktg_pipeline/`). As of **2026-06-03**, the pipeline was migrated from local **Ollama** to **Google/Gemini** for both text and images. Ollama / LM Studio are retained only as an offline `--local` fallback.

This supersedes the local-first routing that was previously canon (Ministral / Qwopus / Ollama by default). See the `> [!update]` callouts on [[model-registry]] and [[hybrid-models-guide]].

## Why migrate

- Single hosted driver (`GEMINI_API_KEY`) instead of a local Ollama/LM Studio runtime that has to be up and warm.
- Faster, more reliable hero-quality prose without GPU/VRAM constraints.
- Native image generation via Nano Banana in the same provider family (see [[banana-claude]]).

## Model routing table

| Task tier | Model | Use |
|---|---|---|
| Text (default) | `gemini-3.5-flash` | Standard prose + structured stages |
| Text (hero / hard) | `gemini-3-pro-preview` | Hardest / highest-quality prose stages |
| Images | `gemini-3.1-flash-image-preview` (Nano Banana) | Image generation |

Driver env var: **`GEMINI_API_KEY`**.

## House voice injection

The KTG house voice — **Myth-Hilarity + Tech Anthropology** (sourced from `blog/user_voice.md`; canon in [[myth-hilarity-tech-anthropology]]) — is injected as a **system prompt into the 6 prose stages only**. It is **never** injected into structured / JSON-output stages, to avoid corrupting machine-readable output.

## Parallelism

The pipeline was parallelized with a `ThreadPoolExecutor`: **8 stages run concurrently (~20s total)**, each error-isolated so one stage failing does not crash the run.

## Bug fixed this session

A real bug was found and fixed: a **double-defined `generate()`** function was shadowing the text-generation path. After the fix the pipeline was **verified live** (returned `PIPELINE OK`, produced **8 files** — the [[Publish-Kit-Pattern]] output).

## Scope boundary

- Gemini's role in the content hub is the **image model + repurposer**, **NOT** the blog writer. The blog post is written in Claude, in-session. See [[Content-Production-Flow]].
- **Ads and videography are Gemini's domain** and are out of scope for the content hub.

## Where it lives

Branch: **`feat/pipeline-google-voice-parallel`**.

## Cross-References
- [[Content-Production-Flow]] — where this engine sits in Kevin's actual flow
- [[Agent-SDK-Orchestration]] — Claude orchestrates; Gemini generates (not orchestrated by Claude)
- [[banana-claude]] — Nano Banana image engine
- [[ktg-hub-Plugin]] — bundles this pipeline + voice
- [[Five-Layer-Architecture]] — this is the Layer 4 runtime engine
- [[Publish-Kit-Pattern]] — the 8-file output
- [[model-registry]] · [[hybrid-models-guide]] — superseded local-model lineup
- [[myth-hilarity-tech-anthropology]] — the injected house voice
