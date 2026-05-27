---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, ai-labs, governance, degradation]
---

# Silent Compute Cuts

The pattern of AI labs degrading model capability without acknowledgement — no announcement, no migration guide, no status page, no email. Workflows that worked yesterday silently stop working today.

## Canonical example

[[Anthropic]] / [[Claude Code]], December 2025: an 18-step cascade workflow built over two years collapses to less than 1 step overnight. From [[the-mirage-of-ethical-ai]]:

> Not broken — *retired*. The model could no longer sustain the chains. Eighteen steps collapsed to not even one. No announcement. No migration guide. No "hey, we changed something fundamental about how this works." Just silence.

## Compounding mechanisms

The cut typically isn't one switch. From the Anthropic case:

1. Default thinking effort silently reduced (e.g. value 85 = "medium"). Model skips deep reasoning on tasks it judges simple. Misjudges constantly.
2. Peak-hour throttling layered on top.
3. Caching bugs silently inflate token costs 10–20×.
4. Off-peak promotional pricing expires without renewal.

Net effect: users burn more tokens failing than they used to spend succeeding.

## Detection signals

- Existing long workflows degrade without code or prompt changes
- Same prompts produce shallower outputs than they did weeks prior
- Token bills climb without throughput climbing
- Bug tracker shows compaction-failure clusters (250k API calls/day wasted globally in the cited Anthropic case)
- Single user reports show calendar-month usable days collapsing (e.g. 12/30 days for one Pro subscriber)
- Senior-engineer GitHub issues with hundreds of session files closed without explanation (e.g. AMD case, 6,852 sessions, March 8 cliff)

## Governance gap

> [!gap] Communication channels
> Official communication during the Anthropic incident was limited to personal tweets from individual engineers and a handful of Reddit comments. No blog post, no email, no status page.

## Related

- [[Ethics as Branding]] — the meta-pattern this serves
- [[Anthropic]] — case subject
- [[Claude Code]] — the affected product
- [[anthropic-2026-q1-degradation]] — full intel snapshot

## Sources

- [[the-mirage-of-ethical-ai]]
