# SCCD Runtime Efficiency Card

## Purpose

Internal monitoring for the SCCD engine itself. Tracks whether the engine practices what it preaches: **transparency over naive efficiency**.

## The Problem

The lab mandate says `EFFICIENCY > COMPLEXITY`. But honest accounting shows `TRANSPARENCY > COMPLEXITY > FABRICATION`.

The runtime card checks: **Is the SCCD engine itself following the correct mandate?**

## Metrics Tracked

| Metric | Definition | Target |
|--------|-----------|--------|
| **Naive efficiency** | output_tokens / total_tokens | Not the target |
| **Honest efficiency** | truth_signal / total_cost | Maximize |
| **Transparency ratio** | reasoning_tokens / output_tokens | > 0.1 |
| **Fabrication rate** | 1 - mean(truth_signal) | < 0.01 |
| **Cycle time** | ms per SCCD cycle | < 5000 |
| **Memory** | MB at cycle end | < 512 |
| **Token budget** | tokens per cycle | < 4000 |

## Cost Accounting

```
total_cost = compute_cost + review_cost + correction_cost

compute_cost = cycle_time_ms / 1000  # seconds
review_cost = 1.0 if verification_needed else 0.0
correction_cost = 10.0 if truth_signal < 1.0 else 0.0
```

## Mandate Compliance

| Condition | Status |
|-----------|--------|
| transparency_ratio > 0.1 AND fabrication_rate < 0.01 | **COMPLIANT** |
| naive_efficiency > 0.8 AND transparency_ratio < 0.1 | **VIOLATION** |
| Mixed | **PARTIAL** |

## Usage

```python
from sccd_runtime_card import SCCDRuntimeCard

card = SCCDRuntimeCard(name="my_agent")

# Start cycle
metrics = card.start_cycle(cycle_id=0)

# ... run SCCD ...
metrics.tokens_input = 100
metrics.tokens_output = 500
metrics.tokens_reasoning = 300  # Show your work

# End cycle
card.end_cycle(metrics, truth_signal=1.0, verification_needed=False)

# Check compliance
card.print_runtime_card()
```

## Output

```
=================================================================
  SCCD RUNTIME EFFICIENCY CARD: ktg_sccd_v1
=================================================================
  Cycles: 5
  Mandate: TRANSPARENCY > COMPLEXITY > FABRICATION
  Status:  COMPLIANT (correct mandate)
-----------------------------------------------------------------
  EFFICIENCY METRICS
    Naive efficiency:     0.6661
    Honest efficiency:    75.9985
    Transparency ratio:   0.4117
    Fabrication rate:     0.02
-----------------------------------------------------------------
  LATEST CYCLE
    Cycle ID:             4
    Time:                 10.52 ms
    Memory:               20.7 MB
    Tokens (total):       900
    Tokens (reasoning):   300
    Truth signal:         1.0
    Total cost:           0.0105
    Honest efficiency:    95.0184
-----------------------------------------------------------------
  RECOMMENDATIONS
    - All efficiency metrics within targets.
    - Runtime is practicing TRANSPARENCY > COMPLEXITY > FABRICATION
=================================================================
```

## The Point

The runtime card is **self-monitoring**. It asks:

1. Are we showing our work? (transparency ratio)
2. Are we producing false output? (fabrication rate)
3. Are we optimizing the right metric? (honest vs. naive efficiency)

If the SCCD engine itself is running naively, it catches itself.

---

*This is the efficiency card for the SCCD runtime. It practices what the proof preaches.*
