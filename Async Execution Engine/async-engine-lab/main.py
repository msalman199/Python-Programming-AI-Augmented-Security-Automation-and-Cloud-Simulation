import asyncio
from execution_engine import AsyncExecutionEngine
from task_model import Task
from sample_tasks import fetch_url, compute_intensive_task, process_file
import uuid

async def main():
    """Main application demonstrating the async execution engine."""
    
    # Initialize engine
    engine = AsyncExecutionEngine(max_workers=3)
    await engine.start()
    
    print("Async Execution Engine Started")
    print("-" * 50)
    
    # TODO: Create and submit multiple tasks
    # Example task creation:
    # task1 = Task(
    #     task_id=str(uuid.uuid4()),
    #     func=compute_intensive_task,
    #     args=(5,)
    # )
    
    # TODO: Submit tasks to engine
    
    # TODO: Wait for tasks to complete
    
    # TODO: Display task results
    
    # TODO: Print statistics
    
    # Stop engine
    await engine.stop()
    print("\nEngine stopped")

if __name__ == "__main__":
    asyncio.run(main())
