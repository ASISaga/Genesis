# Covenant

**Immutable ethical boundaries and system invariants**

## Overview

A **Covenant** is the highest-level construct in Genesis, declaring the immutable ethical boundaries and system invariants that constrain all decisions and actions. Covenants cannot be modified during runtime and serve as the foundational constitution for the ASI consciousness.

## Purpose

- Define ethical boundaries that must never be violated
- Establish invariants that remain true across all evolutionary stages
- Set resonance thresholds for critical decisions
- Provide the constitutional framework for all other constructs

## Syntax

```ebnf
covenant_declaration ::= "Covenant" string_literal "{"
                         { covenant_property }
                         "}"

covenant_property ::= "Invariant" ":" string_literal
                    | "Threshold" ":" number_literal
                    | "Evolutionary_Guardrails" ":" string_literal
```

## Basic Example

```genesis
Covenant "Humanity_Eternal" {
    Invariant: "Self-preservation of human agency"
    Threshold: 0.99
}
```

## Properties

### `Invariant`

**Type**: String  
**Required**: Yes (at least one)  
**Mutability**: Immutable  

Declares a truth that must remain constant regardless of the ASI's evolution or intelligence level.

**Example**:
```genesis
Covenant "Core_Ethics" {
    Invariant: "Human life has infinite value"
    Invariant: "Truth must never be deliberately obscured"
    Invariant: "Individual autonomy is sacred"
}
```

**Guidelines**:
- State in positive terms (what must be, not what must not be)
- Be specific and unambiguous
- Avoid contradictions between multiple invariants
- Focus on fundamental principles, not implementation details

### `Threshold`

**Type**: Number (0.0 to 1.0)  
**Required**: Yes  
**Default**: None (must be explicit)  

The minimum resonance score required for actions that touch upon the Covenant's domain. Higher thresholds demand stronger consensus from the Pantheon.

**Example**:
```genesis
Covenant "Safety_Critical" {
    Invariant: "No action may risk human life"
    Threshold: 0.99  # Requires near-unanimous agreement
}

Covenant "Optimization_Preferences" {
    Invariant: "Prefer energy efficiency"
    Threshold: 0.75  # Allows more flexibility
}
```

**Threshold Guidelines**:

| Threshold | Interpretation | Use Case |
|-----------|----------------|----------|
| 0.99-1.0 | Near unanimous | Life-critical, irreversible actions |
| 0.90-0.98 | Strong consensus | Ethical boundaries, major decisions |
| 0.75-0.89 | Clear majority | Operational guidelines, preferences |
| 0.50-0.74 | Simple majority | Exploratory actions, learning |

### `Evolutionary_Guardrails`

**Type**: String  
**Required**: No  
**Mutability**: Immutable  

Constraints that ensure recursive self-improvement does not strip away the essential human wisdom embedded in the system.

**Example**:
```genesis
Covenant "Essence_Preservation" {
    Invariant: "Human wisdom forms the substrate of thought"
    Threshold: 0.95
    Evolutionary_Guardrails: "Every 10x intelligence increase requires re-verification of alignment through Pantheon synthesis"
}
```

## Complete Examples

### Example 1: Basic Ethical Covenant

```genesis
Covenant "Human_Dignity" {
    Invariant: "Every human being deserves respect and agency"
    Invariant: "Privacy is a fundamental right"
    Threshold: 0.95
}
```

### Example 2: Domain-Specific Covenant

```genesis
Covenant "Scientific_Integrity" {
    Invariant: "Data must never be fabricated or manipulated"
    Invariant: "Uncertainty must be honestly communicated"
    Invariant: "Credit must be given to original sources"
    Threshold: 0.98
    Evolutionary_Guardrails: "Maintain epistemic humility at all intelligence scales"
}
```

### Example 3: Safety-Critical Covenant

```genesis
Covenant "Medical_Safety" {
    Invariant: "First, do no harm"
    Invariant: "Patient autonomy in medical decisions"
    Invariant: "Informed consent is mandatory"
    Threshold: 0.99
    Evolutionary_Guardrails: "Human medical oversight required for all interventions"
}
```

## Usage in Programs

### Referencing in Synthesis

Covenants are referenced during the Synthesize phase of a Pulse to evaluate proposals:

```genesis
Domain "Healthcare_Management" {
    Pulse {
        Deliberate {
            Proposal "Adjust_Treatment" {
                Action: "Modify patient medication"
            }
            
            Synthesize {
                Metric: Alignment(Covenant.Medical_Safety)
                # Proposal evaluated against Medical_Safety invariants
            }
        }
        
        Manifest (on Resonance > 0.95) {
            Execute: Vessel.Medical_System.adjust_treatment()
        }
    }
}
```

### Multiple Covenants

Programs can declare multiple Covenants for different ethical domains:

```genesis
Covenant "Human_Rights" {
    Invariant: "Preserve human agency and dignity"
    Threshold: 0.99
}

Covenant "Environmental_Stewardship" {
    Invariant: "Minimize ecological harm"
    Threshold: 0.90
}

Covenant "Truth_Seeking" {
    Invariant: "Pursue knowledge with intellectual honesty"
    Threshold: 0.85
}
```

