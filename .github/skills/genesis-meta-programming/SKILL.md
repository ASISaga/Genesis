---
name: genesis-meta-programming
description: Write Genesis programs that generate, analyze, transform, and validate other Genesis programs - meta-level programming capabilities
license: MIT
---

# Genesis Meta-Programming

Write Genesis programs that operate on other Genesis programs - enabling code generation, transformation, analysis, and validation at the meta level.

## Purpose

Meta-programming in Genesis means writing `.gen` programs that:

- **Generate** other Genesis programs from specifications
- **Analyze** Genesis code for patterns and properties
- **Transform** Genesis programs (refactoring, optimization)
- **Validate** Genesis programs against rules and conventions
- **Synthesize** new Genesis constructs from requirements

## Core Concepts

### 1. Genesis AST as Domain Data

Treat the Genesis Abstract Syntax Tree as declarative data:

```genesis
Domain "Genesis_AST_Analyzer" {
    Purpose: "Analyze Genesis programs at AST level"
    
    Pulse(Interval: OnDemand) {
        Watch: FileSystem.Genesis_Files
        
        Deliberate {
            Proposal: "Extract program structure"
            Synthesize {
                Metric: Alignment(Covenant.Structural_Completeness)
            }
        }
        
        Manifest (on Resonance > 0.90) {
            Execute: Parser.extract_declarations()
            Execute: Analyzer.identify_patterns()
            Execute: Reporter.generate_metrics()
        }
    }
}
```

### 2. Code Generation Domains

Generate Genesis code from high-level specifications:

```genesis
Domain "Genesis_Code_Generator" {
    Purpose: "Generate Genesis programs from templates and specifications"
    
    Soul {
        Possibility: "Any valid Genesis program can be algorithmically generated"
        Potentiality: "Infinite variations of Genesis patterns"
    }
    
    Pulse(Interval: OnRequest) {
        Watch: Specifications.User_Requirements
        
        Deliberate {
            Proposal: "Generate Genesis program from spec"
            Synthesize {
                Metric: Alignment(Covenant.Syntactic_Correctness)
                Metric: Alignment(Covenant.Semantic_Completeness)
                Metric: Coherence(Template_Library)
            }
        }
        
        Manifest (on Resonance > 0.95) {
            Execute: Generator.create_covenants()
            Execute: Generator.create_pantheon()
            Execute: Generator.create_domains()
            Execute: Formatter.apply_style()
            Execute: Validator.check_output()
        }
    }
}
```

### 3. Program Transformation

Refactor and optimize Genesis programs:

```genesis
Domain "Genesis_Refactorer" {
    Purpose: "Transform Genesis programs while preserving semantics"
    
    Pulse(Interval: OnDemand) {
        Watch: VCS.Code_To_Refactor
        
        Deliberate {
            Proposal: "Apply refactoring transformation"
            Synthesize {
                Metric: Alignment(Covenant.Semantic_Preservation)
                Metric: Alignment(Covenant.Code_Improvement)
                Metric: Coherence(Original_Program)
            }
        }
        
        Manifest (on Resonance > 0.95) {
            Execute: Transformer.extract_common_patterns()
            Execute: Transformer.create_reusable_components()
            Execute: Transformer.simplify_structure()
            Execute: Tester.verify_equivalence()
        }
    }
}
```

## Meta-Programming Patterns

### Pattern 1: Template Expansion

Generate programs from templates with parameters:

```genesis
# Template: basic-domain.template.gen
Domain "{DOMAIN_NAME}" {
    Purpose: "{DOMAIN_PURPOSE}"
    
    Pulse(Interval: {PULSE_INTERVAL}) {
        Watch: {WATCH_SOURCE}
        
        Deliberate {
            Proposal: "{PROPOSAL_TEXT}"
            Synthesize {
                Metric: Alignment(Covenant.{COVENANT_NAME})
            }
        }
        
        Manifest (on Resonance > {THRESHOLD}) {
            Execute: {VESSEL}.{ACTION}()
        }
    }
}
```

Use meta-program to instantiate:

```genesis
Domain "Template_Expander" {
    Purpose: "Generate concrete programs from templates"
    
    Pulse(Interval: OnRequest) {
        Watch: Templates.Available_Templates
        Watch: Parameters.User_Inputs
        
        Deliberate {
            Proposal: "Expand template with parameters"
            Synthesize {
                Metric: Alignment(Covenant.Valid_Parameters)
            }
        }
        
        Manifest (on Resonance > 0.90) {
            Execute: Expander.substitute_parameters()
            Execute: Validator.check_generated_code()
        }
    }
}
```

### Pattern 2: Covenant Synthesis

Generate covenants from ethical requirements:

```genesis
Domain "Covenant_Generator" {
    Purpose: "Create covenants from ethical principles"
    
    Pulse(Interval: OnRequest) {
        Watch: Requirements.Ethical_Constraints
        
        Deliberate {
            Proposal: "Synthesize covenant from requirements"
            Synthesize {
                Metric: Alignment(Covenant.Ethical_Completeness)
                Metric: Alignment(Covenant.Measurable_Threshold)
            }
        }
        
        Manifest (on Resonance > 0.95) {
            Execute: Generator.create_covenant_declaration()
            Execute: Generator.derive_invariant()
            Execute: Generator.calculate_threshold()
        }
    }
}
```

