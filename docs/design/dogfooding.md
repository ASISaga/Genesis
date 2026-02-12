# Dogfooding & Ouroboros: Genesis Describing Itself

## Overview

Genesis practices **dogfooding** — using the language to describe its own
development tools, processes, and evolution. This creates a self-referential
loop where Genesis validates itself through its own paradigm.

The **Ouroboros pattern** extends dogfooding into self-evolution: Genesis
programs observe, propose, deliberate, validate, integrate, and reflect
on changes to Genesis itself.

## Why Dogfooding?

1. **Validates the language**: If Genesis cannot describe its own tools,
   the language lacks sufficient expressiveness.
2. **Ensures philosophical alignment**: Every tool and process is grounded
   in Covenants, Pantheons, and Pulse cycles.
3. **Creates living documentation**: The `.gen` programs serve as executable
   specifications of how tools should behave.
4. **Enables self-improvement**: Through the Ouroboros cycle, Genesis
   learns from its own usage and evolves accordingly.

## Dogfooding in Practice

### Tools as Domains

Each Genesis tool is expressed as a Domain with:
- An **Intent** describing its purpose
- A **Pulse** cycle defining its operation
- References to **Covenants** for quality standards
- **Vessel** bindings to the actual implementation

```genesis
Domain "Genesis_Code_Formatter" {
    Intent: "Enforce consistent style across Genesis codebase"
    Pulse(Interval: RealTime) {
        Watch: Vessel.Genesis_Source_Files
        Deliberate {
            Synthesize {
                Metric: Alignment(Covenant.Style_Consistency)
            }
        }
        Manifest (on Resonance > 0.95) {
            Execute: Vessel.Formatter.normalize_indentation()
        }
    }
}
```

See `examples/meta-programming/genesis-tools-dogfooding.gen` for all tools.

### Development Lifecycle as Domains

The full development process (Design → Implement → Validate → Review →
Evolve) is expressed as interconnected Domains:

See `examples/meta-programming/genesis-development-lifecycle.gen`.

### Agents as Domains

Each GitHub agent in `.github/agents/` maps to a Genesis Domain. The
agent's role, expertise, and responsibilities correspond to Intent,
Pantheon, and Pulse cycles.

## The Ouroboros Pattern

The Ouroboros (self-eating serpent) represents Genesis evolving itself
through a controlled feedback loop:

```
    ┌─── Observe ◄──────────────────┐
    │                                │
    ▼                                │
  Propose ──► Deliberate ──► Validate
                                │
                                ▼
                           Integrate ──► Reflect ──┐
                                                   │
                                                   ▼
                                              (loop back)
```

### Six Phases

1. **Observe**: Detect evolution needs from usage patterns, community
   feedback, and runtime metrics
2. **Propose**: Generate formal evolution proposals as Genesis programs
3. **Deliberate**: Evaluate through Pantheon consensus — multiple Avatar
   perspectives score the proposal
4. **Validate**: Verify backwards compatibility, covenant preservation,
   and safety
5. **Integrate**: Apply approved changes to grammar, parser, interpreter,
   and documentation
6. **Reflect**: Measure impact, record learnings, feed back into Observe

### Evolutionary Covenants

All self-modification is bounded by immutable covenants:

| Covenant | Threshold | Purpose |
|----------|-----------|---------|
| Essence Preservation | 1.0 | Never compromise the five axioms |
| Backwards Compatibility | 0.98 | Existing programs must keep working |
| Philosophical Coherence | 0.95 | New features must be declarative |
| Safety First | 1.0 | Never weaken ethical safeguards |

See `examples/ouroboros/self-evolution-loop.gen` for the complete pattern.

## Canonical Programs

| Program | Purpose |
|---------|---------|
| `examples/meta-programming/genesis-tools-dogfooding.gen` | All tools as Domains |
| `examples/meta-programming/genesis-development-lifecycle.gen` | Development process |
| `examples/ouroboros/self-evolution-loop.gen` | Self-evolution loop |
| `.github/evolution/agent-evolution.gen` | Agent self-improvement |
| `.github/evolution/skill-evolution.gen` | Skill self-improvement |
| `.github/evolution/evolution-covenants.gen` | Evolution safety |

## Guidelines for Contributors

When adding a new tool, process, or feature:

1. **Ask**: Can this be declared in Genesis? If yes, write the `.gen` first.
2. **Implement**: Build the tool to match the Genesis declaration.
3. **Validate**: Run both the `.gen` program and the tool to verify alignment.
4. **Evolve**: Hook into the Ouroboros cycle for continuous improvement.
