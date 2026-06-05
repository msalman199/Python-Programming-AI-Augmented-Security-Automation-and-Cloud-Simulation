# 🚀 Dependency-Aware Pipeline Runner 

<div align="center">

# 🔗 Dependency-Aware Pipeline Runner

### Build a DAG-Based CI/CD Pipeline Orchestration System with Python

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge\&logo=python)
![YAML](https://img.shields.io/badge/YAML-Configuration-orange?style=for-the-badge)
![DAG](https://img.shields.io/badge/DAG-Dependency_Graph-green?style=for-the-badge)
![CI/CD](https://img.shields.io/badge/CI/CD-Pipeline-purple?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-red?style=for-the-badge\&logo=linux)

</div>

---

# 📖 Overview

In this hands-on DevOps lab, you will build a **Dependency-Aware Pipeline Runner** that executes jobs according to dependency relationships using **Directed Acyclic Graphs (DAGs)** and **Topological Sorting**.

The pipeline runner will:

* 🔗 Model job dependencies
* 📊 Build dependency graphs
* 🚦 Resolve execution order automatically
* ❌ Detect dependency cycles
* ⚠️ Handle job failures gracefully
* ⛔ Skip downstream jobs when dependencies fail
* 🚀 Simulate CI/CD workflow execution

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

✅ Model job dependencies using DAGs

✅ Implement topological sorting algorithms

✅ Detect cycles in dependency graphs

✅ Build dependency-aware job schedulers

✅ Propagate failures across dependent jobs

✅ Create practical CI/CD orchestration systems

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

* Basic Python programming knowledge
* Understanding of graphs and data structures
* Familiarity with Linux command line
* Basic CI/CD concepts

---

# 🛠️ Environment Setup

## 📦 Update System Packages

```bash
sudo apt update
```

---

## 🐍 Install Python

```bash
sudo apt install -y python3 python3-pip python3-venv
```

---

## 📁 Create Project Directory

```bash
mkdir -p ~/pipeline-runner
cd ~/pipeline-runner
```

---

## 🔐 Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📥 Install Required Packages

```bash
pip install pyyaml
```

---

# 🏗️ Project Structure

```text
pipeline-runner/
│
├── pipeline_runner.py
├── pipeline_config.yaml
├── pipeline_config_fail.yaml
├── pipeline_complex.yaml
├── test_pipeline.py
│
└── venv/
```

---

# 🚀 Task 1: Model Job Dependencies

---

# 📁 Step 1: Create Project Files

```bash
cd ~/pipeline-runner

touch pipeline_runner.py
touch pipeline_config.yaml
touch test_pipeline.py
```

---

# 🧩 Step 2: Define the Job Class

Create:

```bash
touch pipeline_runner.py
```

---

## 📄 Job Status Enumeration

```python
class JobStatus(Enum):
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"
    SKIPPED = "skipped"
```

---

## 📄 Job Class Responsibilities

Each job should contain:

| Attribute     | Purpose                 |
| ------------- | ----------------------- |
| name          | Job identifier          |
| command       | Command to execute      |
| dependencies  | Required jobs           |
| status        | Current execution state |
| start_time    | Execution start         |
| end_time      | Execution completion    |
| error_message | Failure details         |

---

## ⚙️ Implement execute()

Responsibilities:

* Set status to RUNNING
* Record timestamps
* Execute command
* Capture output
* Mark SUCCESS or FAILED
* Store error information

Example:

```python
result = subprocess.run(
    self.command,
    shell=True,
    capture_output=True,
    text=True
)
```

---

# 🏗️ Step 3: Implement Pipeline Runner

The PipelineRunner manages:

* DAG creation
* Dependency validation
* Execution order
* Failure handling
* Pipeline execution

---

## Core Data Structures

### Dependency Graph

```python
dependency_graph
```

Represents:

```text
Job → Dependents
```

Example:

```text
checkout
   ↓
install_deps
   ↓
lint
```

---

### Reverse Graph

```python
reverse_graph
```

Represents:

```text
Job → Dependencies
```

Example:

```text
build
 ├── lint
 └── unit_tests
```

---

# 📄 Step 4: Create Pipeline Configuration

Create:

```bash
touch pipeline_config.yaml
```

---

## Example Pipeline

```yaml
jobs:
  - name: checkout
    command: "echo 'Checking out code...'"
    dependencies: []

  - name: install_deps
    command: "echo 'Installing dependencies...'"
    dependencies:
      - checkout

  - name: lint
    command: "echo 'Running linter...'"
    dependencies:
      - install_deps

  - name: unit_tests
    command: "echo 'Running unit tests...'"
    dependencies:
      - install_deps

  - name: build
    command: "echo 'Building application...'"
    dependencies:
      - lint
      - unit_tests

  - name: deploy
    command: "echo 'Deploying application...'"
    dependencies:
      - build
```

---

# 🚀 Task 2: Implement Core Functionality

---

# ⚙️ Step 1: Complete Job Execution Logic

Implement:

```python
def execute(self):
```

---

### Workflow

```text
PENDING
   ↓
RUNNING
   ↓
SUCCESS / FAILED
```

---

### Command Execution

```python
subprocess.run(
    self.command,
    shell=True,
    capture_output=True,
    text=True,
    timeout=30
)
```

---

### Success Case

```python
self.status = JobStatus.SUCCESS
```

---

### Failure Case

```python
self.status = JobStatus.FAILED
self.error_message = result.stderr
```

---

# 🔀 Step 2: Implement Topological Sort

Use **Kahn's Algorithm**

---

## Calculate In-Degree

Example:

```text
checkout = 0
install_deps = 1
build = 2
```

---

## Processing Flow

```text
Find nodes with indegree 0
        ↓
Add to queue
        ↓
Process node
        ↓
Decrease dependent indegrees
        ↓
Repeat
```

---

### Expected Execution Order

```text
checkout
↓
install_deps
↓
lint
↓
unit_tests
↓
build
↓
deploy
```

---

# 🔍 Step 3: Implement Cycle Detection

Use DFS color states:

| Color | Meaning   |
| ----- | --------- |
| WHITE | Unvisited |
| GRAY  | Visiting  |
| BLACK | Completed |

---

## Detect Cycle

Example:

```text
A → B
B → C
C → A
```

Result:

```text
Cycle Found
```

Pipeline should stop immediately.

---

# 🚦 Step 4: Dependency Validation

Implement:

```python
def can_execute(job_name):
```

Checks:

```python
All dependencies == SUCCESS
```

Only then execute job.

---

# ⛔ Step 5: Failure Propagation

Implement:

```python
mark_downstream_skipped()
```

Example:

```text
test_integration FAILED
       ↓
build SKIPPED
       ↓
deploy SKIPPED
```

---

# ▶️ Step 6: Execute Pipeline

Workflow:

```text
Validate DAG
      ↓
Topological Sort
      ↓
Execute Jobs
      ↓
Handle Failures
      ↓
Generate Summary
```

---

# 🧪 Task 3: Test Failure Scenarios

---

# 📄 Create Failure Pipeline

Create:

```bash
touch pipeline_config_fail.yaml
```

---

## Example

```yaml
jobs:
  - name: setup
    command: "echo Setup complete"
    dependencies: []

  - name: test_unit
    command: "echo Unit tests passed"
    dependencies:
      - setup

  - name: test_integration
    command: "exit 1"
    dependencies:
      - setup

  - name: build
    command: "echo Building..."
    dependencies:
      - test_unit
      - test_integration

  - name: deploy
    command: "echo Deploying..."
    dependencies:
      - build
```

---

## Expected Behavior

```text
setup             SUCCESS
test_unit         SUCCESS
test_integration  FAILED
build             SKIPPED
deploy            SKIPPED
```

---

# 🧪 Create Test Script

Create:

```bash
touch test_pipeline.py
```

---

## Test Cases

### Test 1

```python
test_successful_pipeline()
```

Validates:

* Correct ordering
* Successful execution

---

### Test 2

```python
test_failed_pipeline()
```

Validates:

* Failure propagation
* Dependency skipping

---

# 🚀 Run Tests

---

## Successful Pipeline

```bash
python3 pipeline_runner.py pipeline_config.yaml
```

---

## Failure Pipeline

```bash
python3 pipeline_runner.py pipeline_config_fail.yaml
```

---

## Full Test Suite

```bash
python3 test_pipeline.py
```

---

# 🔬 Verification

---

## Verify Dependency Resolution

Expected:

```text
checkout
↓
install_deps
↓
lint
↓
unit_tests
↓
build
↓
deploy
```

No job executes before prerequisites complete.

---

## Verify Failure Handling

Expected:

```text
FAILED
   ↓
SKIPPED
   ↓
SKIPPED
```

for all downstream jobs.

---

# 🧩 Complex Pipeline Test

Create:

```bash
touch pipeline_complex.yaml
```

---

## DAG Structure

```text
        init
       /    \
   task_a  task_b
      \     /
       task_c
          \
         finalize
```

---

Run:

```bash
python3 pipeline_runner.py pipeline_complex.yaml
```

Verify correct execution order.

---

# 📊 Expected Results

After completing this lab:

✅ YAML configuration parsing works

✅ Dependency graph creation works

✅ DAG validation detects cycles

✅ Topological sorting resolves order

✅ Job execution succeeds

✅ Failures propagate correctly

✅ Downstream jobs are skipped

---

# 🧠 Concepts Learned

---

## Directed Acyclic Graph (DAG)

Represents dependency relationships.

Example:

```text
Build
 ↑
Tests
 ↑
Install
 ↑
Checkout
```

---

## Topological Sorting

Produces valid execution order.

Guarantees:

```text
Dependencies execute first
```

---

## Failure Propagation

Ensures:

```text
Broken dependency
      ↓
Dependent jobs stop
```

---

# 🛠️ Troubleshooting

---

## Jobs Execute in Wrong Order

Check:

```python
topological_sort()
```

Verify:

```python
in_degree
```

calculations are correct.

---

## Cycle Detection Fails

Verify:

```python
WHITE
GRAY
BLACK
```

state transitions.

---

## Dependents Not Skipped

Review:

```python
mark_downstream_skipped()
```

Ensure BFS/DFS traversal reaches all descendants.

---

## YAML Parsing Errors

Validate syntax:

```bash
python -c "import yaml; yaml.safe_load(open('pipeline_config.yaml'))"
```

Use spaces, not tabs.

---

# 🎓 Conclusion

Congratulations! 🎉

You have successfully built a **Dependency-Aware Pipeline Runner** that:

* 🔗 Models job dependencies as a DAG
* 🚦 Resolves execution order using topological sorting
* ❌ Detects cycles before execution
* ⚠️ Handles failures gracefully
* ⛔ Propagates dependency failures
* 🚀 Executes jobs in a CI/CD-style workflow

---

# 🚀 Real-World Applications

### CI/CD Platforms

* Jenkins
* GitLab CI
* GitHub Actions
* Azure DevOps

### Infrastructure Automation

* Terraform pipelines
* Ansible orchestration
* Kubernetes deployment workflows

### Data Engineering

* ETL pipelines
* Workflow orchestration
* Batch processing systems

---

# 🏅 Skills Gained

* Graph Algorithms
* Directed Acyclic Graphs (DAGs)
* Topological Sorting
* Cycle Detection
* Dependency Resolution
* Pipeline Orchestration
* Failure Propagation
* CI/CD Automation

---

<div align="center">

# ✅ Dependency-Aware Pipeline Runner Lab Completed Successfully

### Ready to Build Production CI/CD Orchestrators 🚀

</div>
