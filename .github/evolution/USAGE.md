# Getting Started with Self-Learning Agents and Skills

This guide shows you how to use and interact with Genesis's self-learning agent and skill system.

## Quick Start

### 1. View Current Knowledge State

See the performance metrics for all agents and skills:

```bash
cd /path/to/Genesis
python3 .github/evolution/evolution-tracker.py report
```

View detailed report for a specific agent:

```bash
python3 .github/evolution/evolution-tracker.py report --entity covenant-guardian
```

### 2. Run the Demo

See the self-learning system in action with a simulated demonstration:

```bash
python3 .github/evolution/demo_self_learning.py
```

This will:
- Simulate 20 agent invocations with varying outcomes
- Show pattern discovery and learning accumulation
- Demonstrate an evolution proposal and integration
- Display the final performance report

### 3. Track Agent/Skill Usage

When agents or skills are used, their metrics can be recorded:

```bash
# Record a successful invocation
python3 .github/evolution/evolution-tracker.py record \
    --entity covenant-guardian \
    --success true \
    --time 4.2 \
    --resonance 0.94 \
    --category code_review

# Record a failed invocation
python3 .github/evolution/evolution-tracker.py record \
    --entity genesis-fmt \
    --success false \
    --time 1.8 \
    --category formatting
```

### 4. Run Evolution Cycles

Trigger the self-improvement cycle for agents:

```bash
python3 tools/genesis.py run .github/evolution/agent-evolution.gen
```

Trigger the self-improvement cycle for skills:

```bash
python3 tools/genesis.py run .github/evolution/skill-evolution.gen
```

## Understanding the Knowledge Base

Each agent and skill has a knowledge directory in `.github/knowledge/<entity-name>/`:

### metrics.yaml

Tracks quantitative performance data:
- Total invocations
- Success rate
- Average execution time
- Resonance scores (mean, min, max)
- Task category breakdown

**Example:**
```yaml
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
```

### learnings.yaml

Stores qualitative insights:
- Effective patterns discovered
- Antipatterns to avoid
- Contextual insights

**Example:**
```yaml
patterns:
  - pattern_id: effective_covenant_check_001
    description: "Check covenant thresholds before and after code changes"
    confidence: 0.94
    examples:
      - "PR #123"
      - "Commit abc123"
```

### evolution-log.yaml

Records all self-modifications:
- Evolution proposals
- Changes made
- Resonance scores
- Impact metrics
- Rollback status

**Example:**
```yaml
evolutions:
  - evolution_id: '001'
    proposal: "Add covenant threshold validation to guidelines"
    resonance_score: 0.96
    validation_status: approved
    impact_metrics:
      success_rate_delta: +0.05
```

### context.yaml

Captures usage patterns:
- Common usage contexts
- Frequent parameters
- User feedback

**Example:**
```yaml
usage_contexts:
  - context: covenant_code_review
    frequency: 0.63
    success_rate: 0.95
```

## The Ouroboros Loop

The self-learning system follows a perpetual cycle:

```
OBSERVE → ANALYZE → PROPOSE → DELIBERATE → INTEGRATE → REFLECT → (loop)
```

### 1. OBSERVE
- Track every agent/skill invocation
- Record success/failure outcomes
- Capture execution metrics
- Collect user feedback

### 2. ANALYZE
- Identify success patterns
- Detect failure antipatterns
- Discover context correlations
- Extract actionable insights

### 3. PROPOSE
- Generate improvement proposals
- Refine instructions or prompts
- Suggest capability enhancements
- Create evolution declarations

### 4. DELIBERATE
- Pantheon consensus scoring
- Covenant compliance checking
- Safety validation
- Impact assessment

### 5. INTEGRATE
- Create rollback point
- Update agent/skill definition
- Record evolution event
- Log changes transparently

### 6. REFLECT
- Measure improvement impact
- Compare to baseline metrics
- Document learnings
- Feed insights back to OBSERVE

## Safety and Governance

### Evolutionary Covenants

All evolution is governed by immutable covenants in `.github/evolution/evolution-covenants.gen`:

- **Purpose_Preservation**: Core purpose never changes
- **User_Trust**: Transparency in all modifications
- **Safety_First**: No vulnerabilities introduced
- **Knowledge_Integrity**: Accurate, validated knowledge
- **Rollback_Capability**: All changes reversible

### Resonance Thresholds

Changes require high consensus scores:

- **Proposal Approval**: Resonance ≥ 0.90
- **Integration**: Resonance ≥ 0.98
- **Rollback Trigger**: Resonance < 0.70

### Rollback Mechanism

Every evolution creates a restore point. If problems arise:

```bash
# View evolution log
cat .github/knowledge/<entity-name>/evolution-log.yaml

# Manually revert (in the future, this will be automated)
git revert <evolution-commit>
```

## Customization

### Adding New Agents/Skills

