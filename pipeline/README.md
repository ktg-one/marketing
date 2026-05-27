# KTG Content Pipeline v2

Cross-platform, reusable, AI-powered content repurposing pipeline.

## What It Does

Takes a blog post → Generates 5 platform variants + SEO + Ads + Images

**Actually uses AI** (your local models or APIs), not templates.

## Quick Start

```bash
# 1. Install dependencies
pip install -r pipeline/requirements.txt

# 2. Configure (edit pipeline/config.yaml or create config.local.yaml)
cp pipeline/config.yaml pipeline/config.local.yaml
# Edit config.local.yaml with your settings

# 3. Run with Ollama (local, free)
ollama pull qwen-opus-hybrid  # or your preferred model
python pipeline/run.py pipeline/input/test-post.md

# 4. Or run with Google AI Studio (cheap, no local GPU)
export GOOGLE_API_KEY="your-key-here"
python pipeline/run.py pipeline/input/test-post.md --provider google
```

## Input Format

Your blog post needs YAML frontmatter:

```markdown
---
title: "Why AI Agents Will Replace Software Engineers by 2028"
slug: "ai-agents-replace-engineers-2028"
topic: "AI, Future of Work, Software Engineering"
tone: "provocative but evidence-based"
target_audience: "tech professionals, founders, investors"
key_points:
  - AI agents already write 40% of code at top startups
  - The bottleneck shifted from coding to specification
  - Engineers who adapt become "AI whisperers"
call_to_action: "Subscribe to KTG for weekly AI strategy breakdowns"
---

# Your Article Content

Write in markdown here...
```

## Supported LLM Providers

| Provider | Setup | Cost | Speed |
|----------|-------|------|-------|
| **Ollama** | Local install | Free | Fast (your 5070) |
| **LM Studio** | Local GUI | Free | Fast (your 5070) |
| **Google AI** | API key | ~$0.001/1K tokens | Fast |
| **OpenRouter** | API key | Varies | Fast |

## Output Structure

```
pipeline/output/{slug}/
├── medium.md          # Full article for Medium
├── reddit.md          # Discussion post for Reddit
├── x-thread.md        # 8-post thread for X
├── linkedin.md        # Professional post for LinkedIn
├── meta.md            # Casual post for Facebook
├── seo.md             # Meta tags, schema, keywords
├── ads.md             # Google, Meta, LinkedIn ad copy
├── image-prompts.md   # Prompts for image generation
└── manifest.json      # Summary of all outputs
```

## Configuration

Edit `pipeline/config.local.yaml`:

```yaml
llm:
  provider: ollama  # or google, openrouter
  
  ollama:
    base_url: http://localhost:11434
    model: qwen-opus-hybrid
    temperature: 0.7
    max_tokens: 2000

# Enable/disable platforms
platforms:
  medium: { enabled: true }
  reddit: { enabled: true }
  x: { enabled: true, thread_posts: 8 }
  linkedin: { enabled: true }
  meta: { enabled: true }
```

## Using Your RTX 5070

```bash
# Option 1: Ollama (recommended)
ollama pull qwen-opus-hybrid
ollama serve
# In another terminal:
python pipeline/run.py input/my-post.md

# Option 2: LM Studio
# 1. Open LM Studio
# 2. Load your GGUF model
# 3. Start server (default: localhost:1234)
# 4. Edit config: provider: lmstudio
```

## Troubleshooting

**"Cannot connect to Ollama"**
- Is Ollama running? `ollama serve`
- Check port: `curl http://localhost:11434/api/tags`

**"Google API key required"**
- Get key from: https://makersuite.google.com/app/apikey
- Set: `export GOOGLE_API_KEY="your-key"`

**"Model not found"**
- List available: `python pipeline/run.py --list-ollama`
- Pull model: `ollama pull llama3` or `ollama pull gemma2`

## Architecture

```
run.py (CLI)
    │
    ▼
ContentPipeline (orchestrator)
    │
    ├──▶ Provider (Ollama/Google/OpenRouter)
    │       └──▶ Real LLM generates content
    │
    ├──▶ Platform agents (5 variants)
    ├──▶ SEO agent
    ├──▶ Ads agent  
    └──▶ Image prompt agent
```

All AI-powered. No templates. Works without Kimi.

## License

MIT — Use it, fork it, sell it. It's yours.
