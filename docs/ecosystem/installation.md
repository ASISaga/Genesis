# Genesis Ecosystem Installation & Setup Guide

This guide walks you through installing and setting up the complete Genesis ecosystem.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git (for cloning the repository)

## Installation

### Option 1: From Source (Current Method)

```bash
# Clone the repository
git clone https://github.com/ASISaga/Genesis.git
cd Genesis

# Verify Python version
python3 --version

# The ecosystem is ready to use!
```

### Option 2: Via pip (Future)

```bash
# Once published to PyPI
pip install genesis-lang

# Verify installation
genesis --version
```

## Verifying Installation

Test that all ecosystem tools are working:

```bash
# Test the unified CLI
python3 tools/genesis.py --version

# Test running a program
python3 tools/genesis.py run examples/hello-world.gen

# Test the REPL (exit with Ctrl+D or :exit)
python3 tools/genesis.py repl

# Test the linter
python3 tools/genesis.py lint examples/

# Test the formatter
python3 tools/genesis.py fmt examples/ --check

# Test package manager
python3 tools/genesis.py pkg list
```

## Creating Your First Project

Initialize a new Genesis project:

```bash
# Create project directory
mkdir my-asi-project
cd my-asi-project

# Initialize the project
python3 /path/to/Genesis/tools/genesis.py init

# Project structure created:
# my-asi-project/
# ├── genesis.manifest.json   # Project metadata
# ├── src/
# │   └── main.gen           # Main program
# ├── avatars/               # Custom avatars
# ├── domains/               # Custom domains
# └── tests/                 # Test files
```

## Using the Standard Library

The Genesis standard library provides pre-built Avatars, Covenants, and Domains:

```genesis
# In your .gen file
Import stdlib.avatars.Marcus_Aurelius
Import stdlib.covenants.Humanity_Eternal

Pantheon "My_Council" {
    Avatar "Stoic" uses stdlib.Marcus_Aurelius {
        Aura: "Inner_Discipline"
    }
}
```

Browse available components:

```bash
# View standard library
ls -R stdlib/
```

## Setting Up Your IDE

### VS Code (Recommended)

1. Install the Genesis extension (future):
   ```bash
   # From VS Code marketplace
   code --install-extension asisaga.genesis
   ```

2. Or use basic syntax highlighting:
   - Create `.vscode/settings.json` in your project:
   ```json
   {
     "files.associations": {
       "*.gen": "javascript"
     }
   }
   ```

### Other Editors

For Vim, Emacs, Sublime, etc., associate `.gen` files with a similar declarative language for basic syntax highlighting.

## Command Reference

### Genesis CLI

```bash
# Run a program
genesis run program.gen

# Start interactive REPL
genesis repl

# Initialize project
genesis init [path]

# Format code
genesis fmt <files>           # Format files
genesis fmt --check <files>   # Check formatting

# Lint code
genesis lint <files>
genesis lint --severity error <files>

# Package manager
genesis pkg init              # Initialize with manifest
genesis pkg install <name>    # Install package
genesis pkg list              # List installed
genesis pkg search <query>    # Search registry
genesis pkg publish           # Publish package
```

### Direct Tool Usage

You can also call tools directly:

```bash
python3 src/genesis_cli.py program.gen
python3 tools/genesis_repl.py
python3 tools/genesis_pkg.py init
python3 tools/genesis_fmt.py files/
python3 tools/genesis_lint.py files/
```

## Environment Configuration

### Genesis Config Directory

Genesis creates a config directory at `~/.genesis/`:

```
~/.genesis/
├── config.json        # Global configuration
└── packages/          # Installed packages
```

### Project Manifest

Each project has a `genesis.manifest.json`:

```json
{
  "name": "my-project",
  "version": "0.1.0",
  "description": "A Genesis ASI project",
  "genesis_version": ">=1.0.0",
  "dependencies": {
    "avatar-templates": "1.0.0"
  },
  "avatars": [],
  "domains": [],
  "covenants": []
}
```

## Troubleshooting

### Module Not Found Errors

If you get import errors, ensure Python can find the modules:

```bash
# Add Genesis to your Python path
export PYTHONPATH="/path/to/Genesis/src:/path/to/Genesis/tools:$PYTHONPATH"
```

### Permission Errors

Make tools executable:

```bash
chmod +x tools/*.py
```

### REPL Issues

If REPL doesn't save history, check:

```bash
# Ensure home directory is writable
touch ~/.genesis_history
```

## Next Steps

1. **Read the Tutorials**: See [tutorials/](../tutorials/README.md)
2. **Explore Examples**: Check [examples/](../../examples/README.md)
3. **Review Documentation**: Browse [docs/](../README.md)
4. **Join the Community**: Visit [GitHub Discussions](https://github.com/ASISaga/Genesis/discussions)

## Getting Help

- **Documentation**: [https://github.com/ASISaga/Genesis](https://github.com/ASISaga/Genesis)
- **Issues**: [GitHub Issues](https://github.com/ASISaga/Genesis/issues)
- **Discussions**: [GitHub Discussions](https://github.com/ASISaga/Genesis/discussions)

---

**Copyright © 2026 ASI Saga**
