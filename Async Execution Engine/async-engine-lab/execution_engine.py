import asyncio
from typing import List, Dict
from task_model import Task, TaskStatus
import time

class AsyncExecutionEngine:
    """
    Manages asynchronous task execution with concurrency control.
    """
    
    def __init__(self, max_workers: int = 5):
        """
        Initialize the execution engine.
        
        Args:
            max_workers: Maximum number of concurrent tasks
        """
        self.max_workers = max_workers
        self.task_queue = asyncio.Queue()
        self.tasks: Dict[str, Task] = {}
        self.workers: List[asyncio.Task] = []
        self.running = False
    
    async def submit_task(self, task: Task) -> str:
        """
        Submit a task for execution.
        
        Args:
            task: Task object to execute
            
        Returns:
            task_id of the submitted task
        """
        # TODO: Add task to tasks dictionary
        # TODO: Put task in the queue
        # TODO: Return task_id
        pass
    
    async def _worker(self, worker_id: int):
        """
        Worker coroutine that processes tasks from the queue.
        
        Args:
            worker_id: Unique identifier for this worker
        """
        print(f"Worker {worker_id} started")
        
        while self.running:
            try:
                # TODO: Get task from queue with timeout
                # TODO: Update task status to RUNNING
                # TODO: Execute the task function
                # TODO: Handle success and failure cases
                # TODO: Update task completion time
                pass
            except asyncio.TimeoutError:
                continue
            except Exception as e:
                print(f"Worker {worker_id} error: {e}")
        
        print(f"Worker {worker_id} stopped")
    
    async def start(self):
        """Start the execution engine and worker pool."""
        # TODO: Set running flag to True
        # TODO: Create worker tasks using asyncio.create_task
        # TODO: Store workers in self.workers list
        pass
    
    async def stop(self):
        """Stop the execution engine gracefully."""
        # TODO: Set running flag to False
        # TODO: Wait for all workers to complete
        # TODO: Cancel any remaining workers
        pass
    
    def get_task_status(self, task_id: str) -> Dict:
        """
        Get the status of a specific task.
        
        Args:
            task_id: ID of the task to check
            
        Returns:
            Dictionary with task status information
        """
        # TODO: Retrieve task from tasks dictionary
        # TODO: Return formatted status dictionary
        pass
    
    def get_statistics(self) -> Dict:
        """
        Get execution statistics.
        
        Returns:
            Dictionary with engine statistics
        """
        # TODO: Count tasks by status
        # TODO: Calculate average execution time
        # TODO: Return statistics dictionary
        pass
