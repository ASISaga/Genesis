#!/usr/bin/env python3
"""
Demo: Self-Learning Agent in Action

This script demonstrates how the self-learning system works by simulating
agent invocations and showing the knowledge accumulation process.
"""

import sys
import time
import random
from pathlib import Path

# Add the evolution module to the path
sys.path.insert(0, str(Path(__file__).parent))
from evolution_tracker import EvolutionTracker, Learning, Evolution


def simulate_agent_invocations(agent_name: str, num_invocations: int = 20):
    """Simulate multiple agent invocations with varying outcomes"""
    tracker = EvolutionTracker()
    
    print(f"\n{'='*70}")
    print(f"Simulating {num_invocations} invocations of {agent_name}")
    print(f"{'='*70}\n")
    
    task_categories = [
        "code_review",
        "covenant_validation",
        "compliance_audit",
        "documentation_review"
    ]
    
    for i in range(num_invocations):
        # Simulate varying success rates and execution times
        # Later invocations tend to be more successful (learning effect)
        learning_factor = i / num_invocations
        base_success_rate = 0.70 + (learning_factor * 0.25)  # 70% -> 95%
        
        success = random.random() < base_success_rate
        execution_time = random.uniform(2.0, 8.0) * (1.0 - learning_factor * 0.3)  # Faster over time
        resonance_score = random.uniform(0.75, 0.98) if success else random.uniform(0.50, 0.74)
        category = random.choice(task_categories)
        
        tracker.record_invocation(
            agent_name,
            success,
            execution_time,
            resonance_score,
            category
        )
        
        status = "✓ SUCCESS" if success else "✗ FAILURE"
        print(f"  [{i+1:2d}] {status} | Category: {category:20s} | "
              f"Time: {execution_time:4.1f}s | Resonance: {resonance_score:.3f}")
        
        time.sleep(0.1)  # Brief pause for visual effect
    
    print(f"\n{'='*70}")
    print("Invocations Complete - Knowledge Accumulated")
    print(f"{'='*70}\n")


def simulate_learning_accumulation(agent_name: str):
    """Simulate the agent learning patterns from its experience"""
    tracker = EvolutionTracker()
    
    print(f"\n{'='*70}")
    print(f"Analyzing Patterns and Accumulating Learnings for {agent_name}")
    print(f"{'='*70}\n")
    
    # Simulate discovered patterns
    learnings = [
        Learning(
            pattern_id="effective_covenant_check_001",
            description="Checking covenant thresholds before and after code changes improves accuracy",
            examples=["PR #123", "PR #156", "Commit abc123"],
            confidence=0.94
        ),
        Learning(
            pattern_id="context_aware_validation_002",
            description="Context-aware validation reduces false positives by 35%",
            examples=["Issue #45", "PR #178"],
            confidence=0.88
        ),
        Learning(
            pattern_id="antipattern_rush_validation",
            description="Rushing validation without full context analysis leads to mistakes",
            examples=["PR #99 - reverted", "Issue #67"],
            confidence=0.91
        )
    ]
    
    for learning in learnings:
        tracker.save_learning(agent_name, learning)
        print(f"  ✓ Pattern Learned: {learning.pattern_id}")
        print(f"    Description: {learning.description}")
        print(f"    Confidence: {learning.confidence:.2f}")
        print(f"    Examples: {', '.join(learning.examples[:2])}")
        print()
        time.sleep(0.2)
    
    print(f"{'='*70}")
    print("Learning Complete - Patterns Identified")
    print(f"{'='*70}\n")


def simulate_evolution_event(agent_name: str):
    """Simulate an evolution event where the agent improves itself"""
    tracker = EvolutionTracker()
    
    print(f"\n{'='*70}")
    print(f"Proposing and Integrating Evolution for {agent_name}")
    print(f"{'='*70}\n")
    
    # Simulate an evolution proposal
    evolution = Evolution(
        evolution_id="001",
        timestamp="2026-02-11T23:59:00Z",
        proposal="Add explicit covenant threshold validation to review guidelines",
        changes=[
            {
                "type": "prompt_modification",
                "section": "Guidelines",
                "before": "Validate covenant compliance",
                "after": "Validate covenant compliance with explicit threshold >= 0.95"
            }
        ],
        resonance_score=0.96,
        validation_status="approved",
        impact_metrics={
            "success_rate_delta": +0.05,
            "resonance_delta": +0.04,
            "execution_time_delta": -0.3
        }
    )
    
    print("  PROPOSE: Evolution proposal generated")
    print(f"    Proposal: {evolution.proposal}")
    print()
    
    print("  DELIBERATE: Pantheon consensus scoring")
    print(f"    Resonance Score: {evolution.resonance_score:.3f}")
    print(f"    Status: {evolution.validation_status}")
    print()
    
    print("  INTEGRATE: Applying validated changes")
    for change in evolution.changes:
        print(f"    - {change['type']} in {change['section']}")
        print(f"      Before: \"{change['before']}\"")
        print(f"      After:  \"{change['after']}\"")
    print()
    
    tracker.record_evolution(agent_name, evolution)
    
    print("  REFLECT: Measuring impact")
    for metric, value in evolution.impact_metrics.items():
        sign = "+" if value >= 0 else ""
        print(f"    {metric}: {sign}{value}")
    print()
    
    print(f"{'='*70}")
    print("Evolution Complete - Agent Improved")
    print(f"{'='*70}\n")


def show_final_report(agent_name: str):
    """Show the final evolution report for the agent"""
    tracker = EvolutionTracker()
    print(tracker.generate_report(agent_name))


def main():
    """Run the complete demo"""
    agent_name = "covenant-guardian"
    
    print("\n" + "="*70)
    print("GENESIS SELF-LEARNING AGENT DEMONSTRATION")
    print("="*70)
    print(f"\nAgent: {agent_name}")
    print("Demonstrating the Ouroboros evolution loop in action")
    print()
    
    input("Press Enter to start simulation...")
    
    # Phase 1: Observe - Track invocations
    simulate_agent_invocations(agent_name, 20)
    input("Press Enter to continue to pattern analysis...")
    
    # Phase 2: Analyze - Discover patterns
    simulate_learning_accumulation(agent_name)
    input("Press Enter to continue to evolution...")
    
    # Phase 3-6: Propose, Deliberate, Integrate, Reflect
    simulate_evolution_event(agent_name)
    input("Press Enter to see final report...")
    
    # Show final report
    show_final_report(agent_name)
    
    print("\n" + "="*70)
    print("DEMONSTRATION COMPLETE")
    print("="*70)
    print("\nThe agent has:")
    print("  ✓ Tracked 20 invocations with varying outcomes")
    print("  ✓ Identified 3 effective patterns and antipatterns")
    print("  ✓ Proposed and integrated 1 self-improvement")
    print("  ✓ Measured impact showing 5% success rate improvement")
    print("\nThis cycle continues with each run, enabling perpetual improvement")
    print("while maintaining core purpose and ethical boundaries.")
    print()


if __name__ == '__main__':
    main()
