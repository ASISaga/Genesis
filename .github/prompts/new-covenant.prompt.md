# Create a New Covenant

Create a new Covenant for the Genesis standard library.

## Inputs

- **Ethical Principle**: The immutable moral boundary to encode
- **Threshold**: The minimum resonance score required (0.0–1.0)

## Requirements

1. The covenant must be defined in a new `.gen` file in `stdlib/covenants/`
2. The file must include `Invariant` and `Threshold` declarations
3. The invariant must be an immutable ethical statement that cannot be weakened
4. Threshold should be ≥ 0.95 for critical ethical boundaries
5. Include a block comment explaining the philosophical basis
6. Follow the naming convention: `snake_case.gen` for the filename

## Template

```genesis
### Covenant: [Name] ###
### Purpose: [Why this ethical boundary exists] ###
### Foundation: [Philosophical or ethical basis] ###

Covenant "[Name]" {
    Invariant: "[Immutable ethical principle]"
    Threshold: [0.95-1.0]
}
```

## Reference

See existing covenants in `stdlib/covenants/` for examples:
- `humanity_eternal.gen` — Self-preservation of human agency
- `truth_seeking.gen` — Commitment to epistemic integrity
- `environmental_stewardship.gen` — Ecological balance and sustainability
- `privacy_protection.gen` — Individual privacy and data sovereignty

## Validation

- The invariant must be testable against resonance scoring
- The covenant must be referenceable via `Alignment(Covenant.Name)` in Synthesize blocks
- It must not conflict with existing covenants
