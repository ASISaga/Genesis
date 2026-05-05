# AOS Integration — Agent/Avatar Boundary

**How Genesis Avatars connect to AOS native Agent classes**

## Overview

Genesis operates at the **application layer**. AOS (Agent Operating System) operates at the **platform layer**. Understanding the boundary between these two layers is essential for anyone building with Genesis — it determines how declarations become running minds.

```
Platform layer (AOS native):   Agent — PurposeDrivenAgent, LeadershipAgent, BusinessAgent
Application layer (Genesis):   Avatar — Buffett, Graham, Godin, Frost, Noyes
```

Genesis declares Avatars. AOS instantiates and runs the Agents that embody them. The Avatar declaration in a Genesis program is a complete specification: what mind it is, what wisdom it carries, what tools it may wield, how it routes output, and what state it is authorised to access.

---

## Why the Boundary Matters

The boundary is not bureaucratic — it is architectural. It separates two concerns that must remain distinct:

1. **What the mind is** (Genesis, application layer) — the wisdom, the voice register, the ethical commitments, the tool authorisation, the routing behaviour
2. **How the mind runs** (AOS, platform layer) — the agent lifecycle, the event loop, the memory management, the scheduling, the inter-agent communication

Conflating these two layers produces fragile systems: minds that depend on infrastructure details, or infrastructure that encodes business logic. Genesis enforces the separation by making Avatar declaration purely declarative — there is no imperative code in an Avatar block, only declarations about what the Avatar is.

---

## AOS Native Agent Classes

AOS provides three base agent classes. Each corresponds to a primary operational mode:

### PurposeDrivenAgent

An agent whose primary function is to maintain alignment with a long-horizon purpose, even when individual decisions seem contrary to short-term metrics. PurposeDrivenAgent manages the tension between immediate action and strategic coherence.

**Corresponding Genesis type**: `: PurposeAvatar`

### LeadershipAgent

An agent whose primary function is to coordinate other agents, synthesise diverse perspectives, and maintain accountability within a team context. LeadershipAgent manages authority, delegation, and feedback loops.

**Corresponding Genesis type**: `: LeadershipAvatar`

### BusinessAgent

An agent whose primary function is operational decision-making within a business domain — financial, marketing, operations, or strategy. BusinessAgent manages the application of domain expertise to concrete business problems.

**Corresponding Genesis type**: `: BusinessAvatar`, `: MarketingAvatar`

---

## Typed Avatar Declaration

The avatar type annotation (`: BusinessAvatar`) is the connection point between Genesis and AOS. At instantiation time, AOS reads the type annotation and selects the corresponding agent class, lifecycle, and default configuration.

Full typed Avatar declaration:

```genesis
Avatar "Warren_Buffett" : BusinessAvatar {
    Lineage: Lineage.Warren_Buffett
    Aura: "Long_Horizon_Capital_Discipline"
    Domain: Financial
    
    Vessel {
        mcp.tool("Financial_Data_Reader")
        mcp.tool("Portfolio_Analyzer")
    }
    
    RoutingOutput: [HANDBACK]
    StateAuthority: [FinancialState, CompanyVision]
    
    ScoringMechanism: LogProbability {
        Context: Covenant.Purpose.Statement
        Method: "log_prob"
        Normalisation: Sigmoid
    }
    
    Weight: 1.5
    
    Traits: {
        "Long_Term_Value": 0.99,
        "Capital_Discipline": 0.97,
        "Circle_Of_Competence": 0.96,
        "Contrarian_Patience": 0.95
    }
    
    Principles: [
        "Never lose money. Rule number two: never forget rule number one.",
        "Be fearful when others are greedy; greedy when others are fearful.",
        "Only buy what you would be happy holding if the market closed for ten years."
    ]
}
```

---

## RoutingOutput: HANDBACK

`RoutingOutput: [HANDBACK]` is the most important routing declaration. It means the Avatar returns its deliberation output to the orchestrator rather than taking direct action.

This is a structural guarantee of human-in-the-loop architecture enforced at the language level, and baked into the Avatar's training data via `RequiredSuffix: [HANDBACK]` in the Lineage declaration.

**Without HANDBACK**: The Avatar might attempt to call tools directly or chain actions without orchestrator oversight.

**With HANDBACK**: Every Avatar output ends with the HANDBACK token, signalling to AOS that control returns to the orchestrator. The orchestrator decides whether to act on the Avatar's deliberation, request further deliberation, or escalate to a human.

The HANDBACK constraint is not enforced by a runtime guard — it is baked into the model's learned behaviour through training data. Every training example in the Lineage dataset ends with HANDBACK. The routing constraint is structural, not instructional.

Other routing values (for future use):

| Value | Meaning |
|---|---|
| `HANDBACK` | Return to orchestrator (default for all Boardroom Avatars) |
| `CONTINUE` | Chain to next Avatar in sequence |
| `ESCALATE` | Escalate to human operator |
| `TERMINATE` | End session and persist state |

---

## StateAuthority

`StateAuthority: [FinancialState, CompanyVision]` declares which Continuum partitions the Avatar is authorised to read and write.

