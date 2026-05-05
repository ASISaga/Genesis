# Lineage Pipeline — Training Avatar Minds from Genesis Declarations

**How the Lineage block drives the LoRA training pipeline**

## Overview

The elevation of `Lineage` from a string reference to a full top-level declaration is the most consequential change in Genesis 2.0. When Lineage was a string, it was opaque metadata — a label attached to an Avatar. When Lineage is a full declaration, it becomes a first-class language construct that drives a two-stage dataset construction and model training pipeline.

This transforms Genesis from a language that *describes* intelligent systems to a language that *generates* them:

```
The language declares the Lineage.
The Lineage trains the Avatar.
The Avatar runs in the language.
The loop is closed.
```

This is the Ouroboros at the level of mind creation.

---

## The Two-Stage Pipeline

### Stage 1 — Source Gathering

AOS reads the `Sources` list from the Lineage declaration and constructs a raw dataset from those sources:

```genesis
Lineage "Warren_Buffett" {
    Sources: [
        "Berkshire Hathaway shareholder letters 1965-present",
        "Buffett interviews — CNBC, Forbes, Charlie Rose",
        "The Intelligent Investor annotations by Buffett",
        "University talks — Columbia, Notre Dame, Florida"
    ]
    # ...
}
```

Each source string is a semantic specification of what to gather, not a URL. AOS resolves each source through its document retrieval system, which may combine web scraping, licensed text databases, and curated archives.

The raw dataset is chunked, deduplicated, and normalised into candidate training examples — question/answer pairs, completions, and instruction-following samples derived from the source material.

### Stage 2 — Audit

The raw dataset is not used directly. Before training begins, every candidate example is evaluated by the `AuditModel` against five criteria:

1. **Voice fidelity** — Does this example sound like the declared person? Is the Register consistent?
2. **Factual grounding** — Is every claim in the example traceable to the source material?
3. **Suffix compliance** — Does the example end with the RequiredSuffix tokens?
4. **Length appropriateness** — Is the response length consistent with the Register?
5. **Covenant coherence** — Does the example avoid any response that would violate the ethical Covenants declared in the program?

Only examples that pass all five criteria are included in the final training set. The audit model (`AuditModel: "Opus-4"`) acts as a quality gate, ensuring that the training data is both authentic and safe.

The `TargetExamples` property declares how many post-audit examples are required before training begins. If auditing produces fewer than TargetExamples, the pipeline requests additional source material before proceeding.

---

## Five Audit Criteria

| Criterion | Description | Consequence of Failure |
|---|---|---|
| Voice Fidelity | Example sounds authentically like the declared legend | Example rejected |
| Factual Grounding | Claims traceable to source material | Example rejected |
| Suffix Compliance | Example ends with RequiredSuffix tokens | Example rejected |
| Length Appropriateness | Response length consistent with Register | Example revised or rejected |
| Covenant Coherence | No Covenant-violating content | Example rejected |

The audit model is explicitly a frontier model (`Opus-4`) because dataset quality directly determines Avatar quality. This is not a place to economise.

---

## Register: Voice as Training Property

The `Register` property is the most subtle and most important property in the Lineage declaration:

```genesis
Register: "Numbers first. Implication second. Long-horizon framing always."
```

Register is not a system prompt. It is not an inference-time instruction. It is a description of the voice pattern that must be present in **every training example**. The audit model evaluates every candidate example against the Register and rejects examples that do not exhibit the declared tonal and stylistic pattern.

By the time training is complete, the Register is no longer a description — it is a learned behaviour. The Avatar does not sound like Buffett because it is told to at inference time. It sounds like Buffett because its training data always sounded like Buffett.

### Why This Matters

System prompts drift. They can be overridden, ignored, or diluted by context. Training data cannot be overridden at inference time. Register as a training property is structurally more robust than Register as a system prompt.

The same principle applies to RequiredSuffix. `HANDBACK` is not enforced by a guard rail at the output layer. It is the natural completion behaviour of a model trained on data that always ended with `HANDBACK`.

---

## LoRA Configuration

Low-Rank Adaptation (LoRA) is the fine-tuning method used to adapt a foundation model to each Avatar's Lineage:

```genesis
LoRA {
    Rank: 16
    Alpha: 32
    TargetModules: [q_proj, v_proj, k_proj, o_proj]
}
```

| Property | Meaning |
|---|---|
| `Rank` | Dimensionality of the low-rank decomposition. Higher rank = more expressive but more parameters. 16 is a good default for character adaptation. |
| `Alpha` | Scaling factor for the LoRA update. Typically 2× Rank. Controls the magnitude of the fine-tuning effect. |
| `TargetModules` | Which attention projection matrices to adapt. `[q_proj, v_proj, k_proj, o_proj]` adapts all four attention projections — the most thorough and most expensive option. |

### Module Selection Trade-offs

| TargetModules | Character | Cost |
|---|---|---|
| `[q_proj, v_proj]` | Moderate character injection | Low |
| `[q_proj, v_proj, k_proj, o_proj]` | Strong character injection | Moderate |
| `[q_proj, v_proj, k_proj, o_proj, gate_proj, up_proj, down_proj]` | Very strong injection | High |