When creating new agents or skills, initialize their knowledge base:

```bash
python3 .github/evolution/evolution-tracker.py init --entity my-new-agent
```

This creates the complete knowledge directory structure.

### Modifying Evolution Covenants

Edit `.github/evolution/evolution-covenants.gen` to adjust:
- Threshold values for approval
- Pantheon avatar composition
- Safety constraints

**Warning**: Weakening covenants requires high resonance approval.

### Custom Metrics

To track custom metrics, modify the knowledge schema in:
- `.github/evolution/evolution-tracker.py` (Python tracker)
- `.github/knowledge/README.md` (Documentation)

## Integration Examples

### In Python Code

```python
from .github.evolution.self_learning_hook import track_agent_execution

def covenant_review_task(code_changes):
    with track_agent_execution("covenant-guardian", "code_review") as tracker:
        # Perform covenant review
        result = analyze_covenant_compliance(code_changes)
        
        # Calculate resonance
        resonance = compute_consensus_score(result)
        tracker.set_resonance(resonance)
        
        # Set success based on outcome
        tracker.set_success(result.compliant)
        
        return result
```

### In Genesis Programs

While the current implementation uses Python utilities, the evolution programs themselves are written in Genesis:

```genesis
Domain "Agent_Performance_Observer" {
    Intent: "Monitor agent execution and outcomes"
    
    Pulse(Interval: RealTime) {
        Watch: Vessel.Agent_Invocations
        
        Deliberate {
            Synthesize {
                Metric: Alignment(Covenant.Purpose_Preservation)
            }
        }
        
        Manifest (on Resonance > 0.70) {
            Execute: Vessel.Metrics.record_invocation()
        }
    }
}
```

## Monitoring and Reporting

### View Summary Report

```bash
python3 .github/evolution/evolution-tracker.py report
```

### View Detailed Entity Report

```bash
python3 .github/evolution/evolution-tracker.py report --entity covenant-guardian
```

### Export Knowledge for Analysis

Knowledge bases are YAML files and can be easily exported:

```bash
# Copy knowledge base for external analysis
cp -r .github/knowledge /path/to/analysis/

# Convert to JSON if needed
python3 -c "
import yaml, json
with open('.github/knowledge/covenant-guardian/metrics.yaml') as f:
    data = yaml.safe_load(f)
print(json.dumps(data, indent=2))
"
```

## Best Practices

### For Users

1. **Regular Monitoring**: Check evolution reports periodically
2. **Provide Feedback**: User feedback improves evolution quality
3. **Trust but Verify**: Review evolution logs for transparency
4. **Report Issues**: Flag problematic evolutions for rollback

### For Developers

1. **Track Usage**: Always record invocations with accurate metrics
2. **Validate Patterns**: Ensure learnings are accurate before storing
3. **Document Changes**: Evolution proposals need clear reasoning
4. **Test Impact**: Measure before/after metrics for evolutions
5. **Preserve Safety**: Never weaken covenant thresholds

## Troubleshooting

### Knowledge Base Corruption

If knowledge YAML files become corrupted:

```bash
# Re-initialize (preserves existing data if valid)
python3 .github/evolution/initialize-knowledge.py
```

### Reverting an Evolution

If an evolution causes problems:

1. Check evolution log: `cat .github/knowledge/<entity>/evolution-log.yaml`
2. Identify problematic evolution ID
3. Revert the agent/skill definition to previous state
4. Record rollback in evolution log

### Performance Degradation

If an agent/skill performs worse after evolution:

1. Compare metrics before/after evolution
2. Check resonance scores in evolution log
3. Review proposed changes
4. Consider rollback if degradation > 10%

## Future Enhancements

Planned improvements to the self-learning system:

- **Automated Evolution Triggers**: Periodic automatic evolution cycles
- **Cross-Agent Learning**: Agents learn from each other
- **Predictive Evolution**: Anticipate needs before issues arise
- **Community Integration**: Direct user feedback into evolution
- **Visualization Tools**: Graphical evolution timelines
- **Meta-Evolution**: The evolution system evolves itself

## Resources

- **Architecture**: `docs/design/self-learning-system.md`
- **Evolution Programs**: `.github/evolution/*.gen`
- **Knowledge Schema**: `.github/knowledge/README.md`
- **Ouroboros Pattern**: `examples/ouroboros/self-evolution-loop.gen`
- **Dogfooding Example**: `examples/meta-programming/genesis-tools-dogfooding.gen`

## Getting Help

If you have questions or issues:

1. Check the documentation in `docs/design/self-learning-system.md`
2. Review existing knowledge bases for examples
3. Run the demo: `python3 .github/evolution/demo_self_learning.py`
4. Open an issue on GitHub with the `self-learning` label

---

**Remember**: The self-learning system embodies the Genesis philosophy of infinite possibility within essential constraints. Agents and skills continuously improve while preserving their core essence and ethical foundations.
