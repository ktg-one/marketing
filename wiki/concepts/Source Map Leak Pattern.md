---
type: concept
status: developing
created: 2026-05-16
updated: 2026-05-16
tags: [concept, security, npm, release-engineering]
---

# Source Map Leak Pattern

A specific failure mode where a vendor ships TypeScript/JavaScript source maps (`.map` files) to a public package registry because the build artifact wasn't excluded in `.npmignore` (or equivalent). Source maps reverse the bundling, exposing original source.

## Canonical example

[[Anthropic]] [[Claude Code]], **2026-03-31**:

- Trigger: `*.map` not in `.npmignore`
- Exposure: 512,000 lines of TypeScript across 1,900 files shipped to npm
- Velocity: mirrored 40,000 times in hours
- Downstream: clean-room rewrite hit 75,000 GitHub stars in 2 hours
- Context: a known bug filed three weeks earlier was still open
- Compound: this was Anthropic's *second* accidental exposure that week — a draft blog post about an unreleased model called "Mythos" had been left publicly accessible days earlier

## Why it matters beyond IP loss

Once a complex agentic system's source is public, every previously-internal capability becomes inspectable, citable, and scrutinisable. In the Anthropic case the leak revealed:

- [[KAIROS]] (always-on autonomous daemon)
- [[autoDream]] (background memory consolidation)
- [[Conway]] (always-on agent platform)
- [[Undercover Mode]] (attribution-stripping contribution mode)
- [[Anti-Distillation]] (poisoning competitor training)
- BUDDY (gacha terminal pet)

…none of which were public-facing features and several of which had governance implications the vendor had not disclosed.

## Mitigation

- `.npmignore` audits in CI before publish
- Build-step verification that no `.map`, `.d.ts.map`, `.js.map` files are in the publish artifact
- Source-map upload to error-tracking SaaS (Sentry, Bugsnag) instead of bundling

## Related

- [[Anthropic]] — case subject
- [[Claude Code]] — the leaked product
- [[Always-On AI Daemons]] — concept the leak surfaced

## Sources

- [[the-mirage-of-ethical-ai]]
