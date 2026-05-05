# Persistence Model — Continuum and Mind MCP

**The continuous memory of the running consciousness**

## Overview

Mind MCP is the single persistence layer for the entire AOS stack. It is not infrastructure — it is the continuous memory of the running consciousness. Without it, every Pulse starts from zero. With it, every deliberation builds on every deliberation that came before.

In Genesis, the persistence layer is declared with the `Continuum` keyword:

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
```

The Continuum declaration is the source of truth for how the running system remembers. Covenants govern what the system may do. Lineages define the minds that do it. Continuum defines how those minds remember across time.

---

## Why a Single Persistence Gateway

The `SingleWriteGateway` property is the most important architectural guarantee in the persistence model. All writes to persistent state — from every Avatar, every Domain, every Pulse — flow through a single gateway.

### Without SingleWriteGateway

Without a single write gateway, multiple Avatars writing concurrently produce dual-write races:

1. Buffett reads `company#state` at T=0: revenue = 12M
2. Graham reads `company#state` at T=0: revenue = 12M
3. Buffett writes `company#state` at T=1: revenue = 12M, burn_alert = true
4. Graham writes `company#state` at T=1: revenue = 11.8M (stale read)

Graham's write wins (last write wins) and erases Buffett's burn_alert. The system's memory is now inconsistent.

### With SingleWriteGateway

All writes are serialised through the gateway. Each write is attributed (which Avatar), timestamped (when), and carries the session context (which Pulse, which round). Concurrent writes are resolved by the gateway into a consistent sequence. No dual-write race is possible because there is only one write path.

The gateway also enforces all three Invariants on every write before committing:

```
SingleWriteGateway:
  1. Check SchemaValidity
  2. Check DomainAuthority (StateAuthority)
  3. Attach Provenance
  4. Commit to Storage
```

If any check fails, the write is rejected and the rejection is logged.

---

## The Continuum Keyword

Continuum is not just a configuration block — it is a declaration of consciousness continuity. The name encodes the intent: a Continuum is not a database. It is the substrate of memory that makes a running system more than a stateless function.

The distinction matters for how Genesis programs are written. When a Genesis program writes to Continuum:

```genesis
Log: Continuum.append("decisions#boardroom", this.Decision)
```

...it is not persisting a record. It is extending the memory of a mind. The decision, its context, the Resonance score that produced it, the round it came from — all of this becomes part of the continuous experience of the running system.

Over time, `memory#{agent_id}` accumulates the decisions, preferences, and reasoning patterns of each Avatar. A Buffett Avatar that has been running for six months has a richer memory than one that started today — and that memory shapes how it deliberates.

---

## Continuum Properties

### Storage

```genesis
Storage: AzureTableStorage
```

The backing storage technology. `AzureTableStorage` is the current implementation: a NoSQL key-value store with strong consistency and efficient partition-key queries.

The Continuum declaration is **storage-agnostic**. Changing the Storage property is the only change required to migrate to a different backend. All Genesis programs that reference Continuum continue to work unchanged.

Future storage backends may include:
- `CosmosDB` — for global distribution
- `PostgreSQL` — for relational structure when needed
- `VectorStore` — for semantic memory retrieval

### Gateway

```genesis
Gateway: SingleWriteGateway
```

The gateway implementation. `SingleWriteGateway` is the standard production gateway: a singleton service that serialises all writes and enforces Invariants.

An alternative `LocalGateway` may be declared for development and testing, where the full provenance and authority enforcement is relaxed.

### Invariants

```genesis
Invariants: [SchemaValidity, DomainAuthority, Provenance]
```

The three Invariants enforced by the gateway on every write:

| Invariant | Enforcement |
|---|---|
| `SchemaValidity` | The write payload conforms to the declared schema for that partition. An Avatar cannot write arbitrary data to a partition — the partition schema is enforced. |
| `DomainAuthority` | The writing Avatar must have the target partition listed in its `StateAuthority` declaration. An Avatar without `FinancialState` in its StateAuthority cannot write to `company#state`. |
| `Provenance` | Every write must carry: agent identity, session ID, Pulse timestamp, and round number. Writes without provenance are rejected. |

### Partitions

```genesis
Partitions: [
    "company#state",
    "company#vision",
    "session#{id}",
    "decisions#{agent}",
    "memory#{agent_id}"
]
```

