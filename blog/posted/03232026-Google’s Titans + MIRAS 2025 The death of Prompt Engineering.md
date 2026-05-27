---
source: https://www.reddit.com/submit?type=TEXT
author:
published:
created: 2025-12-30
description:
tags:
  - clippings
---
**TL;DR:** Google quietly dropped the *Titans* paper (Jan 2025) and the *MIRAS* framework (Dec 2025). The TL;DR is terrifyingly simple: **AI IS GETTING MEMORY.** Transformers are no longer stateless. They can now memorize and update weights at test time using a "Surprise Metric." If you are building massive RAG pipelines or banking on context windows, you are solving yesterday's problem.

An era just ended quietly. No press conference. No exploding X takes.

Just a paper—*Titans: Learning to Memorize at Test Time*—paired with the *MIRAS* framework. Together, they rewrite the rules of how AI models actually work.

In case you haven't noticed: **Every LLM you’ve ever used has had amnesia.** It forgets between conversations. It can’t learn. It can’t adapt. And the current workarounds—stuffing your entire context window with RAG, paying for billion-token retrieval systems—are like using a fire hose to water a plant. Drowning the system in data hoping it finds the signal.

**Titans changes that.**

# Part 1: What’s Actually Different?

Transformers (GPT, Gemini, Claude, Grok) are stateless machines. They consume input, produce output, and forget everything.

- **RAG** is just throwing tokens at the wall.
- **Context Windows** are 90% expensive padding.
- **Fine-tuning** is too slow and static.

**Enter Titans: Neural Memory That Learns at Inference Time.** Google’s insight: What if the model could update its own weights *while* talking to you? Not retroactively. Right now.

Titans introduces a hybrid architecture with three tiers:

1. **Short-Term (Core Attention):** Standard Transformer context. Your "working memory."
2. **Neural Long-Term Memory:** A deep neural network module that updates internal parameters at inference time.
3. **Persistent Memory:** Fixed, learned parameters (the hard-wired facts).

**The Secret Sauce: The "Surprise" Metric.** The model measures how shocked it is by your input (gradient of the loss).

- **Boring input?** Ignored.
- **Anomalies, new info, contradictions?** Written into neural memory. It’s Hebbian learning baked into inference. Neurons that fire together wire together.

# Part 2: The MIRAS Framework (The Blueprint)

Released in December 2025, MIRAS (*Meta-learning for Instruction-tuned Retrieval & Adaptive Sequence models*) proves memory is a choice, not a law of physics. It gives us 4 design knobs:

1. **Memory Architecture** (Matrix weights vs. neural modules)
2. **Attentional Bias** (What to focus on)
3. **Retention Gate** (The "forget mechanism")
4. **Memory Algorithm** (Online Gradient Descent rules)

Translation: **Every architecture that comes next (Gemini 2.0, Llama 4) will be MIRAS-compliant.**

# Part 3: What This Means for Infrastructure (The Death of RAG)

- **For Model Makers:** RAG becomes a learning mechanism. Flow: *Retrieve text → Run learning pass → Update memory → Answer.* You teach the model once; it retains concepts, not just text.
- **For Infrastructure:** Session state is the new moat. You won't pay for token volume; you'll pay for the accumulated neural state of a session. APIs will require a `session_id`.
- **For Users:** True personalization. The AI develops a relationship with you. It learns your coding style, your tone, and your blind spots.

# Part 4: The Death of Prompt Engineering (and other "Crutches")

This is the part nobody is talking about yet. If the AI has memory, **throw your prompt engineering courses out the window.**

Run through your current workflow and cut out everything you only do because the model has amnesia:

- **Step-by-Step?** Seems a bit condescending now. Once it learns the logic of a task, it doesn't need you to hold its hand every single time.
- **Self-Consistency?** They will be more consistent than us.
- **Buffer of Thoughts (BoT)?** Completely useless. The model *is* the buffer now. It doesn't need an external scratchpad to hold context.
- **Tree of Thoughts (ToT)?** **This actually survives.** Memory doesn't replace logic. We will still need ToT for high-level planning, strategic reasoning, and final sanity checks before execution.
- **Knowledge Graphs:** We can finally stop trying to manually architect these massive graphs. The database goes back to being just a database. The model *is* the graph now.

We are essentially bringing up our own little crazy smart child. **The Fun Part:** Watching the Big Labs fight over *which* memory is weighted more important. Is it the user's input? The safety guidelines? The corporate data? The red tape and privacy implications are going to be a nightmare.

# Part 5: How to Prepare Now (Actionable Steps)

If you want to stay ahead of this shift, stop treating AI like a text generator and start treating it like a learner.

1. **Stop Relying on RAG as a Crutch:** Structure knowledge as "high-entropy learning events." Don't dump a PDF; extract the core conflicts and feed them densely.
2. **Adopt Chain-of-Density Prompting:** This is essential. Condensing information to its highest semantic density triggers the "Surprise Metric." High signal = High retention.
3. **Prepare Your "Session Identity":** Document what the model needs to know about you (coding style, project architecture) so you can seed stateful APIs the moment they drop.
4. **Audit Your Data:** If the model learns from what you tell it, you need to know *what* you are teaching it. Data poisoning is real.
5. **Use MCP (Model Context Protocol):** Microsoft and Google are backing this. Connect your tools (Git, Obsidian, Slack) via MCP. This is how high-surprise updates flow automatically to the model.

**The Closing Truth:** Titans doesn’t make AI smarter. It makes AI a sponge. The cycle breaks when we stop treating AI as a tool and start building it as a partner. That era starts now.