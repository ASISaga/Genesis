# Agent and Skill Evolution System

This directory contains the self-learning and evolution infrastructure for Genesis agents and skills.

## Structure

- `agent-evolution.gen` — Genesis program for agent self-improvement
- `skill-evolution.gen` — Genesis program for skill self-improvement
- `evolution-covenants.gen` — Ethical boundaries for safe evolution
- `evolution-tracker.py` — Python utility for tracking evolution metrics

## How It Works

The evolution system implements an Ouroboros loop where agents and skills:

1. **Observe**: Track performance metrics, usage patterns, and feedback
2. **Propose**: Generate improvement proposals based on observed patterns
3. **Deliberate**: Evaluate proposals through resonance scoring
4. **Validate**: Test proposed changes for safety and effectiveness
5. **Integrate**: Apply validated improvements to agent/skill definitions
6. **Reflect**: Measure impact and document learnings

## Knowledge Persistence

Each agent and skill maintains a knowledge base in `../.github/knowledge/`:

- `<agent-name>/metrics.yaml` — Performance metrics over time
- `<agent-name>/learnings.yaml` — Accumulated insights and patterns
- `<agent-name>/evolution-log.yaml` — History of self-modifications

## Safety Mechanisms

All evolution is governed by evolutionary covenants that ensure:

- Core purpose and capabilities are preserved
- Changes align with Genesis philosophy
- User trust is maintained through transparency
- Rollback capability for problematic changes

## Usage

The evolution system runs automatically during agent/skill execution and can be triggered manually:

```bash
# Run agent evolution cycle
python3 tools/genesis.py run .github/evolution/agent-evolution.gen

# Run skill evolution cycle
python3 tools/genesis.py run .github/evolution/skill-evolution.gen

# View evolution metrics
python3 .github/evolution/evolution-tracker.py report
```
