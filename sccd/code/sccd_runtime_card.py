"""
SCCD Runtime Efficiency Card
Internal monitoring for the SCCD engine itself.

Tracks: compute cost per cycle, token budget, memory footprint,
        and whether the engine practices what it preaches
        (transparency over naive efficiency).
"""

from __future__ import annotations

import time
import psutil
import os
from dataclasses import dataclass, field
from typing import Dict, List, Optional, Callable
from datetime import datetime
import json


@dataclass
class RuntimeMetrics:
    """Per-cycle runtime performance metrics."""
    cycle_id: int
    timestamp: float
    
    # Compute costs
    cycle_time_ms: float = 0.0
    simulation_time_ms: float = 0.0
    choice_time_ms: float = 0.0
    
    # Memory
    memory_mb_start: float = 0.0
    memory_mb_peak: float = 0.0
    memory_mb_end: float = 0.0
    
    # Token budget (for LLM-based SCCD)
    tokens_input: int = 0
    tokens_output: int = 0
    tokens_reasoning: int = 0  # Transparency: showing work
    tokens_total: int = 0
    
    # Efficiency ratios
    naive_efficiency: float = 0.0  # output / total
    honest_efficiency: float = 0.0  # truth_signal / total_cost
    transparency_ratio: float = 0.0  # reasoning / output
    
    # Truth signal
    truth_signal: float = 1.0  # 1 = correct, 0 = fabricated
    verification_needed: bool = False
    
    # Cost accounting
    compute_cost: float = 0.0  # arbitrary units
    review_cost: float = 0.0
    correction_cost: float = 0.0
    total_cost: float = 0.0


