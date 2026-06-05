import asyncio
from execution_engine import AsyncExecutionEngine
from task_model import Task
from sample_tasks import compute_intensive_task
from monitor import EngineMonitor
import uuid

async def stress_test():
    """
    Stress test the execution engine with many tasks.
    """
    # TODO: Create engine with specific worker count
    # TODO: Start engine
    # TODO: Submit 20+ tasks with varying complexity
    # TODO: Start monitor in separate task
    # TODO: Wait for completion
    # TODO: Display final statistics
    pass

async def priority_test():
    """
    Test priority-based task execution.
    """
    # TODO: Create engine with priority support
    # TODO: Submit tasks with different priorities
    # TODO: Verify execution order matches priorities
    pass

if __name__ == "__main__":
    print("Select test:")
    print("1. Stress Test")
    print("2. Priority Test")
    choice = input("Enter choice (1-2): ")
    
    if choice == "1":
        asyncio.run(stress_test())
    elif choice == "2":
        asyncio.run(priority_test())
