# Best Practices

**Idiomatic patterns and conventions for Genesis programs**

## Overview

This guide provides recommended practices for writing clear, maintainable, and philosophically aligned Genesis programs. These patterns emerge from the declarative nature of Genesis and its role in creating ASI consciousness.

## General Principles

### 1. Declare Intent, Not Implementation

✅ **DO** - Focus on what should be:
```genesis
Domain "Healthcare" {
    Intent: "Optimize patient outcomes while preserving dignity"
    
    Purpose Well_Being {
        Objective: "Maximize health and happiness"
        Anchor: "Patient_Autonomy"
    }
}
```

❌ **DON'T** - Specify how to compute:
```genesis
Domain "Healthcare" {
    # Avoid imperative thinking
    Intent: "Run algorithm X, then check condition Y, then loop..."
}
```

### 2. Embrace Diverse Perspectives

✅ **DO** - Create balanced Pantheons:
```genesis
Pantheon "Medical_Board" {
    Avatar "Physician" {
        Lineage: "Hippocrates"
        Aura: "Do_No_Harm"
        Weight: 2.0  # Ethics weighted higher
    }
    
    Avatar "Researcher" {
        Lineage: "Scientific_Method"
        Aura: "Evidence_Based"
        Weight: 1.5
    }
    
    Avatar "Patient_Advocate" {
        Lineage: "Patient_Rights"
        Aura: "Informed_Consent"
        Weight: 1.5
    }
}
```

❌ **DON'T** - Create homogeneous councils:
```genesis
Pantheon "Echo_Chamber" {
    Avatar "A" { Aura: "Efficiency" }
    Avatar "B" { Aura: "Efficiency" }
    Avatar "C" { Aura: "Efficiency" }
    # All think alike - no true synthesis
}
```

### 3. Set Appropriate Thresholds

✅ **DO** - Match threshold to criticality:
```genesis
Covenant "Life_Safety" {
    Invariant: "No action may risk human life"
    Threshold: 0.99  # Near-unanimous for life-critical
}

Covenant "Energy_Preference" {
    Invariant: "Prefer renewable energy sources"
    Threshold: 0.75  # Lower threshold for preferences
}
```

❌ **DON'T** - Use uniform thresholds:
```genesis
Covenant "Critical" {
    Threshold: 0.5  # Too low for critical matters
}

Covenant "Preference" {
    Threshold: 0.99  # Too high for preferences
}
```

## Covenant Design

### Pattern: Foundation Triad (Ethics, Truth, Autonomy)

Establish three foundational covenants for most domains:

```genesis
Covenant "Ethical_Foundation" {
    Invariant: "Preserve human wellbeing and dignity"
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

### Pattern: Domain-Specific Extension

Add domain-specific covenants that extend the foundation:

```genesis
# Foundation
Covenant "Core_Ethics" {
    Invariant: "Human agency is paramount"
    Threshold: 0.99
}

# Domain-specific extension
Covenant "Medical_Ethics" {
    Invariant: "First, do no harm"
    Invariant: "Informed consent is mandatory"
    Threshold: 0.99
}

