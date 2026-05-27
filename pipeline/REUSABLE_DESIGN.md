# Reusable Pipeline Design — Works Without Kimi

## The Problem

Current pipeline: Bash script generates templates. No AI. Requires me to run.

## The Solution

Pipeline calls YOUR infrastructure:
- Your 5070 + local models (Qwen, Gemini)
- Your Ollama/LM Studio
- Google AI Studio API (cheap)
- OpenRouter (unified API)

## Architecture

```
User runs pipeline
    │
    ▼
┌─────────────────┐
│  pipeline/run   │ ← Python script, no AI needed
└────────┬────────┘
         │
    ┌────┴────┬────────┬──────────┐
    ▼         ▼        ▼          ▼
 ┌──────┐ ┌──────┐ ┌──────┐ ┌──────────┐
 │Ollama│ │ LM   │ │Google│ │OpenRouter│
 │Qwen  │ │Studio│ │AI    │ │Unified   │
 └──────┘ └──────┘ └──────┘ └──────────┘
    │         │        │          │
    └─────────┴────────┴──────────┘
              │
              ▼
        ┌──────────┐
        │  Output  │
        │  Files   │
        └──────────┘
```

## User Configuration

```yaml
# pipeline/config.yaml
llm:
  provider: ollama  # or lmstudio, google, openrouter
  endpoint: http://localhost:11434
  model: qwen-opus-hybrid

image_gen:
  provider: local  # or google, banana
  endpoint: http://localhost:7860  # ComfyUI/SD

fallback:
  provider: google
  api_key: ${GOOGLE_API_KEY}  # env var
```

## How User Runs It

```bash
# 1. Configure
export OLLAMA_URL=http://localhost:11434
export GOOGLE_API_KEY=xxx

# 2. Run
python pipeline/run.py input/my-post.md

# 3. Done — outputs ready, no AI agent needed
```
