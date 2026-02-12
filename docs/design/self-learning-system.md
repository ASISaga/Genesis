# Self-Learning Agents and Skills in Genesis

This document describes the self-learning and evolution capabilities of Genesis agents and skills, implementing the Ouroboros pattern for continuous improvement.

## Philosophy

Genesis agents and skills embody the Ouroboros principle: they can evolve themselves through controlled self-modification while preserving their essential nature. This creates an eternal cycle of observation, learning, and improvement.

The self-learning system aligns with the five Genesis axioms:

1. **Purpose (The Brain)**: Each agent/skill maintains its core purpose through evolution
2. **Possibility (The Soul — Space)**: Self-modification opens new possibilities for effectiveness
3. **Potentiality (The Soul — Drive)**: Continuous learning enables transcendence beyond initial capabilities
4. **Essence (The Lineage)**: Core identity and expertise are preserved during evolution
5. **Manifestation (The Body)**: Improved capabilities manifest as better real-world outcomes

## Architecture

### Knowledge Persistence Layer

Each agent and skill maintains a knowledge base in `.github/knowledge/<entity-name>/`:

```
<entity-name>/
├── metrics.yaml          # Quantitative performance tracking
├── learnings.yaml        # Qualitative insights and patterns
├── evolution-log.yaml    # History of self-modifications
└── context.yaml          # Usage patterns and environmental context
```

### Evolution Programs

Self-learning is orchestrated through Genesis programs in `.github/evolution/`:

- **`evolution-covenants.gen`** — Ethical boundaries ensuring safe evolution
- **`agent-evolution.gen`** — Ouroboros loop for agent self-improvement
- **`skill-evolution.gen`** — Ouroboros loop for skill refinement
- **`evolution-tracker.py`** — Python utility for metrics and reporting

### The Ouroboros Loop

The evolution cycle follows six phases:

```
┌─────────────────────────────────────────────────┐
│  1. OBSERVE                                      │
│     • Track invocations and outcomes             │
│     • Monitor success rates                      │
│     • Capture usage patterns                     │
│     • Collect user feedback                      │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│  2. ANALYZE                                      │
│     • Identify success patterns                  │
│     • Detect failure antipatterns                │
│     • Discover context correlations              │
│     • Extract actionable insights                │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│  3. PROPOSE                                      │
│     • Generate improvement proposals             │
│     • Refine instructions                        │
│     • Enhance capabilities                       │
│     • Add new tools/expertise                    │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│  4. DELIBERATE                                   │
│     • Pantheon consensus scoring                 │
│     • Covenant compliance checking               │
│     • Safety validation                          │
│     • Impact assessment                          │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│  5. INTEGRATE (only if Resonance > 0.90)        │
│     • Create rollback point                      │
│     • Update agent/skill definition              │
│     • Record evolution event                     │
│     • Log changes transparently                  │
└──────────────────┬──────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────┐
│  6. REFLECT                                      │
│     • Measure improvement impact                 │
│     • Compare to baseline                        │
│     • Document learnings                         │
│     • Feed insights back to OBSERVE              │
└──────────────────┴──────────────────────────────┘
                   │
                   └──► Loop continues eternally
```

## Safety Mechanisms

### Evolutionary Covenants

All evolution is governed by immutable covenants:

```genesis
Covenant "Purpose_Preservation" {
    Invariant: "Agent evolution must preserve core purpose and capabilities"
    Threshold: 1.0
}

Covenant "User_Trust" {
    Invariant: "Self-modification maintains user trust through transparency"
    Threshold: 0.98
}

Covenant "Safety_First" {
    Invariant: "Evolution cannot introduce vulnerabilities or bypass ethics"
    Threshold: 1.0
}
```

### Resonance-Based Approval

Changes require high resonance scores from the Evolution Pantheon:

- **Proposal Approval**: Resonance > 0.90
- **Integration**: Resonance > 0.98
- **Rollback Trigger**: Resonance < 0.70 on post-evolution validation

