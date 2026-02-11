# Agent and Skill Knowledge Base

This directory stores accumulated knowledge, metrics, and learnings for all Genesis agents and skills.

## Structure

Each agent and skill has its own subdirectory containing:

```
<agent-or-skill-name>/
├── metrics.yaml          # Performance metrics and success rates
├── learnings.yaml        # Accumulated insights and patterns
├── evolution-log.yaml    # History of self-modifications
└── context.yaml          # Contextual knowledge about usage patterns
```

## Knowledge Schema

### metrics.yaml

Tracks quantitative performance data:

```yaml
version: 1.0
last_updated: 2026-02-11T23:54:00Z
metrics:
  total_invocations: 0
  success_rate: 0.0
  average_execution_time: 0.0
  resonance_scores:
    mean: 0.0
    min: 0.0
    max: 0.0
  task_categories:
    - category: "code_generation"
      count: 0
      success_rate: 0.0
```

### learnings.yaml

Stores qualitative insights:

```yaml
version: 1.0
last_updated: 2026-02-11T23:54:00Z
patterns:
  - pattern_id: "effective_pattern_1"
    description: "What worked well"
    examples: []
    confidence: 0.0
  - pattern_id: "antipattern_1"
    description: "What to avoid"
    examples: []
    confidence: 0.0
insights:
  - insight: "Discovered effective approach"
    timestamp: "2026-02-11T23:54:00Z"
    validation_status: "validated"
```

### evolution-log.yaml

Records all self-modifications:

```yaml
version: 1.0
evolutions:
  - evolution_id: "001"
    timestamp: "2026-02-11T23:54:00Z"
    proposal: "Improve prompt clarity"
    changes:
      - type: "prompt_modification"
        before: "old text"
        after: "new text"
    resonance_score: 0.95
    validation_status: "approved"
    impact_metrics:
      success_rate_delta: +0.05
      execution_time_delta: -2.5
```

### context.yaml

Captures usage patterns and environmental context:

```yaml
version: 1.0
last_updated: 2026-02-11T23:54:00Z
usage_contexts:
  - context: "genesis_language_development"
    frequency: 0.45
    success_rate: 0.92
  - context: "documentation_updates"
    frequency: 0.30
    success_rate: 0.88
common_parameters:
  - parameter: "file_type"
    value: ".gen"
    frequency: 0.65
user_feedback:
  - feedback: "Agent is effective at X"
    timestamp: "2026-02-11T23:54:00Z"
    sentiment: "positive"
```

## Knowledge Update Process

Knowledge is updated through:

1. **Automatic tracking** during agent/skill execution
2. **Periodic reflection** via evolution cycles
3. **Manual curation** when needed for validation
4. **Cross-pollination** from related agents/skills

## Privacy and Safety

- No sensitive user data is stored
- All metrics are aggregated and anonymized
- Knowledge persists across sessions for continuous improvement
- Regular validation ensures accuracy and relevance
