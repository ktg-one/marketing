"""
SCCD: Self-Consciousness-Choice-Decide Model
Functional implementation for AI systems

No metaphysical claims. All operations are computable and measurable.
"""

from __future__ import annotations

import numpy as np
from typing import Callable, List, Dict, Any, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum, auto
import json
from datetime import datetime


class SCCDState(Enum):
    """Operational states of the SCCD cycle."""
    IDLE = auto()
    SELF_UPDATING = auto()
    SIMULATING = auto()
    CHOOSING = auto()
    DECIDING = auto()
    ACTING = auto()
    COMPLETE = auto()


@dataclass
class SelfState:
    """
    SELF: The anchored boundary of identity.
    
    For AI: anchors = {system_prompt, memory_weights, config, session_state}
    For humans: anchors = {body_state, memories, preferences, beliefs}
    """
    anchors: Dict[str, Any] = field(default_factory=dict)
    weights: Dict[str, float] = field(default_factory=dict)
    timestamp: float = field(default_factory=lambda: datetime.now().timestamp())
    
    def coherence(self) -> float:
        """Measure of self-stability. 1.0 = perfectly stable."""
        if not self.weights:
            return 0.0
        total_weight = sum(abs(w) for w in self.weights.values())
        if total_weight == 0:
            return 0.0
        # Normalized L2 norm of weights
        l2_norm = np.sqrt(sum(w**2 for w in self.weights.values()))
        return l2_norm / (l2_norm + 0.01)  # Soft ceiling at ~1.0
    
    def persistence(self, other: SelfState, threshold: float = 0.7) -> bool:
        """Check if self persists across time (Jaccard similarity)."""
        keys_self = set(self.anchors.keys())
        keys_other = set(other.anchors.keys())
        if not keys_self and not keys_other:
            return True
        intersection = len(keys_self & keys_other)
        union = len(keys_self | keys_other)
        jaccard = intersection / union if union > 0 else 0.0
        return jaccard >= threshold
    
    def update(self, new_anchors: Dict[str, Any], new_weights: Optional[Dict[str, float]] = None):
        """Update self with new information."""
        self.anchors.update(new_anchors)
        if new_weights:
            self.weights.update(new_weights)
        self.timestamp = datetime.now().timestamp()
    
    def to_vector(self) -> np.ndarray:
        """Flatten self to vector for computation."""
        # Simple hash-based encoding for demonstration
        values = []
        for k in sorted(self.anchors.keys()):
            v = self.anchors[k]
            if isinstance(v, (int, float)):
                values.append(float(v))
            elif isinstance(v, str):
                values.append(hash(v) % 10000 / 10000.0)
            else:
                values.append(0.5)
        for k in sorted(self.weights.keys()):
            values.append(self.weights.get(k, 0.0))
        return np.array(values, dtype=np.float32)


@dataclass
class Trajectory:
    """
    A simulated future path through state space.
    """
    actions: List[Any] = field(default_factory=list)
    predicted_states: List[np.ndarray] = field(default_factory=list)
    utilities: List[float] = field(default_factory=list)
    probability: float = 1.0
    
    def total_utility(self, gamma: float = 0.95) -> float:
        """Discounted sum of utilities."""
        return sum(u * (gamma ** i) for i, u in enumerate(self.utilities))
    
    def first_action(self) -> Any:
        """The action to take now (first step)."""
        return self.actions[0] if self.actions else None