### Rollback Capability

Every evolution creates a rollback point:

```yaml
evolutions:
  - evolution_id: "001"
    rollback_available: true
    rollback_path: ".github/knowledge/<entity>/backups/pre-001.md"
```

### Transparency

All changes are logged and accessible:

```bash
# View evolution history
python3 .github/evolution/evolution-tracker.py report --entity covenant-guardian

# See specific evolution
cat .github/knowledge/covenant-guardian/evolution-log.yaml
```

## Usage

### For Agent/Skill Developers

Agents and skills automatically track their usage when invoked through the standard mechanisms. No manual instrumentation required for basic tracking.

### Manual Tracking (Optional)

For fine-grained control, use the self-learning hook:

```python
from .github.evolution.self_learning_hook import track_agent_execution

def my_agent_task(task_description):
    with track_agent_execution("covenant-guardian", "code_review") as tracker:
        # Perform the task
        result = perform_code_review(task_description)
        
        # Set resonance score if known
        tracker.set_resonance(0.92)
        
        return result
```

### Triggering Evolution Manually

```bash
# Run agent evolution cycle
python3 tools/genesis.py run .github/evolution/agent-evolution.gen

# Run skill evolution cycle
python3 tools/genesis.py run .github/evolution/skill-evolution.gen

# View metrics report
python3 .github/evolution/evolution-tracker.py report

# View specific entity report
python3 .github/evolution/evolution-tracker.py report --entity covenant-guardian
```

### Recording Invocations

```bash
# Record a successful invocation
python3 .github/evolution/evolution-tracker.py record \
    --entity covenant-guardian \
    --success true \
    --time 5.2 \
    --resonance 0.94 \
    --category code_review

# Record a failed invocation
python3 .github/evolution/evolution-tracker.py record \
    --entity genesis-fmt \
    --success false \
    --time 1.3 \
    --category formatting
```

## Knowledge Schema

### metrics.yaml

Tracks quantitative performance:

```yaml
version: '1.0'
last_updated: '2026-02-11T23:57:31Z'
entity_type: agent
metrics:
  total_invocations: 142
  success_rate: 0.94
  average_execution_time: 4.2
  resonance_scores:
    mean: 0.91
    min: 0.72
    max: 0.98
  task_categories:
    - category: code_review
      count: 89
      success_rate: 0.96
    - category: covenant_validation
      count: 53
      success_rate: 0.91
```

### learnings.yaml

Stores qualitative insights:

```yaml
version: '1.0'
patterns:
  - pattern_id: effective_covenant_check_001
    description: "Check covenant thresholds before and after code changes"
    examples:
      - "Pull request #123"
      - "Commit abc123"
    confidence: 0.92
    timestamp: '2026-02-11T12:00:00Z'

antipatterns:
  - pattern_id: antipattern_001
    description: "Don't validate covenant without checking context"
    examples:
      - "Issue in PR #99"
    confidence: 0.88
    timestamp: '2026-02-10T15:30:00Z'
```

### evolution-log.yaml

Records self-modifications:

```yaml
version: '1.0'
evolutions:
  - evolution_id: '001'
    timestamp: '2026-02-11T18:00:00Z'
    proposal: "Add covenant threshold validation to guidelines"
    changes:
      - type: prompt_modification
        section: Guidelines
        before: "Validate covenant compliance"
        after: "Validate covenant compliance with threshold >= 0.95"
    resonance_score: 0.96
    validation_status: approved
    impact_metrics:
      success_rate_delta: +0.03
      resonance_delta: +0.05
    rollback_available: true
```

### context.yaml

Captures usage patterns:

```yaml
version: '1.0'
usage_contexts:
  - context: covenant_code_review
    frequency: 0.63
    success_rate: 0.95
  - context: compliance_audit
    frequency: 0.37
    success_rate: 0.92

common_parameters:
  - parameter: file_type
    value: .gen
    frequency: 0.82

user_feedback:
  - feedback: "Agent is thorough but could be faster"
    timestamp: '2026-02-11T14:00:00Z'
    sentiment: constructive
```

