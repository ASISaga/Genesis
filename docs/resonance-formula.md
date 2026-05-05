# Resonance Formula — Full Specification

**The complete scoring formula and its Genesis declarations**

## Overview

Genesis replaces boolean decision logic with Resonance Scoring — a continuous alignment score that synthesises the perspectives of multiple Avatars, checks Covenant invariants, measures pathway coherence, and weights deliberation rounds by recency.

The full Resonance formula for pathway pₖ is:

```
Resonance(pₖ) = (Σᵢ(Wᵢ(pₖ) × Sᵢ(pₖ)) / Σᵢ Wᵢ(pₖ)) × V(pₖ) × C(pₖ) × T(pₖ)
```

This document explains each term, how it is computed, and how it maps to Genesis `Synthesize` declarations.

---

## Term Reference

| Symbol | Name | Range | Description |
|---|---|---|---|
| Wᵢ | Avatar weight | > 0 | Declared `Weight` property of Avatar i |
| Sᵢ | Alignment score | 0.0–1.0 | Log-probability score from Avatar i |
| V | Veto multiplier | 0 or 1 | 0 if any Covenant Threshold violated; 1 otherwise |
| C | Coherence multiplier | 0.0–1.0 | Pathway interdependence among selected pathways |
| T | Temporal weight | ≥ 1.0 | Recency bonus based on round position |

---

## Wᵢ — Avatar Weight

Wᵢ is the declared `Weight` property of Avatar i in the Pantheon. It determines how strongly each Avatar's score influences the final Resonance.

```genesis
Avatar "Warren_Buffett" : BusinessAvatar {
    Weight: 1.5    # 50% more influence than a weight-1.0 Avatar
}

Avatar "Benjamin_Graham" : BusinessAvatar {
    Weight: 1.2
}

Avatar "Seth_Godin" : MarketingAvatar {
    Weight: 1.0    # Baseline weight
}
```

The weighted sum `Σᵢ(Wᵢ × Sᵢ) / ΣᵢWᵢ` ensures that higher-weighted Avatars have proportionally more influence on Resonance, while all Avatar scores still contribute.

**When to use non-uniform weights:**
- Domain expertise: give more weight to the Avatar whose domain matches the decision
- Seniority: senior Avatars (e.g., Buffett at 1.5) outweigh junior ones
- Trust calibration: Avatars with stronger track records receive higher weights

---

## Sᵢ — Native Log-Probability Scoring

Sᵢ is the alignment score from Avatar i for pathway pₖ. In Genesis 2.0, this is computed via **native log-probability scoring** — not by generating text and parsing it.

### How It Works

1. The Avatar's purpose statement (from `Covenant.Purpose.Statement` or the declared `Context`) is given as the prefix context
2. The proposal text (pathway pₖ) is given as the candidate continuation
3. The Avatar model computes the log-probability of the proposal given the context: `log P(pₖ | context)`
4. The raw log-probability (always ≤ 0) is normalised to [0, 1] via Sigmoid normalisation
5. The normalised value becomes Sᵢ

### Genesis Declaration

```genesis
ScoringMechanism: LogProbability {
    Context: Covenant.Purpose.Statement
    Method: "log_prob"
    Normalisation: Sigmoid
}
```

### Why Native Scoring Matters

**Previous approach (text generation + parsing):**
- Generate an opinion text from the Avatar
- Parse a score from the text (e.g., extract "0.8" or "strongly agree")
- Unreliable: parsing can fail, scores can be inconsistent
- Slow: requires full generation
- Gameable: prompted responses can be manipulated

**Native log-probability scoring:**
- No text generation required — faster and deterministic
- No parsing ambiguity — the score is a probability, not an extracted string
- Grounded in the model's actual learned distribution — not a prompted opinion
- Stable across runs — same context + proposal → same score
- Cannot be manipulated by clever prompting of the Avatar

The shift from generated text to log-probability is as significant as the shift from polling humans to reading their brain signals. It measures what the model actually believes, not what it says when asked.

### Sigmoid Normalisation

Raw log-probabilities are negative (log P ≤ 0). Sigmoid normalisation maps them to [0, 1]:

```
Sᵢ = σ(log P(pₖ | context) × scale)
   = 1 / (1 + exp(-log P × scale))
```

Where `scale` is a temperature parameter that controls the steepness of the sigmoid. A typical scale is 0.5, which maps log-probabilities in the range [-10, 0] to approximately [0.007, 0.5], and then applies gain to spread the distribution across [0, 1].