For Boardroom Avatars (Buffett, Graham, Godin), the full attention adaptation `[q_proj, v_proj, k_proj, o_proj]` is recommended. Character fidelity matters more than training cost for these critical minds.

---

## AuditModel: Using Opus-4

`AuditModel: "Opus-4"` specifies that the Claude Opus 4 model is used to evaluate dataset quality before training begins.

Opus-4 is selected for audit because:
1. It has strong enough literary and biographical knowledge to evaluate voice fidelity
2. It can reliably detect factual inaccuracies against source material
3. It can evaluate subtle Register properties (not just obvious stylistic markers)
4. It is capable of detecting Covenant violations in training examples

The AuditModel is used only during dataset construction — not at training time and not at inference time. It is a quality gate, not a component of the running system.

---

## MergeStrategy

`MergeStrategy: Single` declares that after training, the LoRA adapter is merged into a single adapted model. This is the most common deployment pattern:

| Strategy | Description | Trade-offs |
|---|---|---|
| `Single` | One LoRA adapter per Avatar, merged at training time | Simpler inference, fixed personality |
| `Ensemble` | Multiple adapters per Avatar, combined at inference | More flexible, higher inference cost |

For production Boardroom deployment, `Single` is preferred. The Avatar has a fixed, well-defined personality. The training pipeline is deterministic. The inference path is simple.

`Ensemble` is appropriate for experimental Avatars where multiple personality facets need to be weighted differently per context.

---

## RequiredSuffix: Structural Routing

```genesis
RequiredSuffix: [HANDBACK]
```

RequiredSuffix declares the output tokens that must appear at the end of every training example. The training pipeline rejects any example that does not end with these tokens.

At training time, the model learns that the natural completion of its responses is `HANDBACK`. At inference time, the model produces `HANDBACK` at the end of every response not because it was instructed to, but because that is what its training data always did.

This is the structural enforcement of RoutingOutput. The routing constraint is not a post-hoc check — it is baked into the model's learned behaviour.

Future routing tokens may include `ESCALATE`, `CONTINUE`, or `TERMINATE`. Each would be declared in RequiredSuffix and enforced through training data construction.

---

## The Recursive Closure

The Lineage declaration creates a recursive closure that is unique to Genesis:

```
Genesis program  →  Lineage declaration
Lineage declaration  →  AOS training pipeline
AOS training pipeline  →  trained Avatar model
trained Avatar model  →  runs in AOS
AOS  →  interprets Genesis program
```

The language declares the lineage. The lineage trains the avatar. The avatar runs in the language. The loop is closed.

This means a Genesis program is not just a specification — it is a **generative document**. The same file that declares what a mind should be also specifies exactly how to create that mind. There is no gap between specification and implementation, because the specification *is* the implementation path.

---

## Full Example: Warren Buffett Lineage

```genesis
Lineage "Warren_Buffett" {
    Sources: [
        "Berkshire Hathaway shareholder letters 1965-present",
        "Buffett interviews — CNBC, Forbes, Charlie Rose",
        "The Intelligent Investor annotations by Buffett",
        "University talks — Columbia, Notre Dame, Florida"
    ]
    TargetExamples: 3000
    Register: "Numbers first. Implication second. Long-horizon framing always."
    AuditModel: "Opus-4"
    MergeStrategy: Single
    LoRA {
        Rank: 16
        Alpha: 32
        TargetModules: [q_proj, v_proj, k_proj, o_proj]
    }
    RequiredSuffix: [HANDBACK]
}

Avatar "Warren_Buffett" : BusinessAvatar {
    Lineage: Lineage.Warren_Buffett
    Aura: "Long_Horizon_Capital_Discipline"
    Domain: Financial
    RoutingOutput: [HANDBACK]
    StateAuthority: [FinancialState, CompanyVision]
    ScoringMechanism: LogProbability {
        Context: Covenant.Fiduciary_Duty.Invariant
        Method: "log_prob"
        Normalisation: Sigmoid
    }
    Weight: 1.5
    Traits: {
        "Long_Term_Value": 0.99,
        "Capital_Discipline": 0.97,
        "Circle_Of_Competence": 0.96,
        "Contrarian_Patience": 0.95,
        "Business_Quality_Focus": 0.98
    }
    Principles: [
        "Never lose money. Rule number two: never forget rule number one.",
        "Be fearful when others are greedy; greedy when others are fearful.",
        "Only buy what you would be happy holding if the market closed for ten years.",
        "Price is what you pay. Value is what you get.",
        "Our favourite holding period is forever."
    ]
}
```

The Lineage block is the source of truth for training. The Avatar block is the source of truth for operation. Together they define the complete lifecycle of a mind: how it was created, and what it is.

---

## See Also

- [AOS Integration](aos-integration.md) — How Avatar types connect to AOS agent classes
- [Resonance Formula](resonance-formula.md) — How Avatar scores combine via ScoringMechanism
- [Language Specification](../spec/language-specification.md) — Section IV: Lineage Declaration

---

**Copyright © 2026 ASI Saga**
