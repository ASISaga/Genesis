# Genesis Tools

This directory contains the ecosystem tools that make up the Genesis development environment.

## Available Tools

### 1. Unified CLI (`genesis.py`)

The main entry point for all Genesis ecosystem commands.

```bash
# Show help
python3 genesis.py --help

# Run a program
python3 genesis.py run program.gen

# Start REPL
python3 genesis.py repl

# Initialize project
python3 genesis.py init my-project

# Format code
python3 genesis.py fmt file.gen

# Lint code  
python3 genesis.py lint file.gen

# Package management
python3 genesis.py pkg install avatar-templates
```

**Features:**
- Unified interface for all tools
- Consistent command structure
- Built-in help and documentation

### 2. Genesis REPL (`genesis_repl.py`)

Interactive Read-Eval-Print Loop for experimenting with Genesis code.

```bash
# Start REPL
python3 genesis_repl.py

# Or via unified CLI
python3 genesis.py repl
```

**Features:**
- Line-by-line execution
- Multi-line input support
- Command history (saved to `~/.genesis_history`)
- Real-time resonance feedback
- Load and execute .gen files
- Inspect loaded entities (`:show covenants`, `:show avatars`, etc.)
- Interactive commands (`:help`, `:reset`, `:load`, etc.)

**Commands:**
- `:help` - Show help
- `:exit`, `:quit` - Exit REPL
- `:reset` - Reset interpreter state
- `:show <type>` - Show covenants, avatars, or domains
- `:load <file>` - Load a .gen file
- `:clear` - Clear screen

### 3. Package Manager (`genesis_pkg.py`)

Manage Genesis packages and project dependencies.

```bash
# Initialize project
python3 genesis_pkg.py init

# Install package
python3 genesis_pkg.py install avatar-templates

# List installed packages
python3 genesis_pkg.py list

# Search registry
python3 genesis_pkg.py search ethics

# Publish package
python3 genesis_pkg.py publish
```

**Features:**
- Project initialization with `genesis.manifest.json`
- Package installation (local and registry)
- Dependency management
- Project structure scaffolding
- Package search and discovery
- Package publishing (to GenesisHub registry)

**Project Structure Created:**
```
my-project/
├── genesis.manifest.json
├── src/
│   └── main.gen
├── avatars/
├── domains/
└── tests/
```

### 4. Code Formatter (`genesis_fmt.py`)

Automatic code formatter for consistent Genesis style.

```bash
# Format a file
python3 genesis_fmt.py program.gen

# Format directory recursively
python3 genesis_fmt.py examples/

# Check formatting (no changes)
python3 genesis_fmt.py --check program.gen
```

**Features:**
- Automatic indentation (4 spaces)
- Consistent brace alignment
- Preserves empty lines
- Recursive directory formatting
- Check mode for CI/CD integration

**Formatting Rules:**
- 4-space indentation
- Opening braces on same line
- Closing braces dedented to parent level
- Consistent spacing around operators

### 5. Code Linter (`genesis_lint.py`)

Static analysis tool for code quality and best practices.

```bash
# Lint a file
python3 genesis_lint.py program.gen

# Lint directory
python3 genesis_lint.py examples/

# Show only errors
python3 genesis_lint.py --severity error program.gen
```

**Features:**
- Syntax validation
- Style checking
- Best practice enforcement
- Naming convention verification
- Configurable severity levels (error, warning, info)

**Checks Performed:**
- Trailing whitespace (W001)
- Tabs vs spaces (W002)
- Missing Covenants (W003)
- Naming conventions (I001)
- Line length (I002)
- Balanced braces (E001)

### 6. Original CLI (`../src/genesis_cli.py`)

Direct program execution (standalone).

```bash
# Run a Genesis program
python3 ../src/genesis_cli.py program.gen

# Verbose mode
python3 ../src/genesis_cli.py --verbose program.gen
```

**Features:**
- Direct program execution
- Verbose logging
- Runtime integration
- Error reporting

## Installation

All tools are ready to use directly from the repository:

```bash
# Clone repository
git clone https://github.com/ASISaga/Genesis.git
cd Genesis

# Tools are immediately available
python3 tools/genesis.py --version
```

For easier access, you can add to your PATH:

```bash
# Add to ~/.bashrc or ~/.zshrc
export PATH="/path/to/Genesis/tools:$PATH"
alias genesis='python3 /path/to/Genesis/tools/genesis.py'

# Then use as:
genesis run program.gen
genesis repl
```

## Tool Development

### Adding a New Tool

1. Create `tools/genesis_newtool.py`
2. Implement the tool functionality
3. Add to unified CLI in `genesis.py`
4. Update this README
5. Add tests

### Testing Tools

```bash
# Test unified CLI
python3 genesis.py --help

# Test REPL
echo ':exit' | python3 genesis_repl.py

# Test package manager
python3 genesis_pkg.py list

# Test formatter
python3 genesis_fmt.py --check examples/

# Test linter
python3 genesis_lint.py examples/
```

## Configuration

### Global Config

Tools use `~/.genesis/` for configuration:

```
~/.genesis/
├── config.json           # Global settings
├── packages/            # Installed packages
└── .genesis_history     # REPL history (in home dir)
```

### Project Config

Each project has `genesis.manifest.json`:

```json
{
  "name": "project-name",
  "version": "0.1.0",
  "genesis_version": ">=1.0.0",
  "dependencies": {},
  "dev_dependencies": {}
}
```

## Contributing

Contributions to Genesis tools are welcome! See [../CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines.

### Tool Guidelines

- Follow Python best practices (PEP 8)
- Include comprehensive help text
- Provide clear error messages
- Support both file and directory inputs
- Be consistent with existing tools
- Add unit tests for new functionality

## Support

- **Documentation**: [Genesis Documentation](../docs/README.md)
- **Issues**: [GitHub Issues](https://github.com/ASISaga/Genesis/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ASISaga/Genesis/discussions)

---

**Copyright © 2026 ASI Saga**