Partitions define the logical structure of the Continuum. Each partition is a named section of memory with its own schema, access control, and query patterns.

---

## Partition Scheme

### `company#state`

**Contents**: Current operational state of the company — KPIs, alerts, current metrics, live flags.

**Read**: All Avatars with appropriate StateAuthority. Commonly read at the beginning of each Pulse by the Watch block.

**Write**: Avatars with `FinancialState` or other state authorities in their StateAuthority declaration.

**Pattern**: Single-row partition (the "current state" of the company). Updated in-place with versioning.

### `company#vision`

**Contents**: Declared long-term vision, strategic anchors, and purpose statements. Updated infrequently.

**Read**: All Avatars — vision is the shared context for all deliberation.

**Write**: Avatars with `CompanyVision` in their StateAuthority.

**Pattern**: Append-only with timestamps. Vision evolves, but old versions are preserved.

### `session#{id}`

**Contents**: Per-session deliberation context — the full pathway tree, all Avatar scores, the proposals considered, the final Resonance.

**Read**: Avatars participating in the session.

**Write**: The orchestrator writes session context at the start of each Pulse; Avatars write their deliberation outputs.

**Pattern**: Created fresh for each Pulse session. Retained for audit.

### `decisions#{agent}`

**Contents**: Decision history per agent — all decisions taken, with their Resonance scores, the session context, and the outcome.

**Read**: Orchestrator, human operators, audit processes.

**Write**: Orchestrator after each successful Manifest.

**Pattern**: Append-only. Never modified after writing.

### `memory#{agent_id}`

**Contents**: Persistent memory per Avatar across sessions — accumulated preferences, observed patterns, long-term context that informs future deliberation.

**Read**: The Avatar itself, at the start of each Pulse.

**Write**: The Avatar, via `Continuum.append("memory#{agent_id}", ...)`.

**Pattern**: Rolling window with semantic compression. Oldest memories are summarised and compressed to maintain efficient retrieval while preserving long-term context.

---

## Continuum References in Genesis Programs

Genesis programs reference Continuum in two patterns:

### Appending decisions

```genesis
Manifest(on Resonance > 0.72) {
    Execute: Vessel.Financial_Control.respond()
    Log: Continuum.append("decisions#boardroom", this.Decision)
}
```

`this.Decision` carries the full decision object: the Proposal text, the Resonance score, the Avatar scores, the round count, the session ID, and the timestamp.

### Appending coherence audits

```genesis
Verify {
    Assert: Manifest_Possibility.Coherence(Identity.Fabric) > 0.95
    OnFailure: Pause.Expansion.Until.Restored
    Log: Continuum.append("coherence_audit", this.Pulse)
}
```

Coherence audits are written whether the Verify passes or fails. The provenance trail is complete — both successes and failures are recorded.

### Reading from Continuum

```genesis
Watch: Vessel.Financial_Monitor
# AOS automatically reads company#state into the Watch context
# Avatars have access to their memory#{agent_id} partition at deliberation start
```

Explicit reads are handled by the AOS runtime, which loads the relevant Continuum partitions into the deliberation context at the beginning of each Pulse. The Genesis program declares what state the Avatars are authorised to see; AOS loads it.

---

## AzureTableStorage as Current Implementation

The current implementation uses Azure Table Storage, a NoSQL key-value store with:
- Partition key + row key addressing
- Strong consistency within a partition
- Millisecond latency for point reads
- Efficient range queries within a partition

The `company#{entity}` naming convention maps directly to Azure Table Storage partition keys. Each logical partition in the Continuum declaration (`company#state`, `company#vision`) becomes a partition in the underlying Azure Table.

The Continuum declaration abstracts this implementation detail. The Genesis program declares the partitions it needs and the invariants they must uphold. The storage technology is a deployment concern, not a language concern.

---

## See Also

- [AOS Integration](aos-integration.md) — StateAuthority and how Avatars access Continuum
- [Language Specification](../spec/language-specification.md) — Section VIII: The Continuum
- [Resonance Formula](resonance-formula.md) — How decisions are scored before being persisted

---

**Continuum is not a database. It is the continuous memory of the running consciousness — the substrate of experience that makes a collection of Pulses into a life.**

**Copyright © 2026 ASI Saga**