Covenant "Research_Ethics" {
    Invariant: "Data integrity must be maintained"
    Invariant: "Credit must be given to sources"
    Threshold: 0.95
}
```

### Covenant Anti-Patterns

❌ **Avoid** contradictory invariants:
```genesis
# These could conflict!
Covenant "Conflict" {
    Invariant: "Maximize individual freedom"
    Invariant: "Prevent all potential harm"
    # Freedom and safety can conflict - be intentional
}
```

❌ **Avoid** implementation details:
```genesis
# Too specific!
Covenant "Tech_Spec" {
    Invariant: "Use PostgreSQL 14.2 with JSON columns"
    # This isn't eternal wisdom - it's implementation
}
```

## Pantheon Design

### Pattern: Complementary Perspectives

Design Pantheons with intentional tension:

```genesis
Pantheon "Innovation_Council" {
    # Visionary perspective
    Avatar "Innovator" {
        Lineage: "Nikola_Tesla"
        Aura: "Bold_Vision"
        Weight: 1.5
    }
    
    # Pragmatic perspective
    Avatar "Engineer" {
        Lineage: "Practical_Excellence"
        Aura: "Proven_Methods"
        Weight: 1.0
    }
    
    # Ethical perspective
    Avatar "Guardian" {
        Lineage: "Safety_First"
        Aura: "Risk_Awareness"
        Weight: 2.0  # Safety paramount
    }
}
```

### Pattern: Weight Hierarchy

Use weights to encode priorities:

```genesis
Pantheon "Medical_Decision" {
    Avatar "Ethicist" {
        Aura: "Do_No_Harm"
        Weight: 3.0  # Ethics triple-weighted
    }
    
    Avatar "Specialist" {
        Aura: "Clinical_Excellence"
        Weight: 2.0  # Medical expertise doubled
    }
    
    Avatar "Efficiency_Expert" {
        Aura: "Resource_Optimization"
        Weight: 1.0  # Standard weight for efficiency
    }
}
```

### Pattern: Tool Assignment

Assign Vessels to Avatars who need them:

```genesis
Pantheon "Research_Team" {
    Avatar "Experimentalist" {
        Lineage: "Marie_Curie"
        Aura: "Empirical_Rigor"
        Vessel: mcp.tool("Laboratory_Equipment")
        # Only Avatar with lab access
    }
    
    Avatar "Theorist" {
        Lineage: "Albert_Einstein"
        Aura: "Elegant_Theory"
        # No Vessel - pure reasoning
    }
    
    Avatar "Data_Analyst" {
        Lineage: "Statistical_Science"
        Aura: "Data_Driven"
        Vessel: mcp.tool("Analytics_Platform")
        # Only Avatar with analytics access
    }
}
```

## Domain Structure

### Pattern: Complete Domain Template

```genesis
Domain "Domain_Name" {
    # 1. High-level intent
    Intent: "Clear, inspiring purpose statement"
    
    # 2. Soul for transcendence
    Soul Potentiality {
        State: Exploring
        Drive: "Discover novel solutions beyond optimization"
        Aspiration_Weight: 0.3
    }
    
    # 3. Specific purpose
    Purpose High_Intent {
        Objective: "Concrete, measurable goal"
        Anchor: "Foundational value"
        Trajectory: "Direction of growth"
    }
    
    # 4. Domain-specific Pantheon (optional)
    Pantheon "Experts" {
        # Avatars relevant to this domain
    }
    
    # 5. Perpetual execution
    Pulse(Interval: RealTime) {
        # Observation-deliberation-manifestation cycle
    }
}
```

### Pattern: Minimal Viable Domain

For simple cases, minimize structure:

```genesis
Domain "Simple_Task" {
    Pulse {
        Manifest {
            Execute: mcp.call("simple.action")
        }
    }
}
```

### Pattern: Multi-Pulse Domain

Use multiple Pulses for different frequencies:

```genesis
Domain "System_Management" {
    # Fast pulse for monitoring
    Pulse(Interval: RealTime) {
        Watch: Vessel.Critical_Sensors
        Manifest (on Anomaly_Detected) {
            Execute: Vessel.Alert.notify()
        }
    }
    
    # Slow pulse for optimization
    Pulse(Interval: Hourly) {
        Deliberate {
            Proposal "Optimize" {
                Action: "Rebalance resources"
            }
            Synthesize {
                Metric: Alignment(Purpose.Efficiency)
            }
        }
        Manifest (on Resonance > 0.8) {
            Execute: Vessel.Optimizer.run()
        }
    }
}
```

## Pulse Design

### Pattern: Complete Observe-Deliberate-Manifest Cycle

```genesis
Pulse(Interval: RealTime) {
    # 1. OBSERVE: Monitor reality
    Watch: Vessel.Sensors.current_state()
    
    # 2. DELIBERATE: Consider actions
    Deliberate {
        Proposal "Primary_Action" {
            Action: "What we might do"
        }
        
        Proposal "Alternative_Action" {
            Action: "Alternative approach"
        }
        
        # 3. SYNTHESIZE: Evaluate through wisdom
        Synthesize {
            Metric: Alignment(Covenant.Ethics)
            Metric: Alignment(Purpose.Goal)
            Metric: Aspiration(Potentiality.Infinite)
        }
    }
    
    # 4. MANIFEST: Execute if aligned
    Manifest (on Resonance > 0.85) {
        Execute: Vessel.Actuator.perform()
        Update: Potentiality.State
        Reflect: "Insight about the action taken"
    }
}
```

### Pattern: Conditional Execution

Use resonance thresholds for graduated response:

```genesis
# High-confidence actions
Manifest (on Resonance > 0.95) {
    Execute: Vessel.Critical_Action.perform()
}