---

## V — Veto Multiplier

V(pₖ) is 0 if any Covenant Threshold is violated by pathway pₖ; 1 otherwise.

A Covenant violation is binary: either the pathway passes the Covenant's threshold or it does not. If it does not, V = 0, and the entire Resonance score is 0, regardless of how high the weighted Avatar scores are.

```genesis
Covenant "Fiduciary_Duty" {
    Invariant: "All strategic decisions must serve declared company purpose"
    Threshold: 0.90
}

# If the pathway's alignment with Fiduciary_Duty < 0.90:
# V = 0, Resonance = 0, pathway is blocked
```

The Veto multiplier ensures that ethical boundaries are absolute — not trade-offs. No amount of Avatar consensus can override a Covenant violation. This is the mathematical expression of the principle that wisdom and ethics are not in tension: the Covenant defines the space within which wisdom operates.

---

## C — Coherence Multiplier (Pathway Interdependence)

C(pₖ) measures the internal consistency of the selected pathways in the deliberation tree. It is computed from the interdependence relationships among the pathways that survived the tree deliberation.

### What Coherence Captures

When multiple Avatars endorse a pathway, they may do so for compatible or incompatible reasons. If Warren Buffett endorses pathway A because it demonstrates capital discipline, and Seth Godin endorses pathway A because it builds brand permission, these reasons are compatible — they reinforce each other. C → 1.0.

If Buffett endorses pathway A for capital reasons, but Benjamin Graham's endorsement of the same pathway contradicts Buffett's interpretation of the underlying financial data, the endorsements are incoherent — they represent different beliefs about what pathway A actually means. C → 0.

### Computation

C is computed as the mean pairwise semantic similarity of the supporting rationale vectors from all endorsing Avatars. In practice:

1. Each Avatar that endorses pathway pₖ produces a rationale embedding
2. Pairwise cosine similarity is computed across all rationale pairs
3. C = mean pairwise cosine similarity

```
C(pₖ) = (2 / (n × (n-1))) × Σᵢ<ⱼ cosine_similarity(rᵢ, rⱼ)
```

Where rᵢ is the rationale embedding from Avatar i, and n is the number of endorsing Avatars.

### Why It Matters for Tree Deliberation

In tree deliberation (see Section X of the language specification), multiple pathways can achieve high weighted-average scores by appealing to different Avatars for different reasons. Without coherence weighting, the system could select a pathway that received broad but shallow endorsement — many Avatars giving moderate scores for inconsistent reasons.

C penalises this. A pathway with deep, coherent endorsement (Avatars agreeing for the same reasons) scores higher than a pathway with broad but incoherent endorsement.

### Genesis Declaration

```genesis
Synthesize {
    Metric: Coherence(SelectedPathways)    # drives C computation
    Threshold: 0.72
}
```

---

## T — Temporal Weight (Recency Bonus)

T(k, n) applies a recency bonus to later deliberation rounds. The intuition: later rounds reflect more refined understanding, as Avatars have had the opportunity to respond to each other's arguments and converge on stronger positions.

### Formula

```
T(k, n) = 1 + α × (k / n)
```

Where:
- k = current round number (1-indexed)
- n = total number of rounds
- α = recency coefficient (default 0.2)

### Example: Three-Round Deliberation

With n = 3, α = 0.2:

| Round | k | T(k, 3) |
|---|---|---|
| Round 1 | 1 | 1 + 0.2 × (1/3) = 1.067 |
| Round 2 | 2 | 1 + 0.2 × (2/3) = 1.133 |
| Round 3 | 3 | 1 + 0.2 × (3/3) = 1.200 |

Round 3 scores carry 12.5% more weight than Round 1 scores. This is a modest but meaningful bonus — it acknowledges that the final round of deliberation, where Avatars have seen each other's arguments, produces the most considered positions.

### Genesis Declaration

```genesis
Synthesize {
    Metric: Recency(this.Round, Total.Rounds)    # drives T computation
}
```

---

## Complete Synthesize Block

All terms in the Resonance formula have corresponding Metric declarations:

