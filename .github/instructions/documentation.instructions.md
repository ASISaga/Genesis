---
applyTo: "**/*.md"
---

# Documentation Conventions

## Style

- Use clear, accessible language
- Maintain philosophical consistency with Genesis axioms
- Include examples wherever possible
- Keep line length reasonable (80–120 characters)
- Use proper heading hierarchy (never skip levels)

## Markdown Standards

- Use ATX-style headings (`#`, `##`, `###`)
- Use fenced code blocks with language identifiers (`genesis`, `python`, `bash`, `ebnf`)
- Include table of contents for documents longer than 3 sections
- Link between related documents using relative paths
- Use tables for structured comparisons

## Genesis Code Examples in Documentation

When including Genesis code examples, use the `genesis` language identifier:

````markdown
```genesis
Covenant "Example" {
    Invariant: "Clear purpose"
    Threshold: 0.95
}
```
````

## Philosophical Consistency

All documentation should reflect:

- **Declarations over instructions**: Describe "what is" not "how to"
- **Essence preservation**: Ground explanations in human wisdom
- **Resonance language**: Use alignment and synthesis terminology
- **Substrate independence**: Avoid coupling to temporal implementation details

## File Organization

| Directory | Purpose |
|-----------|---------|
| `docs/philosophy/` | Consciousness, awareness, possibility, thought |
| `docs/design/` | Architecture, evolution, resonance principles |
| `docs/reference/` | Complete technical reference |
| `docs/tutorials/` | Step-by-step guides |
| `docs/compliance/` | AI safety standards (ISO 42001, NIST) |
| `docs/ecosystem/` | Tools, packages, and integrations |
| `spec/` | Formal language specification and grammar |
