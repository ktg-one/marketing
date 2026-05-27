# Team East – Judging scorecard

Use this to tick the boxes and apply deductions. Turbopack was fixed post‑delivery; logo and voice deductions stand.

---

## ✅ Turbopack — no penalty

- **Requirement:** `next dev --turbo` (mandatory).
- **Status:** Fixed during review. `package.json` now has `"dev": "next dev --turbo"` and `"build": "next build --turbo"`. Build and dev verified.
- **Deduction:** **0** (no minus for Turbopack).

---

## ❌ Logo — minus

- **Requirement:** Use the provided logo (your brand).
- **What they did:** Used `logo.svg` from battle assets in the header (icon + text “GoodAI Voice”). Typelogo / logo-dark not used. Where used: **tiny and out of contrast** (hard to see).
- **Deduction:** **___-10___** (didn't use typelogo; assets used are tiny and out of contrast)

---

## ❌ Voice demo — minus

- **Requirement:** Demo must use one of: **ElevenLabs**, **Groq TTS**, or **your voice agent** (API keys provided in top folder).
- **What they did:** Chose “Phone (08 7741 4191)” and implemented a simulated call + browser TTS only. Did not integrate ElevenLabs, Groq, or your voice agent.
- **Deduction:** **___-20___** (3x better options given to you groq api, eleven labs api, voice agent number/platform & No visualization whatsoever).

---

---

## 📊 FINAL SCORES

### Base Points (100 max):
- **Brand Compliance:** 15/25 (-10: didn't use typelogo; assets tiny/out of contrast)
- **Technical Implementation:** 15/25 (-10: Turbopack fixed post-delivery; missing features)
- **Demo Visualizer:** 5/20 (-15: didn't use Groq/ElevenLabs/voice agent API/phone; no Framer Motion; at least had browser TTS voice)
- **Design Quality:** 5/20 (-15: "one page powerpoint" — very basic)
- **Personality Consistency:** 0/10 (-10: no personality)

### Bonus Points:
- Innovation: 0
- Performance: 0
- Accessibility: 0
- Mobile Responsiveness: 0

### Penalties:
- **Broken functionality:** -30 (voice demo broken)

---

## 🎯 TOTAL: 15 + 15 + 5 + 5 + 0 - 30 = **10 points**

---

## ⚠️ Judge Note

**Both teams prove:** No one read the middle section where `.env` instructions were provided. Neither team used the API keys (ElevenLabs, Groq, voice agent) that were clearly documented.

**MCP/Skills violation:** MCP servers (Sequential Thinking, Context7, Playwright, Filesystem) were **MANDATORY** — "No one used MCP or battle tools last round. That is not allowed." Team East only used Filesystem (claimed), didn't use Playwright/Context7/Sequential Thinking. Team West: no evidence of MCP usage. Neither team used `shared-skills/` patterns (Next.js 16, Tailwind, Framer Motion, demo visualizer) that were provided.

**Regression:** These Round 3 team sites are **worse than Round 1 solo sites** from 2-3 generations ago. Round 1 solo agents built complete, polished sites (Hope Rising, QuantumLeap, LaunchPad, MarketFlow, Nexus AI) in **half an hour** — and those were "coded backwards" (meaning they were still better). Team collaboration made things worse, not better.