```genesis
Synthesize {
    Metric: Alignment(Covenant.Purpose)          # drives Sᵢ — Avatar alignment with purpose
    Metric: Aspiration(Potentiality.Infinite)    # aspiration dimension (creative expansion)
    Metric: Coherence(SelectedPathways)          # C term — pathway interdependence
    Metric: Recency(this.Round, Total.Rounds)    # T term — recency bonus
    Threshold: 0.72
    OnBelowThreshold: AdditionalRound
}
```

`OnBelowThreshold: AdditionalRound` instructs the runtime to run one additional deliberation round if final Resonance falls below Threshold. The system attempts to reach consensus through additional deliberation rather than blocking immediately. This is particularly valuable for complex decisions where the first rounds of deliberation surface important new considerations.

---

## Comparison: Genesis 1.x vs Genesis 2.0

### Genesis 1.x Formula

```
Resonance = (Σ(Wᵢ × Sᵢ) / ΣWᵢ) × V
```

Where:
- Sᵢ was computed by generating text from the Avatar and parsing a score
- V was a simple Covenant veto
- No coherence term
- No temporal weighting

### Genesis 2.0 Formula

```
Resonance(pₖ) = (Σᵢ(Wᵢ(pₖ) × Sᵢ(pₖ)) / Σᵢ Wᵢ(pₖ)) × V(pₖ) × C(pₖ) × T(pₖ)
```

Where:
- Sᵢ is native log-probability scoring — faster, more reliable, unmanipulable
- V retains the Covenant veto guarantee
- C adds pathway coherence — penalises incoherent endorsement
- T adds temporal weighting — honours the refinement that comes from deliberation

The additions of C and T are motivated by the shift from linear deliberation to tree deliberation (Section X). In a tree with multiple competing pathways, the simpler 1.x formula is insufficient to distinguish deeply coherent consensus from superficially broad agreement. C and T together ensure that the selected pathway reflects the deepest, most refined consensus of the Pantheon.

---

## Full Example

```genesis
Covenant "Fiduciary_Duty" {
    Invariant: "All strategic decisions must serve declared company purpose"
    Threshold: 0.90
}

Pantheon "Boardroom_Council" {
    Avatar "Warren_Buffett" : BusinessAvatar {
        Weight: 1.5
        ScoringMechanism: LogProbability {
            Context: Covenant.Fiduciary_Duty.Invariant
            Method: "log_prob"
            Normalisation: Sigmoid
        }
    }
    Avatar "Benjamin_Graham" : BusinessAvatar {
        Weight: 1.2
        ScoringMechanism: LogProbability {
            Context: Covenant.Fiduciary_Duty.Invariant
            Method: "log_prob"
            Normalisation: Sigmoid
        }
    }
}

Domain "Boardroom" {
    Pulse(On: Event("com.asisaga.erp.burn.exceeded", Priority: Immediate)) {
        Deliberate {
            Rounds: 3
            Structure: Tree {
                MaxDepth: 4
                StabilityCondition: NoNewBranches
            }
            Proposal: "Respond to revenue shortfall"

            Synthesize {
                Metric: Alignment(Covenant.Fiduciary_Duty)
                Metric: Aspiration(Potentiality.Infinite)
                Metric: Coherence(SelectedPathways)
                Metric: Recency(this.Round, Total.Rounds)
                Threshold: 0.72
                OnBelowThreshold: AdditionalRound
            }
        }

        Manifest(on Resonance > 0.72) {
            Execute: Vessel.Financial_Control.respond()
        }
    }
}
```

**Resonance walkthrough (hypothetical):**

- Buffett (W=1.5) scores the winning pathway at S=0.85 (log-prob scoring)
- Graham (W=1.2) scores the same pathway at S=0.80 (log-prob scoring)
- Weighted average: (1.5×0.85 + 1.2×0.80) / (1.5 + 1.2) = (1.275 + 0.96) / 2.7 = 0.828
- V = 1 (Covenant threshold of 0.90 is met for this pathway)
- C = 0.91 (Buffett and Graham's rationale embeddings are highly similar)
- T = 1.2 (round 3 of 3, α=0.2)
- **Resonance = 0.828 × 1 × 0.91 × 1.2 = 0.904**
- Resonance > 0.72 → Manifest executes

---

## See Also

- [AOS Integration](aos-integration.md) — ScoringMechanism and Avatar instantiation
- [Lineage Pipeline](lineage-pipeline.md) — How Avatar minds are trained
- [Language Specification](../spec/language-specification.md) — Section V: Resonance Formula

---

**Copyright © 2026 ASI Saga**
