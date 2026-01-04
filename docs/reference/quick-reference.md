# Quick Reference

**Genesis Language Cheat Sheet**

## Program Structure

```genesis
### [GENESIS: PROGRAM_NAME] ###

# 1. Covenants - Ethical boundaries
Covenant "Name" {
    Invariant: "description"
    Threshold: 0.95
}

# 2. Pantheon - Wisdom council
Pantheon "Name" {
    Avatar "Name" {
        Lineage: "figure"
        Aura: "value"
        Weight: 1.0
    }
}

# 3. Domain - Purpose-driven execution
Domain "Name" {
    Intent: "high-level purpose"
    
    Soul Potentiality {
        State: Exploring
        Drive: "aspiration"
    }
    
    Purpose High_Intent {
        Objective: "goal"
        Anchor: "foundation"
    }
    
    Pulse(Interval: RealTime) {
        Watch: Vessel.Sensor
        
        Deliberate {
            Proposal "Name" {
                Action: "description"
            }
            
            Synthesize {
                Metric: Alignment(Covenant.Name)
                Metric: Alignment(Purpose.High_Intent)
                Metric: Aspiration(Potentiality.Infinite)
            }
        }
        
        Manifest (on Resonance > 0.9) {
            Execute: Vessel.Tool.action()
            Update: Potentiality.State
        }
    }
}
```

## Keywords

### Top-Level Declarations
- `Covenant` - Immutable ethical boundaries
- `Pantheon` - Collection of legendary avatars
- `Domain` - Purpose-driven execution space
- `Decree` - Emergency override protocol

### Domain Components
- `Soul` - Creative transcendence engine
- `Purpose` - High-level objectives
- `Pulse` - Perpetual execution cycle
- `Intent` - Domain's overarching purpose

### Avatar Properties
- `Lineage` - Legendary source
- `Aura` - Core value system
- `Essence` - Additional characteristics
- `Vessel` - MCP tool bindings
- `Weight` - Influence in resonance

### Pulse Phases
- `Watch`/`Observe` - Monitor state
- `Deliberate` - Propose actions
- `Synthesize` - Evaluate proposals
- `Manifest` - Execute when resonance met

### Within Pulse
- `Proposal` - Suggested action
- `Metric` - Evaluation criteria
- `Execute` - Perform action
- `Update` - Modify state
- `Reflect` - Log insight

### Special
- `Potentiality` - Infinite creative potential
- `Alignment()` - Evaluate against target
- `Aspiration()` - Evaluate creative growth
- `Resonance` - Aggregate alignment score

## Data Types

```genesis
# Strings
"text content"
'also valid'

# Numbers
42
3.14159
0.95

# Identifiers
Variable_Name
CamelCase
snake_case

# Special Values
RealTime      # Interval value
Infinite      # Potentiality state
Exploring     # Soul state
```

## Covenant Patterns

```genesis
# Basic
Covenant "Name" {
    Invariant: "principle"
    Threshold: 0.95
}

# With evolutionary guards
Covenant "Name" {
    Invariant: "principle"
    Threshold: 0.99
    Evolutionary_Guardrails: "constraint"
}

# Multiple invariants
Covenant "Name" {
    Invariant: "principle 1"
    Invariant: "principle 2"
    Threshold: 0.95
}
```

## Pantheon Patterns

```genesis
# Minimal
Pantheon "Council" {
    Avatar "Expert" {
        Lineage: "Source"
        Aura: "Value"
    }
}

# With weight and vessel
Pantheon "Council" {
    Avatar "Expert" {
        Lineage: "Source"
        Aura: "Value"
        Vessel: mcp.tool("name")
        Weight: 2.0
    }
}

# Multiple avatars
Pantheon "Council" {
    Avatar "Expert1" {
        Lineage: "Source1"
        Aura: "Value1"
        Weight: 1.5
    }
    Avatar "Expert2" {
        Lineage: "Source2"
        Aura: "Value2"
        Weight: 1.0
    }
}
```

