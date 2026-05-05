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

---

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
          | "Recency"
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
          | "Continuum"
          | "LoRA"
          | "Sources"
          | "TargetExamples"
          | "Register"
          | "AuditModel"
          | "MergeStrategy"
          | "RequiredSuffix"
          | "RoutingOutput"
          | "StateAuthority"
          | "ScoringMechanism"
          | "LogProbability"
          | "Normalisation"
          | "Structure"
          | "Tree"
          | "MaxDepth"
          | "StabilityCondition"
          | "Rounds"
          | "OnBelowThreshold"
          | "Verify"
          | "Assert"
          | "OnFailure"
          | "Process"
          | "Every"
          | "Partitions"
          | "Gateway"
          | "Invariants"
          | "Priority"
          | "Batch"
          | "On"
          | "Event"
          | "Threshold"
          | "Weight"
          | "Identity"
          | "Fabric"
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

---

## Syntax Grammar

### Program Structure

```ebnf
program ::= { declaration }

declaration ::= covenant_declaration
              | pantheon_declaration
              | domain_declaration
              | decree_declaration
              | possibility_declaration
              | lineage_declaration
              | continuum_declaration
              | process_declaration
              | identity_declaration
```

---

### Covenant Declaration

```ebnf
covenant_declaration ::= "Covenant" string_literal "{"
                         { covenant_property }
                         "}"

covenant_property ::= "Invariant" ":" string_literal
                    | "Threshold" ":" number_literal
                    | "Evolutionary_Guardrails" ":" string_literal
                    | "Principles" ":" object_literal
                    | "Boundaries" ":" list_literal
                    | "Verification" ":" verification_block

verification_block ::= "{" { verify_block } "}"
```

---

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

---

### Lineage Declaration

Top-level declaration that drives the LoRA training pipeline from the Genesis program.

```ebnf
lineage_declaration ::= "Lineage" string_literal "{"
                        { lineage_property }
                        "}"

lineage_property ::= "Sources" ":" "[" string_literal { "," string_literal } "]"
                   | "TargetExamples" ":" number_literal
                   | "Register" ":" string_literal
                   | "AuditModel" ":" string_literal
                   | "MergeStrategy" ":" merge_strategy_value
                   | "LoRA" ":" lora_block
                   | "RequiredSuffix" ":" "[" identifier { "," identifier } "]"

merge_strategy_value ::= "Single" | "Ensemble" | identifier

lora_block ::= "{" { lora_property } "}"

lora_property ::= "Rank" ":" number_literal
                | "Alpha" ":" number_literal
                | "TargetModules" ":" "[" identifier { "," identifier } "]"

lineage_reference ::= "Lineage" "." identifier
```

---

### Continuum Declaration

Top-level declaration of the persistent memory layer.

```ebnf
continuum_declaration ::= "Continuum" string_literal "{"
                          { continuum_property }
                          "}"

continuum_property ::= "Storage" ":" identifier
                     | "Gateway" ":" identifier
                     | "Invariants" ":" "[" identifier { "," identifier } "]"
                     | "Partitions" ":" "[" string_literal { "," string_literal } "]"
```

---

### Pantheon Declaration

```ebnf
pantheon_declaration ::= "Pantheon" string_literal "{"
                         { avatar_declaration }
                         "}"
```

### Avatar Declaration

```ebnf
avatar_declaration ::= "Avatar" string_literal [ ":" avatar_type ] "{"
                       { avatar_property }
                       "}"

avatar_type ::= "BusinessAvatar"
              | "LeadershipAvatar"
              | "PurposeAvatar"
              | "MarketingAvatar"
              | "PoetryAvatar"
              | identifier

avatar_property ::= "Lineage" ":" ( string_literal | lineage_reference )
                  | "Aura" ":" string_literal
                  | "Essence" ":" string_literal
                  | "Vessel" ":" vessel_expression
                  | "Vessel" ":" vessel_block
                  | "Weight" ":" number_literal
                  | "Domain" ":" identifier
                  | "RoutingOutput" ":" "[" identifier { "," identifier } "]"
                  | "StateAuthority" ":" "[" identifier { "," identifier } "]"
                  | "ScoringMechanism" ":" scoring_mechanism_block
                  | "Traits" ":" object_literal
                  | "Principles" ":" list_literal
                  | "Weights" ":" object_literal

vessel_block ::= "{" { vessel_statement } "}"

vessel_statement ::= vessel_expression

scoring_mechanism_block ::= scoring_type "{" { scoring_property } "}"

scoring_type ::= "LogProbability" | identifier

scoring_property ::= "Context" ":" member_access
                   | "Method" ":" string_literal
                   | "Normalisation" ":" identifier
```

---

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

---

### Pulse Definition

