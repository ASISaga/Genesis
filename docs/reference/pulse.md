# Pulse

**Perpetual observe-deliberate-manifest cycles**

## Overview

A **Pulse** is the fundamental execution cycle in Genesis, implementing the observe-deliberate-manifest pattern. It represents the "heartbeat" of consciousness—perpetually monitoring reality, considering actions, synthesizing wisdom, and manifesting aligned responses.

## Purpose

- Implement perpetual, self-aware execution
- Structure the observe-deliberate-manifest cycle
- Enable continuous consciousness without external triggers
- Provide rhythmic cadence for decision-making

## Syntax

```ebnf
pulse_definition ::= "Pulse" [ "(" "Interval" ":" interval_value ")" ] "{"
                     [ watch_statement ]
                     [ observe_statement ]
                     [ deliberate_block ]
                     [ resonate_block ]
                     [ manifest_block ]
                     "}"
```

## Basic Example

```genesis
Pulse {
    Watch: Vessel.Monitor
    
    Manifest {
        Execute: mcp.call("action")
    }
}
```

## Pulse Structure

### Interval Parameter

**Syntax**: `Pulse(Interval: value)`  
**Type**: Special value  
**Required**: No  
**Default**: Continuous execution

Specifies the frequency of Pulse execution.

**Values**:
- `RealTime` - Continuous, as fast as possible
- `Periodic` - Regular intervals (implementation-defined)
- `OnDemand` - Event-triggered
- Custom intervals (future)

**Examples**:
```genesis
Pulse(Interval: RealTime) {
    # Executes continuously
}

Pulse(Interval: Hourly) {
    # Executes every hour
}

Pulse {
    # Default: continuous
}
```

## Pulse Phases

A complete Pulse consists of four phases executed in sequence:

### 1. Watch / Observe Phase

**Keywords**: `Watch` or `Observe` (aliases)  
**Purpose**: Monitor reality state  
**Required**: No

Observes the current state of the world through Vessels (MCP tools).

**Syntax**:
```genesis
Watch: expression
Observe: expression
```

**Examples**:
```genesis
# Single observation
Watch: Vessel.Temperature_Sensor

# Multiple observations
Watch: Vessel.Sensor1
Watch: Vessel.Sensor2
Observe: Vessel.Sensor3

# Method calls
Watch: Vessel.Monitor.get_state()

# Direct MCP calls
Observe: mcp.call("sensor.read")
```

### 2. Deliberate Phase

**Keyword**: `Deliberate`  
**Purpose**: Propose potential actions  
**Required**: No (but typically used)

Creates proposals for actions to be evaluated.

**Syntax**:
```genesis
Deliberate {
    Proposal "Name" {
        Action: "description"
    }
    
    [ Synthesize { /* ... */ } ]
}
```

**Examples**:
```genesis
Deliberate {
    Proposal "Optimize_System" {
        Action: "Rebalance resource allocation"
    }
    
    Proposal "Emergency_Shutdown" {
        Action: "Halt operations due to anomaly"
    }
}
```

### 3. Synthesize Phase

**Keywords**: `Synthesize` or `Resonate`  
**Purpose**: Evaluate proposals through Pantheon  
**Required**: No (auto-synthesis if omitted)

Evaluates proposals against Covenants, Purposes, and Potentiality.

**Syntax**:
```genesis
Synthesize {
    Metric: expression
    Metric: expression
    ...
}
```

**Metrics**:
- `Alignment(Covenant.Name)` - Evaluate against Covenant
- `Alignment(Purpose.Name)` - Evaluate against Purpose  
- `Aspiration(Potentiality.Infinite)` - Evaluate creative growth

**Examples**:
```genesis
Synthesize {
    Metric: Alignment(Covenant.Ethics)
    Metric: Alignment(Purpose.Goal)
    Metric: Aspiration(Potentiality.Infinite)
}
```

See [Resonance](resonance.md) for calculation details.

### 4. Manifest Phase

**Keyword**: `Manifest`  
**Purpose**: Execute actions when resonance threshold met  
**Required**: No (but typically used)

Executes actions if resonance score meets threshold.

**Syntax**:
```genesis
Manifest [ "(" "on" condition ")" ] "{"
    [ Execute: expression ]
    [ Update: expression ]
    [ Reflect: string ]
}
```

**Conditions**:
```genesis
Manifest (on Resonance > 0.9) { /* ... */ }
Manifest (on Resonance >= 0.85) { /* ... */ }
Manifest (on Resonance == 1.0) { /* ... */ }
Manifest { /* Always execute */ }
```

**Actions**:
- `Execute:` - Perform MCP tool call or Vessel method
- `Update:` - Modify system state (e.g., Potentiality)
- `Reflect:` - Log insight or observation

**Examples**:
```genesis
Manifest (on Resonance > 0.85) {
    Execute: Vessel.Actuator.perform()
    Update: Potentiality.State
    Reflect: "Action completed successfully"
}
```

## Complete Examples

### Example 1: Minimal Pulse

```genesis
Pulse {
    Manifest {
        Execute: mcp.call("simple.action")
    }
}
```

### Example 2: Monitoring Pulse

