---
status: developing
created: 2026-06-03
updated: 2026-06-03
type: source
title: "STATE.txt — KTG Content Pipeline Quick-State Card"
slug: state-txt
source_path: "STATE.txt"
source_type: status-snapshot
ingested_at: 2026-05-27
tags: [source, pipeline, status, quick-reference]
hash: md5:e5f6a7b8c9d0e1f2a3b4c5d6e7f8a9b0
---

# STATE.txt — KTG Content Pipeline Quick-State Card

> Source file: `STATE.txt` at vault root. A compact plaintext summary of pipeline state — companion to the fuller [[project-state|PROJECT_STATE.md]].

## Summary

`STATE.txt` is a condensed at-a-glance status card for the KTG content pipeline. It distils the same information as `PROJECT_STATE.md` into a ~50-line plaintext file optimised for quick reference.

## Content Overview

### What Works (Production)
- `pipeline/run.sh` — template-based generator, 2 seconds
- `pipeline/publish-kit/*/` — 8 copy-paste ready files
- Image prompts for Google AI Studio — ready to use

### What's Untested (Framework Built)
- `pipeline/ktg_pipeline/` — Python AI framework (~2k lines)
- 4 LLM providers: Ollama, Google AI Studio, LM Studio, OpenRouter
- Needs: real LLM test, prompt fixes, error handling

### What's Impossible
- Auto-post to X/Meta/Medium (APIs blocked)
- 11-agent swarm (overengineering — dropped)

### Cost
- Bash version: $0
- Python local (Ollama/5070): ~$0.01 electricity
- Python API (Google AI Studio): ~$0.02–$0.05/post

### Next Steps (three options)
- **[A] Ship Now** (30 min, $0): `bash pipeline/run.sh` → images → copy-paste to 5 platforms
- **[B] Test Python** (1–2 hrs, $0): install deps → Ollama → test → fix
- **[C] Wire 5070** (2–4 hrs, $0): ComfyUI or SD WebUI with API → end-to-end test

### Verdict
Use [A] now. [B] and [C] are polish for later.

## Relationship to PROJECT_STATE.md

STATE.txt is the "card" version of `PROJECT_STATE.md` — same facts, no tables, no markdown headers, designed for contexts where rendering may be unavailable. They should stay consistent; if they diverge, `PROJECT_STATE.md` is the authoritative source.

## Cross-References
- [[project-state]] — the fuller companion doc
- [[ktg-one]] — project entity
- [[Publish-Kit-Pattern]] — the 8-file pattern referenced as "publish-kit/*"
- [[Five-Layer-Architecture]] — runtime layer context
