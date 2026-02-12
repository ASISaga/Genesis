---
applyTo: "**/*.gen"
---

# Genesis Language Conventions

## Syntax Style

- Use `PascalCase` for declaration keywords: `Covenant`, `Domain`, `Pantheon`, `Avatar`
- Use `Snake_Case` for identifiers: `Humanity_Eternal`, `Global_Energy_Grid`
- Use string literals for human-readable concepts: `Intent: "Universal abundance"`
- Indent with 4 spaces, never tabs
- Use `#` for single-line comments, `### ... ###` for block comments

## Declaration Order

Genesis programs should follow this canonical order:

1. **Covenants** — Ethical foundations first
2. **Pantheon** — Assemble wisdom council
3. **Domains** — Define purpose and operational scope
4. **Decrees** — Evolutionary or emergency instructions

## Covenant Structure

```genesis
Covenant "Name" {
    Invariant: "Immutable ethical principle"
    Threshold: 0.99
}
```

## Avatar Structure

```genesis
Avatar "Title" {
    Lineage: "Historical_Figure"
    Essence: "Domain_of_Expertise"
    Vessel: mcp.tool("Tool_Name")
}
```

## Pulse Pattern

Every Domain should contain a Pulse cycle:

```genesis
Pulse(Interval: RealTime) {
    Watch: Vessel.Data_Source
    Deliberate {
        Proposal: "Action description"
        Synthesize {
            Metric: Alignment(Covenant.Name)
            Metric: Aspiration(Potentiality.Infinite)
        }
    }
    Manifest (on Resonance > 0.95) {
        Execute: Vessel.Tool.action()
    }
}
```

## Resonance Logic

Genesis replaces boolean conditions with resonance scoring:

- Use `Alignment()` for covenant-based metrics
- Use `Aspiration()` for potentiality-based metrics
- Use `Coherence()` for cross-domain consistency
- Threshold values range from 0.0 to 1.0
- Prefer high thresholds (≥ 0.9) for critical decisions

## Naming Guidelines

- **Covenant names** reflect ethical principles: `Humanity_Eternal`, `Truth_Seeking`
- **Avatar titles** reflect archetypes: `The Visionary`, `The Sage`, `The Pioneer`
- **Domain names** describe purpose: `Global_Energy_Grid`, `Research_Discovery`
- **Lineage** references historical figures: `Leonardo_da_Vinci`, `Marcus_Aurelius`

## Keywords Reference

Primary: `Covenant`, `Pantheon`, `Avatar`, `Domain`, `Soul`, `Purpose`, `Pulse`
Actions: `Watch`, `Deliberate`, `Synthesize`, `Manifest`, `Decree`, `Execute`
Properties: `Lineage`, `Aura`, `Vessel`, `Essence`, `Intent`, `Threshold`, `Invariant`
Metrics: `Alignment`, `Aspiration`, `Coherence`, `Resonance`
Possibility: `Possibility`, `Potentiality`, `Declaration`, `Opening`, `Nothing`, `Void`, `Freedom`

## Dogfooding Patterns

Genesis programs can describe Genesis itself — tools, processes, and evolution:

- **Tool as Domain**: Express each tool (CLI, formatter, linter) as a Domain with a Pulse cycle
- **Quality as Covenant**: Encode tool quality standards as immutable Covenants
- **Review as Pantheon**: Create expert councils that evaluate Genesis code quality
- **Self-validation**: Use Genesis programs to validate other Genesis programs

```genesis
# Example: Describing the Genesis formatter as a Domain
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

## Ouroboros Evolution Pattern

The Ouroboros pattern enables controlled self-modification:

```genesis
# The six phases of self-evolution
# 1. Observe → 2. Propose → 3. Deliberate → 4. Validate → 5. Integrate → 6. Reflect
# Results feed back to Observe, creating an eternal improvement cycle

# Safety: All evolution is bounded by Covenants with Threshold: 1.0
Covenant "Essence_Preservation" {
    Invariant: "Evolution must preserve the five axioms and human wisdom"
    Threshold: 1.0
}
```

See `examples/ouroboros/self-evolution-loop.gen` for the complete pattern.
