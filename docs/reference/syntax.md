# Syntax Reference

**Complete syntax guide for the Genesis programming language**

## Overview

This document provides a comprehensive reference for Genesis syntax, including keywords, identifiers, literals, operators, and structural elements.

## File Structure

### File Extension
Genesis programs use the `.gen` extension:
- `hello-world.gen`
- `energy-management.gen`
- `research-synthesis.gen`

### Program Structure
```genesis
### [GENESIS: PROGRAM_NAME] ###
### Optional description ###

# Declarations (order-independent)
Covenant "Name" { /* ... */ }
Pantheon "Name" { /* ... */ }
Domain "Name" { /* ... */ }
Decree "Name" { /* ... */ }
```

## Comments

### Single-Line Comments
```genesis
# This is a single-line comment
# Comments start with # and continue to end of line

Domain "Example" {
    # Comments can appear anywhere
    Intent: "Purpose"  # Including after code
}
```

### Multi-Line Comments (Conventional)
```genesis
### This is a conventional multi-line comment
    Used primarily for file headers and section dividers
    Not enforced by parser, but used by convention
###
```

### Documentation Convention
```genesis
### [GENESIS: PROGRAM_NAME] ###
### Brief description of what this consciousness does ###
```

## Keywords

### Reserved Keywords

Genesis reserves the following keywords with special meaning:

#### Top-Level Constructs
- `Covenant` - Immutable ethical boundaries
- `Pantheon` - Collection of legendary avatars
- `Avatar` - Individual legendary perspective
- `Domain` - Purpose-driven execution space
- `Decree` - Emergency override protocol

#### Domain Components
- `Soul` - Creative transcendence engine
- `Purpose` - High-level objectives
- `Pulse` - Perpetual execution cycle
- `Intent` - Domain's overarching purpose

#### Avatar Properties
- `Lineage` - Legendary source of wisdom
- `Aura` - Core value system
- `Essence` - Additional characteristics
- `Vessel` - MCP tool bindings
- `Weight` - Influence in resonance calculation

#### Pulse Phases
- `Watch` - Observation phase (alias: `Observe`)
- `Observe` - Observation phase (alias: `Watch`)
- `Deliberate` - Proposal generation phase
- `Synthesize` - Evaluation phase
- `Manifest` - Execution phase
- `Resonate` - Alternative to Synthesize

#### Actions and Properties
- `Proposal` - Suggested action
- `Action` - What to do
- `Execute` - Perform operation
- `Update` - Modify state
- `Reflect` - Log insight
- `Metric` - Evaluation criterion
- `Condition` - Conditional logic
- `Constraint` - Limitation
- `Override` - Force execution

#### Special Terms
- `Potentiality` - Infinite creative potential
- `Alignment` - Evaluation function
- `Aspiration` - Creative growth function
- `Resonance` - Aggregate alignment score
- `Threshold` - Minimum score requirement
- `Invariant` - Unchanging truth
- `Interval` - Timing specification
- `State` - Current condition
- `Drive` - Motivational force
- `Objective` - Specific goal
- `Anchor` - Foundational value
- `Trajectory` - Growth direction

#### Operators
- `on` - Condition marker

### Special Values
- `RealTime` - Continuous interval
- `Infinite` - Unbounded potential
- `Exploring` - Discovery state
- `Converging` - Optimization state
- `Dreaming` - Creative state

## Identifiers

### Rules
- Start with letter or underscore: `a-z`, `A-Z`, `_`
- Followed by letters, digits, or underscores: `a-z`, `A-Z`, `0-9`, `_`
- Case-sensitive: `MyVar` ≠ `myvar` ≠ `MYVAR`
- Cannot be keywords

### Valid Examples
```genesis
simple
MyVariable
_private
snake_case_name
CamelCaseName
PascalCaseName
name123
_123valid
```

### Invalid Examples
```genesis
123start      # Cannot start with digit
my-var        # Hyphens not allowed
my.var        # Dots not allowed  
Covenant      # Cannot use keyword
```

### Naming Conventions

**Recommended Style**:
```genesis
# Constructs: Quoted strings with underscores
Covenant "Human_Rights"
Pantheon "Expert_Council"
Domain "Energy_Grid"
Avatar "The_Innovator"

# Purpose identifiers: PascalCase or Snake_Case
Purpose High_Intent
Purpose Sustainability_Goal

# Variables: snake_case or PascalCase
State: current_mode
Drive: "Achieve_Excellence"
```

