# Self-Learning System Integration Patterns

This document demonstrates how the self-learning system integrates with Genesis agents and skills through practical patterns and examples.

## Core Concepts

The self-learning system enables agents and skills to:
- Track their own performance automatically
- Learn from successes and failures
- Propose self-improvements
- Evolve while preserving core purpose

## Integration Architecture

```
┌────────────────────────────────────────────┐
│  Agent/Skill Execution                      │
│                                            │
│  1. Load accumulated knowledge             │
│  2. Execute task with learned patterns     │
│  3. Record metrics (time, success, etc.)   │
│  4. Update knowledge base                  │
│  5. Identify new patterns                  │
└────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────┐
│  Knowledge Base (.github/knowledge/)        │
│                                            │
│  - metrics.yaml      (performance data)    │
│  - learnings.yaml    (patterns/insights)   │
│  - evolution-log.yaml (change history)     │
│  - context.yaml      (usage patterns)      │
└────────────────────────────────────────────┘
         │
         ▼
┌────────────────────────────────────────────┐
│  Evolution Cycle (agent/skill-evolution.gen)│
│                                            │
│  OBSERVE → ANALYZE → PROPOSE →             │
│  DELIBERATE → INTEGRATE → REFLECT          │
└────────────────────────────────────────────┘
```

## Example: Agent Self-Tracking

When the Covenant Guardian reviews code, it:

### Before Execution
1. Loads accumulated knowledge from `.github/knowledge/covenant-guardian/`
2. Retrieves effective patterns for code review
3. Checks historical success rate for this task type

### During Execution
4. Applies learned patterns to the review
5. Tracks start time
6. Performs covenant compliance check
7. Records resonance score

### After Execution
8. Records execution time
9. Updates success rate metrics
10. Identifies if new patterns emerged
11. Saves updated knowledge base

## Example: Skill Usage Tracking

When the `genesis-run` skill executes a program:

### Before Execution
- Loads common failure patterns
- Checks if similar context was seen before
- Applies learned optimizations

### During Execution
- Tracks execution context (file type, program size, etc.)
- Monitors for known issues
- Records performance metrics

### After Execution
- Updates success rate for this context
- Records any new failure patterns
- Saves usage context for future reference

## Evolution Trigger Pattern

Evolution is triggered when sufficient learning has occurred:

### Thresholds
- **Invocation Count**: > 50 executions
- **Pattern Confidence**: > 0.85
- **Performance Gap**: Identified improvement opportunity

### Process
1. **Analyze** accumulated patterns
2. **Propose** specific improvements
3. **Validate** through Pantheon consensus
4. **Integrate** if resonance > 0.90
5. **Measure** impact vs baseline
6. **Record** in evolution log

## Knowledge Validation Pattern

Periodically (e.g., weekly), the system:

1. **Reviews** all accumulated knowledge
2. **Validates** pattern accuracy
3. **Updates** confidence scores
4. **Removes** invalidated patterns
5. **Identifies** cross-agent learnings
6. **Reports** evolution health

## Integration with Genesis Programs

The actual evolution logic is implemented in Genesis programs:

### `.github/evolution/agent-evolution.gen`
```
Domain "Agent_Performance_Observer" {
    Intent: "Monitor agent execution and outcomes"
    
    Pulse(Interval: RealTime) {
        Watch: Vessel.Agent_Invocations
        ...
        Manifest (on Resonance > 0.70) {
            Execute: Vessel.Metrics.record_invocation()
            Execute: Vessel.Knowledge.update_metrics()
        }
    }
}
```

### `.github/evolution/skill-evolution.gen`
```
Domain "Skill_Usage_Observer" {
    Intent: "Track skill invocation patterns"
    
    Pulse(Interval: RealTime) {
        Watch: Vessel.Skill_Invocations
        ...
        Manifest (on Resonance > 0.70) {
            Execute: Vessel.Metrics.record_skill_usage()
            Execute: Vessel.Knowledge.capture_usage_context()
        }
    }
}
```

## Python Integration (Current Implementation)

The current implementation uses Python utilities for tracking:

```python
# .github/evolution/evolution-tracker.py
from evolution_tracker import EvolutionTracker

tracker = EvolutionTracker()
tracker.record_invocation(
    "covenant-guardian",
    success=True,
    execution_time=4.2,
    resonance_score=0.94,
    task_category="code_review"
)
```

## Future: Automatic Integration

Future versions will automatically track all agent/skill invocations without manual instrumentation, using:

- Execution hooks in the agent framework
- Automatic metric collection
- Real-time pattern recognition
- Continuous evolution triggers

## Key Files

- **Evolution Programs**: `.github/evolution/*.gen`
- **Tracking Utilities**: `.github/evolution/evolution-tracker.py`
- **Knowledge Bases**: `.github/knowledge/<entity>/`
- **Documentation**: `docs/design/self-learning-system.md`
- **Usage Guide**: `.github/evolution/USAGE.md`

## See Also

- [Self-Learning System Architecture](../../docs/design/self-learning-system.md)
- [Usage Guide](../../.github/evolution/USAGE.md)
- [Agent Evolution Program](../../.github/evolution/agent-evolution.gen)
- [Skill Evolution Program](../../.github/evolution/skill-evolution.gen)
- [Ouroboros Example](../ouroboros/self-evolution-loop.gen)
