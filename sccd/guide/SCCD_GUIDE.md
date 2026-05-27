# SCCD Guide: Flow, Installation, Use-Cases

## What is SCCD?

**SCCD** = **S**elf → **C**onsciousness → **C**hoice → **D**ecide

A functional, computable model of decision-making. No metaphysics. No philosophy. Just math and code that works.

---

## 1. Installation

### Requirements
- Python 3.10+
- numpy

### Install
```bash
# Clone or copy the sccd/ directory
cd sccd/code

# Install dependencies
pip install numpy

# Run demo
python sccd.py
```

### As a Module
```python
from sccd import SCCD, SelfState, Consciousness, Choice, Decision

# Create agent
agent = SCCD(name="my_agent")

# Initialize self
agent.initialize_self(
    anchors={"goal": "complete_task", "context": "production"},
    weights={"goal": 1.0, "context": 0.5}
)
```

---

## 2. Flow: How SCCD Works

```
┌─────────┐     ┌─────────────┐     ┌─────────┐     ┌─────────┐
│  SELF   │────→│ CONSCIOUSNESS│────→│ CHOICE  │────→│ DECIDE  │
└─────────┘     └─────────────┘     └─────────┘     └─────────┘
     ↑                                               │
     └───────────────────────────────────────────────┘
                    (feedback loop)
```

### Step-by-Step

#### 1. SELF — Who Am I?
```python
self = SelfState(
    anchors={
        "system_prompt": "You are a helpful AI",
        "session_id": "abc123",
        "user_preference": "concise"
    },
    weights={"system_prompt": 1.0, "user_preference": 0.8}
)
```
- **Anchors**: Fixed points that give the system shape
- **Weights**: Importance of each anchor
- **Coherence**: How stable is the self? (0-1)

#### 2. CONSCIOUSNESS — What Could Happen?
```python
consciousness = Consciousness(simulation_depth=3)
consciousness.simulate(
    self_state=self,
    possible_actions=["answer", "ask_clarifying", "refuse"],
    transition_model=my_model,
    utility_fn=my_utility,
    n_trajectories=5
)
```
- Simulates 5 possible futures, each 3 steps deep
- Each trajectory = sequence of (action, predicted_state, utility)
- **Awareness**: How focused are the simulations? (0-1)
- **Entropy**: How uncertain? (lower = more focused)

#### 3. CHOICE — Which Path?
```python
choice = Choice()
choice.select(consciousness, strategy="softmax", temperature=0.5)
```
- Picks one trajectory from the simulation space
- **Commitment**: How confident in the choice? (0-1)
- **Negentropy**: Information gained by choosing (bits/nats)

#### 4. DECIDE — Do It
```python
decision = Decision()
decision.execute(choice, action_fn=my_action_function)
```
- Executes the first action of the chosen trajectory
- **Latency**: Time from choice to action (ms)
- **Consistency**: Did the action match the choice? (0-1)

---

## 3. Use Cases

### Use Case 1: AI Agent with Uncertainty
**Problem**: LLM needs to decide when to ask for clarification vs. answer directly.

```python
agent = SCCD(name="llm_agent", n_trajectories=10)
agent.initialize_self(anchors={"model": "gpt-4", "context_window": 8192})

# Actions
actions = ["answer_directly", "ask_clarifying", "search_knowledge", "delegate"]

# Transition model: predict user satisfaction
def transition(state, action):
    # Simulate: if ambiguous question + direct answer → low satisfaction
    return predicted_state

# Utility: user satisfaction + accuracy
def utility(state):
    return state["user_satisfaction"] * 0.6 + state["accuracy"] * 0.4

metrics = agent.cycle(actions, transition, utility, execute_action)
# If commitment < 0.5, the agent will ask for clarification
```

### Use Case 2: Resource Allocation
**Problem**: Distributed system needs to allocate CPU/memory.

```python
agent = SCCD(name="scheduler", simulation_depth=5)
agent.initialize_self(anchors={"cpu_available": 80, "memory_available": 60})

actions = ["allocate_to_A", "allocate_to_B", "queue_request", "reject"]

# Predict resource usage 5 steps ahead
# Choose allocation that maximizes throughput without overload
```

### Use Case 3: Self-Modifying Code
**Problem**: System needs to decide whether to update its own configuration.

```python
agent = SCCD(name="self_modifier")
agent.initialize_self(anchors={"current_version": "1.0", "uptime": 3600})

actions = ["update_now", "defer_update", "request_approval", "rollback"]

# Simulate: update might improve performance but risk downtime
# Choose based on stability vs. improvement tradeoff
```