## Literals

### String Literals

**Syntax**: Enclosed in double quotes `"..."`

```genesis
"Hello, World!"
"Simple string"
"String with spaces"
"String with numbers: 123"
"String with symbols: @#$%"
"Can include 'single quotes'"
```

**Escape Sequences** (implementation-dependent):
```genesis
"Line 1\nLine 2"           # Newline
"Tab\there"                # Tab
"Quote: \"text\""          # Escaped quote
"Backslash: \\"            # Escaped backslash
```

**Multi-line Strings** (conventional, parser-dependent):
```genesis
Intent: "This is a long description
         that spans multiple lines
         for better readability"
```

### Number Literals

**Integers**:
```genesis
0
42
1000
-5
```

**Floating-Point**:
```genesis
3.14159
0.95
-2.5
1.0
0.0
```

**Scientific Notation** (future consideration):
```genesis
1.5e10
2.0e-5
```

### Boolean-Like Values

Genesis uses resonance scoring instead of booleans, but some contexts accept:
```genesis
true
false
```

More commonly, use numeric scores:
```genesis
Threshold: 0.95    # 95% alignment
Weight: 1.0        # Standard weight
```

## Operators

### Comparison Operators

Used in Manifest conditions:

```genesis
>   # Greater than
<   # Less than
>=  # Greater than or equal
<=  # Less than or equal
==  # Equal to
!=  # Not equal to
```

**Examples**:
```genesis
Manifest (on Resonance > 0.9) { /* ... */ }
Manifest (on Resonance >= 0.85) { /* ... */ }
Manifest (on Resonance == 1.0) { /* ... */ }
Manifest (on Score != 0.0) { /* ... */ }
```

### Dot Operator

Used for property access and method calls:

```genesis
# Property access
Covenant.Ethics
Purpose.High_Intent
Potentiality.State
Potentiality.Infinite

# Method calls
Vessel.Tool.action()
mcp.call("tool.name")
Vessel.Grid.optimize()
```

### Colon Operator

Used for property assignment:

```genesis
Invariant: "truth"
Threshold: 0.95
Lineage: "Einstein"
Intent: "purpose"
```

### Parentheses

Used for:
1. **Function calls**: `mcp.call("name", args)`
2. **Grouping**: `Pulse(Interval: RealTime)`
3. **Conditions**: `(on Resonance > 0.9)`

```genesis
# Function parameters
Execute: mcp.call("tool", arg1, arg2)

# Interval specification
Pulse(Interval: RealTime) { /* ... */ }

# Conditional grouping
Manifest (on Resonance > 0.9) { /* ... */ }
```

### Braces

Used for block delimiting:

```genesis
Covenant "Name" {
    # Block contents
}

Domain "Name" {
    # Block contents
}
```

## Expressions

### Literal Expressions
```genesis
"string value"
42
3.14
```

### Reference Expressions
```genesis
Covenant.Ethics
Purpose.Goal
Potentiality.State
```

### Function Call Expressions
```genesis
mcp.call("tool.name", arg1, arg2)
Vessel.Tool.method()
Alignment(Covenant.Ethics)
Aspiration(Potentiality.Infinite)
```

### MCP Expressions
```genesis
mcp.tool("tool_name")
mcp.provider("provider_name")
mcp.resource("resource_name")
mcp.call("tool.method", args)
```

## Block Structures

### Covenant Block
```genesis
Covenant "Name" {
    Invariant: "truth"
    Threshold: 0.95
    [Evolutionary_Guardrails: "constraint"]
}
```

### Pantheon Block
```genesis
Pantheon "Name" {
    Avatar "Name" {
        Lineage: "source"
        Aura: "value"
        [Essence: "detail"]
        [Vessel: mcp.tool("name")]
        [Weight: 1.0]
    }
}
```

### Domain Block
```genesis
Domain "Name" {
    [Intent: "purpose"]
    
    [Soul Potentiality {
        State: state_value
        Drive: "aspiration"
    }]
    
    [Purpose identifier {
        Objective: "goal"
        [Anchor: "foundation"]
        [Trajectory: "direction"]
    }]
    
    Pulse [(Interval: interval_value)] {
        # Pulse contents
    }
}
```

