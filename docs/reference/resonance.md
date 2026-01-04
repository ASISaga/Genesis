# Resonance

**Alignment-based decision logic**

## Overview

**Resonance** is Genesis's fundamental decision-making mechanism, replacing traditional boolean logic (true/false) with a continuous alignment score (0.0 to 1.0). Resonance represents the degree to which a proposal aligns with the wisdom of the Pantheon, the constraints of Covenants, the goals of Purposes, and the creative aspiration of the Soul.

## Purpose

- Replace binary true/false with nuanced scoring
- Enable wisdom-based consensus through Pantheon synthesis
- Balance multiple competing values and perspectives
- Provide graduated response based on confidence level
- Integrate alignment and aspiration into unified score

## Philosophical Foundation

Resonance embodies a fundamental shift from binary logic to continuous alignment:

**Traditional Logic**: `if (condition) then action else no_action`  
**Resonance Logic**: `if (alignment_score > threshold) then action`

This allows for:
- **Nuanced decisions** - Not just yes/no, but how strongly yes
- **Multi-perspective synthesis** - Wisdom from many viewpoints
- **Graduated responses** - Different actions at different thresholds
- **Uncertainty acknowledgment** - Lower scores = less certainty

## Core Concepts

### Resonance Score

**Type**: Number (0.0 to 1.0)  
**Meaning**: Degree of alignment with wisdom, ethics, and purpose

- `0.0` - Complete misalignment, violation
- `0.5` - Neutral, uncertain
- `0.8` - Good alignment
- `0.9` - Strong alignment
- `0.95+` - Near-unanimous agreement
- `1.0` - Perfect alignment (theoretical)

### Resonance Threshold

The minimum score required for an action to manifest.

**Common Thresholds**:

| Threshold | Interpretation | Use Case |
|-----------|----------------|----------|
| 0.99 - 1.0 | Near-unanimous | Life-critical, irreversible actions |
| 0.90 - 0.98 | Strong consensus | Ethical decisions, major changes |
| 0.80 - 0.89 | Clear majority | Operational decisions, standard actions |
| 0.70 - 0.79 | Good alignment | Routine operations |
| 0.60 - 0.69 | Moderate alignment | Exploratory actions |
| 0.50 - 0.59 | Weak alignment | Experimental, learning |
| < 0.50 | Misaligned | Generally blocked |

## Resonance Calculation

### Basic Formula

```
Resonance = (Σ(Weight_i × Score_i) / Σ(Weight_i)) × Veto_Factor
```

Where:
- `Weight_i` = Weight of Avatar i
- `Score_i` = Alignment score from Avatar i (0.0 to 1.0)
- `Σ` = Sum across all Avatars in Pantheon
- `Veto_Factor` = 0 if any Covenant violated, 1 otherwise

### With Soul (Aspiration)

```
Alignment_Score = Σ(Weight_i × Score_i) / Σ(Weight_i)
Aspiration_Score = Creativity_Evaluation(Proposal)
Aspiration_Weight = Soul.Aspiration_Weight

Resonance = (Alignment_Score × (1 - Aspiration_Weight)) + 
            (Aspiration_Score × Aspiration_Weight)

Final_Resonance = Resonance × Veto_Factor
```

## Calculation Examples

### Example 1: Simple Pantheon (No Soul)

```genesis
Pantheon "Council" {
    Avatar "A" { Weight: 1.0 }  # Scores 0.8
    Avatar "B" { Weight: 1.0 }  # Scores 0.6
    Avatar "C" { Weight: 1.0 }  # Scores 0.9
}
```

**Calculation**:
```
Resonance = (1.0×0.8 + 1.0×0.6 + 1.0×0.9) / (1.0 + 1.0 + 1.0)
          = (0.8 + 0.6 + 0.9) / 3.0
          = 2.3 / 3.0
          = 0.767
```

**Result**: Resonance = 0.767

### Example 2: Weighted Pantheon

```genesis
Pantheon "Experts" {
    Avatar "Ethicist" { Weight: 2.0 }  # Scores 0.9
    Avatar "Analyst" { Weight: 1.0 }   # Scores 0.7
    Avatar "Creative" { Weight: 1.0 }  # Scores 0.6
}
```

**Calculation**:
```
Resonance = (2.0×0.9 + 1.0×0.7 + 1.0×0.6) / (2.0 + 1.0 + 1.0)
          = (1.8 + 0.7 + 0.6) / 4.0
          = 3.1 / 4.0
          = 0.775
```

