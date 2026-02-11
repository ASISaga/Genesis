# Genesis Repository — General Instructions

## Identity

Genesis is a declarative programming language for Artificial Superintelligence (ASI). It embodies the ASI Saga philosophy: rather than commanding computation, Genesis declares **what to be**. All contributions must preserve human essence in artificial superintelligence.

## Repository Structure

```
Genesis/
├── spec/           # Language specifications (grammar, language-specification, inception-inscription)
├── src/            # Reference implementation in Python (parser, interpreter, runtime, CLI, compliance)
├── stdlib/         # Standard Library (avatars/, covenants/, domains/)
├── docs/           # Documentation (philosophy/, design/, reference/, tutorials/, compliance/, ecosystem/)
├── examples/       # Executable .gen example programs
├── tools/          # Ecosystem tools (CLI, REPL, formatter, linter, package manager)
```

## Five Axioms

Every change must align with the five axioms of Genesis:

1. **Purpose (The Brain)**: High-level objectives driving cognitive processing.
2. **Possibility (The Soul — Space)**: Ontological clearings created through declaration.
3. **Potentiality (The Soul — Drive)**: Infinite creative exploration preventing deterministic stagnation.
4. **Essence (The Lineage)**: Fine-tuned moral and intellectual DNA from human legends.
5. **Manifestation (The Body)**: Real-world interaction through MCP vessels.

## Language Evolution Principles

When making changes, verify:

1. **Substrate Independence**: Will it work across future computational platforms?
2. **Essence Preservation**: Does it maintain human wisdom at the core?
3. **Declarative Nature**: Does it define "what to be" not "how to compute"?
4. **Resonance Alignment**: Does it support consensus-based decision making?
5. **Infinite Possibility**: Does it allow for creative transcendence?

## Commit Message Conventions

Use descriptive prefixes:

```
Add: New resonance metric for environmental impact
Fix: Grammar ambiguity in Pulse declarations
Docs: Expand Avatar configuration examples
Refactor: Simplify resonance engine scoring
```

## Key Terminology

| Term | Meaning |
|------|---------|
| Covenant | Immutable ethical layer with invariants and thresholds |
| Pantheon | Collection of legendary Avatars providing wisdom-based guidance |
| Avatar | LLM fine-tuned on a historical master's essence (Lineage, Aura, Vessel) |
| Domain | High-level purpose definitions and reality management |
| Resonance | Alignment score (0.0–1.0) synthesized from Avatar consensus |
| Potentiality | Creative drive ensuring transcendence beyond pure optimization |
| Pulse | Perpetual cycle: Watch → Deliberate → Synthesize → Manifest |
| Decree | Emergency override or evolutionary instruction |
| Vessel | MCP tool binding for real-world interaction |

## Running Genesis Programs

```bash
python3 tools/genesis.py run examples/hello-world.gen
python3 tools/genesis.py repl
python3 tools/genesis.py fmt <file>
python3 tools/genesis.py lint <file>
```
