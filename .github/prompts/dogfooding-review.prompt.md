# Dogfooding & Ouroboros Review

Review changes to ensure they follow Genesis dogfooding and Ouroboros practices.

## Dogfooding Checklist

- [ ] Can this change be expressed as a Genesis program?
- [ ] If a new tool or process is introduced, is there a corresponding `.gen` file?
- [ ] Does the `.gen` description include proper Covenants, Pantheon, and Pulse cycle?
- [ ] Is the dogfooding program referenced in `examples/meta-programming/`?
- [ ] Does the Genesis description match the actual implementation?

## Ouroboros Checklist

- [ ] Does the change follow the six-phase evolution cycle?
  - Observe → Propose → Deliberate → Validate → Integrate → Reflect
- [ ] Are evolutionary covenants preserved?
  - Essence Preservation (Threshold: 1.0)
  - Backwards Compatibility (Threshold: 0.98)
  - Philosophical Coherence (Threshold: 0.95)
  - Safety First (Threshold: 1.0)
- [ ] Is the change tracked in the knowledge base (`.github/knowledge/`)?
- [ ] Can the change be safely rolled back if it causes regressions?
- [ ] Is resonance scoring used instead of boolean logic for decisions?

## Canonical References

- `examples/meta-programming/genesis-tools-dogfooding.gen` — Tools as Domains
- `examples/meta-programming/genesis-development-lifecycle.gen` — Full lifecycle
- `examples/ouroboros/self-evolution-loop.gen` — Ouroboros evolution loop
- `.github/evolution/evolution-covenants.gen` — Evolution safety boundaries

## Questions to Ask

1. **Is this dogfooded?** If not, create a Genesis program that declares it.
2. **Does this preserve essence?** Check against the five axioms.
3. **Is this declarative?** It should say "what to be" not "how to compute."
4. **Can this self-improve?** Hook into the Ouroboros cycle for learning.