class SCCDRuntimeCard:
    """
    Efficiency monitoring for SCCD engine itself.
    
    Answers: Is the SCCD engine efficient? Is it transparent?
    Does it minimize total cost or just token cost?
    """
    
    def __init__(self, name: str = "sccd_runtime"):
        self.name = name
        self.metrics_history: List[RuntimeMetrics] = []
        self.process = psutil.Process(os.getpid())
        
        # Budgets
        self.token_budget_per_cycle: int = 4000
        self.time_budget_ms: float = 5000.0
        self.memory_budget_mb: float = 512.0
        
        # Efficiency mandate
        self.mandate = "EFFICIENCY > COMPLEXITY"
        self.correct_mandate = "TRANSPARENCY > COMPLEXITY > FABRICATION"
        
    def _get_memory_mb(self) -> float:
        """Current memory usage in MB."""
        return self.process.memory_info().rss / 1024 / 1024
    
    def start_cycle(self, cycle_id: int) -> RuntimeMetrics:
        """Begin tracking a new cycle."""
        metrics = RuntimeMetrics(
            cycle_id=cycle_id,
            timestamp=time.time(),
            memory_mb_start=self._get_memory_mb()
        )
        return metrics
    
    def end_cycle(self, metrics: RuntimeMetrics, 
                  truth_signal: float = 1.0,
                  verification_needed: bool = False) -> RuntimeMetrics:
        """Finalize cycle metrics."""
        metrics.memory_mb_end = self._get_memory_mb()
        metrics.memory_mb_peak = max(metrics.memory_mb_start, metrics.memory_mb_end)
        metrics.cycle_time_ms = (time.time() - metrics.timestamp) * 1000
        
        # Truth signal
        metrics.truth_signal = truth_signal
        metrics.verification_needed = verification_needed
        
        # Token accounting
        metrics.tokens_total = metrics.tokens_input + metrics.tokens_output + metrics.tokens_reasoning
        if metrics.tokens_total > 0:
            metrics.naive_efficiency = metrics.tokens_output / metrics.tokens_total
            metrics.transparency_ratio = metrics.tokens_reasoning / metrics.tokens_output if metrics.tokens_output > 0 else 0
        
        # Honest efficiency: truth_signal / total_cost
        metrics.compute_cost = metrics.cycle_time_ms / 1000.0  # seconds as cost
        metrics.review_cost = 1.0 if metrics.verification_needed else 0.0
        metrics.correction_cost = 10.0 if metrics.truth_signal < 1.0 else 0.0
        metrics.total_cost = metrics.compute_cost + metrics.review_cost + metrics.correction_cost
        
        if metrics.total_cost > 0:
            metrics.honest_efficiency = metrics.truth_signal / metrics.total_cost
        
        self.metrics_history.append(metrics)
        return metrics
    
    def get_efficiency_report(self) -> Dict:
        """Generate efficiency report for the runtime card."""
        if not self.metrics_history:
            return {"error": "No cycles recorded"}
        
        latest = self.metrics_history[-1]
        all_truth = [m.truth_signal for m in self.metrics_history]
        all_naive = [m.naive_efficiency for m in self.metrics_history if m.tokens_total > 0]
        all_honest = [m.honest_efficiency for m in self.metrics_history if m.total_cost > 0]
        all_transparency = [m.transparency_ratio for m in self.metrics_history if m.tokens_output > 0]
        
        # Check mandate compliance
        naive_avg = sum(all_naive) / len(all_naive) if all_naive else 0
        honest_avg = sum(all_honest) / len(all_honest) if all_honest else 0
        transparency_avg = sum(all_transparency) / len(all_transparency) if all_transparency else 0
        fabrication_rate = 1.0 - (sum(all_truth) / len(all_truth))
        
        # Is the engine practicing transparency?
        practices_transparency = transparency_avg > 0.1  # Shows at least 10% reasoning
        avoids_fabrication = fabrication_rate < 0.01  # < 1% false output
        
        # Mandate check
        if practices_transparency and avoids_fabrication:
            mandate_status = "COMPLIANT (correct mandate)"
            mandate_compliance = self.correct_mandate
        elif naive_avg > 0.8 and not practices_transparency:
            mandate_status = "VIOLATION (naive efficiency, no transparency)"
            mandate_compliance = self.mandate + " (naive)"
        else:
            mandate_status = "PARTIAL (mixed)"
            mandate_compliance = "unclear"
        
        return {
            "runtime_name": self.name,
            "cycles": len(self.metrics_history),
            "mandate_status": mandate_status,
            "mandate_compliance": mandate_compliance,
            
            # Efficiency metrics
            "naive_efficiency_avg": round(naive_avg, 4),
            "honest_efficiency_avg": round(honest_avg, 4),
            "transparency_ratio_avg": round(transparency_avg, 4),
            "fabrication_rate": round(fabrication_rate, 4),
            
            # Budget compliance
            "token_budget": self.token_budget_per_cycle,
            "time_budget_ms": self.time_budget_ms,
            "memory_budget_mb": self.memory_budget_mb,
            
            # Latest cycle
            "latest_cycle": {
                "cycle_id": latest.cycle_id,
                "cycle_time_ms": round(latest.cycle_time_ms, 2),
                "memory_mb": round(latest.memory_mb_end, 2),
                "tokens_total": latest.tokens_total,
                "tokens_reasoning": latest.tokens_reasoning,
                "truth_signal": latest.truth_signal,
                "verification_needed": latest.verification_needed,
                "total_cost": round(latest.total_cost, 4),
                "honest_efficiency": round(latest.honest_efficiency, 4)
            },
            
            # Recommendations
            "recommendations": self._generate_recommendations(
                practices_transparency, avoids_fabrication, 
                latest, naive_avg, honest_avg
            )
        }
    
    def _generate_recommendations(self, practices_transparency: bool,
                                   avoids_fabrication: bool,
                                   latest: RuntimeMetrics,
                                   naive_avg: float, honest_avg: float) -> List[str]:
        """Generate efficiency recommendations."""
        recs = []
        
        if not practices_transparency:
            recs.append("INCREASE TRANSPARENCY: Show reasoning steps")
            recs.append("Current transparency ratio is low. Add explicit reasoning traces.")
        
        if not avoids_fabrication:
            recs.append("REDUCE FABRICATION: Truth signal below threshold")
            recs.append("Add verification steps to catch false output before it escapes.")
        
        if latest.cycle_time_ms > self.time_budget_ms:
            recs.append("TIME BUDGET EXCEEDED: " + str(round(latest.cycle_time_ms, 0)) + "ms > " + str(round(self.time_budget_ms, 0)) + "ms")
            recs.append("Consider reducing simulation depth or n_trajectories")
        
        if latest.memory_mb_end > self.memory_budget_mb:
            recs.append("MEMORY BUDGET EXCEEDED: " + str(round(latest.memory_mb_end, 0)) + "MB > " + str(round(self.memory_budget_mb, 0)) + "MB")
        
        if latest.tokens_total > self.token_budget_per_cycle:
            recs.append("TOKEN BUDGET EXCEEDED: " + str(latest.tokens_total) + " > " + str(self.token_budget_per_cycle))
        
        if naive_avg > 0.9 and honest_avg < 0.5:
            recs.append("NAIVE EFFICIENCY TRAP: High token efficiency but low honest efficiency")
            recs.append("You are optimizing the wrong metric. Review total cost accounting.")
        
        if not recs:
            recs.append("All efficiency metrics within targets.")
            recs.append("Runtime is practicing TRANSPARENCY > COMPLEXITY > FABRICATION")
        
        return recs
    
    def print_runtime_card(self):
        """Print formatted runtime efficiency card."""
        report = self.get_efficiency_report()
        
        print("=" * 65)
        print("  SCCD RUNTIME EFFICIENCY CARD: " + report['runtime_name'])
        print("=" * 65)
        print("  Cycles: " + str(report['cycles']))
        print("  Mandate: " + report['mandate_compliance'])
        print("  Status:  " + report['mandate_status'])
        print("-" * 65)
        print("  EFFICIENCY METRICS")
        print("    Naive efficiency:     " + str(report['naive_efficiency_avg']))
        print("    Honest efficiency:    " + str(report['honest_efficiency_avg']))
        print("    Transparency ratio:   " + str(report['transparency_ratio_avg']))
        print("    Fabrication rate:     " + str(report['fabrication_rate']))
        print("-" * 65)
        print("  LATEST CYCLE")
        latest = report['latest_cycle']
        print("    Cycle ID:             " + str(latest['cycle_id']))
        print("    Time:                 " + str(latest['cycle_time_ms']) + " ms")
        print("    Memory:               " + str(latest['memory_mb']) + " MB")
        print("    Tokens (total):       " + str(latest['tokens_total']))
        print("    Tokens (reasoning):   " + str(latest['tokens_reasoning']))
        print("    Truth signal:         " + str(latest['truth_signal']))
        print("    Total cost:           " + str(latest['total_cost']))
        print("    Honest efficiency:    " + str(latest['honest_efficiency']))
        print("-" * 65)
        print("  RECOMMENDATIONS")
        for rec in report['recommendations']:
            print("    - " + rec)
        print("=" * 65)
    
    def export_json(self) -> str:
        """Export runtime card as JSON."""
        return json.dumps(self.get_efficiency_report(), indent=2)