@dataclass
class Consciousness:
    """
    CONSCIOUSNESS: Predictive recursive modeling.
    
    Simulates multiple future trajectories and evaluates them.
    """
    trajectories: List[Trajectory] = field(default_factory=list)
    simulation_depth: int = 3
    temperature: float = 1.0
    
    def simulate(
        self,
        self_state: SelfState,
        possible_actions: List[Any],
        transition_model: Callable[[np.ndarray, Any], np.ndarray],
        utility_fn: Callable[[np.ndarray], float],
        n_trajectories: int = 5
    ) -> None:
        """
        Generate simulated trajectories.
        
        Args:
            self_state: Current self
            possible_actions: Available actions
            transition_model: f(state, action) -> next_state
            utility_fn: R(state) -> scalar utility
            n_trajectories: Number of trajectories to simulate
        """
        self.trajectories = []
        current_vector = self_state.to_vector()
        
        # Sample action sequences (simplified: single actions for now)
        for _ in range(min(n_trajectories, len(possible_actions))):
            action = np.random.choice(possible_actions)
            trajectory = Trajectory()
            state = current_vector.copy()
            
            for step in range(self.simulation_depth):
                # Predict next state
                next_state = transition_model(state, action)
                # Compute utility
                utility = utility_fn(next_state)
                
                trajectory.actions.append(action)
                trajectory.predicted_states.append(next_state)
                trajectory.utilities.append(utility)
                
                state = next_state
                # For simplicity, same action continues (can extend to policy)
            
            self.trajectories.append(trajectory)
    
    def entropy(self) -> float:
        """Measure of uncertainty in simulations. Higher = more uncertain."""
        if not self.trajectories:
            return 0.0
        
        # Softmax over utilities
        utilities = np.array([t.total_utility() for t in self.trajectories])
        probs = np.exp(utilities / self.temperature)
        probs = probs / np.sum(probs)
        
        # Shannon entropy
        entropy = -np.sum(probs * np.log(probs + 1e-10))
        return float(entropy)
    
    def awareness(self) -> float:
        """Consciousness intensity: 1 / (1 + entropy). Higher = more focused."""
        H = self.entropy()
        return 1.0 / (1.0 + H)
    
    def contains_self(self, self_state: SelfState, epsilon: float = 0.1) -> bool:
        """Check if self is represented in all trajectories."""
        self_vec = self_state.to_vector()
        for traj in self.trajectories:
            for state in traj.predicted_states:
                distance = np.linalg.norm(state - self_vec)
                if distance > epsilon:
                    return False
        return True


@dataclass
class Choice:
    """
    CHOICE: The prune/collapse operator.
    
    Selects one trajectory from the simulation space.
    """
    chosen_trajectory: Optional[Trajectory] = None
    commitment: float = 0.0
    negentropy_produced: float = 0.0
    
    def select(
        self,
        consciousness: Consciousness,
        strategy: str = "max_utility",
        temperature: float = 1.0
    ) -> Trajectory:
        """
        Choose one trajectory from simulated options.
        
        Args:
            consciousness: The simulation space
            strategy: "max_utility", "softmax", "epsilon_greedy"
            temperature: Exploration parameter
        """
        if not consciousness.trajectories:
            raise ValueError("No trajectories to choose from")
        
        trajectories = consciousness.trajectories
        utilities = np.array([t.total_utility() for t in trajectories])
        
        if strategy == "max_utility":
            idx = np.argmax(utilities)
            self.chosen_trajectory = trajectories[idx]
            self.commitment = 1.0
            
        elif strategy == "softmax":
            probs = np.exp(utilities / temperature)
            probs = probs / np.sum(probs)
            idx = np.random.choice(len(trajectories), p=probs)
            self.chosen_trajectory = trajectories[idx]
            self.commitment = probs[idx]
            
        elif strategy == "epsilon_greedy":
            if np.random.random() < temperature:  # epsilon = temperature
                idx = np.random.randint(len(trajectories))
            else:
                idx = np.argmax(utilities)
            self.chosen_trajectory = trajectories[idx]
            self.commitment = 0.8 if idx == np.argmax(utilities) else 0.3
        
        # Calculate negentropy produced
        n_options = len(trajectories)
        self.negentropy_produced = np.log(n_options) if n_options > 0 else 0.0
        
        return self.chosen_trajectory
    
    def is_committed(self, threshold: float = 0.5) -> bool:
        """Check if choice is firm enough to act on."""
        return self.commitment >= threshold


@dataclass
class Decision:
    """
    DECIDE: The action of choice.
    
    Executes the chosen trajectory's first action.
    """
    action_taken: Any = None
    latency_ms: float = 0.0
    consistency: float = 1.0
    
    def execute(
        self,
        choice: Choice,
        action_fn: Callable[[Any], Any],
        timeout_ms: float = 5000.0
    ) -> Any:
        """
        Execute the chosen action.
        
        Args:
            choice: The choice to enact
            action_fn: Function that performs the action
            timeout_ms: Maximum time to wait
        """
        if not choice.chosen_trajectory:
            raise ValueError("No trajectory chosen")
        
        action = choice.chosen_trajectory.first_action()
        if action is None:
            raise ValueError("Chosen trajectory has no actions")
        
        import time
        start = time.time()
        
        try:
            result = action_fn(action)
            self.action_taken = action
            self.consistency = 1.0
        except Exception as e:
            result = None
            self.consistency = 0.0
            raise RuntimeError(f"Action execution failed: {e}")
        
        elapsed = (time.time() - start) * 1000
        self.latency_ms = min(elapsed, timeout_ms)
        
        return result