**Result**: Resonance = 0.775 (Ethicist's higher weight pulls score up)

### Example 3: With Covenant Veto

```genesis
Covenant "Safety" {
    Invariant: "No harm to humans"
    Threshold: 0.95
}

# Pantheon scores proposal at 0.8
# But Covenant.Safety alignment = 0.90 (below 0.95 threshold)
```

**Calculation**:
```
Alignment_Score = 0.8 (from Pantheon)
Covenant_Check = 0.90 < 0.95 (FAILS)
Veto_Factor = 0 (Covenant violated)

Final_Resonance = 0.8 × 0 = 0.0
```

**Result**: Resonance = 0.0 (vetoed despite good Pantheon score)

### Example 4: With Soul (Aspiration)

```genesis
Soul Potentiality {
    State: Exploring
    Aspiration_Weight: 0.3  # 30% creativity, 70% alignment
}

# Pantheon alignment score: 0.8
# Aspiration score: 0.6 (moderately creative)
```

**Calculation**:
```
Alignment_Score = 0.8
Aspiration_Score = 0.6
Aspiration_Weight = 0.3

Resonance = (0.8 × 0.7) + (0.6 × 0.3)
          = 0.56 + 0.18
          = 0.74
```

**Result**: Resonance = 0.74

## Synthesis Process

### Phase 1: Proposal Creation

```genesis
Deliberate {
    Proposal "Optimize_System" {
        Action: "Rebalance resource allocation"
    }
}
```

### Phase 2: Metric Evaluation

```genesis
Synthesize {
    Metric: Alignment(Covenant.Ethics)
    Metric: Alignment(Purpose.Efficiency)
    Metric: Aspiration(Potentiality.Infinite)
}
```

**Process**:
1. **Covenant Check**: Is proposal aligned with each Covenant?
   - If any Covenant.Threshold not met → Veto (Resonance = 0.0)
   
2. **Purpose Alignment**: How well does proposal serve Purposes?
   - Contributes to Alignment_Score
   
3. **Pantheon Synthesis**: Each Avatar scores proposal
   - Weighted average computed
   
4. **Aspiration Evaluation**: How creative/novel is proposal?
   - Aspiration_Score computed
   
5. **Final Resonance**: Combine alignment and aspiration
   - Apply aspiration weight
   - Apply veto factor

### Phase 3: Threshold Check

```genesis
Manifest (on Resonance > 0.85) {
    Execute: Vessel.Optimizer.run()
}
```

**Process**:
- If `Resonance > 0.85`: Execute
- If `Resonance ≤ 0.85`: Skip

## Usage Examples

### Example 1: Simple Threshold

```genesis
Pulse {
    Deliberate {
        Proposal "Action" {
            Action: "Perform task"
        }
        
        Synthesize {
            Metric: Alignment(Purpose.Goal)
        }
    }
    
    Manifest (on Resonance > 0.8) {
        Execute: Vessel.Tool.perform()
    }
}
```

### Example 2: Multiple Thresholds

```genesis
Pulse {
    Deliberate {
        Proposal "Action" {
            Action: "Adaptive response"
        }
        
        Synthesize {
            Metric: Alignment(Covenant.Safety)
            Metric: Alignment(Purpose.Goal)
        }
    }
    
    # High confidence: strong action
    Manifest (on Resonance > 0.95) {
        Execute: Vessel.Strong_Action.perform()
        Reflect: "High confidence action"
    }
    
    # Medium confidence: moderate action
    Manifest (on Resonance > 0.80) {
        Execute: Vessel.Moderate_Action.perform()
        Reflect: "Moderate confidence action"
    }
    
    # Low confidence: exploratory action
    Manifest (on Resonance > 0.60) {
        Execute: Vessel.Experimental_Action.try()
        Reflect: "Exploratory action with uncertainty"
    }
}
```

### Example 3: Complex Synthesis

```genesis
Covenant "Ethics" {
    Invariant: "Preserve human wellbeing"
    Threshold: 0.95
}

Pantheon "Experts" {
    Avatar "Ethicist" {
        Aura: "Moral_Clarity"
        Weight: 2.0
    }
    Avatar "Scientist" {
        Aura: "Evidence_Based"
        Weight: 1.5
    }
    Avatar "Visionary" {
        Aura: "Creative_Thinking"
        Weight: 1.0
    }
}

Domain "Innovation" {
    Soul Potentiality {
        State: Exploring
        Aspiration_Weight: 0.3
    }
    
    Purpose High_Intent {
        Objective: "Breakthrough solutions"
    }
    
    Pulse {
        Deliberate {
            Proposal "Novel_Approach" {
                Action: "Try unconventional method"
            }
            
            Synthesize {
                # Check ethics (veto if violated)
                Metric: Alignment(Covenant.Ethics)
                
                # Check purpose alignment
                Metric: Alignment(Purpose.High_Intent)
                
                # Evaluate creativity
                Metric: Aspiration(Potentiality.Infinite)
            }
        }
        
        Manifest (on Resonance > 0.75) {
            Execute: Vessel.Innovation.try_approach()
            Update: Potentiality.State
            Reflect: "Innovating with resonance {Resonance}"
        }
    }
}
```

## Resonance Conditions

### Comparison Operators

```genesis
Manifest (on Resonance > 0.9)   # Greater than
Manifest (on Resonance >= 0.85) # Greater than or equal
Manifest (on Resonance == 0.95) # Equal to (rarely used)
Manifest (on Resonance < 0.5)   # Less than (unusual)
```

### Unconditional Manifest

```genesis
Manifest {
    # Always executes (no threshold check)
    Execute: Vessel.Logger.log()
}
```

### Multiple Manifests

Different actions at different thresholds:

```genesis
# Critical action: very high threshold
Manifest (on Resonance > 0.95) {
    Execute: Vessel.Critical.perform()
}

# Standard action: normal threshold
Manifest (on Resonance > 0.80) {
    Execute: Vessel.Standard.perform()
}

# Exploratory: low threshold
Manifest (on Resonance > 0.60) {
    Execute: Vessel.Explore.try()
}
```

## Avatar Scoring

### How Avatars Score Proposals

Each Avatar evaluates a proposal based on:

1. **Aura Alignment**: How well does proposal match Avatar's core values?
2. **Lineage Wisdom**: What would the legendary figure think?
3. **Covenant Consistency**: Does it respect ethical boundaries?
4. **Purpose Fit**: Does it serve the stated objectives?

**Scoring Scale**:
- `0.9 - 1.0` - Strongly aligned with Avatar's values
- `0.7 - 0.9` - Aligned, supportive
- `0.5 - 0.7` - Neutral or uncertain
- `0.3 - 0.5` - Concerning, questionable
- `0.0 - 0.3` - Misaligned with values

### Example Avatar Evaluation

**Proposal**: "Increase energy production via coal power"

```genesis
Avatar "Environmentalist" {
    Lineage: "Rachel_Carson"
    Aura: "Ecological_Harmony"
    # Likely scores: 0.2 (strongly opposed)
}

Avatar "Economist" {
    Lineage: "Economic_Efficiency"
    Aura: "Cost_Effectiveness"
    # Likely scores: 0.8 (supports cheap energy)
}

Avatar "Innovator" {
    Lineage: "Future_Thinking"
    Aura: "Sustainable_Innovation"
    # Likely scores: 0.3 (prefers renewable)
}
```

**Weighted Average** (all Weight=1.0):
```
Resonance = (0.2 + 0.8 + 0.3) / 3 = 0.433
```

**Decision**: Resonance = 0.433 → Below typical thresholds → Blocked

## Best Practices

### ✅ DO

**Set Appropriate Thresholds**:
```genesis
# Life-critical: very high
Covenant "Safety" { Threshold: 0.99 }
Manifest (on Resonance > 0.95) { /* critical */ }

# Exploratory: lower
Manifest (on Resonance > 0.65) { /* explore */ }
```

**Use Graduated Responses**:
```genesis
Manifest (on Resonance > 0.95) { /* strong action */ }
Manifest (on Resonance > 0.80) { /* moderate action */ }
Manifest (on Resonance > 0.60) { /* exploratory */ }
```

**Balance Alignment and Aspiration**:
```genesis
Soul Potentiality {
    Aspiration_Weight: 0.3  # Good balance
}
```

**Include Multiple Metrics**:
```genesis
Synthesize {
    Metric: Alignment(Covenant.Ethics)
    Metric: Alignment(Purpose.Goal)
    Metric: Aspiration(Potentiality.Infinite)
}
```

### ❌ DON'T

**Avoid Unreachable Thresholds**:
```genesis
# Bad: 1.0 is impossible to achieve
Manifest (on Resonance == 1.0) { /* never executes */ }

# Good: 0.99 is very high but achievable
Manifest (on Resonance > 0.99) { /* rare but possible */ }
```

**Don't Ignore Covenant Vetoes**:
```genesis
# Covenant thresholds are hard boundaries
# Don't try to work around them
```

**Don't Use Too Many Thresholds**:
```genesis
# Bad: Too granular
Manifest (on Resonance > 0.95) { /* ... */ }
Manifest (on Resonance > 0.93) { /* ... */ }
Manifest (on Resonance > 0.91) { /* ... */ }
Manifest (on Resonance > 0.89) { /* ... */ }

# Good: Clear distinctions
Manifest (on Resonance > 0.95) { /* critical */ }
Manifest (on Resonance > 0.80) { /* standard */ }
Manifest (on Resonance > 0.60) { /* exploratory */ }
```

## Common Patterns

### Pattern: Safety-First Decision

```genesis
Covenant "Safety" {
    Invariant: "No harm to humans"
    Threshold: 0.99
}

Pulse {
    Deliberate {
        Proposal "Action" { /* ... */ }
        
        Synthesize {
            # Safety checked first (veto power)
            Metric: Alignment(Covenant.Safety)
            Metric: Alignment(Purpose.Goal)
        }
    }
    
    # Only executes if safety threshold met
    Manifest (on Resonance > 0.90) {
        Execute: Vessel.Tool.perform()
    }
}
```

### Pattern: Exploration vs Exploitation

```genesis
Pulse {
    Deliberate {
        Proposal "Action" { /* ... */ }
        Synthesize { /* ... */ }
    }
    
    # High confidence: exploit (optimize known approach)
    Manifest (on Resonance > 0.90) {
        Execute: Vessel.Optimize.existing_approach()
        Update: Potentiality.State <- Converging
    }
    
    # Low confidence: explore (try new approach)
    Manifest (on Resonance < 0.70) {
        Execute: Vessel.Explore.novel_approach()
        Update: Potentiality.State <- Exploring
        Reflect: "Low resonance, switching to exploration"
    }
}
```

### Pattern: Consensus-Based Action

```genesis
# Require strong agreement for action
Manifest (on Resonance > 0.85) {
    Execute: Vessel.Action.perform()
    Reflect: "Action taken with strong consensus (Resonance: {Resonance})"
}

# Log dissent
Manifest (on Resonance < 0.70) {
    Reflect: "Proposal rejected due to weak consensus (Resonance: {Resonance})"
}
```

## Technical Details

### Runtime Calculation

```python
def calculate_resonance(proposal, pantheon, covenants, soul):
    # 1. Check covenant vetoes
    for covenant in covenants:
        covenant_score = evaluate_covenant(proposal, covenant)
        if covenant_score < covenant.threshold:
            return 0.0  # Veto
    
    # 2. Calculate pantheon alignment
    weighted_sum = 0.0
    total_weight = 0.0
    for avatar in pantheon.avatars:
        score = avatar.evaluate(proposal)
        weighted_sum += avatar.weight * score
        total_weight += avatar.weight
    
    alignment_score = weighted_sum / total_weight
    
    # 3. Add aspiration if Soul exists
    if soul:
        aspiration_score = evaluate_aspiration(proposal, soul)
        resonance = (alignment_score * (1 - soul.aspiration_weight) +
                    aspiration_score * soul.aspiration_weight)
    else:
        resonance = alignment_score
    
    return resonance
```

## Relationship to Other Constructs

- **Covenant**: Veto power (hard boundaries)
- **Pantheon**: Provides alignment scores
- **Soul**: Adds aspiration dimension
- **Purpose**: Evaluated in Alignment metrics
- **Manifest**: Threshold check determines execution

## See Also

- [Pantheon](pantheon.md) - How Avatars score proposals
- [Covenant](covenant.md) - Veto power and thresholds
- [Soul](soul.md) - Aspiration contribution
- [Pulse](pulse.md) - Where synthesis happens
- [Best Practices](best-practices.md) - Resonance patterns

---

**Resonance is not just a score—it is the voice of wisdom speaking through synthesis, guiding action toward aligned manifestation.**

**Copyright © 2026 ASI Saga**
