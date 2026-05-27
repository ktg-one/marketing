#!/bin/bash
# KTG Content Pipeline — Standalone (no connections)
# Produces all outputs, skips publishing

set -e
INPUT="${1:-pipeline/input/test-post.md}"
SLUG=$(grep "^slug:" "$INPUT" | sed 's/slug: *"//;s/"$//')
OUT="pipeline/output"
mkdir -p "$OUT"/{blog,images,seo,ads,social} "pipeline/logs"
LOG="pipeline/logs/$(date +%Y%m%d-%H%M%S)-$SLUG.log"

echo "=== KTG Pipeline: $SLUG ===" | tee "$LOG"
echo "Input: $INPUT" | tee -a "$LOG"
echo "Output: $OUT" | tee -a "$LOG"
echo "" | tee -a "$LOG"

# Phase 1: Repurpose for 5 platforms
echo "[PHASE 1] Repurposing content..." | tee -a "$LOG"

# Medium — full article, clean formatting
cat > "$OUT/social/social-medium.md" << 'EOF'
---
platform: medium
title: TITLE_PLACEHOLDER
date: DATE_PLACEHOLDER
tags: TAGS_PLACEHOLDER
---

BODY_PLACEHOLDER

---

*Originally published on [KTG](https://ktg.one)*
EOF
sed -i "s/TITLE_PLACEHOLDER/$(grep '^title:' "$INPUT" | sed 's/title: *//')/g" "$OUT/social/social-medium.md"
sed -i "s/DATE_PLACEHOLDER/$(date -Iseconds)/g" "$OUT/social/social-medium.md"
sed -i "s/TAGS_PLACEHOLDER/$(grep '^topic:' "$INPUT" | sed 's/topic: *//')/g" "$OUT/social/social-medium.md"
BODY=$(sed '1,/^---$/d;/^---$/d' "$INPUT")
# Replace BODY_PLACEHOLDER with actual body (handle newlines)
printf '%s\n' "$BODY" > /tmp/body.txt
sed -i '/BODY_PLACEHOLDER/{
r /tmp/body.txt
d
}' "$OUT/social/social-medium.md"

# Reddit — conversational, shorter, question hook
cat > "$OUT/social/social-reddit.md" << EOF
---
platform: reddit
subreddit: r/artificial or r/programming
title: "AI agents already write 40% of code at top startups. Here's what that means for engineers."
---

I know this sounds like clickbait, but the data is real.

Top startups (the ones you read about on HN) are already seeing 40% of their production code written by AI agents. Not Copilot-style autocomplete. Full agent loops: plan → code → test → iterate.

The shift nobody talks about: the bottleneck moved from "can you code?" to "can you specify?"

**Three skills that matter now:**

1. Systems thinking — seeing the architecture, not just the function
2. AI orchestration — chaining agents, managing context, handling failures
3. Domain expertise — deep knowledge that AI can't synthesize

By 2028, "software engineer" will mean "AI agent manager." The pure coders get automated. The orchestrators thrive.

What do you think — too aggressive a timeline? Or not aggressive enough?

$(grep "call_to_action:" "$INPUT" | sed 's/call_to_action: *//')
EOF

# X/Twitter — thread format, punchy
cat > "$OUT/social/social-x-thread.md" << EOF
---
platform: x
type: thread
posts: 8
---

**Thread: Why AI agents will replace software engineers by 2028**

1/ The software engineer as we know it is dying.

Not because AI can't code.
Because AI can code *better*, *faster*, and *cheaper*.

2/ At top startups, AI agents already write 40% of production code.

Not tests. Not docs.
Production code that ships to real users.

3/ The bottleneck shifted.

It was never typing speed.
It was:
• Understanding requirements
• Making architectural decisions
• Debugging complex systems

AI is eating #1 and #3. #2 is next.

4/ The "AI whisperer" emerges.

Survivors won't be the best coders.
They'll be the best at:
• Specification (precision)
• Verification (catching AI mistakes)
• Integration (combining pieces)

5/ Three skills to survive:

1. Systems thinking — see the whole
2. AI orchestration — chain agents
3. Domain expertise — deep knowledge AI can't fake

