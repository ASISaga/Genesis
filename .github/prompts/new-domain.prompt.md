# Create a New Domain

Create a new Domain template for the Genesis standard library or examples.

## Inputs

- **Domain Name**: A descriptive name for the operational domain
- **Intent**: The high-level purpose of this domain
- **Avatars**: Which avatars from the Pantheon participate
- **Covenants**: Which ethical boundaries apply

## Requirements

1. The domain must include a complete Pulse cycle (Watch → Deliberate → Synthesize → Manifest)
2. At least one Covenant must be referenced in the Synthesize block
3. At least one Avatar must participate in deliberation
4. Include a Potentiality element to prevent deterministic stagnation
5. Resonance thresholds must be appropriate for the domain's criticality
6. Follow 4-space indentation

## Template

```genesis
### Domain: [Name] ###
### Intent: [Purpose description] ###

Covenant "[Ethical_Boundary]" {
    Invariant: "[Principle]"
    Threshold: 0.95
}

Pantheon "[Council_Name]" {
    Avatar "[Role]" {
        Lineage: "[Historical_Figure]"
        Essence: "[Expertise]"
        Vessel: mcp.tool("[Tool]")
    }
}

Domain "[Name]" {
    Intent: "[High-level purpose]"

    Soul Potentiality {
        State: Active
        Drive: "[Creative direction]"
    }

    Pulse(Interval: RealTime) {
        Watch: Vessel.Data_Source

        Deliberate {
            Proposal: "[Action description]"
            Synthesize {
                Metric: Alignment(Covenant.[Name])
                Metric: Aspiration(Potentiality.Infinite)
            }
        }

        Manifest (on Resonance > 0.95) {
            Execute: Vessel.Tool.action()
        }
    }
}
```

## Reference

See `stdlib/domains/` for reusable templates and `examples/` for complete programs.
