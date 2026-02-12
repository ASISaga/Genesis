#!/usr/bin/env python3
"""
Initialize knowledge bases for all Genesis agents and skills
"""

import yaml
from pathlib import Path
from datetime import datetime


def create_template_metrics(entity_name: str, entity_type: str) -> dict:
    """Create template metrics.yaml"""
    return {
        'version': '1.0',
        'last_updated': datetime.utcnow().isoformat() + 'Z',
        'entity_type': entity_type,
        'metrics': {
            'total_invocations': 0,
            'success_rate': 0.0,
            'average_execution_time': 0.0,
            'resonance_scores': {
                'mean': 0.0,
                'min': 0.0,
                'max': 0.0
            },
            'task_categories': []
        }
    }


def create_template_learnings(entity_name: str) -> dict:
    """Create template learnings.yaml"""
    return {
        'version': '1.0',
        'last_updated': datetime.utcnow().isoformat() + 'Z',
        'patterns': [],
        'insights': [],
        'antipatterns': []
    }


def create_template_evolution_log(entity_name: str) -> dict:
    """Create template evolution-log.yaml"""
    return {
        'version': '1.0',
        'evolutions': []
    }


def create_template_context(entity_name: str) -> dict:
    """Create template context.yaml"""
    return {
        'version': '1.0',
        'last_updated': datetime.utcnow().isoformat() + 'Z',
        'usage_contexts': [],
        'common_parameters': [],
        'user_feedback': []
    }


def initialize_entity_knowledge(knowledge_dir: Path, entity_name: str, entity_type: str):
    """Initialize knowledge base for a single entity"""
    entity_dir = knowledge_dir / entity_name
    entity_dir.mkdir(parents=True, exist_ok=True)
    
    # Create metrics.yaml
    metrics_file = entity_dir / 'metrics.yaml'
    if not metrics_file.exists():
        with open(metrics_file, 'w') as f:
            yaml.dump(create_template_metrics(entity_name, entity_type), 
                     f, default_flow_style=False, sort_keys=False)
    
    # Create learnings.yaml
    learnings_file = entity_dir / 'learnings.yaml'
    if not learnings_file.exists():
        with open(learnings_file, 'w') as f:
            yaml.dump(create_template_learnings(entity_name), 
                     f, default_flow_style=False, sort_keys=False)
    
    # Create evolution-log.yaml
    log_file = entity_dir / 'evolution-log.yaml'
    if not log_file.exists():
        with open(log_file, 'w') as f:
            yaml.dump(create_template_evolution_log(entity_name), 
                     f, default_flow_style=False, sort_keys=False)
    
    # Create context.yaml
    context_file = entity_dir / 'context.yaml'
    if not context_file.exists():
        with open(context_file, 'w') as f:
            yaml.dump(create_template_context(entity_name), 
                     f, default_flow_style=False, sort_keys=False)
    
    print(f"✓ Initialized knowledge base for {entity_type}: {entity_name}")


def main():
    """Initialize all agent and skill knowledge bases"""
    repo_root = Path(__file__).parent.parent.parent
    github_dir = repo_root / '.github'
    knowledge_dir = github_dir / 'knowledge'
    knowledge_dir.mkdir(parents=True, exist_ok=True)
    
    print("Initializing Genesis Agent and Skill Knowledge Bases\n")
    
    # Initialize agents
    agents_dir = github_dir / 'agents'
    if agents_dir.exists():
        for agent_file in agents_dir.glob('*.md'):
            agent_name = agent_file.stem
            initialize_entity_knowledge(knowledge_dir, agent_name, 'agent')
    
    # Initialize skills
    skills_dir = github_dir / 'skills'
    if skills_dir.exists():
        for skill_dir in skills_dir.iterdir():
            if skill_dir.is_dir():
                skill_name = skill_dir.name
                initialize_entity_knowledge(knowledge_dir, skill_name, 'skill')
    
    print(f"\n✓ All knowledge bases initialized in {knowledge_dir}")
    print("\nKnowledge base structure:")
    print("  metrics.yaml       - Performance tracking")
    print("  learnings.yaml     - Accumulated insights")
    print("  evolution-log.yaml - Self-modification history")
    print("  context.yaml       - Usage patterns and feedback")


if __name__ == '__main__':
    main()
