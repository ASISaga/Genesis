---
name: genesis-repl
description: Launch the interactive Genesis REPL for exploratory development, testing declarations, and debugging resonance scoring in real-time
self_learning: true
knowledge_base: .github/knowledge/genesis-repl
---

# Genesis REPL

Launch the interactive Genesis Read-Eval-Print Loop for exploratory development.

## Self-Learning Capabilities

This skill implements the Ouroboros evolution pattern and learns from each usage:

- **Performance Tracking**: All invocations are tracked in `.github/knowledge/genesis-repl/metrics.yaml`
- **Pattern Learning**: Effective usage patterns are accumulated in `learnings.yaml`
- **Evolution Log**: Self-modifications are recorded in `evolution-log.yaml`
- **Context Awareness**: Usage contexts guide future improvements in `context.yaml`

The skill evolves through cycles defined in `.github/evolution/skill-evolution.gen`, continuously refining its instructions and examples based on real-world usage.


## Usage

```bash
python3 tools/genesis.py repl
```

Or start the REPL directly:

```bash
python3 tools/genesis_repl.py
```

## What It Does

- Provides an interactive shell for entering Genesis declarations
- Parses and interprets Genesis code in real time
- Maintains session state across commands (defined Covenants, Avatars, Domains persist)
- Supports command history

## When to Use

- To experiment with new Genesis constructs interactively
- To test individual declarations before writing a full `.gen` file
- To debug resonance scoring with immediate feedback
- For developer onboarding and learning the Genesis language
- For rapid prototyping during Ouroboros evolution cycles