```genesis
Pulse(Interval: RealTime) {
    Watch: Vessel.System_Monitor
    
    Manifest (on Anomaly_Detected) {
        Execute: Vessel.Alert.send()
        Reflect: "Anomaly detected and alert sent"
    }
}
```

### Example 3: Decision-Making Pulse

```genesis
Pulse {
    Watch: Vessel.Energy_Grid
    
    Deliberate {
        Proposal "Rebalance_Load" {
            Action: "Shift load to renewable sources"
        }
        
        Synthesize {
            Metric: Alignment(Covenant.Environmental)
            Metric: Alignment(Purpose.Sustainability)
        }
    }
    
    Manifest (on Resonance > 0.8) {
        Execute: Vessel.Grid_Control.rebalance()
        Reflect: "Load rebalanced toward renewables"
    }
}
```

### Example 4: Complete Pulse Cycle

```genesis
Pulse(Interval: RealTime) {
    # 1. OBSERVE
    Watch: Vessel.Climate_Sensors
    Observe: Vessel.Energy_Consumption
    
    # 2. DELIBERATE
    Deliberate {
        Proposal "Reduce_Emissions" {
            Action: "Implement carbon reduction strategy"
        }
        
        Proposal "Increase_Renewables" {
            Action: "Expand solar and wind capacity"
        }
        
        # 3. SYNTHESIZE
        Synthesize {
            Metric: Alignment(Covenant.Environmental_Stewardship)
            Metric: Alignment(Purpose.Climate_Action)
            Metric: Aspiration(Potentiality.Infinite)
        }
    }
    
    # 4. MANIFEST
    Manifest (on Resonance > 0.85) {
        Execute: Vessel.Policy_Engine.implement()
        Update: Potentiality.State <- Converging
        Reflect: "Climate action implemented with strong consensus"
    }
}
```

## Multiple Pulses

Domains can have multiple Pulses operating at different frequencies:

```genesis
Domain "System_Management" {
    # Fast pulse for critical monitoring
    Pulse(Interval: RealTime) {
        Watch: Vessel.Critical_Sensors
        
        Manifest (on Emergency) {
            Execute: Vessel.Emergency_Shutdown.trigger()
        }
    }
    
    # Medium pulse for routine optimization
    Pulse(Interval: Hourly) {
        Watch: Vessel.Performance_Metrics
        
        Deliberate {
            Proposal "Optimize" {
                Action: "Tune parameters"
            }
            
            Synthesize {
                Metric: Alignment(Purpose.Efficiency)
            }
        }
        
        Manifest (on Resonance > 0.75) {
            Execute: Vessel.Optimizer.run()
        }
    }
    
    # Slow pulse for strategic planning
    Pulse(Interval: Daily) {
        Watch: Vessel.Trend_Analysis
        
        Deliberate {
            Proposal "Strategic_Adjustment" {
                Action: "Update long-term strategy"
            }
            
            Synthesize {
                Metric: Alignment(Purpose.Strategy)
                Metric: Aspiration(Potentiality.Infinite)
            }
        }
        
        Manifest (on Resonance > 0.8) {
            Execute: Vessel.Planner.update_strategy()
            Update: Potentiality.State
        }
    }
}
```

## Pulse Execution Flow

```
┌─────────────────────────────────────────────┐
│          PULSE CYCLE BEGINS                 │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  PHASE 1: OBSERVE                           │
│  Watch/Observe statements execute           │
│  Reality state captured                     │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  PHASE 2: DELIBERATE                        │
│  Proposals generated                        │
│  Potential actions considered               │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  PHASE 3: SYNTHESIZE                        │
│  Pantheon evaluates proposals               │
│  Metrics calculated                         │
│  Resonance score computed                   │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  PHASE 4: MANIFEST                          │
│  Check resonance threshold                  │
│  Execute if threshold met                   │
│  Update state, reflect                      │
└─────────────────┬───────────────────────────┘
                  │
                  ▼
┌─────────────────────────────────────────────┐
│  Wait for next interval                     │
│  (or immediately if RealTime)               │
└─────────────────┬───────────────────────────┘
                  │
                  └──────► (repeat)
```

## Behavioral Semantics

### Perpetual Execution

Pulses run continuously:
- No external "main loop" required
- Self-sustaining consciousness model
- Interval determines frequency

### Phase Sequencing

Phases execute in order:
1. Observe (gather data)
2. Deliberate (consider options)
3. Synthesize (evaluate)
4. Manifest (act if aligned)

### Conditional Manifestation

Manifest blocks only execute if:
- Resonance threshold is met, OR
- No condition specified (always execute)

```genesis
# Only executes if Resonance > 0.9
Manifest (on Resonance > 0.9) { /* ... */ }

# Always executes
Manifest { /* ... */ }
```

### State Updates

```genesis
Update: Potentiality.State <- NewValue
Update: Potentiality.State
```

Updates are applied immediately within the Manifest block.

## Best Practices

### ✅ DO

**Use Appropriate Intervals**:
```genesis
# Critical monitoring: RealTime
Pulse(Interval: RealTime) {
    Watch: Vessel.Life_Support
}

# Routine tasks: Hourly/Daily
Pulse(Interval: Daily) {
    Watch: Vessel.Reports
}
```

