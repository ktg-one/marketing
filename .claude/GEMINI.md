# KTG Marketing Funnel: Architectural Map

This document defines the behavioral "Stitch" between the global LLM Wiki and the local execution plugins. Adhere to this sequence when automating marketing workflows.

## The Behavioral Chain (Funnel Sequence)

1.  **The Idea (Start Here)**
    *   **Source:** `wiki/concepts/` (Global Obsidian / LLM Wiki).
    *   **Role:** Capture raw intent and Karpathy-style conceptual notes.
    *   **Tool:** `wiki` and `save` skills.

2.  **The Ad Concept (Claude Azzedine)**
    *   **Action:** `/ads create`
    *   **Handoff:** Transforms the "Idea" into a structured `campaign-brief.md`.
    *   **Source of Truth:** All downstream content must align with this brief.

3.  **The Content Strategy (Claude Blog)**
    *   **Action:** `/blog strategy` → `/blog brief`.
    *   **Stitch:** Reads `campaign-brief.md` to generate topic clusters and outlines that maintain campaign scent.

4.  **The Authority Loop (Claude SEO)**
    *   **Action:** `/blog seo-check` (Pre-writing) → `/seo` (Post-publishing).
    *   **Stitch:** Uses shared Google API credentials (`google-api.json`) to validate authority and ranking gains for the "Idea".

5.  **The Visual Impact (Claude Image)**
    *   **Action:** `/hub` or `/ads generate`.
    *   **Engine:** `banana` skill (Gemini Nano) + `high-end-visual-design` rules.
    *   **Output:** High-end design assets and premium infographics derived from the original data.

## Shared Connective Tissue

-   **`campaign-brief.md`**: The primary data bridge between Ads and Blog.
-   **`google-api.json`**: The shared credential bridge between Blog and SEO.
-   **`brand-profile.json`**: The visual/voice DNA used by the `banana` engine for design consistency.

---
*Built by Reverse Engineering the KTG Plugin Ecosystem.*
