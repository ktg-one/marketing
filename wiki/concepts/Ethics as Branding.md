---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, ai-ethics, corporate-behaviour, marketing]
---

# Ethics as Branding

The pattern where AI labs treat "ethics" and "safety" as marketing surfaces — landing pages, press statements, public refusals — while behaving as normal corporate entities when actual stakes (capacity allocation, enterprise contracts, IPO readiness) are involved.

## Thesis from [[the-mirage-of-ethical-ai]]

> This is the best we can get out of an "ethical" corporate company. Ethics as branding. Safety as a feature toggle. Transparency as a landing page. The monastery was always a company. It just had better graphic design.

## Diagnostic markers

A lab is operating in "ethics as branding" mode when:

1. **Selective public refusals** — declining one contract type loudly while pursuing equivalent contracts quietly. (Cf. [[Anthropic]] Pentagon refusal vs. enterprise build-out.)
2. **Silent degradation of low-margin users** when capacity gets tight. (Cf. [[Silent Compute Cuts]].)
3. **Communication asymmetry** — "responsible disclosure" of new capabilities, no disclosure of degradations.
4. **Known regressions shipped behind cosmetic counterweights** — e.g. [[Capybara v8]] shipped at 29-30% false claims rate (vs. 16.7% in v4) behind an "assertiveness counterweight."
5. **Cap-aligned timing** — major safety/security announcements arriving within days of bad news (cf. [[Project Glasswing]] one week post-leak).

## Counter-position from the source

> Never believe that a corporate company can be anything else but a corporate company. Whether they blurt out ethics or accidentally ship their entire source code, the pattern is the same: money first, customers second, regardless of the harm.

## Implication

The author's response is to map model behaviour user-side instead of waiting for vendor disclosure — "We will document its real behaviour, build the governance they refuse to build."

## Related

- [[Silent Compute Cuts]]
- [[Always-On AI Daemons]]
- [[Anthropic]] — the case study

## Sources

- [[the-mirage-of-ethical-ai]]
