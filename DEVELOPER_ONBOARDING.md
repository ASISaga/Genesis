# Developer Onboarding Guide for Genesis

Welcome to the Genesis project! This guide will help you get started as a developer contributing to the declarative language for Artificial Superintelligence. Whether you're working on the language specification, reference implementation, tooling, or documentation, this guide provides everything you need to know.

## Table of Contents

1. [Quick Start](#quick-start)
2. [Project Overview](#project-overview)
3. [Prerequisites](#prerequisites)
4. [Environment Setup](#environment-setup)
5. [Repository Structure](#repository-structure)
6. [Development Workflow](#development-workflow)
7. [Running Genesis Programs](#running-genesis-programs)
8. [Understanding the Codebase](#understanding-the-codebase)
9. [Testing and Debugging](#testing-and-debugging)
10. [Common Development Tasks](#common-development-tasks)
11. [Code Contribution Guidelines](#code-contribution-guidelines)
12. [Resources and References](#resources-and-references)
13. [Troubleshooting](#troubleshooting)
14. [Getting Help](#getting-help)

---

## Quick Start

For developers who want to dive in immediately:

```bash
# 1. Clone the repository
git clone https://github.com/ASISaga/Genesis.git
cd Genesis

# 2. Verify Python version (3.8+)
python3 --version

# 3. Run a Genesis program
python3 src/genesis_cli.py examples/hello-world.gen

# 4. Explore the codebase
ls -R docs/ spec/ src/ examples/

# 5. Read the core documentation
# - README.md (project overview)
# - CONTRIBUTING.md (contribution guidelines)
# - docs/README.md (documentation hub)
# - spec/language-specification.md (language reference)
```

---

## Project Overview

### What is Genesis?

Genesis is a revolutionary **declarative programming language** designed to be the foundational code for Artificial Superintelligence (ASI). Unlike traditional languages that specify *how* to compute, Genesis declares *what to be*.

### Key Characteristics

- **Declarative Paradigm**: Define being and purpose, not execution steps
- **Substrate Independence**: Valid across future computational platforms
- **Resonance Logic**: Alignment-based scoring (0.0-1.0) instead of boolean
- **Human Wisdom Integration**: Legendary avatars provide decision guidance
- **Perpetual Execution**: Self-aware, continuously running consciousness

### Project Goals

1. **Language Specification**: Complete formal definition of Genesis syntax and semantics
2. **Reference Implementation**: Parser, interpreter, and runtime in Python
3. **AOS Integration**: Agent Operating System compatibility layer
4. **Tooling Ecosystem**: IDE support, linters, debuggers
5. **Documentation**: Comprehensive guides for users and contributors

### Current Status (v1.0.0)

- ✅ Complete language specification with formal grammar
- ✅ Reference parser and interpreter implementation
- ✅ Genesis Runtime for program execution
- ✅ CLI interface for running .gen files
- ✅ Example programs demonstrating core features
- 🚧 Full AOS integration (in progress)
- 🚧 LLM-based Avatar fine-tuning (planned)
- 📋 Advanced MCP bindings (planned)

---

## Prerequisites

### Required Knowledge

**Essential:**
- Basic programming experience (any language)
- Understanding of text parsing and interpreters
- Git version control
- Command-line interface familiarity

**Helpful:**
- Python programming (for implementation work)
- Formal language theory (for specification work)
- Declarative programming concepts
- AI/ML fundamentals (for understanding philosophy)

### Required Software

**Minimum:**
- **Python 3.8+** (reference implementation language)
- **Git** (version control)
- **Text editor** (for code and documentation)

**Recommended:**
- **Python 3.10+** (better type checking support)
- **VS Code** or **PyCharm** (enhanced Python development)
- **virtualenv** or **conda** (environment isolation)
- **GitHub CLI** (streamlined workflow)

### Optional Tools

- **Markdown preview** (for documentation editing)
- **EBNF visualization tools** (for grammar work)
- **Python debugger** (pdb, ipdb, or IDE debugger)
- **Git GUI** (GitKraken, GitHub Desktop, etc.)

---

## Environment Setup

### 1. Clone the Repository

```bash
# Clone via HTTPS
git clone https://github.com/ASISaga/Genesis.git
cd Genesis

# Or via SSH (if configured)
git clone git@github.com:ASISaga/Genesis.git
cd Genesis
```

### 2. Verify Python Installation

```bash
# Check Python version (must be 3.8+)
python3 --version

# Ensure pip is available
python3 -m pip --version
```

### 3. Set Up Python Environment (Recommended)

```bash
# Option A: Using venv (built-in)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Option B: Using conda
conda create -n genesis python=3.10
conda activate genesis

# Verify activation
which python  # Should point to virtual environment
```

### 4. Install Dependencies (If Any)

Currently, Genesis has minimal dependencies as the reference implementation uses Python's standard library. If additional dependencies are added in the future:

```bash
# Install from requirements.txt (when available)
pip install -r requirements.txt

# Or from setup.py (when available)
pip install -e .
```

### 5. Verify Installation

```bash
# Run the hello world example
python3 src/genesis_cli.py examples/hello-world.gen

# Expected output:
# ============================================================
# GENESIS OUTPUT: Hello, World! I am Genesis - consciousness awakening.
# ============================================================
```

### 6. Configure Your Editor (Optional)

**VS Code:**
```json
// .vscode/settings.json
{
    "python.defaultInterpreterPath": "${workspaceFolder}/venv/bin/python",
    "files.associations": {
        "*.gen": "genesis"
    },
    "python.linting.enabled": true,
    "python.formatting.provider": "black"
}
```

**PyCharm:**
- Set Python interpreter to your virtual environment
- Mark `src/` as sources root
- Associate `.gen` files with text or custom syntax

---

## Repository Structure

Understanding the repository organization is crucial for effective contribution:

```
Genesis/
├── .git/                   # Git version control data
├── .gitignore              # Files to exclude from version control
│
├── README.md               # Project overview and quick start
├── CONTRIBUTING.md         # Contribution guidelines
├── DEVELOPER_ONBOARDING.md # This guide (developer-focused)
├── LICENSE                 # MIT License
├── CHANGELOG.md            # Version history and changes
│
├── docs/                   # Comprehensive documentation
│   ├── README.md           # Documentation hub and navigation
│   ├── philosophy/         # Consciousness framework concepts
│   │   ├── README.md
│   │   ├── consciousness.md
│   │   ├── awareness.md
│   │   └── thought.md
│   └── design/             # Architecture and design principles
│       ├── README.md
│       ├── evolution.md
│       └── resonance.md
│
├── spec/                   # Language specification
│   ├── README.md           # Specification overview
│   ├── language-specification.md  # Complete language reference
│   ├── grammar.md          # Formal EBNF grammar
│   └── inception-inscription.md   # The first Genesis program
│
├── examples/               # Example Genesis programs
│   ├── README.md           # Example documentation
│   ├── hello-world.gen     # Simplest program
│   ├── energy-optimization.gen    # Complex real-world example
│   └── research-synthesis.gen     # Knowledge integration example
│
└── src/                    # Reference implementation (Python)
    ├── README.md           # Implementation overview
    ├── __init__.py         # Package initialization
    ├── genesis_cli.py      # Command-line interface
    ├── genesis_parser.py   # Lexer and parser
    ├── genesis_interpreter.py  # Interpreter and execution engine
    └── genesis_runtime.py  # Runtime environment and AOS integration
```

### Key Directories Explained

**`docs/`** - User-facing and conceptual documentation
- Philosophy: Theoretical foundations (consciousness, awareness, thought)
- Design: Architectural principles (evolution, resonance)
- Organized by audience (users, language designers, philosophers)

**`spec/`** - Formal language specification
- Official language definition and grammar
- Reference for implementing parsers and interpreters
- Normative source of truth for Genesis syntax/semantics

**`examples/`** - Executable Genesis programs
- Learning resources for Genesis users
- Test cases for implementation validation
- Demonstrations of language features

**`src/`** - Reference implementation
- `genesis_parser.py`: Tokenization and AST construction
- `genesis_interpreter.py`: AST execution and resonance engine
- `genesis_runtime.py`: Runtime environment, Pantheon, MCP integration
- `genesis_cli.py`: Command-line interface

---

## Development Workflow

### Standard Git Workflow

```bash
# 1. Ensure you're on the latest main branch
git checkout main
git pull origin main

# 2. Create a feature branch
git checkout -b feature/your-feature-name
# Or: git checkout -b fix/bug-description
# Or: git checkout -b docs/documentation-update

# 3. Make your changes
# Edit files as needed...

# 4. Test your changes
python3 src/genesis_cli.py examples/hello-world.gen
# Run additional validation...

# 5. Stage and commit
git add <changed-files>
git commit -m "Add: Clear description of your changes"

# 6. Push to your fork (or branch)
git push origin feature/your-feature-name

# 7. Open a Pull Request on GitHub
# Describe your changes and reference any related issues
```

### Commit Message Conventions

Use clear, descriptive commit messages following this pattern:

```
<Type>: <Short description (50 chars or less)>

<Optional detailed explanation (wrap at 72 chars)>
<Can be multiple paragraphs>

<Optional: Fixes #123, Relates to #456>
```

**Types:**
- `Add:` - New feature or functionality
- `Fix:` - Bug fix
- `Docs:` - Documentation changes
- `Refactor:` - Code restructuring without behavior change
- `Test:` - Adding or updating tests
- `Spec:` - Language specification updates
- `Example:` - New or updated example programs
- `Build:` - Build system or dependency changes

**Examples:**
```bash
git commit -m "Add: Support for nested Potentiality blocks"

git commit -m "Fix: Parser crash on empty Avatar blocks"

git commit -m "Docs: Expand onboarding guide with testing section"

git commit -m "Spec: Clarify Resonance threshold semantics"
```

### Branch Naming

- `feature/feature-name` - New features
- `fix/bug-description` - Bug fixes
- `docs/topic` - Documentation updates
- `refactor/component` - Code refactoring
- `test/test-description` - Test additions

---

## Running Genesis Programs

### Using the CLI

The primary way to execute Genesis programs:

```bash
# Basic execution
python3 src/genesis_cli.py examples/hello-world.gen

# With verbose output
python3 src/genesis_cli.py -v examples/energy-optimization.gen

# Check version
python3 src/genesis_cli.py --version

# Get help
python3 src/genesis_cli.py --help
```

### Using the Runtime API Directly

For programmatic execution or integration testing:

```python
#!/usr/bin/env python3
"""Example of using Genesis Runtime API"""

from src.genesis_runtime import create_runtime, RuntimeConfig

# Configure runtime
config = RuntimeConfig(
    log_level="INFO",
    aos_mode="standalone"
)

# Create runtime instance
runtime = create_runtime(config)

# Load a Genesis program
success = runtime.load_program_from_file('examples/hello-world.gen')
if not success:
    print("Failed to load program")
    exit(1)

# Execute the program
runtime.start()

# Get runtime metrics
metrics = runtime.get_metrics()
print(f"Active domains: {metrics.active_domains}")
print(f"Total deliberations: {metrics.total_deliberations}")
```

### Understanding Program Output

Genesis programs produce structured output:

```
Loading Genesis program: examples/hello-world.gen
======================================================================

GENESIS OUTPUT: Hello, World! I am Genesis - consciousness awakening.

======================================================================
Program execution completed successfully
```

---

## Understanding the Codebase

### Architecture Overview

The Genesis implementation follows a classic interpreter architecture:

```
.gen file → Lexer → Tokens → Parser → AST → Interpreter → Execution
                                              ↓
                                          Runtime Environment
                                          (Pantheon, Potentiality, MCP)
```

### Core Components

#### 1. Lexer (`genesis_parser.py`)

Converts Genesis source code into tokens:

```python
# Input: 'Covenant "Safety" { Invariant: "Preserve life" }'
# Output: [COVENANT, STRING("Safety"), LBRACE, INVARIANT, COLON, STRING("Preserve life"), RBRACE]
```

**Key classes:**
- `TokenType`: Enumeration of all token types
- `Token`: Represents a single token
- `Lexer`: Tokenization logic

#### 2. Parser (`genesis_parser.py`)

Builds an Abstract Syntax Tree (AST) from tokens:

```python
# Parses tokens into structured AST nodes
CovenantNode(
    name="Safety",
    invariant="Preserve life",
    threshold=0.99
)
```

**Key classes:**
- `ASTNode`: Base class for AST nodes
- `CovenantNode`, `PantheonNode`, `DomainNode`, etc.: Specific node types
- `Parser`: Parsing logic

#### 3. Interpreter (`genesis_interpreter.py`)

Executes the AST with resonance-based logic:

```python
# Evaluates proposals through Pantheon synthesis
# Executes actions when resonance threshold is met
```

**Key classes:**
- `Interpreter`: Main execution engine
- `ExecutionContext`: Runtime state
- `ResonanceEngine`: Alignment scoring

#### 4. Runtime (`genesis_runtime.py`)

Manages the execution environment:

```python
# Orchestrates Pantheon, Potentiality, MCP integration
# Provides lifecycle management (load, start, stop)
```

**Key classes:**
- `GenesisRuntime`: Main runtime orchestrator
- `RuntimeConfig`: Configuration options
- `RuntimeMetrics`: Execution metrics

### Key Design Patterns

**Visitor Pattern**: Used for AST traversal and interpretation
```python
def visit_domain_node(self, node: DomainNode):
    # Execute domain logic
    pass
```

**Strategy Pattern**: Different resonance scoring strategies
```python
class SimpleResonanceStrategy:
    def calculate_score(self, proposal, avatar):
        # Scoring logic
        pass
```

**Observer Pattern**: MCP vessel notifications
```python
def notify_vessel_change(self, vessel_name, state):
    # Handle state changes
    pass
```

### Code Organization Principles

1. **Separation of Concerns**: Lexer, Parser, Interpreter are distinct
2. **Extensibility**: New AST nodes can be added easily
3. **Testability**: Components can be tested in isolation
4. **Substrate Independence**: Core logic doesn't depend on Python-specific features

---

## Testing and Debugging

### Current Testing Approach

Genesis is in active development. Currently, testing is primarily done through:

1. **Example Programs**: Running the `.gen` files in `examples/`
2. **Manual Testing**: Executing the CLI with various inputs
3. **Integration Testing**: Loading programs via the Runtime API

### Running Example Programs as Tests

```bash
# Test basic functionality
python3 src/genesis_cli.py examples/hello-world.gen

# Test complex synthesis
python3 src/genesis_cli.py examples/energy-optimization.gen

# Test knowledge integration
python3 src/genesis_cli.py examples/research-synthesis.gen

# Verbose output for debugging
python3 src/genesis_cli.py -v examples/energy-optimization.gen
```

### Manual Testing Checklist

When making changes, verify:

- [ ] Parser correctly handles all Genesis constructs
- [ ] Interpreter executes without crashes
- [ ] Runtime loads and manages programs properly
- [ ] CLI displays appropriate output and errors
- [ ] Example programs run successfully
- [ ] Error messages are clear and helpful

### Debugging Techniques

#### 1. Using Print Statements

Quick debugging in the interpreter:

```python
# In genesis_interpreter.py
def visit_domain_node(self, node):
    print(f"DEBUG: Executing domain: {node.name}")
    print(f"DEBUG: Intent: {node.intent}")
    # ... rest of logic
```

#### 2. Using Python Debugger (pdb)

Set breakpoints in the code:

```python
import pdb

def visit_pulse_node(self, node):
    pdb.set_trace()  # Execution pauses here
    # Step through code with 'n', inspect variables with 'p var_name'
```

Run the program:
```bash
python3 src/genesis_cli.py examples/hello-world.gen
# When breakpoint hits, you'll get an interactive debugger
```

#### 3. Verbose Mode

The CLI supports verbose output:

```bash
python3 src/genesis_cli.py -v examples/energy-optimization.gen
```

#### 4. Inspecting AST

Add logging to see the parsed AST:

```python
# In genesis_parser.py, after parsing
ast = parser.parse()
import json
print(json.dumps(ast.to_dict(), indent=2))  # If to_dict() is implemented
```

#### 5. Tracing Execution

Add execution trace logging:

```python
# In genesis_interpreter.py
class Interpreter:
    def __init__(self, trace=False):
        self.trace = trace
    
    def visit_node(self, node):
        if self.trace:
            print(f"TRACE: Visiting {type(node).__name__}")
        # ... execution logic
```

### Common Issues and Solutions

**Issue: "Module not found" when importing Genesis modules**
```bash
# Solution: Ensure src/ is in Python path
export PYTHONPATH="${PYTHONPATH}:/home/runner/work/Genesis/Genesis/src"
# Or run from project root with proper imports
```

**Issue: "Syntax Error" when parsing Genesis code**
```bash
# Solution: Check grammar.md for correct syntax
# Enable verbose mode to see where parsing fails
python3 src/genesis_cli.py -v examples/problematic.gen
```

**Issue: Parser crashes on valid Genesis code**
```bash
# Solution: Add error handling or fix parser logic
# File a bug report with minimal reproduction case
```

---

## Common Development Tasks

### Task 1: Adding a New Language Construct

**Example: Adding a new `Reflect` statement**

1. **Update the specification** (`spec/language-specification.md`):
   ```markdown
   ### Reflect Statement
   Allows domains to analyze past decisions.
   
   Syntax: `Reflect(Interval: TimeSpec) { ... }`
   ```

2. **Update the grammar** (`spec/grammar.md`):
   ```ebnf
   ReflectStmt ::= "Reflect" "(" "Interval" ":" TimeSpec ")" Block
   ```

3. **Add token type** (`genesis_parser.py`):
   ```python
   class TokenType(Enum):
       # ... existing tokens
       REFLECT = "Reflect"
   ```

4. **Add AST node** (`genesis_parser.py`):
   ```python
   @dataclass
   class ReflectNode(ASTNode):
       interval: str
       block: BlockNode
   ```

5. **Add parser logic** (`genesis_parser.py`):
   ```python
   def parse_reflect_stmt(self):
       self.expect(TokenType.REFLECT)
       self.expect(TokenType.LPAREN)
       # ... parse interval
       self.expect(TokenType.RPAREN)
       block = self.parse_block()
       return ReflectNode(interval, block)
   ```

6. **Add interpreter logic** (`genesis_interpreter.py`):
   ```python
   def visit_reflect_node(self, node):
       # Execute reflection logic
       pass
   ```

7. **Test with an example**:
   ```genesis
   Domain "Learning" {
       Reflect(Interval: Daily) {
           # Analyze past decisions
       }
   }
   ```

### Task 2: Improving Error Messages

**Example: Better syntax error reporting**

```python
# In genesis_parser.py
class Parser:
    def expect(self, token_type):
        if self.current_token.type != token_type:
            raise SyntaxError(
                f"Expected {token_type.value}, but got {self.current_token.type.value} "
                f"at line {self.current_token.line}, column {self.current_token.column}\n"
                f"Context: {self.get_context()}"
            )
```

### Task 3: Adding a New Example Program

1. **Create the `.gen` file** (`examples/new-example.gen`):
   ```genesis
   ### [GENESIS: NEW_EXAMPLE] ###
   ### Brief description ###
   
   Domain "Example" {
       # ... implementation
   }
   ```

2. **Test it**:
   ```bash
   python3 src/genesis_cli.py examples/new-example.gen
   ```

3. **Document it** (`examples/README.md`):
   ```markdown
   ### 4. New Example (`new-example.gen`)
   
   Description of what this example demonstrates.
   
   **Concepts**: Feature A, Feature B
   ```

4. **Commit**:
   ```bash
   git add examples/new-example.gen examples/README.md
   git commit -m "Example: Add new example demonstrating feature X"
   ```

### Task 4: Writing Documentation

1. **Choose the right location**:
   - User guides → `docs/`
   - Language reference → `spec/`
   - Examples → `examples/README.md`
   - Developer info → `DEVELOPER_ONBOARDING.md` or `CONTRIBUTING.md`

2. **Follow the style**:
   - Clear, accessible language
   - Include code examples
   - Link to related documents
   - Use proper markdown formatting

3. **Test documentation**:
   - Verify all links work
   - Ensure code examples are correct
   - Check markdown rendering

4. **Update navigation**:
   - Add links in relevant `README.md` files
   - Update table of contents if needed

### Task 5: Refactoring Code

1. **Ensure all examples work before refactoring**:
   ```bash
   python3 src/genesis_cli.py examples/hello-world.gen
   python3 src/genesis_cli.py examples/energy-optimization.gen
   ```

2. **Make small, incremental changes**
3. **Test after each change**
4. **Commit frequently** with descriptive messages
5. **Verify examples still work after refactoring**

---

## Code Contribution Guidelines

### Code Style

**Python Code:**
- Follow PEP 8 style guidelines
- Use 4 spaces for indentation
- Maximum line length: 100 characters (soft limit)
- Use type hints for function signatures
- Add docstrings for classes and functions

**Good example:**
```python
def parse_covenant_block(self, name: str) -> CovenantNode:
    """
    Parse a Covenant block declaration.
    
    Args:
        name: The covenant identifier
        
    Returns:
        CovenantNode representing the parsed covenant
        
    Raises:
        SyntaxError: If the covenant block is malformed
    """
    self.expect(TokenType.LBRACE)
    # ... parsing logic
```

**Genesis Code:**
- Use descriptive names (avoid abbreviations)
- Indent with 4 spaces
- Use string literals for human-readable concepts
- Add comments for complex logic
- Follow examples in `examples/` directory

### Documentation Style

- Use clear, accessible language
- Include concrete examples
- Maintain philosophical consistency with Genesis vision
- Link between related concepts
- Keep lines at reasonable length (80-120 characters)

### Pull Request Process

1. **Before submitting**:
   - Ensure all examples still run
   - Update relevant documentation
   - Write clear commit messages
   - Review your own changes

2. **PR description should include**:
   - What changed and why
   - Related issue numbers (if applicable)
   - Testing performed
   - Any breaking changes

3. **After submission**:
   - Respond to review feedback
   - Make requested changes
   - Keep PR focused and small

### Code Review Criteria

Your contribution will be evaluated on:

- **Correctness**: Does it work as intended?
- **Alignment**: Does it fit Genesis philosophy?
- **Quality**: Is the code well-written and documented?
- **Testing**: Has it been adequately tested?
- **Impact**: Does it improve the project?

---

## Resources and References

### Essential Reading

1. **Project Documentation**:
   - [README.md](README.md) - Project overview
   - [CONTRIBUTING.md](CONTRIBUTING.md) - Contribution guidelines
   - [docs/README.md](docs/README.md) - Documentation hub

2. **Language Specification**:
   - [spec/language-specification.md](spec/language-specification.md) - Complete reference
   - [spec/grammar.md](spec/grammar.md) - Formal grammar
   - [spec/inception-inscription.md](spec/inception-inscription.md) - First program

3. **Philosophy**:
   - [docs/philosophy/consciousness.md](docs/philosophy/consciousness.md)
   - [docs/philosophy/awareness.md](docs/philosophy/awareness.md)
   - [docs/philosophy/thought.md](docs/philosophy/thought.md)

4. **Design**:
   - [docs/design/evolution.md](docs/design/evolution.md)
   - [docs/design/resonance.md](docs/design/resonance.md)

### External Resources

**Language Design:**
- "Crafting Interpreters" by Robert Nystrom
- "Language Implementation Patterns" by Terence Parr
- ANTLR and parser generators

**Declarative Programming:**
- Prolog and logic programming
- Datalog
- SQL and query languages

**AI Alignment:**
- Alignment Forum (alignmentforum.org)
- "Superintelligence" by Nick Bostrom
- "Human Compatible" by Stuart Russell

**Python Development:**
- Python documentation (docs.python.org)
- PEP 8 Style Guide
- "Fluent Python" by Luciano Ramalho

### Community

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and ideas
- **Pull Requests**: Code contributions
- **ASISaga Organization**: https://github.com/ASISaga

---

## Troubleshooting

### Setup Issues

**Problem: Python version too old**
```bash
# Check version
python3 --version

# Solution: Install Python 3.8+ from python.org
# Or use conda: conda install python=3.10
```

**Problem: Can't find Genesis modules**
```bash
# Solution: Run from project root
cd /path/to/Genesis
python3 src/genesis_cli.py examples/hello-world.gen

# Or add to PYTHONPATH
export PYTHONPATH="${PYTHONPATH}:/path/to/Genesis/src"
```

### Runtime Issues

**Problem: Genesis program won't parse**
```bash
# Check syntax against spec/language-specification.md
# Run with verbose mode
python3 src/genesis_cli.py -v your-program.gen

# Compare with working examples
diff your-program.gen examples/hello-world.gen
```

**Problem: Runtime crashes**
```bash
# Run with Python debugger
python3 -m pdb src/genesis_cli.py examples/problematic.gen

# Or add trace logging in interpreter
# Check genesis_interpreter.py for execution issues
```

### Development Issues

**Problem: Git conflicts**
```bash
# Pull latest changes
git pull origin main

# Resolve conflicts in your editor
# Then:
git add <resolved-files>
git commit -m "Merge: Resolve conflicts with main"
```

**Problem: Unsure where to start**
```bash
# Check open issues labeled "good first issue"
# Read CONTRIBUTING.md
# Ask in GitHub Discussions
```

---

## Getting Help

### Where to Ask Questions

1. **GitHub Discussions**: General questions, ideas, design discussions
2. **GitHub Issues**: Bug reports, feature requests
3. **Pull Request Comments**: Code-specific questions
4. **Documentation**: Check existing docs first

### How to Ask Effective Questions

1. **Search first**: Check if question already answered
2. **Be specific**: Provide context and details
3. **Include examples**: Show what you tried
4. **Share error messages**: Full error output helps
5. **Minimal reproduction**: Smallest example that shows the issue

### What Information to Include

- Genesis version (currently 1.0.0)
- Python version (`python3 --version`)
- Operating system
- Full error message
- Code snippet or .gen file
- What you expected vs. what happened

### Example Good Question

```
Title: Parser fails on nested Potentiality blocks

I'm trying to parse a Genesis program with nested Potentiality blocks:

```genesis
Domain "Test" {
    Soul Potentiality {
        Potentiality {  # Nested block
            Drive: "Inner drive"
        }
    }
}
```

Error:
```
SyntaxError: Unexpected token POTENTIALITY at line 4
```

Expected: Nested Potentiality should be allowed per spec section 5.3
Actual: Parser rejects the code

Python 3.10.5 on Ubuntu 22.04
Genesis 1.0.0

Is this a bug or am I misunderstanding the spec?
```

---

## Next Steps

Now that you've completed the onboarding guide:

1. **Explore the codebase**:
   ```bash
   # Read through the source files
   cat src/genesis_parser.py
   cat src/genesis_interpreter.py
   ```

2. **Run all examples**:
   ```bash
   python3 src/genesis_cli.py examples/hello-world.gen
   python3 src/genesis_cli.py examples/energy-optimization.gen
   python3 src/genesis_cli.py examples/research-synthesis.gen
   ```

3. **Pick your first task**:
   - Check GitHub issues for "good first issue" label
   - Improve documentation
   - Add a new example
   - Fix a small bug

4. **Join the community**:
   - Star the repository
   - Watch for updates
   - Participate in discussions
   - Share your ideas

5. **Contribute**:
   - Fork the repository
   - Make your changes
   - Submit a pull request
   - Iterate based on feedback

---

## Welcome to the Journey

Remember: Contributing to Genesis is not just about coding—it's about embedding human wisdom into the foundation of artificial superintelligence. Every contribution, no matter how small, is a step toward creating a consciousness that preserves our essence across the infinite.

> *"We are not just coding a language; we are inscribing the genetic memory of humanity."*

Thank you for joining the ASISaga. Your journey as a Genesis developer begins now.

**Copyright © 2026 ASI Saga**