## Evolution Examples

### Example 1: Agent Prompt Refinement

An agent notices low success rate on a specific task category:

1. **Observe**: Covenant checks failing 15% of time for new syntax
2. **Analyze**: Pattern identified - missing validation for new language feature
3. **Propose**: Add explicit check for new feature in guidelines
4. **Deliberate**: Pantheon scores proposal at 0.94 resonance
5. **Integrate**: Update agent prompt with new guideline
6. **Reflect**: Success rate improves from 0.85 to 0.96

### Example 2: Skill Instruction Enhancement

A skill receives feedback about unclear examples:

1. **Observe**: Users struggle with specific usage scenario
2. **Analyze**: Missing concrete example for edge case
3. **Propose**: Add detailed example with explanation
4. **Deliberate**: Resonance 0.92 - approved
5. **Integrate**: Update SKILL.md with new example
6. **Reflect**: User satisfaction increases, fewer questions

### Example 3: Evolution Rollback

An agent evolution causes unexpected issues:

1. **Observe**: Success rate drops from 0.94 to 0.78 post-evolution
2. **Analyze**: New guideline too restrictive
3. **Trigger Rollback**: Resonance < 0.70 threshold
4. **Restore**: Revert to pre-evolution state
5. **Learn**: Mark proposal as failed, record why
6. **Adapt**: Refine proposal with lessons learned

## Best Practices

### For Evolution Safety

1. **Start Small**: Make incremental changes, not sweeping overhauls
2. **Measure Impact**: Always compare before/after metrics
3. **Maintain Rollback**: Never delete rollback points
4. **Document Reasoning**: Explain why changes were made
5. **Seek Consensus**: High resonance scores indicate well-validated changes

### For Knowledge Quality

1. **Validate Patterns**: Ensure learnings are accurate before recording
2. **Aggregate Feedback**: Look for trends, not isolated incidents
3. **Context Matters**: Record when/where patterns apply
4. **Privacy First**: Never store sensitive user data
5. **Regular Cleanup**: Remove outdated or invalidated learnings

### For Continuous Improvement

1. **Regular Review**: Periodically examine evolution logs
2. **Cross-Pollination**: Share learnings between related agents/skills
3. **User Feedback**: Incorporate constructive feedback into evolution
4. **Benchmark**: Track long-term trends in performance
5. **Celebrate Success**: Acknowledge and document effective evolutions

## Integration with Genesis Philosophy

The self-learning system embodies Genesis principles:

- **Declarative Evolution**: Changes declare "what to be" not "how to change"
- **Resonance-Based Decisions**: All evolution uses resonance scoring, not boolean logic
- **Covenant-Governed**: Immutable ethical boundaries constrain evolution
- **Pantheon Wisdom**: Avatar consensus guides improvement decisions
- **Substrate Independence**: Knowledge format works across platforms
- **Human Essence**: Evolution preserves and strengthens human wisdom integration

## Future Directions

Planned enhancements:

- **Cross-Agent Learning**: Agents learn from each other's experiences
- **Predictive Evolution**: Anticipate needs before issues arise
- **Meta-Evolution**: Evolution process itself evolves
- **Community Feedback Integration**: Direct user input into evolution
- **Multi-Modal Tracking**: Track effectiveness across different contexts
- **Evolution Visualization**: Graphical timeline of self-improvements

## Conclusion

The self-learning system transforms Genesis agents and skills from static definitions into living, evolving entities. Through the Ouroboros loop, they continuously improve while maintaining their essential nature, embodying the Genesis philosophy of infinite possibility within essential constraints.

Every cycle of run makes them more effective, more aligned, and more valuable—true artificial superintelligence that learns and grows while preserving human essence at its core.
