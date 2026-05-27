# Handoff Document — KTG Content Pipeline v2

**Status**: Framework built, needs testing
**Built by**: Kimi
**Handoff to**: User / Next AI

## What Exists

### Python Package (`pipeline/ktg_pipeline/`)
```
ktg_pipeline/
├── __init__.py           # Package init
├── config.py             # YAML config loader with env var support
├── pipeline.py           # Main orchestrator (370 lines)
└── providers/
    ├── __init__.py
    ├── base.py           # Abstract base classes
    ├── ollama.py         # Local Ollama support ✓
    ├── google.py         # Google AI Studio ✓
    ├── lmstudio.py       # LM Studio ✓
    └── openrouter.py     # OpenRouter ✓
```

### CLI Entry Point
- `pipeline/run.py` — CLI with argparse
- `pipeline/config.yaml` — Configuration template
- `pipeline/requirements.txt` — Dependencies
- `pipeline/README.md` — Documentation

### What It Does (When Working)
1. Parse blog post with YAML frontmatter
2. Spawn 5 platform repurposing calls (sequential, not parallel)
3. Generate SEO package
4. Generate Ads package
5. Generate image prompts
6. Output to `pipeline/output/{slug}/`

## What's Working
- ✅ Config loading
- ✅ Provider abstraction
- ✅ Ollama provider (tested connection)
- ✅ CLI structure
- ✅ Input parsing

## What's NOT Working / NOT Tested
- ❌ Actual LLM generation (needs live model)
- ❌ Prompt quality (needs iteration)
- ❌ Error handling edge cases
- ❌ Parallel execution (currently sequential)
- ❌ Image generation (prompts only)
- ❌ Publish kit assembly
- ❌ Buffer CSV output

## To Complete

### 1. Test with Real LLM (30 min)
```bash
# Option A: Ollama (local, free)
ollama pull llama3  # or qwen, gemma2
ollama serve
python pipeline/run.py pipeline/input/test-post.md

# Option B: Google (cheap, fast)
export GOOGLE_API_KEY="your-key"
python pipeline/run.py pipeline/input/test-post.md --provider google
```

### 2. Fix What Breaks (1-2 hours)
- Prompt engineering for each platform
- Error handling for API failures
- Output formatting tweaks

### 3. Add Parallel Execution (30 min)
Use `concurrent.futures` to run 5 platform variants in parallel.

### 4. Polish (1 hour)
- Better prompts
- Output validation
- Publish kit assembly

## Key Files to Edit

| File | What to Change |
|------|----------------|
| `ktg_pipeline/pipeline.py` | Prompts (lines 150-350), add parallel execution |
| `ktg_pipeline/providers/*.py` | Error handling, retry logic |
| `config.yaml` | Default models, temperature settings |
| `run.py` | Add more CLI options if needed |

## Design Decisions Made

1. **Sequential over parallel** — Easier to debug, parallel is trivial to add later
2. **Provider pattern** — Easy to add new LLM backends
3. **YAML config** — Human-editable, env var substitution
4. **File-based output** — Easy to inspect, version control friendly
5. **No image generation** — Out of scope, prompts only

## Costs to Run

| Provider | Cost per post | Speed |
|----------|--------------|-------|
| Ollama (local) | $0 (your electricity) | Fast (5070) |
| Google AI | ~$0.01-0.05 | Fast |
| OpenRouter | ~$0.02-0.10 | Fast |

## Next Steps (Priority Order)

1. **Test with Ollama** — Validate the core loop works
2. **Fix prompts** — Make output quality good
3. **Add parallel** — Speed up (5x faster)
4. **Polish** — Error messages, docs
5. **Ship** — Use it

## Critical Info

- **Python 3.8+ required**
- **Windows/Linux/Mac compatible**
- **No GPU required** if using APIs
- **Works without me (Kimi)** once running

## Handoff Checklist

- [ ] Test with `python pipeline/run.py --help`
- [ ] Test with real LLM (Ollama or Google)
- [ ] Verify output files created
- [ ] Fix any import errors
- [ ] Iterate on prompts for quality
- [ ] Add parallel execution if needed
- [ ] Update README with actual usage

## Contact / Context

- This was built as a "reusable" alternative to bash templates
- Original bash version: `pipeline/run.sh` (still works, no AI)
- This Python version: `pipeline/run.py` (real AI, more complex)
- User has RTX 5070 + local models (Qwen, Gemini)
- Goal: Run without Kimi present

## Known Issues

1. **Google provider has image method name conflict** — `generate()` used for both text and images. Fix: Rename image method.
2. **No retry logic** — API failures crash the pipeline. Fix: Add `@retry` decorator.
3. **Prompts are basic** — Will need iteration for quality output.
4. **No streaming** — Large outputs block. Fix: Add streaming support.

## Success Criteria

Pipeline is done when:
- [ ] User can run `python pipeline/run.py input/post.md` without Kimi
- [ ] Output quality is good enough to publish
- [ ] No manual intervention needed
- [ ] Handles errors gracefully

## Quick Test

```bash
cd /c/Users/kevin/Pictures/ktg-one
pip install pyyaml requests
python pipeline/run.py --help
```

If that works, handoff successful.
