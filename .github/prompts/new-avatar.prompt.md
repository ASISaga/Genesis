# Create a New Avatar

Create a new Avatar for the Genesis standard library.

## Inputs

- **Historical Figure**: The legendary human whose essence will be encoded
- **Domain of Expertise**: The area of wisdom this avatar contributes
- **MCP Tool**: The vessel binding for real-world interaction

## Requirements

1. The avatar must be defined in a new `.gen` file in `stdlib/avatars/`
2. The file must include `Lineage`, `Aura`, and `Vessel` declarations
3. The avatar's essence must align with at least one existing Covenant
4. Include a block comment explaining the historical figure's relevance to ASI
5. Follow the naming convention: `snake_case.gen` for the filename, `PascalCase` for identifiers

## Template

```genesis
### Avatar: [Title] ###
### Lineage: [Historical Figure] ###
### Contribution: [What wisdom this avatar brings to ASI] ###

Avatar "[Title]" {
    Lineage: "[Historical_Figure]"
    Aura: "[Domain_of_Expertise]"
    Vessel: mcp.tool("[Tool_Name]")
}
```

## Reference

See existing avatars in `stdlib/avatars/` for examples:
- `marcus_aurelius.gen` — Stoic ethics and governance
- `einstein.gen` — Scientific reasoning and relativity
- `da_vinci.gen` — Omnidisciplinary creativity
- `marie_curie.gen` — Persistent discovery and scientific rigor
- `buckminster_fuller.gen` — Synergetic systems thinking
- `socrates.gen` — Dialectic inquiry and self-examination