### Use Case 4: Game AI
**Problem**: NPC needs to make tactical decisions.

```python
agent = SCCD(name="npc_tactical", n_trajectories=20)

actions = ["attack", "defend", "retreat", "flank", "use_ability"]

# Simulate 20 possible move sequences
# Choose based on predicted damage dealt vs. received
```

### Use Case 5: Content Pipeline (KTG Use Case)
**Problem**: Decide which content optimization to apply.

```python
agent = SCCD(name="content_optimizer")
agent.initialize_self(anchors={
    "post_topic": "AI tools",
    "target_platform": "blog",
    "seo_score": 75
})

actions = [
    "add_schema_markup",
    "optimize_headings",
    "generate_hero_image",
    "repurpose_for_x",
    "publish_as_is"
]

# Simulate: each action's effect on engagement, SEO, time cost
# Choose optimal sequence
```

---

## 4. Configuration

### Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `simulation_depth` | 3 | How many steps ahead to simulate |
| `n_trajectories` | 5 | How many futures to consider |
| `temperature` | 1.0 | Exploration vs. exploitation (higher = more random) |
| `choice_strategy` | "max_utility" | "max_utility", "softmax", "epsilon_greedy" |

### Strategies

**max_utility**: Always pick the best predicted outcome.
- Use when: High confidence in model, low noise
- Risk: Can get stuck in local optima

**softmax**: Probabilistic selection based on utility.
- Use when: Need exploration, uncertain environment
- Risk: Might pick suboptimal actions

**epsilon_greedy**: Mostly best, sometimes random.
- Use when: Need to discover new strategies
- Risk: Wasted actions on exploration

---

## 5. Metrics

### SCCD Score
Integrated score combining all four components:
```
SCCD_score = 0.25*self_stability + 0.25*consciousness_bandwidth + 0.25*choice_efficiency + 0.25*decision_fidelity
```

### Interpreting Metrics

| Metric | Good | Bad | Action |
|--------|------|-----|--------|
| Self coherence > 0.8 | Stable identity | Identity drift | Review anchors |
| Awareness > 0.7 | Focused simulation | Scattered attention | Reduce trajectories or increase depth |
| Commitment > 0.6 | Confident choice | Indecision | Gather more info or reduce options |
| Latency < 100ms | Fast execution | Slow action | Optimize action_fn |

---

## 6. Integration

### With LLMs
```python
# Use LLM as transition model
import openai

def llm_transition(state, action):
    prompt = f"State: {state}\nAction: {action}\nPredict next state:"
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return parse_state(response.choices[0].message.content)
```

### With Reinforcement Learning
```python
# Use RL policy as utility function
def rl_utility(state):
    return rl_agent.predict_value(state)

# SCCD becomes the "deliberation" layer on top of RL
```

### With Multi-Agent Systems
```python
# Each agent has its own SCCD
agents = [SCCD(name=f"agent_{i}") for i in range(10)]

# Shared consciousness: agents simulate each other's trajectories
shared_consciousness = merge_consciousness([a.consciousness for a in agents])
```

---

## 7. Troubleshooting

### Low Self Coherence
- **Cause**: Anchors changing too rapidly
- **Fix**: Increase anchor weights, add persistence threshold

### High Consciousness Entropy
- **Cause**: Too many trajectories or noisy model
- **Fix**: Reduce n_trajectories, improve transition model

### Low Commitment
- **Cause**: Utilities too similar or model uncertain
- **Fix**: Sharpen utility function, gather more information

### High Latency
- **Cause**: Action execution is slow
- **Fix**: Optimize action_fn, use async execution

---

## 8. Advanced

### Recursive SCCD
An SCCD agent can simulate other SCCD agents:
```python
# Agent A simulates Agent B's decision process
agent_b_simulation = SCCD(name="simulated_B")
agent_b_simulation.initialize_self(anchors={"role": "adversary"})

# Agent A's transition model includes B's predicted response
def transition_with_opponent(state, action):
    b_response = agent_b_simulation.cycle(...)
    return update_state(state, action, b_response)
```

### Hierarchical SCCD
Multiple SCCD layers operating at different timescales:
```python
# Fast layer: milliseconds (reflexes)
fast_sccd = SCCD(simulation_depth=1, n_trajectories=3)

# Medium layer: seconds (tactical)
medium_sccd = SCCD(simulation_depth=3, n_trajectories=10)

# Slow layer: minutes (strategic)
slow_sccd = SCCD(simulation_depth=10, n_trajectories=20)
```

---

*Version: 1.0.0 | Functional Model | No Metaphysical Claims*
