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
async def cancel_task(self, task_id: str) -> bool:
    """
    Cancel a pending or running task.
    
    Args:
        task_id: ID of task to cancel
        
    Returns:
        True if cancelled, False otherwise
    """
    # TODO: Check if task exists
    # TODO: Check if task can be cancelled (not completed/failed)
    # TODO: Update task status to FAILED with cancellation message
    # TODO: Return success status
    pass

from dataclasses import dataclass, field
from typing import Any

@dataclass(order=True)
class PrioritizedTask:
    """Wrapper for tasks with priority."""
    priority: int
    task: Any = field(compare=False)
    
    def __init__(self, priority: int, task: Task):
        self.priority = priority
        self.task = task
def __init__(self, max_workers: int = 5, use_priority: bool = False):
    """
    Initialize the execution engine.
    
    Args:
        max_workers: Maximum number of concurrent tasks
        use_priority: Enable priority-based task execution
    """
    # TODO: Initialize with PriorityQueue if use_priority is True
    # TODO: Otherwise use regular Queue
    pass

# Time sequential vs concurrent execution
python -c "
import asyncio
import time
from execution_engine import AsyncExecutionEngine
from task_model import Task
from sample_tasks import compute_intensive_task
import uuid

async def test():
    engine = AsyncExecutionEngine(max_workers=5)
    await engine.start()
    
    start = time.time()
    tasks = [Task(str(uuid.uuid4()), compute_intensive_task, (3,)) for _ in range(10)]
    for t in tasks:
        await engine.submit_task(t)
    
    await asyncio.sleep(5)
    print(f'Time: {time.time() - start:.2f}s')
    await engine.stop()

asyncio.run(test())
"

