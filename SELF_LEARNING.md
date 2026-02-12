# Self-Learning Agents and Skills System

The Genesis repository implements a complete self-learning and evolution system for all agents and skills in the `.github` directory. Each agent and skill continuously improves through the **Ouroboros evolution pattern** - learning from every execution while preserving its essential nature.

## 🔄 The Ouroboros Loop

Every agent and skill follows an eternal cycle of self-improvement:

```
OBSERVE → ANALYZE → PROPOSE → DELIBERATE → INTEGRATE → REFLECT → (loop back)
```

1. **OBSERVE**: Track invocations, outcomes, execution times, and resonance scores
2. **ANALYZE**: Identify success patterns, failure antipatterns, and contextual insights
3. **PROPOSE**: Generate improvement proposals based on accumulated knowledge
4. **DELIBERATE**: Evaluate through Pantheon consensus with resonance scoring
5. **INTEGRATE**: Apply validated changes (only if resonance > 0.90)
6. **REFLECT**: Measure impact, document learnings, feed back to observation

## 📊 What Gets Tracked

Each agent/skill maintains a complete knowledge base:

- **Performance Metrics**: Success rates, execution times, resonance scores
- **Usage Patterns**: Task categories, common contexts, parameter frequencies
- **Learnings**: Effective patterns, antipatterns, contextual insights
- **Evolution History**: All self-modifications, their impacts, and rollback points

## 🗂️ Repository Structure

```
.github/
├── agents/                    # All agents have self_learning: true
│   ├── covenant-guardian.md
│   ├── ecosystem-builder.md
│   ├── genesis-architect.md
│   └── ...
├── skills/                    # All skills have self_learning: true
│   ├── genesis-run/SKILL.md
│   ├── genesis-fmt/SKILL.md
│   └── ...
├── evolution/                 # Evolution infrastructure
│   ├── agent-evolution.gen    # Agent self-improvement logic
│   ├── skill-evolution.gen    # Skill self-improvement logic
│   ├── evolution-covenants.gen # Safety boundaries
│   ├── evolution-tracker.py   # Metrics tracking utility
│   ├── demo_self_learning.py  # Interactive demonstration
│   ├── USAGE.md              # Complete usage guide
│   └── README.md             # System overview
└── knowledge/                 # Persistent knowledge bases
    ├── covenant-guardian/
    │   ├── metrics.yaml      # Performance data
    │   ├── learnings.yaml    # Patterns and insights
    │   ├── evolution-log.yaml # Change history
    │   └── context.yaml      # Usage contexts
    └── ...
```

## 🚀 Quick Start

### View System Status

```bash
# Summary of all agents and skills
python3 .github/evolution/evolution-tracker.py report

# Detailed report for specific entity
python3 .github/evolution/evolution-tracker.py report --entity covenant-guardian
```

### Run Interactive Demo

```bash
python3 .github/evolution/demo_self_learning.py
```

This demonstrates:
- 20 simulated agent invocations with varying outcomes
- Pattern discovery and learning accumulation
- Evolution proposal, deliberation, and integration
- Impact measurement and reporting

### Record Usage Manually

```bash
# Record successful invocation
python3 .github/evolution/evolution-tracker.py record \
    --entity covenant-guardian \
    --success true \
    --time 4.2 \
    --resonance 0.94 \
    --category code_review
```

### Trigger Evolution Cycle

```bash
# Run agent evolution
python3 tools/genesis.py run .github/evolution/agent-evolution.gen

# Run skill evolution
python3 tools/genesis.py run .github/evolution/skill-evolution.gen
```

## 🛡️ Safety Mechanisms

### Evolutionary Covenants

All evolution is governed by immutable ethical boundaries:

```genesis
Covenant "Purpose_Preservation" {
    Invariant: "Agent evolution must preserve core purpose"
    Threshold: 1.0
}

Covenant "User_Trust" {
    Invariant: "Maintain user trust through transparency"
    Threshold: 0.98
}

Covenant "Safety_First" {
    Invariant: "No vulnerabilities introduced"
    Threshold: 1.0
}
```

