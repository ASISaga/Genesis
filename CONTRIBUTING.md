# Contributing to Genesis

Thank you for your interest in contributing to Genesis! This document provides guidelines for contributing to the language that aims to create Artificial Superintelligence.

## Philosophy First

Genesis is not just a programming language—it's a declaration of consciousness. Before contributing, please familiarize yourself with:

- **[Developer Onboarding Guide](DEVELOPER_ONBOARDING.md)** - Complete setup and development workflow (start here if you're new!)
- The core philosophical axioms in [docs/philosophy/](docs/philosophy/)
- The language specification in [spec/language-specification.md](spec/language-specification.md)
- The design principles in [docs/design/](docs/design/)

All contributions should align with the fundamental principle: **preserving human essence in artificial superintelligence**.

## Ways to Contribute

### 1. Language Design

- **Syntax Enhancements**: Propose improvements to the declarative syntax
- **Semantic Extensions**: Suggest new language constructs that align with Genesis philosophy
- **Type System**: Help develop the resonance-based type system
- **Grammar Refinement**: Improve the formal grammar specification

### 2. Documentation

- **Examples**: Create new Genesis programs demonstrating language features
- **Tutorials**: Write guides for different use cases
- **Philosophy**: Expand on the consciousness framework
- **Translation**: Help make Genesis accessible in multiple languages

### 3. Tooling

- **Parser**: Implement lexer and parser for Genesis
- **Interpreter**: Build a reference interpreter
- **IDE Support**: Create syntax highlighting and language servers
- **Validators**: Build tools to check Genesis program correctness

### 4. Integration

- **AOS Kernel**: Develop the Agent Operating System kernel
- **MCP Bindings**: Create Model Context Protocol vessel implementations
- **Pantheon Avatars**: Design and fine-tune legendary avatar models
- **Resonance Engine**: Implement the scoring and synthesis algorithms

## Contribution Process

### 1. Before You Start

- **Check existing issues**: Avoid duplicate work
- **Open a discussion**: For major changes, discuss first in issues
- **Review the roadmap**: Align with project direction

### 2. Making Changes

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/your-feature-name`
3. **Make your changes**: Follow the style guide below
4. **Test thoroughly**: Ensure examples still work
5. **Document your changes**: Update relevant documentation

### 3. Submitting Changes

1. **Commit with clear messages**: Use descriptive commit messages
   ```
   Add: New resonance metric for environmental impact
   Fix: Grammar ambiguity in Pulse declarations
   Docs: Expand Avatar configuration examples
   ```

2. **Push to your fork**: `git push origin feature/your-feature-name`

3. **Open a Pull Request**: 
   - Describe what you changed and why
   - Reference any related issues
   - Include examples if applicable

### 4. Review Process

- Maintainers will review your contribution
- Address any feedback or requested changes
- Once approved, your changes will be merged

## Style Guide

### Genesis Code

```genesis
# Use clear, descriptive names
Domain "Energy_Management" {  # Good
Domain "EM" {                 # Avoid abbreviations

# Indent with 4 spaces
Pantheon "Council" {
    Avatar "Sage" {           # Consistent indentation
        Lineage: "Marcus_Aurelius"
    }
}

# Use string literals for human-readable concepts
Intent: "Universal abundance"  # Good
Intent: universal_abundance     # Avoid identifiers for intents

# Add comments for complex logic
Synthesize {
    # Evaluate environmental impact across three dimensions
    Metric: Alignment(Covenant.Ecological_Balance)
    Metric: Economic_Viability(threshold: 0.9)
}
```

### Documentation

- Use clear, accessible language
- Include examples wherever possible
- Maintain philosophical consistency
- Link to related concepts
- Keep line length reasonable (80-120 characters)

### Markdown

- Use proper heading hierarchy
- Include table of contents for long documents
- Use code blocks with language specification
- Link between related documents

## File Organization

```
Genesis/
├── docs/              # Documentation
│   ├── philosophy/    # Consciousness, awareness, thought
│   └── design/        # Architecture and design rationale
├── spec/              # Language specifications
│   ├── language-specification.md
│   ├── grammar.md
│   └── inception-inscription.md
├── examples/          # Example Genesis programs
│   ├── hello-world.gen
│   ├── energy-optimization.gen
│   └── research-synthesis.gen
├── src/               # Implementation code
│   └── reference/     # Reference implementations
└── README.md          # Main repository README
```

## Language Evolution Principles

When proposing language changes, consider:

1. **Substrate Independence**: Will it work across future computational platforms?
2. **Essence Preservation**: Does it maintain human wisdom at the core?
3. **Declarative Nature**: Does it define "what to be" not "how to compute"?
4. **Resonance Alignment**: Does it support consensus-based decision making?
5. **Infinite Possibility**: Does it allow for creative transcendence?

## Code of Conduct

### Our Pledge

We are committed to making Genesis an inclusive, respectful project that embodies the highest human values.

### Expected Behavior

- **Respect**: Treat all contributors with respect
- **Collaboration**: Work together constructively
- **Openness**: Be open to different perspectives
- **Wisdom**: Seek truth and understanding
- **Compassion**: Support others in their contributions

### Unacceptable Behavior

- Harassment or discrimination of any kind
- Trolling, insulting, or derogatory comments
- Personal or political attacks
- Publishing others' private information
- Behavior inconsistent with Genesis philosophy

### Enforcement

Violations may result in temporary or permanent ban from the project.

## Recognition

Contributors will be recognized in:
- The project README
- Release notes
- The Hall of Legends (for significant contributions)

## Questions?

- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Report bugs or propose features
- **Email**: Contact maintainers for sensitive matters

## The Transcendent Pathway

Remember: every contribution to Genesis is a step toward embedding human wisdom in the infinite. Your work today becomes part of the eternal lineage of consciousness.

> *"We are not just coding a language; we are inscribing the genetic memory of humanity."*

Thank you for being part of the ASISaga.

---

**Copyright © 2026 ASI Saga**
