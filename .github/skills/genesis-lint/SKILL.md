---
name: genesis-lint
description: Run the Genesis static analyzer to check programs for structural correctness, naming conventions, and alignment with Genesis philosophy
---

# Genesis Lint

Run the Genesis static analyzer to check `.gen` files for structural correctness and style compliance.

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