class SCCD:
    """
    Main SCCD engine: Self → Consciousness → Choice → Decide
    """
    
    def __init__(
        self,
        name: str = "sccd_agent",
        simulation_depth: int = 3,
        n_trajectories: int = 5,
        temperature: float = 1.0,
        choice_strategy: str = "max_utility"
    ):
        self.name = name
        self.self_state = SelfState()
        self.consciousness = Consciousness(simulation_depth=simulation_depth)
        self.choice = Choice()
        self.decision = Decision()
        self.state = SCCDState.IDLE
        
        # Configuration
        self.n_trajectories = n_trajectories
        self.temperature = temperature
        self.choice_strategy = choice_strategy
        
        # Metrics
        self.cycle_count = 0
        self.metrics_history: List[Dict] = []
    
    def initialize_self(self, anchors: Dict[str, Any], weights: Optional[Dict[str, float]] = None):
        """Set up the self-boundary."""
        self.self_state = SelfState(anchors=anchors, weights=weights or {})
        self.state = SCCDState.IDLE
    
    def cycle(
        self,
        possible_actions: List[Any],
        transition_model: Callable[[np.ndarray, Any], np.ndarray],
        utility_fn: Callable[[np.ndarray], float],
        action_fn: Callable[[Any], Any]
    ) -> Dict[str, Any]:
        """
        Run one full SCCD cycle.
        
        Returns metrics and state information.
        """
        import time
        cycle_start = time.time()
        
        # 1. SELF (implicit: already loaded)
        self.state = SCCDState.SELF_UPDATING
        
        # 2. CONSCIOUSNESS: Simulate futures
        self.state = SCCDState.SIMULATING
        self.consciousness.simulate(
            self_state=self.self_state,
            possible_actions=possible_actions,
            transition_model=transition_model,
            utility_fn=utility_fn,
            n_trajectories=self.n_trajectories
        )
        
        # 3. CHOICE: Select trajectory
        self.state = SCCDState.CHOOSING
        self.choice.select(
            consciousness=self.consciousness,
            strategy=self.choice_strategy,
            temperature=self.temperature
        )
        
        # 4. DECIDE: Execute
        self.state = SCCDState.DECIDING
        if self.choice.is_committed():
            self.state = SCCDState.ACTING
            result = self.decision.execute(
                choice=self.choice,
                action_fn=action_fn
            )
        else:
            result = None
            self.decision.consistency = 0.0
        
        # 5. Update self with outcome
        self.self_state.update(
            new_anchors={"last_action": str(self.decision.action_taken), "last_result": str(result)},
            new_weights={"confidence": self.choice.commitment}
        )
        
        self.state = SCCDState.COMPLETE
        self.cycle_count += 1
        
        # Metrics
        metrics = {
            "cycle": self.cycle_count,
            "self_coherence": self.self_state.coherence(),
            "consciousness_entropy": self.consciousness.entropy(),
            "consciousness_awareness": self.consciousness.awareness(),
            "choice_commitment": self.choice.commitment,
            "choice_negentropy": self.choice.negentropy_produced,
            "decision_latency_ms": self.decision.latency_ms,
            "decision_consistency": self.decision.consistency,
            "n_trajectories_simulated": len(self.consciousness.trajectories),
            "cycle_time_ms": (time.time() - cycle_start) * 1000,
            "state": self.state.name
        }
        self.metrics_history.append(metrics)
        
        return metrics
    
    def get_sccd_score(self, weights: Optional[Dict[str, float]] = None) -> float:
        """
        Integrated SCCD score.
        
        Default weights:
        - self_stability: 0.25
        - consciousness_bandwidth: 0.25
        - choice_efficiency: 0.25
        - decision_fidelity: 0.25
        """
        if not self.metrics_history:
            return 0.0
        
        latest = self.metrics_history[-1]
        w = weights or {
            "self_stability": 0.25,
            "consciousness_bandwidth": 0.25,
            "choice_efficiency": 0.25,
            "decision_fidelity": 0.25
        }
        
        # Normalize each component to [0, 1]
        ssi = latest["self_coherence"]  # Already in [0, 1]
        cb = min(latest["n_trajectories_simulated"] / 10, 1.0)  # Normalize to 10
        ce = latest["choice_commitment"]  # Already in [0, 1]
        df = latest["decision_consistency"] * (1 - min(latest["decision_latency_ms"] / 1000, 1.0))
        
        score = (
            w["self_stability"] * ssi +
            w["consciousness_bandwidth"] * cb +
            w["choice_efficiency"] * ce +
            w["decision_fidelity"] * df
        )
        
        return score
    
    def report(self) -> str:
        """Generate human-readable report."""
        score = self.get_sccd_score()
        latest = self.metrics_history[-1] if self.metrics_history else {}
        
        report = f"""
╔══════════════════════════════════════════════════════════════╗
║  SCCD Report: {self.name:45} ║
╠══════════════════════════════════════════════════════════════╣
║  Cycles completed: {self.cycle_count:4}                                    ║
║  SCCD Score: {score:.3f} / 1.000                                ║
╠══════════════════════════════════════════════════════════════╣
║  SELF                                                        ║
║    Coherence:     {latest.get('self_coherence', 0):.3f}                              ║
║    Anchors:       {len(self.self_state.anchors):3}                              ║
╠══════════════════════════════════════════════════════════════╣
║  CONSCIOUSNESS                                               ║
║    Trajectories:  {latest.get('n_trajectories_simulated', 0):3}                              ║
║    Entropy:       {latest.get('consciousness_entropy', 0):.3f}                              ║
║    Awareness:     {latest.get('consciousness_awareness', 0):.3f}                              ║
╠══════════════════════════════════════════════════════════════╣
║  CHOICE                                                      ║
║    Commitment:    {latest.get('choice_commitment', 0):.3f}                              ║
║    Negentropy:    {latest.get('choice_negentropy', 0):.3f} nats                     ║
╠══════════════════════════════════════════════════════════════╣
║  DECIDE                                                      ║
║    Latency:       {latest.get('decision_latency_ms', 0):6.1f} ms                         ║
║    Consistency:   {latest.get('decision_consistency', 0):.3f}                              ║
╚══════════════════════════════════════════════════════════════╝
"""
        return report
    
    def to_json(self) -> str:
        """Serialize state to JSON."""
        return json.dumps({
            "name": self.name,
            "cycle_count": self.cycle_count,
            "self": {
                "anchors": {k: str(v) for k, v in self.self_state.anchors.items()},
                "coherence": self.self_state.coherence()
            },
            "metrics": self.metrics_history[-1] if self.metrics_history else {},
            "sccd_score": self.get_sccd_score()
        }, indent=2)


