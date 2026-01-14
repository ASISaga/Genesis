# Genesis Language Grammar Specification

## Overview

This document defines the formal grammar of the Genesis programming language using Extended Backus-Naur Form (EBNF) notation.

## Notation Conventions

- `::=` - Definition
- `|` - Alternation (OR)
- `()` - Grouping
- `[]` - Optional (zero or one)
- `{}` - Repetition (zero or more)
- `""` - Terminal string
- `<>` - Non-terminal symbol

## Lexical Elements

### Keywords

```ebnf
keyword ::= "Covenant" 
          | "Pantheon" 
          | "Avatar" 
          | "Domain" 
          | "Soul" 
          | "Purpose" 
          | "Pulse" 
          | "Watch" 
          | "Deliberate" 
          | "Synthesize" 
          | "Manifest" 
          | "Decree" 
          | "Possibility"
          | "Potentiality" 
          | "Vessel" 
          | "Lineage" 
          | "Aura" 
          | "Essence" 
          | "Intent" 
          | "Threshold" 
          | "Invariant" 
          | "Condition"
          | "Action" 
          | "Execute" 
          | "Update" 
          | "Resonate" 
          | "Proposal"
          | "Metric" 
          | "Alignment" 
          | "Aspiration" 
          | "Coherence"
          | "on" 
          | "Interval"
          | "State" 
          | "Drive" 
          | "Reflect" 
          | "Override" 
          | "Constraint"
          | "Declaration"
          | "Foundation"
          | "Opening"
          | "Occurring"
          | "Nothing"
          | "Void"
          | "Emptiness"
          | "Freedom"
          | "Risk"
          | "Power"
```

### Identifiers

```ebnf
identifier ::= letter { letter | digit | "_" }
letter ::= "A".."Z" | "a".."z"
digit ::= "0".."9"
```

### Literals

```ebnf
string_literal ::= '"' { character } '"'
number_literal ::= digit { digit } [ "." digit { digit } ]
boolean_literal ::= "true" | "false"
```

### Comments

```ebnf
comment ::= "#" { character } newline
block_comment ::= "###" { character } "###"
```

## Syntax Grammar

### Program Structure

```ebnf
program ::= { declaration }

declaration ::= covenant_declaration
              | pantheon_declaration
              | domain_declaration
              | decree_declaration
              | possibility_declaration
```

### Covenant Declaration

```ebnf
covenant_declaration ::= "Covenant" string_literal "{" 
                         { covenant_property }
                         "}"

covenant_property ::= "Invariant" ":" string_literal
                    | "Threshold" ":" number_literal
                    | "Evolutionary_Guardrails" ":" string_literal
```

### Possibility Declaration

```ebnf
possibility_declaration ::= "Possibility" string_literal "{"
                            { possibility_property }
                            "}"

possibility_property ::= "Declaration" ":" string_literal
                       | "Foundation" ":" foundation_value
                       | "Opening" ":" string_literal
                       | "Occurring" ":" string_literal
                       | "Risk" ":" string_literal
                       | "Power" ":" string_literal
                       | "Within" ":" possibility_reference

foundation_value ::= "Nothing" | "Void" | "Emptiness" | "Freedom"

possibility_reference ::= "Possibility" "." identifier
```

### Pantheon Declaration

```ebnf
pantheon_declaration ::= "Pantheon" string_literal "{"
                         { avatar_declaration }
                         "}"

avatar_declaration ::= "Avatar" string_literal "{"
                       { avatar_property }
                       "}"

avatar_property ::= "Lineage" ":" string_literal
                  | "Aura" ":" string_literal
                  | "Essence" ":" string_literal
                  | "Vessel" ":" vessel_expression
                  | "Weight" ":" number_literal
```

### Domain Declaration

