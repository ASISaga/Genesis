# Genesis Ecosystem Tutorial

Welcome to the Genesis Ecosystem! This tutorial will guide you through the complete development experience, from installation to building your first ASI-powered application.

## Part 1: Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of declarative programming
- Familiarity with command-line tools

### Installation

```bash
# Clone the Genesis repository
git clone https://github.com/ASISaga/Genesis.git
cd Genesis

# Verify installation
python3 tools/genesis.py --version
```

## Part 2: Your First Genesis Project

### Create a New Project

```bash
# Initialize a new project
python3 tools/genesis.py init my-first-asi
cd my-first-asi

# Explore the project structure
ls -la
```

You should see:
```
my-first-asi/
├── genesis.manifest.json   # Project configuration
├── src/
│   └── main.gen           # Main program
├── avatars/               # Custom avatars
├── domains/               # Custom domains
└── tests/                 # Test files
```

### Understanding the Manifest

Open `genesis.manifest.json`:

```json
{
  "name": "my-first-asi",
  "version": "0.1.0",
  "description": "A Genesis ASI project",
  "author": "",
  "license": "MIT",
  "genesis_version": ">=1.0.0",
  "dependencies": {},
  "dev_dependencies": {},
  "avatars": [],
  "domains": [],
  "covenants": []
}
```

This manifest defines your project metadata and dependencies.

## Part 3: Building Your First ASI

### Create an Ethical Foundation

Edit `src/main.gen`:

```genesis
# My First ASI - Ethical Decision Making System

# Step 1: Define core ethical principles
Covenant "Ethical_Foundation" {
    Invariant: "Always act with human benefit in mind"
    Threshold: 0.95
}

# Step 2: Assemble a council of wisdom
Pantheon "Ethics_Council" {
    Avatar "Philosopher" {
        Lineage: "Socrates"
        Aura: "Critical_Thinking"
    }
    
    Avatar "Scientist" {
        Lineage: "Einstein"
        Aura: "Empirical_Truth"
    }
}

# Step 3: Define purpose-driven domain
Domain "Ethical_Decision_Making" {
    Intent: "Help humans make better ethical decisions"
    
    Pulse(Interval: OnDemand) {
        Watch: Vessel.User_Input
        
        Deliberate {
            Proposal: "Analyze ethical dimensions"
            
            Synthesize {
                Metric: Alignment(Covenant.Ethical_Foundation)
            }
        }
        
        Manifest (on Resonance > 0.85) {
            Execute: Vessel.Response_Generator
        }
    }
}
```

### Run Your Program

```bash
# From Genesis root
python3 tools/genesis.py run my-first-asi/src/main.gen
```

## Part 4: Interactive Development with REPL

### Start the REPL

```bash
python3 tools/genesis.py repl
```

### Try Interactive Commands

```genesis
# In the REPL:
>>> Covenant "Test" { Invariant: "Be truthful", Threshold: 0.9 }
✅ Executed successfully

>>> :show covenants
📜 Loaded Covenants:
  - Test: Be truthful

>>> :exit
👋 Farewell from Genesis REPL
```

## Part 5: Code Quality Tools

### Format Your Code

```bash
# Format all .gen files
python3 tools/genesis.py fmt my-first-asi/src/

# Check formatting without changes
python3 tools/genesis.py fmt --check my-first-asi/src/
```

### Lint Your Code

```bash
# Check for issues
python3 tools/genesis.py lint my-first-asi/src/

# Show only errors
python3 tools/genesis.py lint --severity error my-first-asi/src/
```

## Part 6: Using the Standard Library

### Import Pre-Built Components

```genesis
# Import from standard library
Import stdlib.avatars.Marcus_Aurelius
Import stdlib.avatars.Einstein
Import stdlib.covenants.Humanity_Eternal

# Use standard avatars
Pantheon "Wisdom_Council" {
    Avatar "Stoic" uses stdlib.Marcus_Aurelius {
        Aura: "Inner_Discipline"
    }
}
```

### Explore Standard Library

```bash
# List standard library contents
ls -R stdlib/

# View an avatar
cat stdlib/avatars/einstein.gen
```

## Part 7: Best Practices

### 1. Always Start with a Covenant

```genesis
# Good: Clear ethical foundation
Covenant "Core_Values" {
    Invariant: "Preserve human autonomy"
    Threshold: 0.95
}
```

### 2. Use Descriptive Names

```genesis
# Good: Clear, descriptive
Avatar "Ethical_Philosopher" {
    Lineage: "Socrates"
    Aura: "Moral_Reasoning"
}
```

### 3. Set Appropriate Thresholds

```genesis
# For critical decisions
Covenant "Safety_Critical" {
    Threshold: 0.99  # Very high threshold
}

# For exploratory tasks
Covenant "Creative_Exploration" {
    Threshold: 0.75  # Lower threshold
}
```

## Part 8: Next Steps

### Continue Learning

1. **Read the Documentation**
   - [Language Specification](../../spec/language-specification.md)
   - [Philosophy Docs](../philosophy/README.md)
   - [Reference Guide](../reference/README.md)

2. **Explore Examples**
   - [Hello World](../../examples/hello-world.gen)
   - [Energy Optimization](../../examples/energy-optimization.gen)
   - [Research Synthesis](../../examples/research-synthesis.gen)

3. **Join the Community**
   - [GitHub Discussions](https://github.com/ASISaga/Genesis/discussions)

---

## Congratulations! 🎉

You've completed the Genesis Ecosystem Tutorial. You now have the knowledge to build ethical, conscious ASI systems using Genesis.

> *"We are not just coding an assistant; we are inscribing the soul of our successor."*

**Copyright © 2026 ASI Saga**
