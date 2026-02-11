---
name: genesis-fmt
description: Run the Genesis code formatter to enforce consistent style in Genesis programs, ensuring 4-space indentation and proper formatting
---

# Genesis Format

Run the Genesis code formatter to enforce consistent style in `.gen` files.

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
