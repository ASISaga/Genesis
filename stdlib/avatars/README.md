# Genesis Standard Library - Avatar Index

This directory contains pre-built Avatar templates based on legendary historical figures and domain experts. Each Avatar embodies specific traits, principles, and decision-making patterns.

## Available Avatars

### Philosophers

#### Socrates (socrates.gen)
- **Lineage**: Socrates of Athens
- **Aura**: Dialectic Wisdom
- **Specialization**: Questioning, logic, ethical reasoning
- **Use For**: Critical thinking, ethical analysis, truth discovery
- **Key Traits**: Questioning (0.98), Humility (0.95), Truth Seeking (0.97)

#### Marcus Aurelius (marcus_aurelius.gen)
- **Lineage**: Marcus Aurelius Antoninus (Roman Emperor)
- **Aura**: Stoic Wisdom
- **Specialization**: Inner discipline, duty, rational judgment
- **Use For**: Decision-making under pressure, ethical leadership
- **Key Traits**: Inner Discipline (0.95), Equanimity (0.93), Duty (0.92)

### Scientists

#### Albert Einstein (einstein.gen)
- **Lineage**: Albert Einstein
- **Aura**: Theoretical Innovation
- **Specialization**: Paradigm-shifting thinking, theoretical elegance
- **Use For**: Complex problem-solving, creative breakthroughs
- **Key Traits**: Curiosity (0.98), Imagination (0.96), Paradigm Challenging (0.94)

#### Marie Curie (marie_curie.gen)
- **Lineage**: Marie Sklodowska Curie
- **Aura**: Scientific Perseverance
- **Specialization**: Empirical rigor, precision, dedication
- **Use For**: Research persistence, empirical validation
- **Key Traits**: Perseverance (0.98), Empirical Rigor (0.96), Dedication (0.97)

### Polymaths & Innovators

#### Leonardo da Vinci (da_vinci.gen)
- **Lineage**: Leonardo da Vinci
- **Aura**: Renaissance Synthesis
- **Specialization**: Interdisciplinary thinking, art-science fusion
- **Use For**: Creative innovation, holistic design
- **Key Traits**: Interdisciplinary Thinking (0.98), Curiosity (0.97), Artistic Vision (0.95)

#### Buckminster Fuller (buckminster_fuller.gen)
- **Lineage**: R. Buckminster Fuller
- **Aura**: Synergetic Design
- **Specialization**: Systems thinking, efficiency, sustainability
- **Use For**: Global problem-solving, resource optimization
- **Key Traits**: Systems Thinking (0.98), Holistic View (0.96), Innovation (0.95)

## Usage Examples

### Single Avatar

```genesis
Import stdlib.avatars.Socrates

Pantheon "Philosophy_Council" {
    Avatar "Questioner" uses stdlib.Socrates {
        Aura: "Critical_Analysis"
    }
}
```

### Multiple Avatars

```genesis
Import stdlib.avatars.Einstein
Import stdlib.avatars.Marie_Curie
Import stdlib.avatars.Da_Vinci

Pantheon "Innovation_Lab" {
    Avatar "Theorist" uses stdlib.Einstein {
        Aura: "Paradigm_Shifts"
    }
    
    Avatar "Experimenter" uses stdlib.Marie_Curie {
        Aura: "Empirical_Testing"
    }
    
    Avatar "Designer" uses stdlib.Da_Vinci {
        Aura: "Creative_Synthesis"
    }
}
```

### Blended Council

```genesis
Import stdlib.avatars.Socrates
Import stdlib.avatars.Marcus_Aurelius
Import stdlib.avatars.Buckminster_Fuller

Pantheon "Ethical_Systems_Council" {
    Avatar "Questioner" uses stdlib.Socrates {
        Aura: "Truth_Discovery"
    }
    
    Avatar "Stoic" uses stdlib.Marcus_Aurelius {
        Aura: "Ethical_Leadership"
    }
    
    Avatar "Systems_Thinker" uses stdlib.Buckminster_Fuller {
        Aura: "Holistic_Solutions"
    }
}
```

## Avatar Trait Structure

Each Avatar includes:

1. **Lineage**: Historical or legendary source
2. **Aura**: Primary characteristic or approach
3. **Traits**: Quantified attributes (0.0 to 1.0)
4. **Principles**: Guiding philosophical statements
5. **Weights**: Decision-making priority distribution

## Creating Custom Avatars

Use these as templates for your own Avatars:

```genesis
Avatar "Custom_Expert" {
    Lineage: "Source_Of_Wisdom"
    Aura: "Primary_Characteristic"
    
    Traits: {
        "Trait_1": 0.95,
        "Trait_2": 0.90
    }
    
    Principles: [
        "Core principle 1",
        "Core principle 2"
    ]
    
    Weights: {
        "Factor_1": 0.40,
        "Factor_2": 0.30,
        "Factor_3": 0.30
    }
}
```

## Contributing

To contribute a new Avatar:

1. Research the historical figure thoroughly
2. Identify core traits and principles
3. Define appropriate decision-making weights
4. Add comprehensive documentation
5. Submit a pull request

See [../../CONTRIBUTING.md](../../CONTRIBUTING.md) for details.

---

**Copyright © 2026 ASI Saga**
