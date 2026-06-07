# 🚀 Automation Platform MVP 

> *"Automate repetitive operations through policy-driven orchestration, APIs, background workers, and CLI tooling."*

---

![Automation](https://img.shields.io/badge/Automation-Platform-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-green?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?style=for-the-badge&logo=flask)
![Redis](https://img.shields.io/badge/Redis-Broker-red?style=for-the-badge&logo=redis)
![Celery](https://img.shields.io/badge/Celery-Workers-green?style=for-the-badge)
![CLI](https://img.shields.io/badge/CLI-Management-orange?style=for-the-badge)

---

# 📚 Overview

This lab demonstrates how to build a complete Automation Platform MVP capable of:

✅ Policy-based validation

✅ REST API task submission

✅ Background task execution

✅ Redis message broker integration

✅ Celery worker processing

✅ CLI task management

✅ Task status tracking

✅ Automation orchestration

---

# 🎯 Learning Objectives

By completing this lab, you will:

- Build an end-to-end automation platform
- Implement policy-driven validation
- Create asynchronous task processing
- Build REST APIs for automation
- Develop a command-line management interface
- Integrate Redis and Celery
- Manage automation workflows efficiently

---

# 🛠 Prerequisites

- Basic Python programming
- Linux command-line experience
- REST API knowledge
- JSON familiarity
- Understanding of background workers

---

# ⚙️ Environment Setup

## Install Required Packages

```bash
sudo apt update

sudo apt install -y \
python3 \
python3-pip \
python3-venv \
redis-server
```

Start Redis:

```bash
sudo systemctl start redis-server
sudo systemctl enable redis-server

redis-cli ping
```

Expected:

```text
PONG
```

---

# 📂 Create Project Structure

```bash
mkdir -p ~/automation-platform
cd ~/automation-platform

python3 -m venv venv
source venv/bin/activate

pip install flask redis celery click pyyaml requests
```

Create directories:

```bash
mkdir -p \
api \
cli \
workers \
policies \
logs
```

---

# ⚙️ Configuration File

## config.yaml

```yaml
redis:
  host: localhost
  port: 6379
  db: 0

api:
  host: 0.0.0.0
  port: 5000

workers:
  concurrency: 2

policies:
  max_retries: 3
  timeout: 300
```

---

# 🔒 Policy Engine

## policies/policy_engine.py

```python
import yaml
from typing import Dict, Any


class PolicyEngine:

    def __init__(self, config_path="config.yaml"):
        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.allowed_task_types = [
            "backup",
            "deploy",
            "cleanup"
        ]

    def validate_task(self, task_data: Dict[str, Any]):

        required_fields = ["task_type", "parameters"]

        for field in required_fields:
            if field not in task_data:
                return False, f"Missing field: {field}"

        task_type = task_data["task_type"]

        if task_type not in self.allowed_task_types:
            return False, f"Invalid task type: {task_type}"

        timeout = task_data.get(
            "timeout",
            self.config["policies"]["timeout"]
        )

        if timeout > self.config["policies"]["timeout"]:
            return False, "Timeout exceeds policy"

        return True, "Valid"

    def get_retry_policy(self, task_type):

        return self.config["policies"]["max_retries"]
```

---

# ⚡ Worker System

## workers/task_worker.py

```python
from celery import Celery
import yaml
import time
from datetime import datetime

with open("config.yaml") as f:
    config = yaml.safe_load(f)

redis_url = (
    f"redis://{config['redis']['host']}:"
    f"{config['redis']['port']}/"
    f"{config['redis']['db']}"
)

app = Celery(
    "automation_platform",
    broker=redis_url,
    backend=redis_url
)


@app.task(bind=True, max_retries=3)
def execute_automation_task(
    self,
    task_id,
    task_type,
    parameters
):
    try:

        print(
            f"[{datetime.now()}] "
            f"Running task {task_id}"
        )

        if task_type == "backup":

            time.sleep(5)

            result = {
                "message":
                f"Backup completed for {parameters}"
            }

        elif task_type == "deploy":

            time.sleep(3)

            result = {
                "message":
                f"Deployment completed for {parameters}"
            }

        elif task_type == "cleanup":

            time.sleep(2)

            result = {
                "message":
                f"Cleanup completed for {parameters}"
            }

        else:
            raise Exception("Unknown task type")

        return {
            "status": "success",
            "timestamp": str(datetime.now()),
            "result": result
        }

    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)
```

---

# 🌐 REST API

## api/automation_api.py

```python
from flask import Flask, request, jsonify
from policies.policy_engine import PolicyEngine
from workers.task_worker import execute_automation_task

import redis
import yaml
import uuid
import json
from datetime import datetime

app = Flask(__name__)

with open("config.yaml") as f:
    config = yaml.safe_load(f)

r = redis.Redis(
    host=config["redis"]["host"],
    port=config["redis"]["port"],
    db=config["redis"]["db"],
    decode_responses=True
)

policy = PolicyEngine()


@app.route("/api/tasks", methods=["POST"])
def create_task():

    data = request.get_json()

    valid, msg = policy.validate_task(data)

    if not valid:
        return jsonify({"error": msg}), 400

    task_id = (
        f"{datetime.now().strftime('%Y%m%d')}-"
        f"{uuid.uuid4().hex[:8]}"
    )

    celery_task = execute_automation_task.delay(
        task_id,
        data["task_type"],
        data["parameters"]
    )

    metadata = {
        "task_id": task_id,
        "celery_id": celery_task.id,
        "task_type": data["task_type"],
        "status": "queued",
        "created": str(datetime.now())
    }

    r.setex(
        f"task:{task_id}",
        3600,
        json.dumps(metadata)
    )

    return jsonify(metadata)


@app.route("/api/tasks/<task_id>")
def get_task_status(task_id):

    task = r.get(f"task:{task_id}")

    if not task:
        return jsonify({"error": "Task not found"}), 404

    return jsonify(json.loads(task))


@app.route("/api/tasks")
def list_tasks():

    tasks = []

    for key in r.keys("task:*"):
        tasks.append(json.loads(r.get(key)))

    return jsonify(tasks)


if __name__ == "__main__":
    app.run(
        host=config["api"]["host"],
        port=config["api"]["port"]
    )
```

---

# 💻 CLI Interface

## cli/automation_cli.py

```python
import click
import requests
import json

API_BASE_URL = "http://localhost:5000/api"


@click.group()
def cli():
    pass


@cli.command()
@click.option(
    "--type",
    required=True,
    type=click.Choice([
        "backup",
        "deploy",
        "cleanup"
    ])
)
@click.option(
    "--params",
    required=True
)
@click.option(
    "--priority",
    default="medium"
)
def submit(type, params, priority):

    payload = {
        "task_type": type,
        "parameters": json.loads(params),
        "priority": priority
    }

    response = requests.post(
        f"{API_BASE_URL}/tasks",
        json=payload
    )

    click.echo(response.json())


@cli.command()
@click.argument("task_id")
def status(task_id):

    response = requests.get(
        f"{API_BASE_URL}/tasks/{task_id}"
    )

    click.echo(
        json.dumps(
            response.json(),
            indent=2
        )
    )


@cli.command()
def list():

    response = requests.get(
        f"{API_BASE_URL}/tasks"
    )

    click.echo(
        json.dumps(
            response.json(),
            indent=2
        )
    )


if __name__ == "__main__":
    cli()
```

---

# ▶️ Platform Startup Script

## start_platform.sh

```bash
#!/bin/bash

cd ~/automation-platform

source venv/bin/activate

python3 api/automation_api.py &
API_PID=$!

echo "API PID: $API_PID"

celery -A workers.task_worker worker --loglevel=info &
WORKER_PID=$!

echo "Worker PID: $WORKER_PID"

echo "Platform Started"

wait
```

Make executable:

```bash
chmod +x start_platform.sh
```

---

# 🧪 Testing

## Start Platform

```bash
./start_platform.sh
```

---

## Submit Backup Task

```bash
python3 cli/automation_cli.py submit \
--type backup \
--params '{"path":"/data","destination":"/backup"}' \
--priority high
```

---

## Check Status

```bash
python3 cli/automation_cli.py status TASK_ID
```

---

## List Tasks

```bash
python3 cli/automation_cli.py list
```

---

# 🌐 API Testing

## Create Task

```bash
curl -X POST http://localhost:5000/api/tasks \
-H "Content-Type: application/json" \
-d '{
  "task_type":"deploy",
  "parameters":{
    "service":"web-app",
    "version":"1.2.3"
  },
  "priority":"high"
}'
```

---

## Task Status

```bash
curl http://localhost:5000/api/tasks/TASK_ID
```

---

## List Tasks

```bash
curl http://localhost:5000/api/tasks
```

---

# ✅ Verification

Check Redis:

```bash
redis-cli KEYS "task:*"
```

Check worker logs:

```bash
celery -A workers.task_worker worker \
--loglevel=debug
```

Verify API:

```bash
curl http://localhost:5000/api/tasks
```

---

# 📊 Expected Outcomes

After completing this lab:

✅ Policy Engine validates requests

✅ API accepts automation tasks

✅ Redis stores metadata

✅ Celery processes tasks

✅ CLI manages automation workflows

✅ Background workers execute jobs

✅ Automation platform operates end-to-end

---

# 🧹 Cleanup

```bash
pkill -f automation_api.py

pkill -f celery

sudo systemctl stop redis-server

cd ~

rm -rf ~/automation-platform
```

---

# 🎓 Conclusion

You successfully built an **Automation Platform MVP** featuring:

- 🔒 Policy-Based Validation
- 🌐 REST API Management
- ⚡ Celery Background Workers
- 📦 Redis Message Broker
- 💻 CLI Management Tool
- 🔄 Asynchronous Task Execution
- 🚀 End-to-End Automation Workflows

This architecture mirrors real-world DevOps automation platforms used for deployments, backups, infrastructure operations, orchestration pipelines, and enterprise automation systems.

### 🚀 Next Steps

- Add Authentication & RBAC
- Integrate Monitoring & Metrics
- Add Task Scheduling
- Implement Web Dashboard
- Add Kubernetes Automation Support
- Integrate CI/CD Pipelines

---
**Happy Automating! 🎉**
