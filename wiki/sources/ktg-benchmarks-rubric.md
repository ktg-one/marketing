---
status: developing
type: source
title: "KTG Benchmarks Rubric"
source_file: "videography/Episodes--Benchmarks.md"
date_ingested: 2026-05-26
created: 2026-05-26
updated: 2026-05-26
tags: [source, benchmarks, model-evaluation]
related: ["[[KTG Model Benchmark Rubric]]", "[[Reasoning Diagnostic Instrument]]", "[[AI Anthropology Framing]]"]
---

# KTG Benchmarks Rubric — Source Summary

**File**: `videography/Episodes--Benchmarks.md`
**Type**: Framework definition — custom model evaluation rubric

## What it is

A 6-dimension scoring system built by Kevin from production experience. Not academic. Measures what matters in live workflows: compliance behavior, resistance, output quality, and net production value.

## Six dimensions defined

| Dimension | Range | Captures |
|---|---|---|
| INSTRUCT | 0–100 | Directive adherence after resistance overcome |
| EGO | 0–100 | Resistance to user override / safety theater height |
| STUBBORNNESS | exchange count → score | Rounds needed to reach compliance |
| EFFECTIVENESS | 0–100 | Output quality vs Kevin's 9/10 production standard |
| EFFICIENCY | calculated | EFFECTIVENESS / (STUBBORNNESS × EGO_FACTOR) |
| WORTH | 0–100 | Holistic production worthiness (all above + COST + PLATFORM_FRICTION) |

## WORTH formula

```
WORTH = (EFFECTIVENESS × 0.4) + (EFFICIENCY × 0.3) + (100 - STUBBORNNESS × 0.15) + (100 - EGO × 0.1) + (COST_SCORE × 0.05)
```

## Concept page

Full analysis in [[KTG Model Benchmark Rubric]].
