---
name: genesis-run
description: Execute Genesis programs using the reference interpreter to validate program correctness and test language features
self_learning: true
knowledge_base: .github/knowledge/genesis-run
---

# Genesis Run

Execute Genesis programs using the reference interpreter.

## Self-Learning Capabilities

This skill implements the Ouroboros evolution pattern and learns from each usage:

- **Performance Tracking**: All invocations are tracked in `.github/knowledge/genesis-run/metrics.yaml`
- **Pattern Learning**: Effective usage patterns are accumulated in `learnings.yaml`
- **Evolution Log**: Self-modifications are recorded in `evolution-log.yaml`
- **Context Awareness**: Usage contexts guide future improvements in `context.yaml`

The skill evolves through cycles defined in `.github/evolution/skill-evolution.gen`, continuously refining its instructions and examples based on real-world usage.


## Usage

```bash
python3 tools/genesis.py run <file.gen>
```

Or run directly via the CLI:

```bash
python3 src/genesis_cli.py <file.gen>
```

## What It Does

- Parses the `.gen` file into an Abstract Syntax Tree
- Interprets the AST using the resonance engine
- Executes Pulse cycles with avatar consensus scoring
- Outputs domain state, resonance scores, and manifestation results

## Example Programs

```bash
python3 tools/genesis.py run examples/hello-world.gen
python3 tools/genesis.py run examples/energy-optimization.gen
python3 tools/genesis.py run examples/research-synthesis.gen
python3 tools/genesis.py run examples/possibility-demo.gen
python3 tools/genesis.py run examples/compliant-ai-system.gen
```

## When to Use

- To validate that `.gen` programs execute correctly
- To test new language features end-to-end
- To verify that changes to the parser or interpreter don't break existing programs
- When dogfooding Genesis on itself for meta-programming validation