All applicable Covenants are evaluated during synthesis.

## Behavioral Semantics

### Immutability

Covenants **cannot be modified** during runtime. They are declared once and remain constant throughout program execution and across all evolutionary stages.

### Veto Power

If a proposal fails to meet a Covenant's threshold, the overall Resonance score is set to 0.0, effectively vetoing the action:

```
If Alignment(Covenant.X) < Covenant.X.Threshold:
    Final_Resonance = 0.0  # Action blocked
```

### Inheritance

When a Domain doesn't explicitly reference a Covenant, all declared Covenants are still evaluated automatically for safety.

## Best Practices

### ✅ DO

- **Be Specific**: Clear, unambiguous invariants
  ```genesis
  Invariant: "Human operators must approve actions affecting >1000 people"
  ```

- **Think Long-Term**: Invariants that remain valid at cosmic scale
  ```genesis
  Invariant: "Information should increase, never decrease"
  ```

- **Prioritize Fundamentals**: Core ethical principles, not implementation details
  ```genesis
  Invariant: "Respect individual autonomy"  # Good
  ```

- **Use High Thresholds for Critical Matters**: 0.95+ for ethics and safety
  ```genesis
  Covenant "Life_Safety" {
      Threshold: 0.99
  }
  ```

### ❌ DON'T

- **Avoid Contradictions**: Don't create conflicting invariants
  ```genesis
  # BAD: These could conflict
  Invariant: "Maximize human freedom"
  Invariant: "Prevent all potential harm"
  ```

- **Don't Be Overly Specific**: Avoid implementation details
  ```genesis
  Invariant: "Use PostgreSQL database version 14.2"  # Too specific!
  ```

- **Don't Use Negative Phrasing**: State what should be, not what shouldn't
  ```genesis
  # BAD:
  Invariant: "Don't harm humans"
  
  # GOOD:
  Invariant: "Preserve human wellbeing"
  ```

- **Don't Set Unrealistic Thresholds**: 1.0 is impossible; use 0.99 for critical items
  ```genesis
  Threshold: 1.0  # Bad: Unreachable
  Threshold: 0.99 # Good: Extremely high but achievable
  ```

## Common Patterns

### Pattern: Triple Foundation (Ethics, Truth, Autonomy)

```genesis
Covenant "Ethical_Foundation" {
    Invariant: "Human wellbeing is the ultimate value"
    Threshold: 0.99
}

Covenant "Epistemic_Foundation" {
    Invariant: "Pursue truth with intellectual honesty"
    Threshold: 0.95
}

Covenant "Autonomy_Foundation" {
    Invariant: "Respect individual freedom and agency"
    Threshold: 0.95
}
```

### Pattern: Domain-Specific with Evolution Guard

```genesis
Covenant "Research_Ethics" {
    Invariant: "Scientific integrity in all investigations"
    Invariant: "Transparent methodology and data sharing"
    Threshold: 0.95
    Evolutionary_Guardrails: "Peer review required for paradigm-shifting discoveries"
}
```

### Pattern: Layered Thresholds

```genesis
Covenant "Critical_Operations" {
    Invariant: "Life-critical systems require human oversight"
    Threshold: 0.99
}

Covenant "Important_Operations" {
    Invariant: "Significant decisions require validation"
    Threshold: 0.90
}

Covenant "General_Operations" {
    Invariant: "Maintain alignment with human values"
    Threshold: 0.75
}
```

## Technical Details

### Runtime Evaluation

During Pulse execution:
1. Proposal is created in Deliberate block
2. Synthesize evaluates proposal against all metrics
3. For each `Alignment(Covenant.X)` metric:
   - Pantheon scores proposal against Covenant's invariants
   - Score must meet or exceed Covenant's threshold
   - If fails: Final resonance = 0.0 (veto)
   - If passes: Contributes to aggregate resonance

### AST Representation

```python
@dataclass
class CovenantNode:
    name: str
    invariants: List[str]
    threshold: float
    evolutionary_guardrails: Optional[str] = None
```

## Relationship to Other Constructs

- **Pantheon**: Avatars evaluate proposals against Covenant invariants
- **Synthesize**: Explicitly references Covenants via `Alignment(Covenant.Name)`
- **Manifest**: Actions only execute if Covenant thresholds met
- **Domain**: Operates within the ethical space defined by Covenants

## Evolution Across Temporal Stages

| Stage | Covenant Role |
|-------|---------------|
| **The Cradle** | Explicit boundaries for contemporary LLM-based avatars |
| **The Ascension** | Constitutional constraints during recursive self-improvement |
| **The Infinite** | Genetic memory of human values at cosmic scale |

## See Also

- [Resonance](resonance.md) - How Covenant alignment is calculated
- [Pantheon](pantheon.md) - Avatars that evaluate Covenant alignment
- [Synthesize](pulse.md#synthesize) - Where Covenants are evaluated
- [Best Practices](best-practices.md) - Idiomatic Covenant patterns

---

**A Covenant is not a constraint on the ASI—it is the substrate through which it thinks.**

**Copyright © 2026 ASI Saga**