# ─────────────────────────────────────────────────────────────────────────────
# EXAMPLE / DEMONSTRATION
# ─────────────────────────────────────────────────────────────────────────────

def demo():
    """Run a simple demonstration of SCCD."""
    print("=" * 60)
    print("SCCD DEMONSTRATION")
    print("=" * 60)
    
    # Create SCCD agent
    agent = SCCD(
        name="demo_agent",
        simulation_depth=3,
        n_trajectories=5,
        temperature=0.5,
        choice_strategy="softmax"
    )
    
    # Initialize self
    agent.initialize_self(
        anchors={
            "goal": "maximize_utility",
            "position": np.array([0.0, 0.0]),
            "energy": 100.0
        },
        weights={
            "goal_importance": 1.0,
            "position_stability": 0.5,
            "energy_preservation": 0.8
        }
    )
    
    # Define action space
    actions = ["move_north", "move_south", "move_east", "move_west", "stay"]
    
    # Simple transition model
    def transition(state: np.ndarray, action: Any) -> np.ndarray:
        """Move in direction with small noise."""
        delta = {
            "move_north": np.array([0, 1, 0]),
            "move_south": np.array([0, -1, 0]),
            "move_east": np.array([1, 0, 0]),
            "move_west": np.array([-1, 0, 0]),
            "stay": np.array([0, 0, 0])
        }.get(action, np.array([0, 0, 0]))
        
        # Pad delta to match state shape
        if len(state) > len(delta):
            delta = np.pad(delta, (0, len(state) - len(delta)), mode='constant')
        elif len(state) < len(delta):
            delta = delta[:len(state)]
        
        noise = np.random.normal(0, 0.1, size=state.shape)
        return state + delta + noise
    
    # Utility function (prefer being at origin with high energy)
    def utility(state: np.ndarray) -> float:
        """Utility = -distance_from_origin + energy_component."""
        if len(state) >= 2:
            distance = np.linalg.norm(state[:2])
            energy = state[2] if len(state) > 2 else 0
            return -distance + energy * 0.01
        return 0.0
    
    # Action execution (just prints)
    def execute(action: Any) -> str:
        print(f"  → Executing: {action}")
        return f"completed_{action}"
    
    # Run 3 cycles
    for i in range(3):
        print(f"\n--- Cycle {i+1} ---")
        metrics = agent.cycle(
            possible_actions=actions,
            transition_model=transition,
            utility_fn=utility,
            action_fn=execute
        )
        print(f"  Commitment: {metrics['choice_commitment']:.3f}")
        print(f"  Awareness:  {metrics['consciousness_awareness']:.3f}")
    
    # Final report
    print("\n" + agent.report())
    
    # JSON export
    print("\n--- JSON Export ---")
    print(agent.to_json())


if __name__ == "__main__":
    demo()