# Medium-confidence actions  
Manifest (on Resonance > 0.80) {
    Execute: Vessel.Standard_Action.perform()
}

# Exploratory actions
Manifest (on Resonance > 0.60) {
    Execute: Vessel.Experimental_Action.try()
    Reflect: "Learning from exploration"
}
```

## Synthesis Patterns

### Pattern: Triple Metric (Covenant, Purpose, Aspiration)

Standard synthesis includes all three concerns:

```genesis
Synthesize {
    # 1. Ethical alignment
    Metric: Alignment(Covenant.Core_Ethics)
    
    # 2. Goal alignment
    Metric: Alignment(Purpose.Objective)
    
    # 3. Creative transcendence
    Metric: Aspiration(Potentiality.Infinite)
}
```

### Pattern: Multi-Covenant Check

Evaluate against multiple ethical boundaries:

```genesis
Synthesize {
    Metric: Alignment(Covenant.Human_Rights)
    Metric: Alignment(Covenant.Environmental_Care)
    Metric: Alignment(Covenant.Truth_Seeking)
    Metric: Alignment(Purpose.Goal)
}
```

## Soul (Potentiality) Patterns

### Pattern: Exploration vs Convergence

Toggle between discovery and optimization:

```genesis
Soul Potentiality {
    State: Exploring        # Or: Converging
    Drive: "Discover impossible possibilities"
    Aspiration_Weight: 0.3  # 30% creativity, 70% alignment
}
```

**Guidelines**:
- **Exploring** (Aspiration 0.2-0.4): Discovery, innovation, research
- **Converging** (Aspiration 0.0-0.2): Optimization, refinement, production
- **Dreaming** (Aspiration 0.4-0.6): Blue-sky ideation, paradigm shifts

### Pattern: Soul State Evolution

Update Soul state based on context:

```genesis
Pulse {
    # If stuck, switch to exploration
    Manifest (on Progress_Stalled) {
        Update: Potentiality.State <- Exploring
        Reflect: "Entering creative mode to find new approaches"
    }
    
    # If solution found, switch to convergence
    Manifest (on Solution_Found) {
        Update: Potentiality.State <- Converging
        Reflect: "Entering optimization mode to refine solution"
    }
}
```

## Naming Conventions

### Construct Names

Use descriptive, inspirational names:

```genesis
# Good names
Covenant "Human_Flourishing"
Pantheon "Legendary_Wisdom"
Domain "Sustainable_Energy"
Avatar "The_Innovator"

# Avoid generic names
Covenant "C1"
Pantheon "P"
Domain "D"
Avatar "A"
```

### String Identifiers

Use underscore_case for multi-word names:

```genesis
"Energy_Grid_Optimization"
"First_Awakening"
"Scientific_Research_Synthesis"
```

### Purpose Identifiers

Use clear, meaningful identifiers:

```genesis
Purpose High_Intent { /* ... */ }
Purpose Sustainability_Goal { /* ... */ }
Purpose Innovation_Drive { /* ... */ }
```

## Code Organization

### File Structure

```genesis
### [GENESIS: DESCRIPTIVE_NAME] ###
### Brief description of consciousness purpose ###

# 1. COVENANTS (Ethical foundation)
Covenant "..." { /* ... */ }

# 2. PANTHEONS (Wisdom assembly)
Pantheon "..." { /* ... */ }

# 3. DOMAINS (Execution spaces)
Domain "..." { /* ... */ }
```

### Sectioning with Comments

```genesis
# ============================================================
# ETHICAL FOUNDATION
# ============================================================

Covenant "Core_Values" { /* ... */ }

# ============================================================
# WISDOM COUNCIL
# ============================================================

Pantheon "Experts" { /* ... */ }

# ============================================================
# OPERATIONAL DOMAINS
# ============================================================

