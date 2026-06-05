# ⚡ Async Execution Engine

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![AsyncIO](https://img.shields.io/badge/AsyncIO-Concurrency-green?style=for-the-badge)
![AIOHTTP](https://img.shields.io/badge/AIOHTTP-Async%20HTTP-orange?style=for-the-badge)
![AIOFiles](https://img.shields.io/badge/AIOFiles-Async%20Files-purple?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-yellow?style=for-the-badge&logo=linux)

---

# 📖 Overview

Modern DevOps platforms must process thousands of tasks concurrently without blocking system resources.

In this lab, you will build a fully functional **Async Execution Engine** using Python's **asyncio** framework. The engine will support:

- ⚡ Concurrent task execution
- 👷 Worker pools
- 📋 Task queues
- 📊 Monitoring and statistics
- ❌ Task cancellation
- 🎯 Priority-based scheduling

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Implement asynchronous task execution using asyncio

✅ Manage concurrency with worker pools

✅ Build scalable execution engines

✅ Monitor running tasks and execution metrics

✅ Implement task prioritization and cancellation

✅ Improve performance through async programming patterns

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming knowledge
- Understanding of functions and decorators
- Familiarity with Linux command line
- Basic understanding of concurrency concepts
- Python 3.8+ installed

---

# 🛠️ Environment Setup

## Step 1: Update Package Repository

```bash
sudo apt update
```

---

## Step 2: Install Python Requirements

```bash
sudo apt install -y python3 python3-pip python3-venv
```

---

## Step 3: Create Project Directory

```bash
mkdir -p ~/async-engine-lab
cd ~/async-engine-lab
```

---

## Step 4: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install aiohttp aiofiles
```

---

# 🏗️ Task 1: Build Async Task Executor

---

# 📦 Step 1: Create Task Model

Create:

```bash
touch task_model.py
```

Add:

```python
from dataclasses import dataclass
from typing import Any, Callable
from enum import Enum
import time

class TaskStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"

@dataclass
class Task:
    task_id: str
    func: Callable
    args: tuple = ()
    kwargs: dict = None
    status: TaskStatus = TaskStatus.PENDING
    result: Any = None
    error: str = None
    created_at: float = None
    completed_at: float = None

    def __post_init__(self):
        if self.kwargs is None:
            self.kwargs = {}

        if self.created_at is None:
            self.created_at = time.time()
```

---

# ⚙️ Step 2: Create Execution Engine

Create:

```bash
touch execution_engine.py
```

Core engine structure:

```python
import asyncio
from typing import Dict, List
from task_model import Task, TaskStatus
import time

class AsyncExecutionEngine:

    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.task_queue = asyncio.Queue()
        self.tasks: Dict[str, Task] = {}
        self.workers: List[asyncio.Task] = []
        self.running = False
```

---

## Submit Tasks

```python
async def submit_task(self, task: Task):
    self.tasks[task.task_id] = task
    await self.task_queue.put(task)
    return task.task_id
```

---

## Worker Coroutine

```python
async def _worker(self, worker_id):

    print(f"Worker {worker_id} started")

    while self.running:

        try:
            task = await asyncio.wait_for(
                self.task_queue.get(),
                timeout=1
            )

            task.status = TaskStatus.RUNNING

            try:
                result = await task.func(
                    *task.args,
                    **task.kwargs
                )

                task.result = result
                task.status = TaskStatus.COMPLETED

            except Exception as e:
                task.error = str(e)
                task.status = TaskStatus.FAILED

            task.completed_at = time.time()

            self.task_queue.task_done()

        except asyncio.TimeoutError:
            continue
```

---

## Start Engine

```python
async def start(self):

    self.running = True

    for worker_id in range(self.max_workers):

        worker = asyncio.create_task(
            self._worker(worker_id)
        )

        self.workers.append(worker)
```

---

## Stop Engine

```python
async def stop(self):

    self.running = False

    await asyncio.gather(
        *self.workers,
        return_exceptions=True
    )
```

---

## Task Status API

```python
def get_task_status(self, task_id):

    task = self.tasks.get(task_id)

    if not task:
        return None

    return {
        "task_id": task.task_id,
        "status": task.status.value,
        "result": task.result,
        "error": task.error
    }
```

---

## Statistics

```python
def get_statistics(self):

    stats = {
        "pending": 0,
        "running": 0,
        "completed": 0,
        "failed": 0
    }

    for task in self.tasks.values():
        stats[task.status.value] += 1

    return stats
```

---

# 🌐 Step 3: Create Async Task Functions

Create:

```bash
touch sample_tasks.py
```

---

## Async URL Fetcher

```python
import aiohttp

async def fetch_url(url):

    async with aiohttp.ClientSession() as session:

        async with session.get(url) as response:

            content = await response.text()

            return {
                "status": response.status,
                "length": len(content)
            }
```

---

## Async File Processor

```python
import aiofiles

async def process_file(filename, operation):

    if operation == "read":

        async with aiofiles.open(filename, "r") as f:

            content = await f.read()

            return {
                "lines": len(content.splitlines())
            }

    elif operation == "write":

        async with aiofiles.open(filename, "w") as f:

            await f.write(
                "Generated by Async Engine"
            )

        return {
            "status": "written"
        }
```

---

## Compute Intensive Task

```python
import asyncio

async def compute_intensive_task(n):

    await asyncio.sleep(n)

    return n * n
```

---

# 🚀 Step 4: Main Application

Create:

```bash
touch main.py
```

Add:

```python
import asyncio
import uuid

from execution_engine import AsyncExecutionEngine
from task_model import Task
from sample_tasks import (
    compute_intensive_task,
    process_file
)

async def main():

    engine = AsyncExecutionEngine(
        max_workers=3
    )

    await engine.start()

    task1 = Task(
        str(uuid.uuid4()),
        compute_intensive_task,
        (3,)
    )

    task2 = Task(
        str(uuid.uuid4()),
        compute_intensive_task,
        (5,)
    )

    await engine.submit_task(task1)
    await engine.submit_task(task2)

    await asyncio.sleep(6)

    print(engine.get_statistics())

    await engine.stop()

asyncio.run(main())
```

---

# 🧪 Step 5: Create Test File

```bash
echo "Sample data for testing" > test_input.txt
```

Run:

```bash
python main.py
```

---

# 🏆 Task 2: Add Monitoring and Control

---

# ❌ Step 1: Task Cancellation

Add:

```python
async def cancel_task(self, task_id):

    task = self.tasks.get(task_id)

    if not task:
        return False

    if task.status in [
        TaskStatus.COMPLETED,
        TaskStatus.FAILED
    ]:
        return False

    task.status = TaskStatus.FAILED
    task.error = "Cancelled"

    return True
```

---

# 🎯 Step 2: Priority Queue Support

Add:

```python
from dataclasses import dataclass, field

@dataclass(order=True)
class PrioritizedTask:

    priority: int

    task: any = field(compare=False)
```

---

Modify constructor:

```python
def __init__(
    self,
    max_workers=5,
    use_priority=False
):

    self.max_workers = max_workers

    if use_priority:
        self.task_queue = asyncio.PriorityQueue()
    else:
        self.task_queue = asyncio.Queue()
```

---

# 📊 Step 3: Monitoring Dashboard

Create:

```bash
touch monitor.py
```

Add:

```python
import asyncio
import os

class EngineMonitor:

    def __init__(self, engine):

        self.engine = engine
        self.monitoring = False

    async def display_stats(
        self,
        interval=2
    ):

        self.monitoring = True

        while self.monitoring:

            os.system("clear")

            stats = self.engine.get_statistics()

            print("=== Engine Statistics ===")

            for k, v in stats.items():
                print(f"{k}: {v}")

            print(
                f"Queue Size: "
                f"{self.engine.task_queue.qsize()}"
            )

            await asyncio.sleep(interval)

    def stop(self):
        self.monitoring = False
```

---

# 🔥 Step 4: Advanced Stress Testing

Create:

```bash
touch advanced_test.py
```

---

## Stress Test

```python
import asyncio
import uuid

from execution_engine import AsyncExecutionEngine
from task_model import Task
from sample_tasks import compute_intensive_task

async def stress_test():

    engine = AsyncExecutionEngine(
        max_workers=5
    )

    await engine.start()

    for i in range(20):

        task = Task(
            str(uuid.uuid4()),
            compute_intensive_task,
            (2,)
        )

        await engine.submit_task(task)

    await asyncio.sleep(10)

    print(
        engine.get_statistics()
    )

    await engine.stop()

asyncio.run(stress_test())
```

---

# ✅ Verification

---

## Test 1: Basic Execution

```bash
python main.py
```

Expected:

```text
Worker 0 started
Worker 1 started
Worker 2 started

Task completed

{'completed': 2}
```

---

## Test 2: Concurrent Processing

```bash
python advanced_test.py
```

Verify:

- Multiple tasks run simultaneously
- Workers share workload
- Tasks complete successfully

---

## Test 3: Failure Handling

Modify task:

```python
async def broken_task():
    raise Exception("Simulated Failure")
```

Expected:

```text
Status: FAILED
Error: Simulated Failure
```

---

## Test 4: Performance Benchmark

```bash
time python advanced_test.py
```

Expected:

Concurrent execution completes significantly faster than sequential execution.

---

# 🔍 Troubleshooting

## Tasks Not Running

```text
Cause:
Engine not started

Fix:
await engine.start()
```

---

## Event Loop Errors

```text
Cause:
Incorrect async invocation

Fix:
Use asyncio.run()
```

---

## Tasks Hanging

```text
Cause:
Blocking operations

Fix:
Replace with await calls
```

---

## Missing Packages

```bash
pip install aiohttp aiofiles
```

---

# 🎉 Conclusion

Congratulations! You have successfully built an **Async Execution Engine** capable of:

✅ Concurrent task execution

✅ Worker pool management

✅ Async file processing

✅ Async HTTP operations

✅ Task monitoring

✅ Task cancellation

✅ Priority scheduling

✅ Execution statistics

---

# 🚀 Real-World DevOps Applications

This architecture is widely used in:

- CI/CD Pipeline Executors
- Kubernetes Controllers
- Infrastructure Automation
- Distributed Job Scheduling
- Monitoring Systems
- Log Aggregation Pipelines
- Cloud Orchestration Platforms
- Event-Driven Microservices

---

# 📚 Key Takeaways

- AsyncIO enables high-performance concurrency.
- Worker pools improve scalability.
- Task queues simplify workload distribution.
- Monitoring improves operational visibility.
- Async programming is essential for modern cloud-native systems.

Happy Learning! 🚀