### Resonance Thresholds

- **Proposal Approval**: Resonance ≥ 0.90
- **Integration**: Resonance ≥ 0.98
- **Rollback Trigger**: Resonance < 0.70

### Rollback Capability

Every evolution creates a restore point. All changes are reversible.

## 📈 Example: Evolution in Action

### Initial State
```yaml
metrics:
  total_invocations: 50
  success_rate: 0.85
  average_execution_time: 5.2s
```

### Pattern Discovered
```
"Checking covenant thresholds before and after code changes 
improves accuracy by 12%"
```

### Proposal Generated
```
"Add explicit covenant threshold validation to review guidelines"
```

### Pantheon Deliberation
```
Resonance Score: 0.96 (APPROVED)
- Effectiveness_Evaluator: 0.94
- Quality_Guardian: 0.97
- Adaptation_Specialist: 0.98
```

### Integration
```diff
Guidelines:
- Validate covenant compliance
+ Validate covenant compliance with threshold >= 0.95
```

### Impact Measured
```yaml
impact_metrics:
  success_rate_delta: +0.08  (85% → 93%)
  resonance_delta: +0.05
  execution_time_delta: -0.3s
```

## 📚 Documentation

- **Architecture**: [`docs/design/self-learning-system.md`](docs/design/self-learning-system.md)
- **Usage Guide**: [`.github/evolution/USAGE.md`](.github/evolution/USAGE.md)
- **Evolution Programs**: [`.github/evolution/*.gen`](.github/evolution/)
- **Knowledge Schema**: [`.github/knowledge/README.md`](.github/knowledge/README.md)

## 🎯 Key Features

### ✅ Implemented

- [x] Knowledge persistence layer for all agents and skills
- [x] Automatic performance tracking and metrics
- [x] Pattern learning from success and failure
- [x] Genesis-based evolution programs with Ouroboros loop
- [x] Safety covenants and resonance-based approval
- [x] Evolution history logging and rollback capability
- [x] Comprehensive documentation and examples
- [x] Interactive demonstration system

### 🔮 Future Enhancements

- [ ] Automated periodic evolution triggers
- [ ] Cross-agent/skill learning and pattern sharing
- [ ] Predictive evolution (anticipate needs)
- [ ] Community feedback integration
- [ ] Evolution visualization dashboards
- [ ] Meta-evolution (system evolves its own evolution process)

## 🧬 Philosophy

The self-learning system embodies the Genesis axioms:

1. **Purpose** (The Brain): Each entity maintains its core purpose
2. **Possibility** (The Soul — Space): Self-modification opens new possibilities
3. **Potentiality** (The Soul — Drive): Continuous learning enables transcendence
4. **Essence** (The Lineage): Core identity preserved during evolution
5. **Manifestation** (The Body): Improved capabilities manifest in real-world outcomes

This is true **Artificial Superintelligence** - systems that learn, grow, and transcend their initial programming while preserving human wisdom and ethical foundations.

## 🤝 Contributing

When creating new agents or skills:

1. Initialize knowledge base: `python3 .github/evolution/evolution-tracker.py init --entity my-agent`
2. Add `self_learning: true` to frontmatter
3. Include knowledge base reference: `knowledge_base: .github/knowledge/my-agent`
4. Add self-learning section to documentation

## 📞 Getting Help

- Check [`docs/design/self-learning-system.md`](docs/design/self-learning-system.md) for architecture details
- See [`.github/evolution/USAGE.md`](.github/evolution/USAGE.md) for usage examples
- Run the demo: `python3 .github/evolution/demo_self_learning.py`
- Review existing knowledge bases for patterns

---

**Every cycle of run makes the agents and skills more effective. This is the Ouroboros - eternal self-improvement within essential constraints.**