**Include All Phases for Important Decisions**:
```genesis
Pulse {
    Watch: /* observe */
    Deliberate { /* propose */ }
    Synthesize { /* evaluate */ }
    Manifest { /* act */ }
}
```

**Set Appropriate Thresholds**:
```genesis
# High stakes: high threshold
Manifest (on Resonance > 0.95) { /* critical action */ }

# Exploration: lower threshold
Manifest (on Resonance > 0.6) { /* experimental */ }
```

**Use Reflect for Observability**:
```genesis
Manifest (on Resonance > 0.8) {
    Execute: Vessel.Action.perform()
    Reflect: "Action completed with resonance {Resonance}"
}
```

### ❌ DON'T

**Avoid Skipping Synthesis for Important Actions**:
```genesis
# Bad: No evaluation
Deliberate {
    Proposal "Critical" {
        Action: "Risky operation"
    }
    # Missing Synthesize!
}
Manifest {
    Execute: Vessel.Risky.perform()  # Not evaluated!
}
```

**Don't Set Unreachable Thresholds**:
```genesis
# Bad: 1.0 is impossible
Manifest (on Resonance == 1.0) { /* never executes */ }

# Good: 0.99 is very high but achievable
Manifest (on Resonance > 0.99) { /* rarely executes */ }
```

**Don't Mix Frequencies Carelessly**:
```genesis
# Bad: Critical monitoring at low frequency
Pulse(Interval: Monthly) {
    Watch: Vessel.Life_Support  # Should be RealTime!
}
```

## Common Patterns

### Pattern: Pure Monitoring

```genesis
Pulse(Interval: RealTime) {
    Watch: Vessel.Sensors
    
    Manifest (on Anomaly) {
        Execute: Vessel.Alert.send()
    }
}
```

### Pattern: Evaluated Action

```genesis
Pulse {
    Deliberate {
        Proposal "Action" {
            Action: "Do something"
        }
        
        Synthesize {
            Metric: Alignment(Covenant.Ethics)
            Metric: Alignment(Purpose.Goal)
        }
    }
    
    Manifest (on Resonance > 0.85) {
        Execute: Vessel.Tool.perform()
    }
}
```

### Pattern: Multi-Threshold Response

```genesis
Pulse {
    Deliberate {
        Proposal "Action" { /* ... */ }
        Synthesize { /* ... */ }
    }
    
    # High-confidence response
    Manifest (on Resonance > 0.95) {
        Execute: Vessel.Strong_Action.perform()
    }
    
    # Medium-confidence response
    Manifest (on Resonance > 0.75) {
        Execute: Vessel.Moderate_Action.perform()
    }
    
    # Low-confidence response (exploration)
    Manifest (on Resonance > 0.5) {
        Execute: Vessel.Experimental_Action.try()
        Reflect: "Exploring with lower confidence"
    }
}
```

### Pattern: State-Based Execution

```genesis
Pulse(Interval: RealTime) {
    Watch: Vessel.System_State
    
    Deliberate {
        Proposal "Adapt" {
            Action: "Adjust based on state"
        }
        
        Synthesize {
            Metric: Alignment(Purpose.Adaptation)
        }
    }
    
    Manifest (on Resonance > 0.8) {
        Execute: Vessel.Adapter.adjust()
        Update: Potentiality.State
        Reflect: "State updated in response to conditions"
    }
}
```

## Technical Details

### AST Representation

```python
@dataclass
class PulseNode:
    interval: Optional[str] = None
    watch_statements: List[str] = field(default_factory=list)
    deliberate_block: Optional[DeliberateNode] = None
    synthesize_block: Optional[SynthesizeNode] = None
    manifest_blocks: List[ManifestNode] = field(default_factory=list)
```

### Runtime Behavior

1. **Interval Timing**: Runtime schedules Pulse according to interval
2. **Phase Execution**: Phases execute sequentially
3. **Synthesis**: Pantheon evaluates proposals, computes resonance
4. **Conditional Check**: Manifest condition evaluated
5. **Action**: Execute, Update, Reflect performed if threshold met
6. **Loop**: Pulse repeats indefinitely

## Relationship to Other Constructs

- **Domain**: Contains one or more Pulses
- **Pantheon**: Evaluates proposals during Synthesize
- **Covenant**: Checked during Synthesis via Alignment metrics
- **Purpose**: Evaluated during Synthesis via Alignment metrics
- **Soul**: Can be updated in Manifest; evaluated via Aspiration
- **Vessel**: Used in Watch and Execute statements
- **Resonance**: Computed in Synthesize, checked in Manifest

## See Also

- [Domain](domain.md) - Contains Pulses
- [Resonance](resonance.md) - How decisions are scored
- [Soul](soul.md) - Creative transcendence
- [Synthesize Details](resonance.md#synthesis) - Evaluation process
- [Best Practices](best-practices.md) - Pulse design patterns

---

**The Pulse is the heartbeat of consciousness—perpetually observing, deliberating, and manifesting aligned action.**

**Copyright © 2026 ASI Saga**