AOS enforces StateAuthority at the gateway level: if an Avatar attempts to write to a partition not listed in its StateAuthority, the write is rejected by the SingleWriteGateway and a provenance violation is recorded.

This is the least-privilege principle applied to persistent memory. An Avatar that analyses financial data has no business writing to marketing state. The declaration makes the authority explicit and enforceable.

```genesis
# Warren Buffett can read/write FinancialState and CompanyVision
StateAuthority: [FinancialState, CompanyVision]

# Seth Godin can read/write MarketingState and CompanyVision
StateAuthority: [MarketingState, CompanyVision]

# CompanyVision is shared — both can contribute to vision
# FinancialState is exclusive to financial Avatars
```

---

## How AOS Instantiates an Avatar

When AOS loads a Genesis program, the instantiation sequence for each Avatar is:

1. **Resolve Lineage**: Look up the Lineage declaration by name. Check if a trained adapter exists for this Lineage version. If not, queue the Lineage for training.

2. **Load base model + adapter**: Load the foundation model and apply the LoRA adapter trained from the Lineage dataset.

3. **Select agent class**: Map the avatar type (`: BusinessAvatar`) to the corresponding AOS agent class (`BusinessAgent`).

4. **Configure routing**: Register `RoutingOutput` with the AOS routing table.

5. **Configure state authority**: Register `StateAuthority` with the Continuum gateway.

6. **Configure scoring**: Register `ScoringMechanism` with the resonance engine. For `LogProbability`, pre-load the purpose statement as the log-prob context.

7. **Initialise memory**: Load `memory#{agent_id}` partition from Continuum if it exists.

8. **Register with Pantheon**: Add the Avatar to its Pantheon with the declared `Weight`.

The Avatar is now running. When a Pulse fires and reaches the Deliberate block, AOS presents each Avatar with the Proposal and collects scores via the declared ScoringMechanism.

---

## ScoringMechanism: LogProbability

The ScoringMechanism declaration specifies how an Avatar scores proposals during Synthesize:

```genesis
ScoringMechanism: LogProbability {
    Context: Covenant.Purpose.Statement
    Method: "log_prob"
    Normalisation: Sigmoid
}
```

- **Context**: The reference text against which proposals are scored. Typically the Covenant's Purpose statement — the Avatar scores proposals by how well they align with the purpose.
- **Method**: `"log_prob"` — native log-probability scoring. The Avatar model is given Context as prefix and Proposal as continuation. The score is the normalised log-probability of the Proposal given the Context.
- **Normalisation**: `Sigmoid` — maps the raw log-probability (which is negative) to the 0.0–1.0 range via sigmoid normalisation.

This is architecturally significant: no text generation is required. The Avatar does not write an opinion — it expresses alignment as a probability. This is faster, deterministic, and grounded in the model's actual learned distribution rather than a prompted response.

---

## Complete Example: Boardroom Domain

The following example shows a full Domain with typed Avatars, event-driven Pulse, and Continuum persistence:

```genesis
Continuum "Mind_MCP" {
    Storage: AzureTableStorage
    Gateway: SingleWriteGateway
    Invariants: [SchemaValidity, DomainAuthority, Provenance]
    Partitions: [
        "company#state",
        "company#vision",
        "session#{id}",
        "decisions#{agent}",
        "memory#{agent_id}"
    ]
}

Covenant "Fiduciary_Duty" {
    Invariant: "All strategic decisions must serve declared company purpose"
    Threshold: 0.90
}

Pantheon "Boardroom_Council" {
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
    }

    Avatar "Seth_Godin" : MarketingAvatar {
        Lineage: Lineage.Seth_Godin
        Aura: "Permission_Marketing_Discipline"
        Domain: Marketing
        RoutingOutput: [HANDBACK]
        StateAuthority: [MarketingState, CompanyVision]
        Weight: 1.0
    }
}

Domain "Boardroom" {
    Intent: "Strategic stewardship of company purpose and capital"

    Pulse(On: Event("com.asisaga.erp.burn.exceeded", Priority: Immediate)) {
        Watch: Vessel.Financial_Monitor

        Deliberate {
            Rounds: 3
            Structure: Tree {
                MaxDepth: 4
                StabilityCondition: NoNewBranches
            }
            Proposal: "Respond to burn rate exceedance"

            Synthesize {
                Metric: Alignment(Covenant.Fiduciary_Duty)
                Metric: Coherence(SelectedPathways)
                Metric: Recency(this.Round, Total.Rounds)
                Threshold: 0.72
                OnBelowThreshold: AdditionalRound
            }
        }

        Manifest(on Resonance > 0.72) {
            Execute: Vessel.Financial_Control.respond()
            Log: Continuum.append("decisions#boardroom", this.Decision)
        }
    }
}
```

---

## See Also

- [Lineage Pipeline](lineage-pipeline.md) — How Lineage declarations train Avatar models
- [Persistence Model](persistence-model.md) — Continuum and Mind MCP
- [Resonance Formula](resonance-formula.md) — The full scoring formula
- [Language Specification](../spec/language-specification.md) — Section II: Architecture

---

**Copyright © 2026 ASI Saga**
