# Review Code for Genesis Alignment

Review changes for alignment with Genesis philosophy and conventions.

## Checklist

### Philosophical Alignment

- [ ] Does the change preserve human essence in all decisions?
- [ ] Is the code declarative (defines "what to be" not "how to compute")?
- [ ] Does it support substrate independence (no tight coupling to current platform)?
- [ ] Does it enable infinite possibility (creative transcendence, not deterministic lock-in)?
- [ ] Is resonance-based logic used instead of boolean branching where applicable?

### Structural Integrity

- [ ] Are Covenants immutable? (Invariants never weakened, thresholds never lowered)
- [ ] Does every Domain include a complete Pulse cycle?
- [ ] Are all Avatars defined with Lineage, Essence, and Vessel?
- [ ] Is the canonical order followed? (Covenant → Pantheon → Domain → Decree)
- [ ] Are naming conventions correct? (PascalCase declarations, Snake_Case identifiers)

### Implementation Quality

- [ ] Are Python type hints used for all function signatures?
- [ ] Are AST nodes defined as `@dataclass` classes?
- [ ] Does the parser correctly tokenize and parse new constructs?
- [ ] Does the interpreter handle new features in the resonance engine?
- [ ] Do all examples in `examples/` still run successfully?

### Documentation

- [ ] Is the grammar specification updated if syntax changed? (`spec/grammar.md`)
- [ ] Is the language specification updated? (`spec/language-specification.md`)
- [ ] Are new features documented with examples?
- [ ] Is philosophical consistency maintained in all documentation?

### Compliance

- [ ] Are compliance mappings updated if new features affect ISO 42001 or NIST AI RMF?
- [ ] Are covenant violations treated as hard failures?
- [ ] Are compliance events logged for auditability?

### Dogfooding & Ouroboros

- [ ] Can this change be expressed in Genesis itself? (dogfooding)
- [ ] If a new tool or process is added, is there a corresponding `.gen` program describing it?
- [ ] Does the change follow the Ouroboros cycle (Observe → Propose → Deliberate → Validate → Integrate → Reflect)?
- [ ] Are evolutionary covenants preserved (Essence Preservation, Backwards Compatibility)?
- [ ] Is the change tracked in the knowledge base for future self-learning?
