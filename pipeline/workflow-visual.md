# Full Workflow — Visual

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         INPUT: Blog Post                                │
│  pipeline/input/test-post.md                                            │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PHASE 1: REPURPOSE                                 │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │   Medium     │ │   Reddit     │ │   X Thread   │ │   LinkedIn   │   │
│  │  Full article│ │Conversational│ │  8 posts     │ │Professional  │   │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘   │
│  ┌──────────────┐                                                      │
│  │    Meta      │                                                      │
│  │Emoji+casual  │                                                      │
│  └──────────────┘                                                      │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PHASE 2: IMAGES                                    │
│  ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐   │
│  │    Hero      │ │  LinkedIn    │ │      X       │ │   Square     │   │
│  │   16:9       │ │   1.91:1     │ │    2:1       │ │    1:1       │   │
│  │Blog+Social   │ │Professional  │ │Bold/contrast │ │ Meta/Insta   │   │
│  └──────────────┘ └──────────────┘ └──────────────┘ └──────────────┘   │
│                                                                         │
│  Status: PROMPTS READY → Google AI Studio / Local 5070                 │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PHASE 3: SEO                                       │
│  • Title tag (60 chars)                                                 │
│  • Meta description (160 chars)                                         │
│  • Open Graph tags                                                      │
│  • Twitter Cards                                                        │
│  • Schema.org JSON-LD                                                   │
│  • Keyword targets                                                      │
│  • GEO optimization checklist                                           │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PHASE 4: ADS                                       │
│  • Google Search headlines + descriptions                               │
│  • Meta carousel concept                                                │
│  • LinkedIn Sponsored Content                                           │
│  • LinkedIn InMail template                                             │
│  • A/B test plan                                                        │
└──────────────────────────────┬──────────────────────────────────────────┘
                               │
                               ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      PHASE 5: PUBLISH KIT                               │
│  ┌─────────────────────────────────────────────────────────────────┐   │
│  │  publish-kit/ai-agents-replace-engineers-2028/                  │   │
│  │  ├── README.md          (quick start)                           │   │
│  │  ├── linkedin.txt       (copy-paste)                            │   │
│  │  ├── reddit.txt         (copy-paste)                            │   │
│  │  ├── x-thread.txt       (copy-paste)                            │   │
│  │  ├── meta.txt           (copy-paste)                            │   │
│  │  ├── medium.md          (import story)                          │   │
│  │  ├── buffer.csv         (bulk upload)                           │   │
│  │  ├── review-checklist.md(quality gate)                          │   │
│  │  └── all-image-prompts.md(Google AI Studio ready)               │   │
│  └─────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘

Total runtime: ~2 seconds
Total outputs: 8 files + 1 publish kit (9 files)
Manual work remaining: Copy-paste to platforms (10 min)
```
