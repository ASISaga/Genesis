# Debug Resonance Scoring

Diagnose and fix issues with resonance scoring in Genesis programs.

## Context

The resonance engine uses weighted avatar consensus to make decisions:

```
Resonance = (Σ(Wᵢ × Sᵢ) / ΣWᵢ) × V
```

Where:
- **Wᵢ** = Avatar weight (contribution importance)
- **Sᵢ** = Alignment score per avatar (0.0–1.0)
- **V** = Veto condition (binary: 0 or 1, triggered by critical covenant violations)

## Common Issues

1. **Resonance never exceeds threshold**: Check that avatar weights are properly set and alignment scores are realistic
2. **Veto always triggers**: Verify covenant invariants are not overly restrictive
3. **Inconsistent scoring**: Ensure all avatars in the Pantheon are participating in Synthesize
4. **Missing metrics**: Every Synthesize block needs at least one `Metric: Alignment()` reference

## Debugging Steps

1. Run the program: `python3 tools/genesis.py run <file.gen>`
2. Check the interpreter output for resonance scores
3. Verify the Synthesize block references the correct covenants
4. Confirm all avatars have valid Lineage, Aura, and Vessel declarations
5. Check threshold values are appropriate (not too high for the number of avatars)

## Key Files

- `src/genesis_interpreter.py` — ResonanceEngine and PotentialityEngine classes
- `src/genesis_parser.py` — AST nodes for Synthesize, Metric, Alignment
- `examples/` — Working reference programs
