#!/usr/bin/env python3
"""
Dependency-Aware Pipeline Runner
Executes jobs based on their dependencies using topological sorting
"""

import time
import yaml
from typing import Dict, List, Set, Optional
from enum import Enum
from collections import defaultdict, deque


class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"


class Job:
    """Represents a single job in the pipeline"""
    
    def __init__(self, name: str, command: str, dependencies: List[str] = None):
        self.name = name
        self.command = command
        self.dependencies = dependencies or []
        self.status = JobStatus.PENDING
        self.start_time = None
        self.end_time = None
        self.error_message = None
    
    def execute(self) -> bool:
        """
        Execute the job command.
        
        Returns:
            bool: True if successful, False otherwise
        
        TODO: Implement job execution logic
        - Set status to RUNNING
        - Record start_time
        - Execute the command using subprocess or eval for simple commands
        - Handle success/failure
        - Record end_time
        - Return execution result
        """
        pass
    
    def __repr__(self):
        return f"Job({self.name}, status={self.status.value})"

class PipelineRunner:
    """Manages and executes jobs based on dependencies"""
    
    def __init__(self, config_file: str):
        self.jobs: Dict[str, Job] = {}
        self.dependency_graph: Dict[str, List[str]] = defaultdict(list)
        self.reverse_graph: Dict[str, List[str]] = defaultdict(list)
        self.load_config(config_file)
    
    def load_config(self, config_file: str):
        """
        Load pipeline configuration from YAML file.
        
        TODO: Implement configuration loading
        - Read YAML file
        - Create Job objects
        - Build dependency_graph (job -> dependents)
        - Build reverse_graph (job -> dependencies)
        """
        pass
    
    def validate_dag(self) -> bool:
        """
        Validate that the dependency graph is a DAG (no cycles).
        
        Returns:
            bool: True if valid DAG, False if cycles detected
        
        TODO: Implement cycle detection using DFS or Kahn's algorithm
        - Use color-based DFS (white, gray, black) or
        - Track visited nodes and recursion stack
        - Return False if cycle found
        """
        pass
    
    def topological_sort(self) -> List[str]:
        """
        Perform topological sort to determine execution order.
        
        Returns:
            List[str]: Ordered list of job names
        
        TODO: Implement topological sorting
        - Use Kahn's algorithm (BFS-based) or DFS-based approach
        - Calculate in-degrees for each node
        - Process nodes with zero in-degree
        - Return sorted order
        """
        pass
    
    def can_execute(self, job_name: str) -> bool:
        """
        Check if a job's dependencies are satisfied.
        
        TODO: Implement dependency checking
        - Check all dependencies have SUCCESS status
        - Return True only if all dependencies succeeded
        """
        pass
    
    def mark_downstream_skipped(self, job_name: str):
        """
        Mark all downstream jobs as skipped when a job fails.
        
        TODO: Implement downstream propagation
        - Use BFS or DFS to find all dependent jobs
        - Set their status to SKIPPED
        """
        pass
    
    def execute_pipeline(self) -> Dict[str, JobStatus]:
        """
        Execute all jobs in dependency order.
        
        Returns:
            Dict[str, JobStatus]: Final status of all jobs
        
        TODO: Implement pipeline execution
        - Get execution order from topological_sort
        - For each job in order:
          - Check if can_execute
          - Execute if ready
          - Handle failures (mark downstream as skipped)
        - Return final status dictionary
        """
        pass
    
    def print_summary(self):
        """Print execution summary"""
        print("\n" + "="*60)
        print("PIPELINE EXECUTION SUMMARY")
        print("="*60)
        
        for job_name, job in self.jobs.items():
            duration = ""
            if job.start_time and job.end_time:
                duration = f" ({job.end_time - job.start_time:.2f}s)"
            
            status_symbol = {
                JobStatus.SUCCESS: "✓",
                JobStatus.FAILED: "✗",
                JobStatus.SKIPPED: "⊘",
                JobStatus.PENDING: "○"
            }.get(job.status, "?")
            
            print(f"{status_symbol} {job_name}: {job.status.value}{duration}")
            if job.error_message:
                print(f"  Error: {job.error_message}")
        
        print("="*60)

