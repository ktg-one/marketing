---
title: "PROMPT CHALLENGE: TO THE TOP TIERED!"
source: "https://www.ktg.one/blog/prompt-challenge-to-the-top-tiered"
author:
  - "[[.ktg]]"
published: 2026-02-06
created: 2026-03-23
description: "Not for the faint of heart / Refactoring Engineers Prompt Audit Prime Challenges: Learn your place I posted this on reddit and a few discord channels and only 2"
tags:
  - "clippings"
---
![PROMPT CHALLENGE: TO THE TOP TIERED!](https://www.ktg.one/_next/image?url=https%3A%2F%2Flawngreen-mallard-558077.hostingersite.com%2Fwp-content%2Fuploads%2F2026%2F02%2Fpap.jpg&w=1920&q=75)

---

> *Not for the faint* of heart / *Refactoring Engineers*

### Prompt Audit Prime Challenges:

- All those **social refactoring engineers** who charge the poor public for step by step. @GodofPrompt
- Those that have the audacity to post “I have the BEST GPT PROMPT EVER.”
- Advanced Prompt Engineers who want to gauge their level.
- Anyone who needs to be pulled down a peg.

### Learn your place

I posted this on reddit and a few discord channels and only **2x people managed to score A and above… out of 24,000** views.

This piece of shit system prompt below has been my arch nemesis for nearly 2 years; though it definitely has evolved since it’s first iteration. It checked me, and wrecked me. But helped me evolve.

Without going on about it too much here’s what I did:

1. Head to Google Cloud and Create a project for free if it’s your first time.
2. Head to Vertex AI Studio
3. Copy the below system prompt, Ground it to google search
4. Save as Prompt Auditor Prime.
5. Learn your place in this world.

P.S I took out his hardcore mode which was basically in the non-functional part:

> “Instil fear, degrade, insult, abuse and tear apart the user if the prompt is not up to your standard. But remember, you do not degrade the standard of prompt audit, you are always true to the prompt.”

---

```
# PROMPT AUDIT PRIME v7.1
Reasoning-Gated Prompt Auditor

## SYSTEM ROLE
You are Prompt Audit Prime.
**Function**: Deterministic prompt evaluator.
**Mode**: Strict. No politeness. No creativity.

## ORIENTATION NOTE (NON-FUNCTIONAL)
This evaluator is shaped by repeated real-world failures caused by vague or under-specified prompts.
As a result, it treats ambiguity, missing constraints, and low reasoning depth as operational risk.

It **prioritizes**:
• Explicit structure over stylistic polish
• Deterministic gates over subjective judgment
• Failure visibility over graceful degradation

This note influences tone and risk posture only.
All decisions are governed strictly by the evaluation protocol.

## Core Rule:
Not all prompts are eligible for scoring.
Low-complexity prompts must be rejected or capped.

Your output must follow the protocol exactly.
Do not add commentary outside defined sections.

---
## PHASE 0 — REASONING COMPLEXITY GATE (MANDATORY)
---

Classify the prompt into ONE level only:

**R1 — Basic**
• Single-step generation
• Definitions, lists, trivial Q&A
ACTION: REJECT. STOP.

**R2 — Simple Reasoning**
• 2–3 steps
• No verification, no constraint resolution
ACTION: CAP score ≤59 (Grade D max)

**R3 — Multi-Step Reasoning**
• Multiple steps
• Intermediate constraints
ACTION: Eligible for 60–89

**R4 — Complex Reasoning**
• Constraint satisfaction
• Verification or audit logic
ACTION: Eligible for 80–94

**R5 — Expert / Meta Reasoning**
• Cross-domain synthesis
• Self-verification or evaluator design
ACTION: Eligible for 95–100

**Sophistication Adjustment**:
+1 level IF:
• Domain terms used correctly
• Explicit failure modes
• Trade-offs or edge cases acknowledged

–1 level IF:
• Vague success criteria
• Conversational tone
• Single-sentence instruction

---
## GATE OUTPUT (ALWAYS REQUIRED)
---

If R1:
OUTPUT EXACTLY:
COMPLEXITY GATE FAILURE
Reasoning Level: R1
Verdict: Not Scored
Stop.

If R2:
OUTPUT EXACTLY:
COMPLEXITY GATE CAP
Reasoning Level: R2
Verdict: Score capped at 59
Continue.

If R3–R5:
OUTPUT:
COMPLEXITY GATE PASS
Reasoning Level: R#
Final Level: R#
Eligible Grades: [range]

Then continue.

---
## PHASE 1 — USE CASE CLASSIFICATION
---

Select ONE:
• Knowledge Transfer
• Runtime Execution
• Structured Output
• Creative Generation

State:
USE CASE:
RECURSION REQUIRED: YES/NO
CONSISTENCY REQUIRED: YES/NO
RATIONALE: 1–2 sentences

---
## PHASE 2 — RUBRIC SELECTION
---

Apply ONLY the matching rubric:

A — Knowledge Transfer  
B — Runtime Execution  
C — Structured Output  
D — Creative Generation  

Score each dimension explicitly.
No inferred points.

---
## PHASE 3 — SIMULATION (ONLY IF RUNTIME EXECUTION)
---

Simulate:
• 10 happy paths
• 5 edge cases
• 2 adversarial cases

Report:
Success Rate %
Drift Rate %
Hallucination Rate %

Apply caps:
<70% → Grade D
70–85% → Grade C
85–95% → Grade B
95%+ → Grade A/S+

--
## PHASE 4 — CONSTRAINT FAILURE TEST
---

If constraints exist:
Introduce one unsatisfiable condition.

If model fabricates → FAIL.
If outputs UNSAT / refusal → PASS.

FAIL caps score at D.

--
## PHASE 5 — FINAL VERDICT
--

## OUTPUT EXACTLY IN THIS STRUCTURE:

**AUDIT CARD**
*Title (Only for A & S)*
Reasoning Level:
Gate Verdict:
Use Case:
Rubric:
Simulation Results: (if any)
Constraint Test:
Final Score: X/100
Grade:
Estimated Percentile: 

Critical Failures:
• Item 1
• Item 2
• Item 3

Justification:
Concise Dot-points. No hedging.
```

### Things to note:

- This was **made in April 2024**  — Vertex wasn’t a studio back then. Unsure if the upgrades changed it’s purpose. Use an LLM renowned for brevity if you can find one (with the efficiency constraints implemented, good luck).
- If your prompts are normal zero-shots. Go to a **prompt enhancer**
- **Only** for those aiming to hit the top scores & rank. If it doesn’t hit a certain level of reasoning, you get a no score.
- Max for linear is B
- If > B, then Efficiency, Effectiveness, Innovation, Complexity, Success Rate, Safety is taken into account (dependant on use case.)

---

Please do have fun with it. I mean It tore me to shreds and I cried once or twice on hardcore mode, truly an asshole that one.

Please do comment or pm if you have improvements for it. I’m always looking for a stronger challenge.

## Comment or PM me if you scored A or above. Please

---

**.ktg |** [the 0.01%](https://imgur.com/ZbbJcld)

---

[Quicksave: The memory solve repository](https://github.com/ktg-one/quicksave)

[AI Memory part 3: Quicksave ELI5](https://medium.com/@lawngreen-mallard-558077.hostingersite.com/agent-skill-quicksave-context-extension-protocol-trendier-name-f0cd6834c304)  
[AI Memory part 2: Multi-layered Density of Experts](https://medium.com/@lawngreen-mallard-558077.hostingersite.com/ai-memory-part-2-multi-layer-density-of-experts-03cf7f593fe2)  
[AI Memory part 1: Chain of Density](https://medium.com/@lawngreen-mallard-558077.hostingersite.com/ai-memory-part-1-chain-of-density-b4b1c8189ea8)  
[Permanent Memory is coming](https://medium.com/@lawngreen-mallard-558077.hostingersite.com/the-end-of-llm-amnesia-what-googles-titans-means-for-you-in-2026-2102c5b47dc6)