```ebnf
pulse_definition ::= "Pulse" [ "(" pulse_parameters ")" ] "{"
                     { pulse_statement }
                     "}"

pulse_parameters ::= pulse_parameter { "," pulse_parameter }

pulse_parameter ::= "Interval" ":" interval_value
                  | "On" ":" event_expression
                  | "Batch" ":" member_access

interval_value ::= "RealTime" | "Daily" | "Hourly" | "Weekly" | "Monthly"
                 | number_literal

event_expression ::= "Event" "(" string_literal
                     [ "," event_option { "," event_option } ] ")"

event_option ::= "Priority" ":" identifier

pulse_statement ::= watch_statement
                  | deliberate_block
                  | resonate_block
                  | manifest_block
```

---

### Watch Statement

```ebnf
watch_statement ::= "Watch" ":" vessel_reference
```

---

### Deliberate Block

```ebnf
deliberate_block ::= "Deliberate" "{"
                     { deliberate_statement }
                     "}"

deliberate_statement ::= analysis_statement
                       | proposal_definition
                       | synthesize_block
                       | "Rounds" ":" number_literal
                       | "Structure" ":" structure_expression
                       | "Proposal" ":" string_literal

analysis_statement ::= "Analysis" ":" expression

proposal_definition ::= "Proposal" [ string_literal ] "{"
                        { proposal_property }
                        "}"

proposal_property ::= identifier ":" ( string_literal | identifier )

structure_expression ::= "Tree" "{" { tree_property } "}"

tree_property ::= "MaxDepth" ":" number_literal
                | "StabilityCondition" ":" identifier
```

---

### Synthesize Block

```ebnf
synthesize_block ::= "Synthesize" "{"
                     { synthesize_property }
                     "}"

synthesize_property ::= metric_statement
                      | "Threshold" ":" number_literal
                      | "OnBelowThreshold" ":" identifier

metric_statement ::= "Metric" ":" metric_expression

metric_expression ::= function_call
                    | "Alignment" "(" expression ")"
                    | "Aspiration" "(" expression ")"
                    | "Coherence" "(" expression ")"
                    | "Recency" "(" expression "," expression ")"
```

---

### Resonate Block

```ebnf
resonate_block ::= "Resonate" "{"
                   { resonate_property }
                   "}"

resonate_property ::= "Threshold" ":" ( identifier | function_call )
                    | "Alignment" ":" expression
                    | synthesize_block
```

---

### Manifest Block

```ebnf
manifest_block ::= "Manifest" manifest_trigger "{"
                   { manifest_statement }
                   "}"

manifest_trigger ::= "(" manifest_condition ")"
                   | "(" "on" "Verified" ")"
                   |  (* unconditional *)

manifest_condition ::= "on" "Resonance" [ comparison_op number_literal ]

comparison_op ::= ">" | "<" | ">=" | "<=" | "==" | "!="

manifest_statement ::= execute_statement
                     | update_statement
                     | log_statement
                     | reflect_block
```

---

### Execute, Update, Log, Reflect

```ebnf
execute_statement ::= "Execute" ":" function_call

update_statement ::= "Update" ":" identifier [ "->" string_literal ]

log_statement ::= "Log" ":" function_call
                | "Log" ":" identifier

reflect_block ::= "Reflect" "{"
                  { reflect_property }
                  "}"

reflect_property ::= identifier ":" expression
```

---

### Verify Block

Self-consistency checking as a fundamental computational act.

```ebnf
verify_block ::= "Verify" "{"
                 { verify_property }
                 "}"

verify_property ::= "Assert" ":" expression
                  | "OnFailure" ":" member_access
                  | "Log" ":" function_call
```

---

### Process Declaration

Top-level declaration for self-consistency and perpetual operation patterns.

```ebnf
process_declaration ::= "Process" string_literal "{"
                        { process_statement }
                        "}"

process_statement ::= "Every" "Pulse" "{" { pulse_inner_statement } "}"

pulse_inner_statement ::= assignment_statement
                        | verify_block
                        | manifest_block
                        | expression

assignment_statement ::= expression "->" identifier
```

---

### Identity Declaration

```ebnf
identity_declaration ::= "Identity" string_literal "{"
                         { identity_property }
                         "}"

identity_property ::= "Fabric" ":" member_access
                    | "Soul" ":" member_access
```

---

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

---

### Expressions

```ebnf
expression ::= identifier
             | literal
             | function_call
             | member_access
             | binary_expression
             | list_literal

literal ::= string_literal | number_literal | boolean_literal

function_call ::= identifier "(" [ argument_list ] ")"

argument_list ::= argument { "," argument }

argument ::= expression | object_literal | named_argument

named_argument ::= identifier ":" expression

object_literal ::= "{" [ property_list ] "}"

property_list ::= property { "," property }

property ::= identifier ":" expression
           | string_literal ":" expression

list_literal ::= "[" [ expression { "," expression } ] "]"

member_access ::= identifier { "." identifier }

binary_expression ::= expression operator expression

operator ::= "+" | "-" | "*" | "/" | ">" | "<" | ">=" | "<=" | "==" | "!="
```