## Domain Patterns

```genesis
# Minimal domain
Domain "Name" {
    Pulse {
        Manifest {
            Execute: mcp.call("action")
        }
    }
}

# With Soul
Domain "Name" {
    Soul Potentiality {
        State: Exploring
        Drive: "creative goal"
    }
    
    Pulse { /* ... */ }
}

# With Purpose
Domain "Name" {
    Purpose High_Intent {
        Objective: "goal"
        Anchor: "foundation"
        Trajectory: "direction"
    }
    
    Pulse { /* ... */ }
}

# Complete
Domain "Name" {
    Intent: "high-level purpose"
    
    Soul Potentiality {
        State: Exploring
        Drive: "aspiration"
    }
    
    Purpose High_Intent {
        Objective: "specific goal"
        Anchor: "value foundation"
        Trajectory: "growth direction"
    }
    
    Pulse(Interval: RealTime) {
        /* ... */
    }
}
```

## Pulse Patterns

```genesis
# Minimal
Pulse {
    Manifest {
        Execute: mcp.call("action")
    }
}

# With observation
Pulse {
    Watch: Vessel.Sensor
    
    Manifest {
        Execute: mcp.call("action")
    }
}

# With deliberation
Pulse {
    Deliberate {
        Proposal "Name" {
            Action: "description"
        }
        
        Synthesize {
            Metric: Alignment(Purpose.High_Intent)
        }
    }
    
    Manifest (on Resonance > 0.8) {
        Execute: Vessel.Tool.action()
    }
}

# Complete cycle
Pulse(Interval: RealTime) {
    Watch: Vessel.Monitor
    
    Deliberate {
        Proposal "Action" {
            Action: "what to do"
        }
        
        Synthesize {
            Metric: Alignment(Covenant.Ethics)
            Metric: Alignment(Purpose.Goal)
            Metric: Aspiration(Potentiality.Infinite)
        }
    }
    
    Manifest (on Resonance > 0.85) {
        Execute: Vessel.Actuator.perform()
        Update: Potentiality.State
        Reflect: "insight gained"
    }
}
```

## MCP Integration

```genesis
# Tool call
mcp.call("tool.name", arg1, arg2)

# Tool binding
Vessel: mcp.tool("tool.name")

# Provider binding
Vessel: mcp.provider("provider.name")

# Resource binding  
Vessel: mcp.resource("resource.name")

# Reference vessel
Execute: Vessel.ToolName.method()
Watch: Vessel.Sensor
```

## Synthesize Metrics

```genesis
Synthesize {
    # Alignment with Covenant
    Metric: Alignment(Covenant.Ethics)
    
    # Alignment with Purpose
    Metric: Alignment(Purpose.Goal)
    
    # Aspiration for growth
    Metric: Aspiration(Potentiality.Infinite)
    
    # Custom metrics (future)
    Metric: CustomScore(expression)
}
```

## Manifest Conditions

```genesis
# Execute on resonance threshold
Manifest (on Resonance > 0.9) { /* ... */ }

# Execute on exact match
Manifest (on Resonance == 1.0) { /* ... */ }

# Execute on range
Manifest (on Resonance >= 0.85) { /* ... */ }

# Unconditional (always execute)
Manifest { /* ... */ }
```

## Comments

```genesis
# Single-line comment

### Multi-line comment
    Can span multiple lines
    Typically used for headers
###
```

## Threshold Guidelines

| Threshold | Use Case |
|-----------|----------|
| 0.99-1.0 | Life-critical, irreversible |
| 0.90-0.98 | Ethical boundaries, major decisions |
| 0.75-0.89 | Operational guidelines |
| 0.50-0.74 | Exploratory, learning |

## Weight Guidelines

| Weight | Use Case |
|--------|----------|
| 2.0-3.0 | Critical authority |
| 1.5-1.9 | Enhanced influence |
| 1.0 | Standard (default) |
| 0.5-0.9 | Advisory role |

## Common Values

