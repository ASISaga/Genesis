---
applyTo: "**/*.py"
---

# Python Runtime Conventions

## Architecture

The Genesis reference implementation in Python follows this architecture:

- `src/genesis_parser.py` — Lexer, Parser, and AST node definitions
- `src/genesis_interpreter.py` — Runtime interpreter with resonance engine
- `src/genesis_runtime.py` — AOS integration, compliance, and lifecycle management
- `src/genesis_cli.py` — Command-line interface for executing .gen files
- `src/compliance.py` — ISO 42001 and NIST AI RMF compliance layer
- `tools/` — Ecosystem tools (CLI, REPL, formatter, linter, package manager)

## Style

- Use Python type hints from `typing` for all function signatures
- Use `dataclass` for AST nodes and data structures
- Use `Enum` for token types and categorical values
- Follow PEP 8 with these project-specific conventions:
  - Section separators: `# ====...====` comments between major sections
  - Docstrings: Triple-quoted strings on classes and public functions
  - Module docstrings: Describe architecture and philosophy at the top

## Parser Conventions

- Token types are defined as `Enum` members matching Genesis keywords exactly
- AST nodes use `@dataclass` with typed fields
- The Lexer tokenizes Genesis source into a stream of `Token` objects
- The Parser consumes tokens and produces an AST tree
- Error handling uses descriptive messages referencing Genesis concepts

## Interpreter Conventions

- The `GenesisRuntime` class is the main execution engine
- The `ResonanceEngine` calculates alignment scores using weighted avatar consensus
- The `PotentialityEngine` manages creative exploration and dream cycles
- Resonance formula: `(Σ(Wᵢ × Sᵢ) / ΣWᵢ) × V` where W=weight, S=score, V=veto

## Compliance

- All runtime operations log compliance events for ISO 42001 and NIST AI RMF
- Covenant violations are treated as hard failures (never silent)
- Threshold checks must use the resonance scoring system, not boolean logic

## Substrate Independence

The Python implementation is designed for "The Cradle" temporal stage. Code should:

- Abstract computational primitives behind clear interfaces
- Avoid tight coupling to Python-specific features where possible
- Use patterns that map to the Genesis declarative model
- Document which substrate assumptions are made