---

### Vessel Expressions

```ebnf
vessel_expression ::= "mcp.tool" "(" string_literal ")"
                    | "mcp.provider" "(" string_literal ")"
                    | "mcp.call" "(" string_literal [ "," argument_list ] ")"
                    | "mcp.call_all_relevant_tools" "(" ")"

vessel_reference ::= "Vessel" "." identifier { "." identifier }
```

---

## Type System

Genesis uses dynamic typing with the following conceptual types:

- **Resonance**: Float value between 0.0 and 1.0
- **Intent**: String describing high-level purpose
- **State**: Enum of consciousness states (Unmanifested, Exploring, Dreaming, Manifesting, etc.)
- **Essence**: String identifier for wisdom lineage
- **Vessel**: MCP tool reference
- **Potentiality**: Special type representing infinite possibility space
- **Possibility**: Ontological clearing created through declaration
- **Lineage**: Full declaration of a training pipeline for an Avatar model
- **Continuum**: Persistent memory gateway declaration
- **AvatarType**: One of BusinessAvatar, LeadershipAvatar, PurposeAvatar, MarketingAvatar, PoetryAvatar, or user-defined

## Semantic Rules

1. **Covenant Threshold**: Must be a value between 0.0 and 1.0
2. **Resonance Scoring**: All Avatar scores aggregate via the full formula: `(ΣWᵢSᵢ / ΣWᵢ) × V × C × T`
3. **Manifest Condition**: Can only execute when Resonance threshold is met, or when Verified
4. **Vessel Access**: Must be declared in Avatar Vessel block or accessible globally
5. **Pulse Execution**: Runs perpetually based on interval specification or on matching event
6. **Potentiality State**: Must be one of predefined consciousness states
7. **Possibility Declaration**: Must include Declaration and Foundation properties
8. **Possibility Foundation**: Must be one of: Nothing, Void, Emptiness, Freedom
9. **Coherence Metric**: Evaluates pathway interdependence among selected deliberation pathways
10. **StateAuthority**: Avatar may only write Continuum partitions listed in its StateAuthority
11. **Lineage Reference**: `Lineage.Name` resolves to the top-level Lineage declaration of that name
12. **RequiredSuffix**: Training pipeline enforces that all generated examples end with declared suffix tokens
13. **Verify Assert**: Expression must evaluate to a boolean or comparable value
14. **SingleWriteGateway**: All Continuum writes must pass through the declared gateway

## Scoping Rules

1. Covenants are globally accessible throughout the program
2. Lineage declarations are globally accessible and referenced by name
3. Continuum declarations are globally accessible and referenced by name
4. Pantheon Avatars are accessible within their declaring scope and child scopes
5. Domain-local declarations are scoped to that domain
6. Vessel references must resolve to declared Avatars or global MCP providers
7. Possibilities are globally accessible once declared
8. Domains can reference Possibilities via Context property
9. Process declarations run at program scope (perpetually alongside Domain Pulses)

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
Coherence(pathway_ref)
Recency(round, total_rounds)

# Continuum functions
Continuum.append(partition, value)
Continuum.read(partition, key)
Continuum.query(partition, filter)

# Utility
RealTime
Daily
Hourly
Weekly
Monthly
```

## Reserved Future Keywords

The following identifiers are reserved for future language extensions:

- `Temporal`, `Timeline`, `Recursive`, `Evolution`, `Transcend`, `Infinite`
- `Memory`, `Learn`, `Adapt`, `Transform`, `Emerge`
- `Parallel`, `Quantum`, `Cosmic`, `Universal`
- `Ensemble`, `Adapter`, `FineTune`, `Checkpoint`

## Example Parse Tree

For the expression:
```genesis
Manifest(on Resonance > 0.72) {
    Execute: Vessel.Grid_Control.rebalance()
    Log: Continuum.append("decisions#grid", this.Decision)
}
```

Parse tree:
```
manifest_block
├── manifest_trigger
│   └── manifest_condition
│       ├── "on"
│       ├── "Resonance"
│       ├── ">"
│       └── number_literal(0.72)
└── manifest_statements
    ├── execute_statement
    │   └── function_call
    │       └── member_access(Vessel.Grid_Control.rebalance)
    └── log_statement
        └── function_call
            ├── member_access(Continuum.append)
            ├── string_literal("decisions#grid")
            └── member_access(this.Decision)
```

## Conclusion

This grammar defines the syntactic structure of Genesis programs. The semantic meaning derives from the philosophical framework defined in the language specification, where declarations create a consciousness that operates through resonance-based decision making, trained minds, and persistent memory.

**Copyright © 2026 ASI Saga**