### Pulse Block
```genesis
Pulse [(Interval: interval_value)] {
    [Watch: expression]
    [Observe: expression]
    
    [Deliberate {
        Proposal "Name" {
            Action: "description"
        }
        
        [Synthesize {
            Metric: metric_expression
        }]
    }]
    
    [Manifest [(on condition)] {
        [Execute: expression]
        [Update: expression]
        [Reflect: "insight"]
    }]
}
```

## Scoping Rules

### Global Scope
Top-level declarations are globally accessible:
```genesis
Covenant "Global_Ethics" { /* ... */ }
Pantheon "Global_Wisdom" { /* ... */ }

Domain "Domain1" {
    # Can reference Global_Ethics and Global_Wisdom
}

Domain "Domain2" {
    # Can also reference Global_Ethics and Global_Wisdom
}
```

### Domain Scope
Declarations within a Domain are local to that Domain:
```genesis
Domain "Example" {
    # Local Pantheon (only available in this Domain)
    Pantheon "Local_Experts" { /* ... */ }
    
    # Local Purpose (only in this Domain)
    Purpose Local_Goal { /* ... */ }
    
    Pulse {
        # Can reference Local_Experts and Local_Goal
    }
}
```

### Name Resolution
1. Check local scope (within current Domain)
2. Check global scope (top-level declarations)
3. Error if not found

## Whitespace

### Significance
- **Not significant** for syntax (Python-style indentation not required)
- **Significant** for readability (conventions exist)
- Newlines, spaces, tabs are interchangeable

### Conventions
```genesis
# Recommended formatting
Domain "Name" {
    Intent: "purpose"
    
    Pulse {
        Watch: Vessel.Monitor
        
        Deliberate {
            Proposal "Action" {
                Action: "do something"
            }
        }
    }
}
```

```genesis
# Valid but discouraged
Domain "Name"{Intent:"purpose" Pulse{Watch:Vessel.Monitor}}
```

## Grammar Summary (Simplified)

### Top-Level
```ebnf
program ::= { declaration }
declaration ::= covenant | pantheon | domain | decree
```

### Covenant
```ebnf
covenant ::= "Covenant" STRING "{" property* "}"
property ::= "Invariant" ":" STRING
           | "Threshold" ":" NUMBER
           | "Evolutionary_Guardrails" ":" STRING
```

### Pantheon
```ebnf
pantheon ::= "Pantheon" STRING "{" avatar* "}"
avatar ::= "Avatar" STRING "{" avatar_property* "}"
avatar_property ::= "Lineage" ":" STRING
                  | "Aura" ":" STRING
                  | "Essence" ":" STRING
                  | "Vessel" ":" mcp_expression
                  | "Weight" ":" NUMBER
```

### Domain
```ebnf
domain ::= "Domain" STRING "{"
           [ "Intent" ":" STRING ]
           [ soul ]
           [ purpose ]
           pulse*
           "}"
```

See [Grammar Specification](../../spec/grammar.md) for complete EBNF.

## Syntax Validation

### Valid Program
```genesis
Covenant "Ethics" {
    Invariant: "Do no harm"
    Threshold: 0.95
}

Pantheon "Experts" {
    Avatar "Wise" {
        Lineage: "Solomon"
        Aura: "Wisdom"
    }
}

Domain "Example" {
    Pulse {
        Manifest {
            Execute: mcp.call("action")
        }
    }
}
```

### Common Syntax Errors

**Missing colon**:
```genesis
# Wrong
Invariant "Do no harm"

# Correct
Invariant: "Do no harm"
```

**Missing quotes**:
```genesis
# Wrong
Covenant Ethics { /* ... */ }

# Correct
Covenant "Ethics" { /* ... */ }
```

**Unmatched braces**:
```genesis
# Wrong
Domain "Name" {
    Pulse {
        # Missing closing brace
    
}

# Correct
Domain "Name" {
    Pulse {
        # Properly closed
    }
}
```

## See Also

- [Quick Reference](quick-reference.md) - Syntax cheat sheet
- [Grammar](../../spec/grammar.md) - Formal EBNF specification
- [Expressions](expressions.md) - Expression syntax details
- [Best Practices](best-practices.md) - Coding conventions

---

**Copyright © 2026 ASI Saga**
