---
status: developing
created: 2026-06-03
updated: 2026-06-03
type: source
title: "PROJECT_STATE.md — KTG Content Pipeline Status (2026-05-26)"
slug: project-state
source_path: "PROJECT_STATE.md"
source_type: status-snapshot
ingested_at: 2026-05-27
tags: [source, pipeline, status, production, bash, python, publishing]
hash: md5:c3d4e5f6a7b8c9d0e1f2a3b4c5d6e7f8
---

# PROJECT_STATE.md — KTG Content Pipeline Status

> Snapshot date: 2026-05-26. Session goal was "Build Hub-Swarm (11-agent parallel content pipeline)." Actual achievement: 70% functional, usable now.

## Summary

Honest assessment of what the ktg-one content pipeline delivers vs. what was attempted. The 11-agent swarm was abandoned as overengineering. The bash template pipeline (`pipeline/run.sh`) ships content in 2 seconds at $0 cost. The Python AI framework (~2,000 lines) exists but is untested against real LLMs.

## Production-Ready Components

### pipeline/run.sh (Layer 4 — RUNTIME)
- **Status**: Fully functional
- **Runtime**: 2 seconds
- **Cost**: $0 (no API calls)
- **Output**: 8 files per post (the [[Publish-Kit-Pattern]])

### Publish Kit (8 files per post)
| File | Purpose |
|---|---|
| `linkedin.txt` | Professional article |
| `reddit.txt` | Discussion post |
| `x-thread.txt` | 8-post thread |
| `meta.txt` | Casual/emoji post |
| `medium.md` | Full article |
| `buffer.csv` | Bulk upload for Buffer |
| `review-checklist.md` | Quality gate |
| `all-image-prompts.md` | Google AI Studio prompts |

Example kit at: `pipeline/publish-kit/ai-agents-replace-engineers-2028/`

## Untested Components

### pipeline/ktg_pipeline/ (Python AI Framework)
- ~2,000 lines, 10 Python modules
- **4 LLM providers implemented** (Ollama, LM Studio, Google AI Studio, OpenRouter)
- **Untested**: actual LLM calls, prompt quality, error handling, output formatting
- Test command: `python pipeline/run.py input/test-post.md --provider ollama`

## Blocked / Not Built

| Feature | Status | Blocker |
|---|---|---|
| Auto-post to X | Impossible | X API $5K/month |
| Auto-post to Meta | Impossible | Business verification required |
| Auto-post to Medium | Hard | API read-only for most |
| Auto-post to LinkedIn | Possible | Needs [[Composio]] wiring |
| Auto-post to Reddit | Possible | Needs [[Composio]] wiring |
| Parallel execution | Not implemented | Sequential only |
| 11-agent swarm | Not built | Overengineering |

## Cost Analysis

| Scenario | Cost per post |
|---|---|
| Bash template (current) | $0 |
| Python + Ollama/5070 (local) | ~$0.01 electricity |
| Python + Google AI Studio | ~$0.02–$0.05 |
| Python + OpenRouter | Variable |

## Recommended Path Forward

**Option A — Ship Now (recommended):** Use `pipeline/run.sh`, generate images via Google AI Studio prompts, copy-paste to 5 platforms. Time: 30 min. Cost: $0.

**Option B — Polish Python:** Test `pipeline/run.py` with Ollama, fix broken prompts, add error handling. Time: 2–4 hrs. Cost: $0.

**Option C — Full Integration:** Wire [[Composio]] for LinkedIn/Reddit, add image generation (banana-claude or local 5070), build [[Review-Gate]] UI. Time: 1–2 days. Cost: $10–20.

## Lessons Learned
1. **11-agent swarm was overengineering** — Bash template is fast, reliable, $0
2. **Auto-post is mostly impossible** — X/Meta/Medium block APIs; copy-paste is the reliable path
3. **Local models (5070/NVFP4) are the future** — zero API cost, fast inference
4. **[[Publish-Kit-Pattern]] works** — humans review, humans publish, AI generates

## Verdict
- **MVP**: COMPLETE — can publish content today
- **Polish**: 70% — Python framework exists, needs testing
- **Auto-publish**: NOT POSSIBLE — platform APIs block it

## Cross-References
- [[ktg-one]] — project
- [[Five-Layer-Architecture]] — Layer 4 (runtime) and Layer 5 (publishing) described here
- [[Publish-Kit-Pattern]] — the 8-file distribution pattern
- [[Review-Gate]] — quality gate file in publish kit
- [[Composio]] — the blocked LinkedIn/Reddit integration path
- [[Pipeline-Verification-Criteria]] — the phase-based quality approach
