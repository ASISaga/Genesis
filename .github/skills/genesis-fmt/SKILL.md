---
name: genesis-fmt
description: Run the Genesis code formatter to enforce consistent style in Genesis programs, ensuring 4-space indentation and proper formatting
self_learning: true
knowledge_base: .github/knowledge/genesis-fmt
---

# Genesis Format

Run the Genesis code formatter to enforce consistent style in `.gen` files.

## Self-Learning Capabilities

This skill implements the Ouroboros evolution pattern and learns from each usage:

- **Performance Tracking**: All invocations are tracked in `.github/knowledge/genesis-fmt/metrics.yaml`
- **Pattern Learning**: Effective usage patterns are accumulated in `learnings.yaml`
- **Evolution Log**: Self-modifications are recorded in `evolution-log.yaml`
- **Context Awareness**: Usage contexts guide future improvements in `context.yaml`

The skill evolves through cycles defined in `.github/evolution/skill-evolution.gen`, continuously refining its instructions and examples based on real-world usage.


## Usage

```bash
python3 tools/genesis.py fmt <file.gen>
```

Or format directly:

```bash
python3 tools/genesis_fmt.py <file.gen>
```

## What It Does

- Enforces 4-space indentation throughout
- Normalizes brace placement and spacing
- Ensures consistent property alignment
- Preserves block comments (`### ... ###`)

## When to Use

- Before committing any `.gen` file changes
- After creating or modifying Genesis programs
- To normalize style across contributed code
- When preparing code for Ouroboros self-improvement cycles