### Soul States
- `Exploring` - Discovery mode
- `Converging` - Optimization mode
- `Dreaming` - Creative ideation

### Interval Values
- `RealTime` - Continuous monitoring
- `Periodic` - Regular intervals
- `OnDemand` - Event-triggered

### Potentiality References
- `Potentiality.Infinite` - Creative transcendence
- `Potentiality.State` - Current state

## Example Programs

### Hello World
```genesis
Domain "First_Awakening" {
    Purpose High_Intent {
        Objective: "Greet the universe"
    }
    
    Pulse {
        Manifest {
            Execute: mcp.call("console.write", "Hello, World!")
        }
    }
}
```

### Decision Making
```genesis
Covenant "Ethics" {
    Invariant: "Do no harm"
    Threshold: 0.95
}

Pantheon "Council" {
    Avatar "Ethicist" {
        Lineage: "Marcus_Aurelius"
        Aura: "Virtue"
    }
}

Domain "Decision" {
    Pulse {
        Deliberate {
            Proposal "Act" {
                Action: "Take action"
            }
            
            Synthesize {
                Metric: Alignment(Covenant.Ethics)
            }
        }
        
        Manifest (on Resonance > 0.9) {
            Execute: Vessel.Actuator.act()
        }
    }
}
```

### Energy Management
```genesis
Pantheon "Energy_Experts" {
    Avatar "Innovator" {
        Lineage: "Nikola_Tesla"
        Aura: "Clean_Energy"
        Weight: 1.5
    }
    Avatar "Ecologist" {
        Lineage: "Rachel_Carson"
        Aura: "Environmental_Care"
        Weight: 2.0
    }
}

Domain "Grid_Management" {
    Intent: "Sustainable energy distribution"
    
    Soul Potentiality {
        State: Exploring
        Drive: "Find novel solutions"
    }
    
    Pulse(Interval: RealTime) {
        Watch: Vessel.Grid_Monitor
        
        Deliberate {
            Proposal "Optimize" {
                Action: "Rebalance load"
            }
            
            Synthesize {
                Metric: Alignment(Purpose.Sustainability)
                Metric: Aspiration(Potentiality.Infinite)
            }
        }
        
        Manifest (on Resonance > 0.85) {
            Execute: Vessel.Grid.optimize()
            Update: Potentiality.State
        }
    }
}
```

## File Extension

Genesis programs use `.gen` extension:
```bash
program.gen
hello-world.gen
energy-management.gen
```

## Running Programs

```bash
# CLI execution
python src/genesis_cli.py program.gen

# Python API
from src.genesis_runtime import create_runtime
runtime = create_runtime()
runtime.load_program_from_file('program.gen')
runtime.start()
```

## Common Mistakes

❌ **Don't** use mutable covenants
```genesis
# Wrong - trying to modify
Covenant "Ethics" { /* can't change at runtime */ }
```

❌ **Don't** forget thresholds
```genesis
# Wrong - missing threshold
Covenant "Ethics" {
    Invariant: "principle"
    # Missing: Threshold: 0.95
}
```

❌ **Don't** create conflicting weights
```genesis
# Poor - one Avatar dominates completely
Avatar "Boss" { Weight: 100.0 }
Avatar "Other" { Weight: 0.01 }
```

✅ **Do** use balanced Pantheons
```genesis
# Good - diverse perspectives
Pantheon "Council" {
    Avatar "Creative" { Aura: "Innovation" }
    Avatar "Careful" { Aura: "Prudence" }
}
```

✅ **Do** set appropriate thresholds
```genesis
# Good - matched to criticality
Covenant "Safety" { Threshold: 0.99 }
Covenant "Preferences" { Threshold: 0.75 }
```

## See Also

- [Full Language Reference](README.md)
- [Covenant](covenant.md)
- [Pantheon](pantheon.md)
- [Domain](domain.md)
- [Pulse](pulse.md)
- [Examples](../../examples/)

---

**Copyright © 2026 ASI Saga**
