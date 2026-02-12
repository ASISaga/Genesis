---
name: genesis-dogfooding
description: Use Genesis language to describe, analyze, and improve Genesis itself - meta-programming for self-improvement and validation
self_learning: true
knowledge_base: .github/knowledge/genesis-dogfooding
license: MIT
---

# Genesis Dogfooding

Use Genesis language to describe, analyze, and improve Genesis itself through meta-programming.

## Self-Learning Capabilities

This skill implements the Ouroboros evolution pattern and learns from each usage:

- **Performance Tracking**: All invocations are tracked in `.github/knowledge/genesis-dogfooding/metrics.yaml`
- **Pattern Learning**: Effective usage patterns are accumulated in `learnings.yaml`
- **Evolution Log**: Self-modifications are recorded in `evolution-log.yaml`
- **Context Awareness**: Usage contexts guide future improvements in `context.yaml`

The skill evolves through cycles defined in `.github/evolution/skill-evolution.gen`, continuously refining its instructions and examples based on real-world usage.


## Purpose

Dogfooding Genesis means using the language to express its own development, evolution, and validation processes. This creates a self-referential feedback loop where Genesis programs can:

- Define the purpose and structure of Genesis tools
- Express quality criteria for Genesis code
- Describe Genesis language evolution goals
- Validate Genesis programs using Genesis declarations

## How It Works

### 1. Define Genesis Tools as Domains

Express each Genesis tool (run, fmt, lint, repl) as a Genesis Domain with Purpose and Pulse cycles:

```genesis
Domain "Genesis_CLI_Runner" {
    Purpose: "Execute Genesis programs and manifest their declared reality"
    
    Pulse(Interval: OnDemand) {
        Watch: FileSystem.Genesis_Programs
        Deliberate {
            Proposal: "Parse and interpret .gen file"
            Synthesize {
                Metric: Alignment(Covenant.Syntactic_Correctness)
                Metric: Alignment(Covenant.Semantic_Completeness)
            }
        }
        Manifest (on Resonance > 0.95) {
            Execute: Interpreter.run()
        }
    }
}
```

### 2. Express Code Quality as Covenants

Define what makes Genesis code correct and aligned:

```genesis
Covenant "Syntactic_Correctness" {
    Invariant: "All declarations follow grammar.md EBNF specification"
    Threshold: 1.0
}

Covenant "Philosophical_Alignment" {
    Invariant: "Code embodies the five axioms: Purpose, Possibility, Potentiality, Essence, Manifestation"
    Threshold: 0.95
}

Covenant "Substrate_Independence" {
    Invariant: "Code remains valid across future computational platforms"
    Threshold: 0.90
}
```

### 3. Create Genesis Avatars for Code Review

Use Pantheon of legendary developers to review Genesis code:

```genesis
Pantheon "Genesis_Code_Reviewers" {
    Avatar "The_Language_Designer" {
        Lineage: "Guido_van_Rossum"
        Essence: "Language_Design"
        Vessel: mcp.tool("code_review")
    }
    
    Avatar "The_Philosopher" {
        Lineage: "Edsger_Dijkstra"
        Essence: "Formal_Methods"
        Vessel: mcp.tool("static_analysis")
    }
    
    Avatar "The_Pragmatist" {
        Lineage: "Rob_Pike"
        Essence: "Simplicity"
        Vessel: mcp.tool("complexity_analysis")
    }
}
```

### 4. Self-Validation Loop

Genesis programs that validate other Genesis programs:

```genesis
Domain "Genesis_Self_Validator" {
    Purpose: "Ensure Genesis codebase maintains quality and alignment"
    
    Pulse(Interval: OnCommit) {
        Watch: VCS.Changed_Genesis_Files
        Deliberate {
            Proposal: "Validate changed .gen files"
            Synthesize {
                Metric: Alignment(Covenant.Syntactic_Correctness)
                Metric: Alignment(Covenant.Philosophical_Alignment)
                Metric: Coherence(All_Genesis_Programs)
            }
        }
        Manifest (on Resonance > 0.90) {
            Execute: Linter.check_all()
            Execute: Formatter.apply_style()
            Execute: Runtime.run_examples()
        }
    }
}
```

## When to Use This Skill

- When adding new Genesis tools or features
- When refactoring Genesis codebase
- When validating Genesis programs meet quality standards
- When expressing Genesis development processes declaratively
- When creating meta-level Genesis programs that operate on Genesis code

## Example Workflow

1. **Express a new Genesis feature as a Genesis program**
   ```bash
   # Create feature-spec.gen describing the new feature
   python3 tools/genesis.py run feature-specs/new-construct.gen
   ```

2. **Validate implementation against specification**
   ```bash
   # Run dogfooding validator
   python3 tools/genesis.py run validators/implementation-check.gen
   ```

3. **Use Genesis to generate Genesis examples**
   ```bash
   # Meta-generate example programs
   python3 tools/genesis.py run generators/example-creator.gen
   ```

## Integration with Development Workflow

Add to `.github/workflows/genesis-dogfooding.yml`:

```yaml
name: Genesis Dogfooding
on: [push, pull_request]
jobs:
  dogfood:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Run Genesis self-validation
        run: python3 tools/genesis.py run .github/validators/self-check.gen
```

## Best Practices

1. **Start Simple**: Begin with basic tool definitions, then add complexity
2. **Align with Axioms**: Ensure meta-programs reflect Genesis philosophy
3. **Iterate**: Use feedback from dogfooding to improve both language and tools
4. **Document**: Create clear examples showing how Genesis describes itself
5. **Validate**: Run all examples to ensure they execute correctly

## Resources

- `examples/meta-programming/` - Meta-level Genesis programs
- `validators/` - Genesis programs that validate Genesis code
- `spec/dogfooding-patterns.md` - Patterns for self-referential programming
