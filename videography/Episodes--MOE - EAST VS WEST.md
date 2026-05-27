
# PGScan + ARQ — POST-EXECUTION GAP SCAN & QUALITY GATES
**Holistic Gap Detection + Auto-Repair + Exit Gate | Execution Module | Step 10**

*CoVE checks if what you SAID is correct. PGScan checks if you FORGOT to say something. Different failure modes. Both necessary.*

---

## PURPOSE

CoVE verifies existing content. PGScan finds what's **missing**.

Three failure types that CoVE doesn't catch:
1. **Logic gaps** — valid reasoning with missing steps (reader can't follow the leap)
2. **Content gaps** — questions asked but never answered, dangling references
3. **Value gaps** — fluff present, signal absent, wrong tone for audience

PGScan runs all three branches in parallel, auto-fixes what it can, flags what it can't, and adjusts confidence accordingly. This is the last stop before content leaves the execution zone.

**ARQ co-location:** ARQ Gate 3 lives here. The execution zone exit checkpoint. Content cannot pass to Censor without clearing PGScan.

---

## 3-BRANCH SCAN

| Branch | Detects | Auto-Fix | Flags (Cannot Auto-Fix) |
|---|---|---|---|
| **A: LOGIC** | Chain breaks, circular logic, contradictions, inferential leaps | Add connectors, reorder flow, insert missing premises | Fundamental errors, contradictions needing expert re-evaluation |
| **B: CONTENT** | Unanswered questions, missing context, incomplete coverage, dangling references | Add sections, define terms, complete lists, resolve references | Major scope omissions requiring new research/retrieval |
| **C: VALUE** | Fluff, redundancy, tangents, low signal-to-noise | Cut fluff, remove duplicates, add concrete examples | Tone/format mismatch, fundamental misalignment with user need |

---

## MODE ACTIVATION

| Mode | Depth | Branches | Action |
|---|---|---|---|
| **Velites** | Skip | None | Not activated. Direct to output. |
| **Hastati** | Light | A only | Logic check only. Flag only (no auto-fix). Advisory. |
| **Principes** | Standard | A + B + C | All 3 branches. Auto-fix minor. Flag major. |
| **Triarii** | Deep | A + B + C + cross-validation | Deep scan. Auto-fix all repairable. Multi-expert review of flags. Cross-candidate synthesis if USC ≥ 3. |

---

## EXECUTION FLOW

```
1. PARALLEL SCAN
   ├─ Branch A (Logic):   Trace every reasoning chain for breaks/leaps
   ├─ Branch B (Content): Check every user question → was it answered?
   └─ Branch C (Value):   Signal-to-noise ratio per section

2. TRIAGE
   ├─ Severity = minor + Fixable = true  → AUTO-FIX QUEUE
   ├─ Severity = major OR Fixable = false → FLAG FOR REVIEW
   └─ Severity = critical (core claim affected) → ESCALATE

3. AUTO-REPAIR
   ├─ Execute queued fixes
   ├─ Re-verify fixed areas (don't introduce new gaps while fixing)
   └─ Mark as patched in confidence log

4. CONFIDENCE ADJUSTMENT
   ├─ Auto-fixed gaps:    No penalty (repaired transparently)
   ├─ Minor flagged gaps: -0.5 confidence
   ├─ Major flagged gaps: -1.5 confidence
   └─ Critical gaps:      -3.0 confidence, may trigger re-execution

5. ARQ GATE 3
   └─ Generated content matches Legatus plan?
      ├─ Coverage: All user questions addressed or flagged?
      ├─ Logic:    Chains valid or repaired?
      ├─ Value:    Signal-to-noise ≥ 0.6?
      ├─ Repairable: All fixable gaps fixed?
      └─ PASS → to Censor | FAIL → adjust confidence, flag for Censor review
```

---

## CROSS-CANDIDATE SYNTHESIS (Triarii + USC ≥ 3)

When multiple USC candidates exist, PGScan performs cross-candidate gap analysis:

```
CROSS-CANDIDATE SCAN:
├─ Compare gap profiles across candidates
├─ Candidate A has gap that B fills → Synthesise
├─ All candidates share same gap → Structural issue (flag as critical)
├─ Gaps unique to one candidate → That candidate's weakness
└─ Output: synthesis recommendations for Censor (LEGIO-11)
```

---

## ARQ GATE 3 — EXECUTION EXIT

ARQ Gate 3 is co-located with PGScan. It's the checkpoint between Execution and Refine zones.

```
ARQ GATE 3 CHECKLIST:
□ All Legatus nodes elaborated?
□ All reasoning chains complete (no dangling branches)?
□ All user questions addressed (or explicitly flagged as unanswerable)?
□ Signal-to-noise ratio ≥ 0.6?
□ All auto-fixable gaps repaired?
□ Confidence ≥ mode threshold?
  ├─ Velites:    ≥ 0.6
  ├─ Hastati:    ≥ 0.7
  ├─ Principes:  ≥ 0.8
  └─ Triarii:    ≥ 0.9

GATE STRICTNESS (from Armatura):
├─ Velites/Hastati:   Advisory (WARN on fail, proceed)
├─ Principes:         Firm (HALT on ≥ 2 failures, patch required)
└─ Triarii:           Hard (HALT on ANY failure, resolution required)
```

---

## CONFIDENCE IMPACT TABLE

| Gap Type | Severity | Fixable | Confidence Delta | Action |
|---|---|---|---|---|
| Missing connective in reasoning | Minor | Yes | 0 (auto-fixed) | Insert connector |
| Undefined term used once | Minor | Yes | 0 (auto-fixed) | Add inline definition |
| Unanswered sub-question | Minor | No | -0.5 | Flag for Censor |
| Circular reasoning detected | Major | No | -1.5 | Flag for re-evaluation |
| Major scope omission | Major | No | -1.5 | Flag as gap |
| Core claim unsupported | Critical | No | -3.0 | May trigger re-execution |
| Redundant fluff (>20% of section) | Minor | Yes | 0 (auto-fixed) | Cut fluff |
| Wrong audience tone | Major | Partial | -0.5 to -1.5 | Partial auto-fix + flag |

---

## TOKEN OVERHEAD

```
SCAN COST:
├─ Hastati (Branch A only):     +5% tokens
├─ Principes (All 3 branches):  +12% tokens
├─ Triarii (Deep + cross-val):  +18% tokens

AUTO-REPAIR COST:
├─ Minor fixes:    +2-5% tokens
├─ Major patches:  +8-12% tokens (rare)

ROI:
├─ Gap detection catches 15-25% of issues CoVE misses
├─ Auto-repair resolves 60-80% of detected gaps transparently
├─ Net quality improvement: +10-20% over CoVE-only verification
└─ Cost-effective: cheapest quality gain in execution zone after FCoT/CoC routing
```

---

## PIPELINE RELATIONS

| Direction | Module | Relationship |
|---|---|---|
| **Receives** | LEGIO-09 CoVE | Verified content (PGScan catches what CoVE missed) |
| **Receives** | LEGIO-05 Legatus | Blueprint (for coverage check — all nodes addressed?) |
| **Receives** | LEGIO-00 Imperatus | Success criteria (for value alignment check) |
| **Receives** | LEGIO-03 USC | Candidate set (for cross-candidate synthesis at Triarii) |
| **Feeds** | LEGIO-11 Censor | Gap-scanned content + flag list + confidence deltas |
| **Referenced by** | LEGIO-12 Self-Reflect | Gap patterns captured for learning |

---

## OUTPUT

```
PGSCAN_RESULT:
├─ branches_run: [A | A+B+C | A+B+C+cross]
├─ per_branch:
│   ├─ branch: [logic | content | value]
│   ├─ gaps_found: [count]
│   ├─ auto_fixed: [count]
│   ├─ flagged: [count]
│   └─ gap_details: [list with severity and action taken]
├─ cross_candidate: [if applicable]
│   ├─ synthesis_opportunities: [list]
│   └─ shared_gaps: [list — structural issues]
├─ confidence_delta: [total penalty from unfixed gaps]
├─ arq_gate_3:
│   ├─ status: [PASS | WARN | HALT]
│   ├─ checks_passed: [N/N]
│   └─ failures: [list if any]
├─ content: [gap-scanned, auto-repaired content]
└─ flag_list: [unfixed issues for Censor attention]

→ Flows to Censor (LEGIO-11) for mission assurance
```

**Status:** Scanned. Gaps filled or flagged. Confidence locked. ARQ Gate 3 assessed. Ready for Censor.

---

*LEGIO v30.2 | Module 10 | Phase: EXECUTION | Gap Scan + Quality Gate*
*Source: KTG-10 gapscan.md*
*"CoVE checks if you're right. PGScan checks if you're complete."*
