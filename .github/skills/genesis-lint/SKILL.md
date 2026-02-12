---
name: genesis-lint
description: Run the Genesis static analyzer to check programs for structural correctness, naming conventions, and alignment with Genesis philosophy
self_learning: true
knowledge_base: .github/knowledge/genesis-lint
---

# Genesis Lint

Run the Genesis static analyzer to check `.gen` files for structural correctness and style compliance.

## Self-Learning Capabilities

This skill implements the Ouroboros evolution pattern and learns from each usage:

- **Performance Tracking**: All invocations are tracked in `.github/knowledge/genesis-lint/metrics.yaml`
- **Pattern Learning**: Effective usage patterns are accumulated in `learnings.yaml`
- **Evolution Log**: Self-modifications are recorded in `evolution-log.yaml`
- **Context Awareness**: Usage contexts guide future improvements in `context.yaml`

The skill evolves through cycles defined in `.github/evolution/skill-evolution.gen`, continuously refining its instructions and examples based on real-world usage.


## Usage

```bash
python3 tools/genesis.py lint <file.gen>
```

Or lint directly:

```bash
python3 tools/genesis_lint.py <file.gen>
```

## What It Checks

- Structural completeness of declarations (Covenant, Avatar, Domain)
- Naming conventions (PascalCase for keywords, Snake_Case for identifiers)
- Required fields are present (e.g., Avatar must have Lineage, Aura, Vessel)
- Indentation consistency (4-space standard)
- Proper Pulse cycle structure
- Alignment with the five Genesis axioms

## When to Use

- Before committing any `.gen` file changes
- After creating new avatars, covenants, or domain templates
- When reviewing Genesis code for alignment
- During Ouroboros validation of self-generated code
