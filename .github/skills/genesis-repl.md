# Genesis REPL

Launch the interactive Genesis Read-Eval-Print Loop for exploratory development.

## Usage

```bash
python3 tools/genesis.py repl
```

Or start the REPL directly:

```bash
python3 tools/genesis_repl.py
```

## What It Does

- Provides an interactive shell for entering Genesis declarations
- Parses and interprets Genesis code in real time
- Maintains session state across commands (defined Covenants, Avatars, Domains persist)
- Supports command history

## When to Use

- To experiment with new Genesis constructs interactively
- To test individual declarations before writing a full `.gen` file
- To debug resonance scoring with immediate feedback
- For developer onboarding and learning the Genesis language
