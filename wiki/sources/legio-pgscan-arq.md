---
status: developing
type: source
title: "LEGIO-10: PGScan + ARQ — Post-Execution Gap Scan & Quality Gates"
source_file: "videography/Episodes--MOE - EAST VS WEST.md"
date_ingested: 2026-05-26
created: 2026-05-26
updated: 2026-05-26
tags: [source, legio, framework, quality-gate, execution-module]
related: ["[[STRAWHATS-DIRECTIVE]]", "[[Cognitive Architecture (Prompt-Only)]]"]
---

# LEGIO-10: PGScan + ARQ — Source Summary

**File**: `videography/Episodes--MOE - EAST VS WEST.md`
**Note**: File is mislabeled — content is LEGIO framework documentation, not an MoE episode script.
**Type**: LEGIO execution module spec (Module 10, Phase: EXECUTION)
**Version**: LEGIO v30.2

## What it is

PGScan (Post-Execution Gap Scan) + ARQ Gate 3. The execution zone exit checkpoint before content passes to Censor (LEGIO-11). Companion to CoVE (LEGIO-09): *"CoVE checks if you're right. PGScan checks if you're complete."*

## Three failure types PGScan catches (that CoVE misses)

1. **Logic gaps** — valid reasoning with missing steps
2. **Content gaps** — questions asked but never answered, dangling references
3. **Value gaps** — fluff present, signal absent, wrong tone

## 3-Branch scan

| Branch | Detects | Auto-Fix |
|---|---|---|
| A: LOGIC | Chain breaks, circular logic, contradictions | Add connectors, reorder flow |
| B: CONTENT | Unanswered questions, incomplete coverage | Add sections, resolve references |
| C: VALUE | Fluff, redundancy, low signal-to-noise | Cut fluff, add concrete examples |

## Mode activation (depth tiers)

| Mode | Branches | Depth |
|---|---|---|
| Velites | None | Skip — direct to output |
| Hastati | A only | Light — logic check, flag only |
| Principes | A + B + C | Standard — auto-fix minor, flag major |
| Triarii | A + B + C + cross-validation | Deep — multi-expert review, cross-candidate synthesis |

## ARQ Gate 3 checklist

- All Legatus nodes elaborated?
- All reasoning chains complete?
- All user questions addressed (or flagged)?
- Signal-to-noise ratio ≥ 0.6?
- All auto-fixable gaps repaired?
- Confidence ≥ mode threshold? (Velites 0.6 → Triarii 0.9)

Gate is advisory for Velites/Hastati; firm for Principes (HALT on ≥2 failures); hard for Triarii (HALT on ANY failure).

## Pipeline position

Receives from: CoVE (LEGIO-09), Legatus (LEGIO-05), Imperatus (LEGIO-00), USC (LEGIO-03).
Feeds: Censor (LEGIO-11).
Referenced by: Self-Reflect (LEGIO-12) for gap pattern learning.

## Token overhead

- Hastati (Branch A): +5%
- Principes (All 3): +12%
- Triarii (Deep + cross-val): +18%
- Net quality improvement over CoVE-only: +10–20%

## Framework home

LEGIO lives in `C:/Users/kevin/knowledge2026/Projects-Coding/LEGIO/`. This module is part of the v30.2 spec. See [[STRAWHATS-DIRECTIVE]] for the top-level KTG cognitive architecture.
