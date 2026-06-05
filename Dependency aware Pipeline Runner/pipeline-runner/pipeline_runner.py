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
def execute(self) -> bool:
    """Execute the job command"""
    import subprocess
    
    self.status = JobStatus.RUNNING
    self.start_time = time.time()
    
    print(f"\n[RUNNING] {self.name}")
    print(f"Command: {self.command}")
    
    try:
        # TODO: Execute command using subprocess
        # Hint: Use subprocess.run() with shell=True
        # Capture output and check return code
        # Set status to SUCCESS or FAILED based on result
        
        result = subprocess.run(
            self.command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=30
        )
        
        # TODO: Handle result
        # if result.returncode == 0: SUCCESS
        # else: FAILED with error_message
        
        self.end_time = time.time()
        return self.status == JobStatus.SUCCESS
        
    except Exception as e:
        # TODO: Handle exceptions
        # Set status to FAILED
        # Store error message
        self.end_time = time.time()
        return False

def topological_sort(self) -> List[str]:
    """Perform topological sort using Kahn's algorithm"""
    
    # TODO: Calculate in-degrees
    in_degree = {job: 0 for job in self.jobs}
    
    # TODO: Count incoming edges for each node
    # Hint: Use self.reverse_graph
    
    # TODO: Find all nodes with in-degree 0
    queue = deque()
    # Add jobs with no dependencies to queue
    
    sorted_order = []
    
    # TODO: Process queue
    # while queue is not empty:
    #   - Remove node from queue
    #   - Add to sorted_order
    #   - For each dependent, decrease in-degree
    #   - If in-degree becomes 0, add to queue
    
    return sorted_order

def validate_dag(self) -> bool:
    """Validate DAG using DFS cycle detection"""
    
    WHITE, GRAY, BLACK = 0, 1, 2
    color = {job: WHITE for job in self.jobs}
    
    def has_cycle(node: str) -> bool:
        """DFS helper to detect cycles"""
        # TODO: Implement DFS cycle detection
        # - Mark node as GRAY (visiting)
        # - For each neighbor:
        #   - If GRAY: cycle found
        #   - If WHITE: recurse
        # - Mark node as BLACK (visited)
        # - Return cycle status
        pass
    
    # TODO: Check all nodes
    for job in self.jobs:
        if color[job] == WHITE:
            if has_cycle(job):
                return False
    
    return True


def execute_pipeline(self) -> Dict[str, JobStatus]:
    """Execute pipeline in dependency order"""
    
    print("\n" + "="*60)
    print("STARTING PIPELINE EXECUTION")
    print("="*60)
    
    # TODO: Validate DAG
    if not self.validate_dag():
        print("ERROR: Cycle detected in dependencies!")
        return {}
    
    # TODO: Get execution order
    execution_order = self.topological_sort()
    print(f"\nExecution order: {' -> '.join(execution_order)}")
    
    # TODO: Execute jobs in order
    for job_name in execution_order:
        job = self.jobs[job_name]
        
        # TODO: Check if can execute
        # if not self.can_execute(job_name):
        #     job.status = JobStatus.SKIPPED
        #     continue
        
        # TODO: Execute job
        # success = job.execute()
        
        # TODO: Handle failure
        # if not success:
        #     self.mark_downstream_skipped(job_name)
    
    return {name: job.status for name, job in self.jobs.items()}

def main():
    """Main entry point"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 pipeline_runner.py <config_file>")
        sys.exit(1)
    
    config_file = sys.argv[1]
    
    runner = PipelineRunner(config_file)
    runner.execute_pipeline()
    runner.print_summary()


if __name__ == "__main__":
    main()