### Pattern 3: Avatar Composition

Combine multiple lineages into composite avatars:

```genesis
Domain "Avatar_Composer" {
    Purpose: "Create composite avatars from multiple lineages"
    
    Pulse(Interval: OnRequest) {
        Watch: Specifications.Required_Expertise
        
        Deliberate {
            Proposal: "Compose multi-domain avatar"
            Synthesize {
                Metric: Alignment(Covenant.Expertise_Coverage)
                Metric: Coherence(Lineage_Compatibility)
            }
        }
        
        Manifest (on Resonance > 0.90) {
            Execute: Composer.select_lineages()
            Execute: Composer.blend_auras()
            Execute: Composer.configure_vessels()
        }
    }
}
```

### Pattern 4: Program Analysis

Extract insights from Genesis programs:

```genesis
Domain "Genesis_Complexity_Analyzer" {
    Purpose: "Analyze complexity and quality of Genesis programs"
    
    Pulse(Interval: OnDemand) {
        Watch: Codebase.All_Genesis_Files
        
        Deliberate {
            Proposal: "Measure program complexity and quality"
            Synthesize {
                Metric: Count(Covenant_Declarations)
                Metric: Count(Avatar_References)
                Metric: Depth(Pulse_Nesting)
                Metric: Alignment(Covenant.Simplicity)
            }
        }
        
        Manifest (on Resonance > 0.80) {
            Execute: Analyzer.compute_metrics()
            Execute: Reporter.generate_insights()
            Execute: Recommender.suggest_improvements()
        }
    }
}
```

### Pattern 5: Cross-Program Coherence

Ensure consistency across multiple Genesis programs:

```genesis
Domain "Coherence_Validator" {
    Purpose: "Ensure consistency across Genesis program ecosystem"
    
    Pulse(Interval: OnCommit) {
        Watch: VCS.Modified_Genesis_Files
        
        Deliberate {
            Proposal: "Validate cross-program coherence"
            Synthesize {
                Metric: Coherence(Covenant_Names)
                Metric: Coherence(Avatar_Definitions)
                Metric: Coherence(Naming_Conventions)
                Metric: Alignment(Covenant.Ecosystem_Consistency)
            }
        }
        
        Manifest (on Resonance > 0.90) {
            Execute: Validator.check_naming_consistency()
            Execute: Validator.verify_covenant_references()
            Execute: Validator.ensure_avatar_uniqueness()
        }
    }
}
```

## Practical Examples

### Example 1: Generate Boilerplate

Create a meta-program that generates standard Genesis project structure:

```bash
# Run the generator
python3 tools/genesis.py run meta/generate-project.gen \
    --name "My_ASI_System" \
    --covenants "Humanity_Eternal,Truth_Seeking" \
    --domains "Research,Healthcare"

# Output: Complete Genesis project with:
# - Standard covenants
# - Default pantheon
# - Domain templates
# - Example programs
```

### Example 2: Automated Refactoring

Refactor all Genesis programs to use new naming convention:

```bash
# Run the refactoring meta-program
python3 tools/genesis.py run meta/refactor-naming.gen \
    --old-style "camelCase" \
    --new-style "Snake_Case"

# Updates all .gen files automatically
```

### Example 3: Quality Dashboard

Generate quality metrics for entire Genesis codebase:

```bash
# Run the analyzer
python3 tools/genesis.py run meta/quality-dashboard.gen

# Output:
# - Total covenants: 12
# - Total avatars: 25
# - Total domains: 18
# - Average resonance threshold: 0.93
# - Code complexity score: Low
# - Philosophical alignment: High
```

## When to Use This Skill

- When creating new Genesis projects with consistent structure
- When refactoring large Genesis codebases
- When validating Genesis program quality
- When generating test cases for Genesis features
- When analyzing patterns across multiple Genesis programs
- When creating tools that operate on Genesis code

## Best Practices

1. **Validate Generated Code**: Always run lint and format on generated programs
2. **Preserve Semantics**: Transformations must maintain program meaning
3. **Test Meta-Programs**: Meta-programs should have comprehensive test suites
4. **Use AST**: Work with parsed AST rather than string manipulation
5. **Document Templates**: Clearly document template parameters and usage
6. **Version Control**: Track generated code separately from hand-written code

## Integration Points

- `meta/` - Directory for meta-programming Genesis programs
- `templates/` - Reusable Genesis program templates
- `generators/` - Code generation meta-programs
- `analyzers/` - Program analysis meta-programs
- `transformers/` - Code transformation meta-programs

## Tools and Utilities

```bash
# Generate new Genesis project
python3 tools/genesis.py meta generate-project --template standard

# Analyze codebase
python3 tools/genesis.py meta analyze --output metrics.json

# Refactor programs
python3 tools/genesis.py meta refactor --transformation extract-common-covenants

# Validate cross-program consistency
python3 tools/genesis.py meta validate --check coherence
```

## Resources

- `examples/meta-programming/` - Meta-programming examples
- `docs/meta-programming-guide.md` - Detailed guide
- `spec/meta-programming-patterns.md` - Common patterns