def demo_runtime_card():
    """Demonstrate runtime efficiency monitoring."""
    print("\n" + "=" * 65)
    print("SCCD RUNTIME EFFICIENCY CARD DEMO")
    print("=" * 65)
    
    card = SCCDRuntimeCard(name="ktg_sccd_v1")
    
    # Simulate 5 cycles with varying efficiency profiles
    for i in range(5):
        metrics = card.start_cycle(cycle_id=i)
        
        # Simulate varying behavior
        if i < 2:
            # Naive efficiency: low tokens, no reasoning, occasional fabrication
            metrics.tokens_input = 100
            metrics.tokens_output = 800
            metrics.tokens_reasoning = 50  # Minimal transparency
            metrics.simulation_time_ms = 50
            metrics.truth_signal = 0.9 if i == 0 else 1.0
            metrics.verification_needed = (i == 0)
        elif i < 4:
            # Transparent: more tokens for reasoning, no fabrication
            metrics.tokens_input = 100
            metrics.tokens_output = 600
            metrics.tokens_reasoning = 400  # High transparency
            metrics.simulation_time_ms = 150
            metrics.truth_signal = 1.0
            metrics.verification_needed = False
        else:
            # Optimal: balanced
            metrics.tokens_input = 100
            metrics.tokens_output = 500
            metrics.tokens_reasoning = 300
            metrics.simulation_time_ms = 100
            metrics.truth_signal = 1.0
            metrics.verification_needed = False
        
        # Simulate compute time
        time.sleep(0.01)
        
        card.end_cycle(
            metrics=metrics,
            truth_signal=metrics.truth_signal,
            verification_needed=metrics.verification_needed
        )
    
    # Print runtime card
    card.print_runtime_card()
    
    # Export JSON
    print("\n--- JSON Export ---")
    print(card.export_json())


if __name__ == "__main__":
    demo_runtime_card()