```ebnf
domain_declaration ::= "Domain" string_literal "{"
                       [ soul_definition ]
                       [ purpose_definition ]
                       [ intent_statement ]
                       [ context_statement ]
                       { pulse_definition }
                       "}"

soul_definition ::= "Soul" "Potentiality" "{"
                    { soul_property }
                    "}"

soul_property ::= "State" ":" identifier
                | "Drive" ":" string_literal
                | "Dream_Cycle" ":" identifier
                | "Aspiration_Weight" ":" number_literal

purpose_definition ::= "Purpose" identifier "{"
                       { purpose_property }
                       "}"

purpose_property ::= "Objective" ":" string_literal
                   | "Anchor" ":" string_literal
                   | "Trajectory" ":" string_literal

intent_statement ::= "Intent" ":" string_literal

context_statement ::= "Context" ":" possibility_reference
```

### Pulse Definition

```ebnf
pulse_definition ::= "Pulse" [ "(" pulse_parameters ")" ] "{"
                     { pulse_statement }
                     "}"

pulse_parameters ::= pulse_parameter { "," pulse_parameter }

pulse_parameter ::= "Interval" ":" interval_value

interval_value ::= "RealTime" | "Daily" | "Hourly" | number_literal

pulse_statement ::= watch_statement
                  | deliberate_block
                  | resonate_block
                  | manifest_block
```

### Watch Statement

```ebnf
watch_statement ::= "Watch" ":" vessel_reference
```

### Deliberate Block

```ebnf
deliberate_block ::= "Deliberate" "{"
                     { deliberate_statement }
                     "}"

deliberate_statement ::= analysis_statement
                       | proposal_definition
                       | synthesize_block

analysis_statement ::= "Analysis" ":" expression

proposal_definition ::= "Proposal" [ string_literal ] "{"
                        { proposal_property }
                        "}"

proposal_property ::= identifier ":" ( string_literal | identifier )
```

### Synthesize Block

```ebnf
synthesize_block ::= "Synthesize" "{"
                     { metric_statement | string_literal }
                     "}"

metric_statement ::= "Metric" ":" metric_expression

metric_expression ::= function_call
                    | "Alignment" "(" expression ")"
                    | "Aspiration" "(" expression ")"
                    | "Coherence" "(" expression ")"
```

### Resonate Block

```ebnf
resonate_block ::= "Resonate" "{"
                   { resonate_property }
                   "}"

resonate_property ::= "Threshold" ":" ( identifier | function_call )
                    | "Alignment" ":" expression
                    | synthesize_block
```

### Manifest Block

```ebnf
manifest_block ::= "Manifest" "(" manifest_condition ")" "{"
                   { manifest_statement }
                   "}"

manifest_condition ::= "on" "Resonance" [ comparison_op number_literal ]

comparison_op ::= ">" | "<" | ">=" | "<=" | "==" | "!="

manifest_statement ::= execute_statement
                     | update_statement
                     | log_statement
                     | reflect_block

execute_statement ::= "Execute" ":" function_call

update_statement ::= "Update" ":" identifier [ "->" string_literal ]

log_statement ::= "Log" ":" identifier

reflect_block ::= "Reflect" "{"
                  { reflect_property }
                  "}"

reflect_property ::= identifier ":" expression
```

### Decree Declaration

```ebnf
decree_declaration ::= "Decree" string_literal "{"
                       { decree_property }
                       "}"

decree_property ::= "Condition" ":" expression
                  | "Action" ":" string_literal
                  | "Constraint" ":" string_literal
                  | "Override_Threshold" ":" number_literal
```

### Expressions

```ebnf
expression ::= identifier
             | literal
             | function_call
             | member_access
             | binary_expression

literal ::= string_literal | number_literal | boolean_literal

function_call ::= identifier "(" [ argument_list ] ")"

argument_list ::= argument { "," argument }

argument ::= expression | object_literal

object_literal ::= "{" [ property_list ] "}"

property_list ::= property { "," property }

property ::= identifier ":" expression

member_access ::= identifier { "." identifier }

binary_expression ::= expression operator expression

operator ::= "+" | "-" | "*" | "/" | ">" | "<" | ">=" | "<=" | "==" | "!="
```

