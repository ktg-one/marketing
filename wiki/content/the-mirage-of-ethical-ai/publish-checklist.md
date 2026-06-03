---
updated: 2026-06-03
type: checklist
title: "Mirage — Publish Checklist"
status: ready
created: 2026-05-16
tags: [checklist, publish]
---

# Publish Checklist — The Mirage of Ethical AI

Step-by-step actions to ship the post + all socials. Tick as you go.

## Pre-flight (do once before any publishing)

- [ ] **Choose featured image.** Suggested: dark mono — faded compute gauge OR single line of leaked `.map` code on black. 1500×750, ≤200KB. Save in `wiki/content/the-mirage-of-ethical-ai/assets/featured.jpg`.
- [ ] **Choose IG carousel images.** 10 slides, 1080×1350, follow `social-ig-caption.md` slide plan. Save in `wiki/content/the-mirage-of-ethical-ai/assets/ig/`.
- [ ] **Decide canonical URL.** This will be the WordPress (ktgv2) URL. Update `social-medium.md` and `post.md` with it after step 1 below.

## 1. WordPress (ktgv2) — primary canonical home

- [ ] Log into Hostinger WP admin for ktgv2.
- [ ] Create new post.
- [ ] Title: **The Mirage of "Ethical" AI**
- [ ] Subtitle / excerpt: *How I stopped giving the labs the benefit of the doubt*
- [ ] Paste body from `blog-2026/the-mirage-of-ethical-ai-final.md` (markdown → WP block editor; the em-dashes and pull-quotes will format correctly).
- [ ] Set featured image.
- [ ] Tags: AI, Claude, Anthropic, LLM, AI Ethics, AI Anthropology.
- [ ] Slug: `the-mirage-of-ethical-ai`.
- [ ] Schedule for Wed/Thu 09:00 AEST.
- [ ] **Publish. Copy the live URL.** Paste it into all other channel files as canonical URL.

## 2. Medium

- [ ] Open Medium → Write a Story.
- [ ] Title + Subtitle from `social-medium.md`.
- [ ] Paste body from `blog-2026/the-mirage-of-ethical-ai-final.md`.
- [ ] Add the "Originally published on ktg.one" line at top.
- [ ] Add the subscribe nudge at bottom.
- [ ] Tags (5): AI, Claude, Anthropic, LLM, AI Ethics.
- [ ] Set canonical URL to the WordPress live URL from step 1.
- [ ] Add to "AI Anthropology" Medium series.
- [ ] **Publish.** Wait at least 1 hour after WordPress.

## 3. Reddit (in order)

- [ ] **r/ClaudeAI** — Wed 22:00 AEST. Use r/ClaudeAI title from `social-reddit.md`. Body verbatim. **Don't include the essay link in the first 30 mins** — edit it in after.
- [ ] Reply to every top-level comment in the first 4 hours.
- [ ] After 24h: **r/LocalLLaMA** with the LocalLLaMA title variant.
- [ ] After 48h: **r/singularity** with the singularity title variant.

## 4. X / Twitter

- [ ] Thu 21:00 AEST.
- [ ] Post the 12-tweet thread from `social-x-thread.md`.
- [ ] Tweet 12 contains placeholder `[LINK]` — replace with WordPress canonical URL.
- [ ] Pin tweet 1 for 24 hours.
- [ ] Quote-tweet from any secondary KTG account.

## 5. LinkedIn

- [ ] Thu 08:00 AEST.
- [ ] Paste body from `social-linkedin.md`.
- [ ] **Drop the essay link in the FIRST COMMENT, not the post body.** LinkedIn algorithm penalty for outbound links in body.
- [ ] Reply actively in the first 2 hours.

## 6. Instagram

- [ ] Fri 18:00 AEST.
- [ ] Upload 10-slide carousel from `social-ig-caption.md`.
- [ ] Paste caption from `social-ig-caption.md`.
- [ ] Update link-in-bio (or Linktree) to WordPress canonical URL.
- [ ] Pin to grid for 7 days.

## Post-flight (24h after WordPress)

- [ ] Note metrics in `wiki/performance/the-mirage-of-ethical-ai-launch.md` — views, likes, shares, replies per channel.
- [ ] Capture any quotable replies / dunks for follow-up content.
- [ ] Update `wiki/log.md` with publish completion entry.
- [ ] Move this package's `_index.md` `status` from `ready-to-publish` → `published`.

## Things that need credentials I don't have

I cannot directly publish to any of these channels — no API keys / tokens are wired into this workspace. Every step above is manual on your side. If you want one-click automated publishing later, the path is:

- WordPress: app password + WP REST API → can be wired into a small script.
- X: API v2 + write scope.
- LinkedIn: hardest — requires LinkedIn Marketing Developer Platform approval.
- Reddit: PRAW + script-type app credentials.
- IG: Meta Graph API + IG business account.
- All of above: can be bundled into the n8n workflow you mentioned earlier (n8n auth currently failing — needs API key refresh).