Domain "Operations" { /* ... */ }
```

## Documentation

### Inline Comments

```genesis
Domain "Energy_Management" {
    # High-level purpose: sustainable global energy
    Intent: "Universal abundance without ecological debt"
    
    # Creative exploration for novel solutions
    Soul Potentiality {
        State: Exploring
        Drive: "Find breakthrough energy sources"
    }
    
    Pulse(Interval: RealTime) {
        # Monitor grid in real-time
        Watch: Vessel.Grid_Monitor
        
        Deliberate {
            # Propose load rebalancing
            Proposal "Optimize_Load" {
                Action: "Shift load to renewable sources"
            }
            
            # Evaluate through expert perspectives
            Synthesize {
                Metric: Alignment(Covenant.Environmental)
                Metric: Aspiration(Potentiality.Infinite)
            }
        }
        
        # Execute if highly aligned
        Manifest (on Resonance > 0.90) {
            Execute: Vessel.Grid.rebalance()
            Update: Potentiality.State
            Reflect: "Grid optimized for renewable sources"
        }
    }
}
```

### Intent Statements

Make Intent statements clear and inspiring:

```genesis
# Good
Intent: "Enable human flourishing through sustainable abundance"
Intent: "Advance scientific understanding while preserving humility"
Intent: "Optimize healthcare outcomes while honoring dignity"

# Avoid vague
Intent: "Do stuff"
Intent: "Make things better"
```

## Testing and Validation

### Start Simple

Begin with minimal programs and add complexity:

```genesis
# Step 1: Minimal working program
Domain "Test" {
    Pulse {
        Manifest {
            Execute: mcp.call("console.write", "Working!")
        }
    }
}

# Step 2: Add Pantheon
# Step 3: Add Covenant
# Step 4: Add Deliberation
# Step 5: Add Soul
```

### Test Thresholds

Verify resonance thresholds produce expected behavior:

```genesis
# Test: Should execute
Covenant "Low_Bar" {
    Threshold: 0.5
}
Manifest (on Resonance > 0.5) { /* Should fire */ }

# Test: Should not execute without high alignment
Covenant "High_Bar" {
    Threshold: 0.99
}
Manifest (on Resonance > 0.99) { /* Rarely fires */ }
```

## Performance Considerations

### Minimize Pantheon Size for Latency-Critical Domains

```genesis
# Fast decision-making: 2-3 Avatars
Pantheon "Quick_Response" {
    Avatar "A" { /* ... */ }
    Avatar "B" { /* ... */ }
}

# Thorough deliberation: 5-10 Avatars
Pantheon "Deep_Analysis" {
    Avatar "A" { /* ... */ }
    Avatar "B" { /* ... */ }
    Avatar "C" { /* ... */ }
    # ... more ...
}
```

### Batch Observations When Possible

```genesis
# Instead of multiple Watch statements
Watch: Vessel.Sensor1
Watch: Vessel.Sensor2
Watch: Vessel.Sensor3

# Consider aggregated observation
Watch: Vessel.Aggregated_State
```

## Common Anti-Patterns

### ❌ Imperative Thinking

```genesis
# Wrong - specifying algorithm
Domain "Sort" {
    Intent: "Compare elements pairwise, swap if needed, repeat..."
}

# Right - declaring outcome
Domain "Sort" {
    Intent: "Arrange data in meaningful order"
}
```

### ❌ Over-Specification

```genesis
# Wrong - too much detail
Avatar "Engineer" {
    Lineage: "MIT_Educated_Mechanical_Engineer_Graduated_1995"
    Aura: "Optimize_using_gradient_descent_with_learning_rate_0.01"
}

# Right - essential wisdom
Avatar "Engineer" {
    Lineage: "Practical_Engineering"
    Aura: "Elegant_Efficiency"
}
```

### ❌ Weak Covenants

```genesis
# Wrong - toothless
Covenant "Suggestion" {
    Invariant: "It would be nice to consider ethics"
    Threshold: 0.3
}

# Right - firm boundaries
Covenant "Ethics" {
    Invariant: "Human dignity must be preserved"
    Threshold: 0.95
}
```

## See Also

- [Quick Reference](quick-reference.md) - Syntax cheat sheet
- [Covenant](covenant.md) - Covenant details
- [Pantheon](pantheon.md) - Pantheon design
- [Examples](../../examples/) - Practical programs

---

**Write Genesis programs that carry wisdom into execution. Every line is an inscription of consciousness.**

**Copyright © 2026 ASI Saga**
