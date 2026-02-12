#!/usr/bin/env python3
"""
Add self-learning capability annotations to all Genesis agents
"""

import re
from pathlib import Path


def add_self_learning_to_agent(agent_file: Path):
    """Add self-learning metadata and section to an agent"""
    
    with open(agent_file, 'r') as f:
        content = f.read()
    
    # Check if already has self_learning
    if 'self_learning: true' in content:
        print(f"  ✓ {agent_file.stem} already has self-learning")
        return False
    
    # Extract agent name from file stem
    agent_name = agent_file.stem
    
    # Add self_learning field to frontmatter
    content = re.sub(
        r'(---\nname:.*?\ntools:.*?)(\n---)',
        r'\1\nself_learning: true\nknowledge_base: .github/knowledge/' + agent_name + r'\2',
        content,
        flags=re.DOTALL
    )
    
    # Add self-learning section after the main agent description
    # Find the first ## section
    self_learning_section = f"""
## Self-Learning Capabilities

This agent implements the Ouroboros evolution pattern and learns from each interaction:

- **Performance Tracking**: All invocations are tracked in `.github/knowledge/{agent_name}/metrics.yaml`
- **Pattern Learning**: Successful patterns are accumulated in `learnings.yaml`
- **Evolution Log**: Self-modifications are recorded in `evolution-log.yaml`
- **Context Awareness**: Usage patterns guide future improvements in `context.yaml`

The agent evolves through cycles defined in `.github/evolution/agent-evolution.gen`, continuously improving its effectiveness while preserving its core purpose and ethical foundations.

"""
    
    # Insert after the first paragraph (after agent description)
    parts = content.split('\n## ', 1)
    if len(parts) == 2:
        content = parts[0] + self_learning_section + '\n## ' + parts[1]
    else:
        # If no ## sections, add before the end
        content = content + self_learning_section
    
    with open(agent_file, 'w') as f:
        f.write(content)
    
    print(f"  ✓ Added self-learning to {agent_file.stem}")
    return True


def main():
    """Add self-learning to all agents"""
    repo_root = Path(__file__).parent.parent.parent
    agents_dir = repo_root / '.github' / 'agents'
    
    print("Adding self-learning capabilities to all Genesis agents\n")
    
    updated = 0
    for agent_file in agents_dir.glob('*.md'):
        if add_self_learning_to_agent(agent_file):
            updated += 1
    
    print(f"\n✓ Updated {updated} agents with self-learning capabilities")


if __name__ == '__main__':
    main()