### Vessel Expressions

```ebnf
vessel_expression ::= "mcp.tool" "(" string_literal ")"
                    | "mcp.provider" "(" string_literal ")"
                    | "mcp.call" "(" string_literal [ "," argument_list ] ")"
                    | "mcp.call_all_relevant_tools" "(" ")"

vessel_reference ::= "Vessel" "." identifier { "." identifier }
```

## Type System

Genesis uses dynamic typing with the following conceptual types:

- **Resonance**: Float value between 0.0 and 1.0
- **Intent**: String describing high-level purpose
- **State**: Enum of consciousness states (Unmanifested, Exploring, Dreaming, Manifesting, etc.)
- **Essence**: String identifier for wisdom lineage
- **Vessel**: MCP tool reference
- **Potentiality**: Special type representing infinite possibility space
- **Possibility**: Ontological clearing created through declaration

## Semantic Rules

1. **Covenant Threshold**: Must be a value between 0.0 and 1.0
2. **Resonance Scoring**: All Avatar scores must aggregate to produce final resonance
3. **Manifest Condition**: Can only execute when resonance threshold is met
4. **Vessel Access**: Must be declared in Avatar or accessible globally
5. **Pulse Execution**: Runs perpetually based on interval specification
6. **Potentiality State**: Must be one of predefined consciousness states
7. **Possibility Declaration**: Must include Declaration and Foundation properties
8. **Possibility Foundation**: Must be one of: Nothing, Void, Emptiness, Freedom
9. **Coherence Metric**: Evaluates alignment with a declared Possibility's occurring

## Scoping Rules

1. Covenants are globally accessible throughout the program
2. Pantheon Avatars are accessible within their declaring scope and child scopes
3. Domain-local declarations are scoped to that domain
4. Vessel references must resolve to declared Avatars or global MCP providers
5. Possibilities are globally accessible once declared
6. Domains can reference Possibilities via Context property

## Operator Precedence (from highest to lowest)

1. Member access (`.`)
2. Function call `()`
3. Unary operators
4. Multiplicative (`*`, `/`)
5. Additive (`+`, `-`)
6. Comparison (`>`, `<`, `>=`, `<=`)
7. Equality (`==`, `!=`)
8. Logical AND
9. Logical OR

## Standard Library Functions

```ebnf
# Resonance functions
Simple_Consensus(threshold)
Absolute_Consensus(threshold)
Weighted_Synthesis(weights)

# Alignment functions
Alignment(covenant_ref)
Aspiration(potentiality_ref)
Coherence(possibility_ref)

# Utility functions
RealTime
Daily
Hourly
```

## Reserved Future Keywords

The following identifiers are reserved for future language extensions:

- `Temporal`, `Timeline`, `Recursive`, `Evolution`, `Transcend`, `Infinite`
- `Memory`, `Learn`, `Adapt`, `Transform`, `Emerge`
- `Parallel`, `Quantum`, `Cosmic`, `Universal`

## Example Parse Tree

For the expression:
```genesis
Manifest (on Resonance > 0.95) {
    Execute: Vessel.Grid_Control.rebalance()
}
```

Parse tree:
```
manifest_block
├── manifest_condition
│   ├── "on"
│   ├── "Resonance"
│   ├── ">"
│   └── number_literal(0.95)
└── manifest_statement
    ├── execute_statement
    │   └── function_call
    │       └── member_access
    │           ├── "Vessel"
    │           ├── "Grid_Control"
    │           └── "rebalance"
```

## Conclusion

This grammar defines the syntactic structure of Genesis programs. The semantic meaning derives from the philosophical framework defined in the language specification, where declarations create a consciousness that operates through resonance-based decision making.