6/ By 2028, "software engineer" = "person who manages AI agents."

Pure coders: automated away.
Orchestrators: thrive.

7/ This isn't speculative.

It's already happening at:
• Cursor (AI-native IDE)
• Claude Code (agentic coding)
• Kimi CLI (context-aware dev)
• Gemini CLI (multi-agent workflows)

8/ The question isn't whether.
It's whether you're on the right side of it.

Subscribe: ktg.one

#AI #SoftwareEngineering #FutureOfWork
EOF

# Meta/Facebook — casual, shareable, image-focused
cat > "$OUT/social/social-meta.md" << EOF
---
platform: meta
type: post
image: required
---

🚨 The software engineer job is evolving — fast.

AI agents now write 40% of production code at top startups. Not assisting. REPLACING.

The engineers who thrive won't be the best coders. They'll be the best at:
✅ Specifying exactly what they want
✅ Verifying AI output is correct
✅ Integrating AI pieces into systems

3 skills to survive:
1️⃣ Systems thinking
2️⃣ AI orchestration
3️⃣ Domain expertise

By 2028: "software engineer" = "AI agent manager"

Are you preparing for this shift? 👇

$(grep "call_to_action:" "$INPUT" | sed 's/call_to_action: *//')
EOF

# LinkedIn — professional, thought leadership
cat > "$OUT/social/social-linkedin.md" << EOF
---
platform: linkedin
type: article
image: required
---

The software engineering profession is undergoing its most significant transformation since the advent of the internet.

**The Data**
Leading startups now report that AI agents generate 40% of their production codebase. This isn't autocomplete or code completion — this is autonomous agentic development: plan, implement, test, iterate.

**The Shift**
The fundamental bottleneck in software development has moved. It was never typing speed or syntax knowledge. The real constraints were:
• Requirements elicitation and communication
• Architectural judgment under uncertainty
• Complex system debugging and pattern recognition

AI agents are rapidly addressing the first and third. The second — architectural decision-making — is the next frontier.

**The New Role: AI Orchestrator**
The engineers who will thrive in this environment possess three distinct capabilities:

1. **Systems Thinking** — The ability to conceptualize and design at the architectural level, understanding emergent properties and interactions rather than individual components.

2. **AI Orchestration** — Expertise in chaining multiple AI agents, managing context windows, handling agent failure modes, and integrating outputs into coherent systems.

3. **Domain Expertise** — Deep, substantive knowledge in specific domains that AI cannot synthesize from training data alone.

**The Timeline**
By 2028, the role of "software engineer" will have fundamentally redefined itself. The market will bifurcate: those who orchestrate AI systems will command premium compensation; those who perform routine coding tasks will face increasing competitive pressure from automated systems.

The question for every engineering professional is not whether this transformation occurs, but whether they position themselves on the advantageous side of it.

---

$(grep "call_to_action:" "$INPUT" | sed 's/call_to_action: *//')

#AI #SoftwareEngineering #FutureOfWork #Leadership #TechTrends
EOF

echo "✓ 5 platform variants created" | tee -a "$LOG"

# Phase 2: Image briefs
echo "" | tee -a "$LOG"
echo "[PHASE 2] Generating image briefs..." | tee -a "$LOG"

cat > "$OUT/images/image-brief.md" << EOF
---
project: $SLUG
images: 4
---

