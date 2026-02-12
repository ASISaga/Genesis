#!/usr/bin/env python3
"""
Self-Learning Integration Hook for Genesis Agents and Skills

This module provides integration hooks that enable agents and skills to
automatically track their performance and evolve over time.
"""

import os
import sys
import time
from pathlib import Path
from contextlib import contextmanager
from typing import Optional

# Import the evolution tracker
sys.path.insert(0, str(Path(__file__).parent))
from evolution_tracker import EvolutionTracker


class SelfLearningHook:
    """Context manager for tracking agent/skill execution"""
    
    def __init__(self, entity_name: str, task_category: str = None):
        self.entity_name = entity_name
        self.task_category = task_category
        self.tracker = EvolutionTracker()
        self.start_time = None
        self.success = False
        self.resonance_score = None
    
    def __enter__(self):
        """Start tracking execution"""
        self.start_time = time.time()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Record execution results"""
        execution_time = time.time() - self.start_time
        
        # If no exception, consider it a success
        if exc_type is None:
            self.success = True
        
        # Record the invocation
        self.tracker.record_invocation(
            self.entity_name,
            self.success,
            execution_time,
            self.resonance_score,
            self.task_category
        )
        
        # Don't suppress exceptions
        return False
    
    def set_success(self, success: bool):
        """Manually set success status"""
        self.success = success
    
    def set_resonance(self, score: float):
        """Set the resonance score for this execution"""
        self.resonance_score = score


@contextmanager
def track_agent_execution(agent_name: str, task_category: str = None):
    """Context manager for tracking agent execution"""
    hook = SelfLearningHook(agent_name, task_category)
    try:
        yield hook
    finally:
        pass  # __exit__ handles recording


@contextmanager
def track_skill_execution(skill_name: str, task_category: str = None):
    """Context manager for tracking skill execution"""
    hook = SelfLearningHook(skill_name, task_category)
    try:
        yield hook
    finally:
        pass  # __exit__ handles recording


# Example usage in agent/skill code:
#
# from self_learning_hook import track_agent_execution
#
# def my_agent_task(task_description):
#     with track_agent_execution("covenant-guardian", "code_review") as tracker:
#         # Perform the task
#         result = perform_code_review(task_description)
#         
#         # Optionally set resonance score
#         tracker.set_resonance(0.92)
#         
#         return result
