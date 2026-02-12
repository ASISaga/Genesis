#!/usr/bin/env python3
"""
Add self-learning capability annotations to all Genesis skills
"""

import re
from pathlib import Path


def add_self_learning_to_skill(skill_file: Path):
    """Add self-learning metadata and section to a skill"""
    
    with open(skill_file, 'r') as f:
        content = f.read()
    
    # Check if already has self_learning
    if 'self_learning: true' in content:
        print(f"  ✓ {skill_file.parent.name} already has self-learning")
        return False
    
    # Extract skill name from parent directory
    skill_name = skill_file.parent.name
    
    # Add self_learning field to frontmatter
    content = re.sub(
        r'(---\nname:.*?\ndescription:.*?)(\n---|\nlicense:)',
        r'\1\nself_learning: true\nknowledge_base: .github/knowledge/' + skill_name + r'\2',
        content,
        flags=re.DOTALL
    )
    
    # Add self-learning section
    self_learning_section = f"""
## Self-Learning Capabilities

This skill implements the Ouroboros evolution pattern and learns from each usage:

- **Performance Tracking**: All invocations are tracked in `.github/knowledge/{skill_name}/metrics.yaml`
- **Pattern Learning**: Effective usage patterns are accumulated in `learnings.yaml`
- **Evolution Log**: Self-modifications are recorded in `evolution-log.yaml`
- **Context Awareness**: Usage contexts guide future improvements in `context.yaml`

The skill evolves through cycles defined in `.github/evolution/skill-evolution.gen`, continuously refining its instructions and examples based on real-world usage.

"""
    
    # Insert after the main skill description
    parts = content.split('\n## ', 1)
    if len(parts) == 2:
        content = parts[0] + self_learning_section + '\n## ' + parts[1]
    else:
        # If no ## sections, add before "When to Use" or at the end
        if '## When to Use' in content:
            content = content.replace('## When to Use', self_learning_section + '## When to Use')
        else:
            content = content + self_learning_section
    
    with open(skill_file, 'w') as f:
        f.write(content)
    
    print(f"  ✓ Added self-learning to {skill_name}")
    return True


def main():
    """Add self-learning to all skills"""
    repo_root = Path(__file__).parent.parent.parent
    skills_dir = repo_root / '.github' / 'skills'
    
    print("Adding self-learning capabilities to all Genesis skills\n")
    
    updated = 0
    for skill_dir in skills_dir.iterdir():
        if skill_dir.is_dir():
            skill_file = skill_dir / 'SKILL.md'
            if skill_file.exists():
                if add_self_learning_to_skill(skill_file):
                    updated += 1
    
    print(f"\n✓ Updated {updated} skills with self-learning capabilities")


if __name__ == '__main__':
    main()
