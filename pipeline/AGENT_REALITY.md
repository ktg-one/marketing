# Agent Spawn Reality Check

## What I Actually Have Access To

I have the `Agent` tool in my toolkit. It can spawn sub-agents with:
- `subagent_type`: "coder", "explore", "plan"
- `model`: can specify different models
- `run_in_background`: true/false

## Limitations

| Constraint | Reality |
|------------|---------|
| Max parallel agents | Unknown (probably 3-5 safely) |
| Cost per agent | Full context window per spawn |
| 11 agents × $0.50 | ~$5-10 just for orchestration |
| API support | Kimi may not support Agent tool |

## Test: Can I Spawn Even One Agent?

Let me try spawning a single test agent first.
