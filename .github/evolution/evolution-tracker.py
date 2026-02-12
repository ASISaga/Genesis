#!/usr/bin/env python3
"""
Evolution Tracker for Genesis Agents and Skills

Tracks performance metrics, learnings, and evolution history for self-learning
agents and skills in the Genesis ecosystem.
"""

import os
import sys
import yaml
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
from dataclasses import dataclass, field, asdict


@dataclass
class PerformanceMetrics:
    """Performance metrics for an agent or skill"""
    total_invocations: int = 0
    success_rate: float = 0.0
    average_execution_time: float = 0.0
    resonance_scores: Dict[str, float] = field(default_factory=lambda: {
        'mean': 0.0, 'min': 0.0, 'max': 0.0
    })
    task_categories: List[Dict[str, Any]] = field(default_factory=list)


@dataclass
class Learning:
    """A learned pattern or insight"""
    pattern_id: str
    description: str
    examples: List[str] = field(default_factory=list)
    confidence: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + 'Z')


@dataclass
class Evolution:
    """A single evolution event"""
    evolution_id: str
    timestamp: str
    proposal: str
    changes: List[Dict[str, str]]
    resonance_score: float
    validation_status: str
    impact_metrics: Dict[str, float] = field(default_factory=dict)


class EvolutionTracker:
    """Tracks and manages evolution data for agents and skills"""
    
    def __init__(self, knowledge_dir: Path = None):
        if knowledge_dir is None:
            # Default to .github/knowledge in the repo root
            repo_root = Path(__file__).parent.parent.parent
            knowledge_dir = repo_root / '.github' / 'knowledge'
        
        self.knowledge_dir = Path(knowledge_dir)
        self.knowledge_dir.mkdir(parents=True, exist_ok=True)
    
    def get_entity_dir(self, entity_name: str) -> Path:
        """Get the knowledge directory for an agent or skill"""
        entity_dir = self.knowledge_dir / entity_name
        entity_dir.mkdir(parents=True, exist_ok=True)
        return entity_dir
    
    def load_metrics(self, entity_name: str) -> PerformanceMetrics:
        """Load performance metrics for an entity"""
        metrics_file = self.get_entity_dir(entity_name) / 'metrics.yaml'
        
        if not metrics_file.exists():
            return PerformanceMetrics()
        
        with open(metrics_file, 'r') as f:
            data = yaml.safe_load(f)
            if data and 'metrics' in data:
                return PerformanceMetrics(**data['metrics'])
        
        return PerformanceMetrics()
    
    def save_metrics(self, entity_name: str, metrics: PerformanceMetrics):
        """Save performance metrics for an entity"""
        metrics_file = self.get_entity_dir(entity_name) / 'metrics.yaml'
        
        data = {
            'version': '1.0',
            'last_updated': datetime.utcnow().isoformat() + 'Z',
            'metrics': asdict(metrics)
        }
        
        with open(metrics_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    def record_invocation(self, entity_name: str, success: bool, 
                         execution_time: float, resonance_score: float = None,
                         task_category: str = None):
        """Record a single invocation of an agent or skill"""
        metrics = self.load_metrics(entity_name)
        
        # Update totals
        metrics.total_invocations += 1
        
        # Update success rate
        old_successes = int(metrics.success_rate * (metrics.total_invocations - 1))
        new_successes = old_successes + (1 if success else 0)
        metrics.success_rate = new_successes / metrics.total_invocations
        
        # Update average execution time
        old_total_time = metrics.average_execution_time * (metrics.total_invocations - 1)
        metrics.average_execution_time = (old_total_time + execution_time) / metrics.total_invocations
        
        # Update resonance scores if provided
        if resonance_score is not None:
            if metrics.resonance_scores['mean'] == 0.0:
                metrics.resonance_scores['mean'] = resonance_score
                metrics.resonance_scores['min'] = resonance_score
                metrics.resonance_scores['max'] = resonance_score
            else:
                old_mean_total = metrics.resonance_scores['mean'] * (metrics.total_invocations - 1)
                metrics.resonance_scores['mean'] = (old_mean_total + resonance_score) / metrics.total_invocations
                metrics.resonance_scores['min'] = min(metrics.resonance_scores['min'], resonance_score)
                metrics.resonance_scores['max'] = max(metrics.resonance_scores['max'], resonance_score)
        
        # Update task category metrics
        if task_category:
            category_found = False
            for cat in metrics.task_categories:
                if cat['category'] == task_category:
                    cat['count'] += 1
                    old_cat_successes = int(cat['success_rate'] * (cat['count'] - 1))
                    new_cat_successes = old_cat_successes + (1 if success else 0)
                    cat['success_rate'] = new_cat_successes / cat['count']
                    category_found = True
                    break
            
            if not category_found:
                metrics.task_categories.append({
                    'category': task_category,
                    'count': 1,
                    'success_rate': 1.0 if success else 0.0
                })
        
        self.save_metrics(entity_name, metrics)
    
    def load_learnings(self, entity_name: str) -> List[Learning]:
        """Load accumulated learnings for an entity"""
        learnings_file = self.get_entity_dir(entity_name) / 'learnings.yaml'
        
        if not learnings_file.exists():
            return []
        
        with open(learnings_file, 'r') as f:
            data = yaml.safe_load(f)
            if data and 'patterns' in data:
                return [Learning(**pattern) for pattern in data['patterns']]
        
        return []
    
    def save_learning(self, entity_name: str, learning: Learning):
        """Save a new learning for an entity"""
        learnings = self.load_learnings(entity_name)
        learnings.append(learning)
        
        learnings_file = self.get_entity_dir(entity_name) / 'learnings.yaml'
        data = {
            'version': '1.0',
            'last_updated': datetime.utcnow().isoformat() + 'Z',
            'patterns': [asdict(l) for l in learnings]
        }
        
        with open(learnings_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    def load_evolution_log(self, entity_name: str) -> List[Evolution]:
        """Load evolution history for an entity"""
        log_file = self.get_entity_dir(entity_name) / 'evolution-log.yaml'
        
        if not log_file.exists():
            return []
        
        with open(log_file, 'r') as f:
            data = yaml.safe_load(f)
            if data and 'evolutions' in data:
                return [Evolution(**evo) for evo in data['evolutions']]
        
        return []
    
    def record_evolution(self, entity_name: str, evolution: Evolution):
        """Record an evolution event"""
        evolutions = self.load_evolution_log(entity_name)
        evolutions.append(evolution)
        
        log_file = self.get_entity_dir(entity_name) / 'evolution-log.yaml'
        data = {
            'version': '1.0',
            'evolutions': [asdict(e) for e in evolutions]
        }
        
        with open(log_file, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    
    def generate_report(self, entity_name: str = None) -> str:
        """Generate a report on evolution metrics"""
        if entity_name:
            return self._generate_entity_report(entity_name)
        else:
            return self._generate_summary_report()
    
    def _generate_entity_report(self, entity_name: str) -> str:
        """Generate a detailed report for a specific entity"""
        metrics = self.load_metrics(entity_name)
        learnings = self.load_learnings(entity_name)
        evolutions = self.load_evolution_log(entity_name)
        
        report = f"\n{'='*60}\n"
        report += f"Evolution Report: {entity_name}\n"
        report += f"{'='*60}\n\n"
        
        report += "## Performance Metrics\n"
        report += f"  Total Invocations: {metrics.total_invocations}\n"
        report += f"  Success Rate: {metrics.success_rate:.2%}\n"
        report += f"  Avg Execution Time: {metrics.average_execution_time:.2f}s\n"
        report += f"  Resonance Score (mean): {metrics.resonance_scores['mean']:.3f}\n"
        report += f"  Resonance Score (range): [{metrics.resonance_scores['min']:.3f}, {metrics.resonance_scores['max']:.3f}]\n"
        
        if metrics.task_categories:
            report += "\n  Task Categories:\n"
            for cat in metrics.task_categories:
                report += f"    - {cat['category']}: {cat['count']} invocations, {cat['success_rate']:.2%} success\n"
        
        report += f"\n## Learnings: {len(learnings)} patterns identified\n"
        for learning in learnings[:5]:  # Show top 5
            report += f"  - {learning.pattern_id}: {learning.description} (confidence: {learning.confidence:.2f})\n"
        
        report += f"\n## Evolution History: {len(evolutions)} evolutions\n"
        for evo in evolutions[-5:]:  # Show last 5
            report += f"  - {evo.evolution_id} ({evo.timestamp}): {evo.proposal}\n"
            report += f"    Status: {evo.validation_status}, Resonance: {evo.resonance_score:.3f}\n"
        
        return report
    
    def _generate_summary_report(self) -> str:
        """Generate a summary report for all entities"""
        report = f"\n{'='*60}\n"
        report += "Evolution System Summary Report\n"
        report += f"{'='*60}\n\n"
        
        entities = [d for d in self.knowledge_dir.iterdir() if d.is_dir()]
        
        for entity_dir in sorted(entities):
            entity_name = entity_dir.name
            metrics = self.load_metrics(entity_name)
            evolutions = self.load_evolution_log(entity_name)
            
            report += f"\n{entity_name}:\n"
            report += f"  Invocations: {metrics.total_invocations}\n"
            report += f"  Success Rate: {metrics.success_rate:.2%}\n"
            report += f"  Evolutions: {len(evolutions)}\n"
        
        return report


def main():
    """CLI for evolution tracker"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Genesis Evolution Tracker')
    parser.add_argument('command', choices=['report', 'record', 'init'],
                       help='Command to execute')
    parser.add_argument('--entity', help='Agent or skill name')
    parser.add_argument('--success', type=bool, help='Invocation success')
    parser.add_argument('--time', type=float, help='Execution time')
    parser.add_argument('--resonance', type=float, help='Resonance score')
    parser.add_argument('--category', help='Task category')
    
    args = parser.parse_args()
    
    tracker = EvolutionTracker()
    
    if args.command == 'report':
        print(tracker.generate_report(args.entity))
    
    elif args.command == 'record':
        if not args.entity or args.success is None or args.time is None:
            print("Error: --entity, --success, and --time required for record command")
            sys.exit(1)
        
        tracker.record_invocation(
            args.entity,
            args.success,
            args.time,
            args.resonance,
            args.category
        )
        print(f"Recorded invocation for {args.entity}")
    
    elif args.command == 'init':
        if not args.entity:
            print("Error: --entity required for init command")
            sys.exit(1)
        
        tracker.get_entity_dir(args.entity)
        print(f"Initialized knowledge base for {args.entity}")


if __name__ == '__main__':
    main()
