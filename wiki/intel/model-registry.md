---
status: developing
type: intel
title: "Model Registry"
created: 2026-05-26
updated: 2026-05-26
tags: [intel, models, local, api]
---

# Model Registry

> [!update] 2026-06-03 — Content engine migrated to Google/Gemini
> The [[ktg-one]] Python pipeline (`pipeline/ktg_pipeline/`) no longer routes content generation through local Ollama models by default. The content engine is now **Google/Gemini** (see [[Google-Gemini-Engine]]): text = `gemini-3.5-flash` (hero/hard = `gemini-3-pro-preview`), images = Nano Banana `gemini-3.1-flash-image-preview`, driver `GEMINI_API_KEY`. **Ollama / LM Studio are now offline `--local` fallback only.** The "Local Models (Downloaded)" + local-first routing tables below are SUPERSEDED for the content pipeline — kept for historical/fallback reference.

## Local Models (Downloaded)

| Model | Size | Type | Status | Use Case |
|-------|------|------|--------|----------|
| Qwen Opus | ~?B | Distilled hybrid | Active | Research, reasoning |
| Gemini distilled | ~?B | Distilled hybrid | Active | Content generation |
| (Add more as downloaded) | | | | |

## API Models (Cloud)

| Model | Provider | Status | Use Case |
|-------|----------|--------|----------|
| kimi-for-coding | Moonshot AI | Active | Primary coding agent |
| gemini-2.5-flash | Google | Active | agentmemory LLM |
| claude-sonnet-4 | Anthropic | Active | Claude Code sidecar |
| gpt-4 | OpenAI | Backup | General tasks |

## Model Routing

> [!contradiction] Superseded by 2026-06-03 Gemini migration
> The routing below shows **local** content gen (Gemini distilled via Ollama). As of 2026-06-03 the content pipeline routes to **hosted Google/Gemini** by default (`gemini-3.5-flash` / `gemini-3-pro-preview`), with Ollama as `--local` fallback. See [[Google-Gemini-Engine]] for the authoritative routing table.

```
Task type → Model
─────────────────
Coding → kimi-for-coding (primary)
Research → Qwen Opus (local) or Gemini (local)
Content gen → Gemini distilled (local)
Image gen → Gemini Nano (banana-claude)
SEO data → DataForSEO API
```

## Notes

- Local models run via Ollama, LM Studio, or similar
- Distilled hybrids = smaller, faster, specialized for specific tasks
- Qwen Opus = strong reasoning, good for research phase
- Gemini distilled = good for content generation, fast
- Update this registry when new models are downloaded

## Distilled Hybrids Explained

**What is a distilled hybrid?**
- Take a large model (Qwen 72B, Gemini Pro)
- Distill knowledge into smaller model (7B-14B)
- Fine-tune for specific tasks (coding, writing, reasoning)
- Result: faster, cheaper, task-specialized

**Your Current Hybrids**

| Hybrid | Base | Distilled From | Specialization |
|--------|------|----------------|----------------|
| Qwen Opus hybrid | Qwen2.5-7B/14B | Qwen-72B + RLHF | Reasoning, research |
| Gemini distilled | Gemma-2-9B | Gemini Pro + SFT | Content generation |

**Why use distilled?**
- 10x faster inference
- Runs on consumer GPU (8-16GB VRAM)
- 100x cheaper than API
- No rate limits
- Private (no data leaves machine)

**Trade-offs**
- Less general knowledge than full model
- May hallucinate on edge cases
- Needs specific prompt formats
- Requires local inference setup

## Recommended Local Stack

```
Task: Research paper analysis
→ Qwen Opus hybrid (reasoning)

Task: Blog post writing  
→ Gemini distilled (content gen)

Task: Code review
→ DeepSeek-Coder-V2 (coding)

Task: Image generation
→ FLUX.1-schnell (fast images)

Task: General chat
→ Mixtral-8x7B (broad knowledge)
```