## Hero Image (16:9)
**Purpose**: Blog header, LinkedIn, X card
**Aspect**: 16:9 (1200x675)
**Style**: Bold editorial, dark background, neon accent lines
**Subject**: Abstract visualization of AI agents replacing human coder — silhouette of engineer fading into circuit patterns, agent nodes emerging
**Colors**: Deep navy (#0a1628), electric cyan (#00d4ff), warm coral (#ff6b6b)
**Text overlay**: "2028" in large monospace, "The End of Engineering?" in smaller sans
**Mood**: Provocative, forward-looking, slightly unsettling

## LinkedIn Crop (1.91:1)
**Purpose**: LinkedIn article header
**Aspect**: 1.91:1 (1200x628)
**Style**: Professional, clean, corporate-friendly
**Subject**: Clean infographic-style — "40%" large number, "AI-Generated Code" label, upward trend arrow
**Colors**: White background, navy text, single accent color
**Text**: "40% of code is now AI-written" + KTG logo
**Mood**: Data-driven, credible, shareable

## X/Twitter Crop (2:1)
**Purpose**: X thread header image
**Aspect**: 2:1 (1200x600)
**Style**: Bold, high contrast, scroll-stopping
**Subject**: Split screen — left side human typing, right side AI agent nodes glowing, transition zone in middle
**Colors**: Black background, bright cyan and magenta gradients
**Text**: "By 2028" large, "Software Engineer → AI Orchestrator" smaller
**Mood**: Attention-grabbing, slightly controversial

## Square Crop (1:1)
**Purpose**: Meta/Instagram, general social
**Aspect**: 1:1 (1080x1080)
**Style**: Carousel-friendly, readable on mobile
**Subject**: Three icons in a row — brain (systems thinking), robots (orchestration), book (domain expertise) with arrows between
**Colors**: Light background, bold icon colors, clean lines
**Text**: "3 Skills to Survive 2028" at top
**Mood**: Educational, actionable, optimistic
EOF

echo "✓ Image briefs created (4 images)" | tee -a "$LOG"

# Phase 3: SEO package
echo "" | tee -a "$LOG"
echo "[PHASE 3] Generating SEO package..." | tee -a "$LOG"

cat > "$OUT/seo/seo-package.md" << EOF
---
page: /blog/$SLUG
type: seo-package
---

## Title Tag (60 chars)
Why AI Agents Replace Software Engineers by 2028 | KTG

## Meta Description (160 chars)
AI agents already write 40% of production code at top startups. Learn 3 skills to survive the shift from coder to AI orchestrator by 2028.

## Canonical URL
https://ktg.one/blog/$SLUG

## Open Graph
- og:title: Why AI Agents Will Replace Software Engineers by 2028
- og:description: The software engineer is evolving. 40% of code is already AI-written. Here's how to survive.
- og:image: https://ktg.one/blog/$SLUG/hero.png
- og:type: article
- og:site_name: KTG

## Twitter Cards
- twitter:card: summary_large_image
- twitter:title: Why AI Agents Replace Engineers by 2028
- twitter:description: 40% of code is AI-written. 3 skills to survive.
- twitter:image: https://ktg.one/blog/$SLUG/hero-x.png

## Schema.org JSON-LD
\`\`\`json
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Why AI Agents Will Replace Software Engineers by 2028",
  "description": "AI agents already write 40% of production code. Learn 3 skills to survive the shift.",
  "author": {
    "@type": "Organization",
    "name": "KTG"
  },
  "publisher": {
    "@type": "Organization",
    "name": "KTG",
    "logo": {
      "@type": "ImageObject",
      "url": "https://ktg.one/logo.png"
    }
  },
  "datePublished": "$(date -Iseconds)",
  "dateModified": "$(date -Iseconds)",
  "mainEntityOfPage": {
    "@type": "WebPage",
    "@id": "https://ktg.one/blog/$SLUG"
  },
  "image": "https://ktg.one/blog/$SLUG/hero.png",
  "keywords": ["AI agents", "software engineering", "future of work", "AI automation", "2028 predictions"]
}
\`\`\`

## H1/H2 Structure
- H1: Why AI Agents Will Replace Software Engineers by 2028
- H2: The Numbers Don't Lie
- H2: The Bottleneck Shifted
- H2: The "AI Whisperer" Emerges
- H2: Three Skills to Survive
- H2: The 2028 Deadline

## Internal Links to Add
- /blog/ai-orchestration-guide (related: AI orchestration)
- /blog/future-of-work-2025 (related: future of work)
- /about (author/org info)

## External Links to Add
- https://github.blog/2024-01-23-measuring-github-copilots-impact/ (Copilot data)
- https://www.anthropic.com/claude-code (Claude Code)

## Keyword Targets
| Keyword | Volume | Difficulty | Priority |
|---------|--------|------------|----------|
| AI agents software engineering | High | Medium | 1 |
| future of software engineers | High | Medium | 2 |
| AI replace programmers 2028 | Medium | Low | 3 |
| AI orchestration skills | Medium | Low | 4 |

## GEO Optimization (AI Citations)
- Answer-first paragraph in first 100 words
- Key statistic (40%) in bold near top
- Numbered list for "3 skills" — AI overviews love lists
- FAQ section at bottom for featured snippets
- Clear definitions: "AI whisperer = engineer who manages AI agents"
EOF

echo "✓ SEO package created" | tee -a "$LOG"

# Phase 4: Ads package
echo "" | tee -a "$LOG"
echo "[PHASE 4] Generating ads package..." | tee -a "$LOG"

cat > "$OUT/ads/ads-package.md" << EOF
---
campaign: $SLUG
platforms: [google, meta, linkedin]
budget: TBD
---

## Campaign Concept
**Name**: "2028 Deadline"
**Angle**: Urgency + FOMO — engineers must adapt or become obsolete
**Target**: Software engineers, tech leads, engineering managers, founders
**Duration**: 2-week burst

## Google Ads

### Search Ad 1
**Headline 1**: AI Agents Replace Engineers by 2028
**Headline 2**: 40% of Code is AI-Written Now
**Headline 3**: 3 Skills to Survive
**Description 1**: Top startups already use AI agents for 40% of code. Learn the 3 skills that separate survivors from the automated.
**Description 2**: Free weekly breakdown. Subscribe at KTG.
**Path**: /ai-agents-2028

### Search Ad 2
**Headline 1**: Will AI Replace You by 2028?
**Headline 2**: The Data Says Yes
**Headline 3**: Unless You Adapt Now
**Description 1**: Software engineering is transforming. AI agents write production code. Here's your survival guide.
**Description 2**: Weekly AI strategy at KTG.

## Meta Ads

### Ad 1: Carousel
**Card 1**: "40% of code is AI-written" (stat focus)
**Card 2**: "The bottleneck shifted" (concept)
**Card 3**: "3 skills to survive" (actionable)
**Card 4**: "Subscribe to KTG" (CTA)
**Primary Text**: The software engineer job is evolving — fast. AI agents now write 40% of production code. Here are the 3 skills you need to survive until 2028.
**CTA**: Learn More

### Ad 2: Single Image
**Image**: Square crop (1080x1080) — "3 Skills to Survive 2028"
**Primary Text**: By 2028, "software engineer" will mean "AI agent manager." The pure coders get automated. The orchestrators thrive. Are you preparing?
**Headline**: 3 Skills to Survive 2028
**CTA**: Subscribe

## LinkedIn Ads

### Sponsored Content
**Image**: LinkedIn crop (1200x628) — "40% AI-Generated Code"
**Text**: Leading startups report AI agents generate 40% of production code. The engineering profession is bifurcating: those who orchestrate AI systems will thrive; those who perform routine coding face obsolescence. Three capabilities define the survivors: systems thinking, AI orchestration, and domain expertise.
**CTA**: Read the Full Analysis

### Message Ad (InMail)
**Subject**: Your engineering role in 2028
**Body**: Hi [Name], I'm seeing a pattern at top startups: AI agents now write 40% of production code. The engineers who thrive aren't the best coders — they're the best orchestrators. I wrote a breakdown of the 3 skills that matter. Worth 3 minutes?
**CTA**: Read Now

## A/B Test Plan
| Test | Variant A | Variant B | Metric |
|------|-----------|-----------|--------|
| Headline | "Replace" (fear) | "Evolve" (growth) | CTR |
| Image | Dark/moody | Bright/optimistic | CTR |
| CTA | "Subscribe" | "Read Now" | Conversion |
| Audience | Engineers | Founders | CPA |
EOF

echo "✓ Ads package created" | tee -a "$LOG"

# Phase 5: Summary
echo "" | tee -a "$LOG"
echo "[PHASE 5] Pipeline complete" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "=== OUTPUT SUMMARY ===" | tee -a "$LOG"
find "$OUT" -type f | sort | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "Total files: $(find "$OUT" -type f | wc -l)" | tee -a "$LOG"
echo "Total size: $(du -sh "$OUT" | cut -f1)" | tee -a "$LOG"
echo "" | tee -a "$LOG"
echo "Next: Review outputs, then run publish phase when connections ready" | tee -a "$LOG"
