# 🐳 Containerize API and Worker

<div align="center">

![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED?style=for-the-badge\&logo=docker)
![Python](https://img.shields.io/badge/Python-3.11-yellow?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-REST%20API-black?style=for-the-badge\&logo=flask)
![Redis](https://img.shields.io/badge/Redis-Queue-red?style=for-the-badge\&logo=redis)
![DevOps](https://img.shields.io/badge/DevOps-Microservices-blue?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge\&logo=linux)

# 🚀 Containerized API & Worker Services

### Build • Package • Deploy • Scale

Learn how to containerize microservices using Docker and enable consistent deployments across environments.

</div>

---

# 📖 Overview

Containerization is a fundamental DevOps practice that enables applications to run consistently across development, testing, and production environments.

In this lab, you will build and containerize:

✅ REST API Service

✅ Background Worker Service

✅ Shared Configuration Module

✅ Redis Task Queue

✅ Docker Networking

✅ Production-Ready Docker Images

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

* 🔹 Create production-ready Dockerfiles
* 🔹 Build optimized Docker images
* 🔹 Configure multi-container networking
* 🔹 Use environment variables for configuration
* 🔹 Connect services using Redis
* 🔹 Deploy applications consistently across environments

---

# 📋 Prerequisites

Before starting, ensure you have:

* 🐳 Basic Docker knowledge
* 🐍 Familiarity with Python
* 🌐 Understanding of REST APIs
* 🐧 Linux command-line experience
* ⚙️ Understanding of environment variables

---

# 🏗️ Environment Setup

You will use the Linux machine provided through the lab environment.

---

# 🔹 Install Required Tools

Update packages:

```bash
sudo apt update
```

Install Docker:

```bash
curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh
```

Add current user:

```bash
sudo usermod -aG docker $USER

newgrp docker
```

Verify installation:

```bash
docker --version
```

Expected:

```text
Docker version XX.X.X
```

---

# 🧩 Task 1: Create Application Services

---

# 🔹 Step 1: Create Project Structure

Create workspace:

```bash
mkdir ~/containerize-lab

cd ~/containerize-lab
```

Create folders:

```bash
mkdir -p api worker shared
```

---

## 📁 Project Structure

```text
containerize-lab/
│
├── api/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── worker/
│   ├── worker.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── shared/
│   └── config.py
│
└── docker-compose.yml
```

---

# 🔹 Step 2: Create Shared Configuration

Create:

```bash
shared/config.py
```

Purpose:

✅ Centralized configuration

✅ Environment variable handling

✅ Redis connectivity

✅ API configuration

---

### Example Variables

```python
REDIS_HOST
REDIS_PORT
API_PORT
```

---

### Redis URL Generator

Implement:

```python
def get_redis_url():
```

Expected Output:

```text
redis://redis:6379
```

---

# 🔹 Step 3: Create API Service

Create:

```bash
api/app.py
```

---

## 🌐 API Responsibilities

The API service will:

* Accept tasks
* Store tasks in Redis
* Retrieve task results
* Provide health checks

---

### Endpoints

| Endpoint          | Method | Purpose         |
| ----------------- | ------ | --------------- |
| /health           | GET    | Health Check    |
| /task             | POST   | Submit Task     |
| /result/<task_id> | GET    | Retrieve Result |

---

### Health Check

```http
GET /health
```

Response:

```json
{
  "status": "healthy"
}
```

---

### Task Submission

```http
POST /task
```

Request:

```json
{
  "task_type": "process",
  "data": {
    "value": 42
  }
}
```

---

### Redis Client

Implement:

```python
def get_redis_client():
```

Responsibilities:

* Connect Redis
* Use shared configuration
* Return Redis client object

---

## API Dependencies

Create:

```bash
api/requirements.txt
```

```text
flask==3.0.0
redis==5.0.1
```

---

# 🔹 Step 4: Create Worker Service

Create:

```bash
worker/worker.py
```

---

## ⚙️ Worker Responsibilities

Worker will:

✅ Listen to Redis queue

✅ Process incoming tasks

✅ Store results

✅ Run continuously

---

### Processing Flow

```text
Receive Task
      │
      ▼
Process Data
      │
      ▼
Store Result
      │
      ▼
Wait For Next Task
```

---

### Redis Queue

Use:

```python
BLPOP
```

Queue Name:

```text
task_queue
```

---

### Simulated Processing

Use:

```python
time.sleep()
```

Duration:

```text
2–5 Seconds
```

---

## Worker Dependencies

Create:

```bash
worker/requirements.txt
```

```text
redis==5.0.1
```

---

# 🧩 Task 2: Create Dockerfiles

---

# 🔹 Step 1: Create API Dockerfile

Create:

```bash
api/Dockerfile
```

---

## Required Configuration

### Base Image

```dockerfile
FROM python:3.11-slim
```

---

### Working Directory

```dockerfile
WORKDIR /app
```

---

### Install Dependencies

```dockerfile
RUN pip install --no-cache-dir
```

---

### Copy Files

```dockerfile
COPY shared/ /app/shared/
COPY api/app.py /app/
```

---

### Expose Port

```dockerfile
EXPOSE 5000
```

---

### Start Application

```dockerfile
CMD ["python", "app.py"]
```

---

# 🔹 Step 2: Create Worker Dockerfile

Create:

```bash
worker/Dockerfile
```

---

## Required Configuration

### Base Image

```dockerfile
FROM python:3.11-slim
```

### Working Directory

```dockerfile
WORKDIR /app
```

### Install Requirements

```dockerfile
RUN pip install --no-cache-dir
```

### Copy Files

```dockerfile
COPY shared/ /app/shared/
COPY worker/worker.py /app/
```

### Start Worker

```dockerfile
CMD ["python", "worker.py"]
```

---

# 🔹 Step 3: Docker Compose Architecture

Create:

```bash
docker-compose.yml
```

---

## Service Relationships

```text
       Client
          │
          ▼
     API Service
          │
          ▼
        Redis
          │
          ▼
     Worker Service
```

---

### Components

| Service | Purpose         |
| ------- | --------------- |
| Redis   | Message Queue   |
| API     | Task Submission |
| Worker  | Task Processing |

---

# 🧩 Task 3: Build and Run Services

---

# 🔹 Step 1: Build Docker Images

Build API:

```bash
docker build \
-t task-api:v1 \
-f api/Dockerfile .
```

Build Worker:

```bash
docker build \
-t task-worker:v1 \
-f worker/Dockerfile .
```

Verify:

```bash
docker images | grep task-
```

Expected:

```text
task-api
task-worker
```

---

# 🔹 Step 2: Create Docker Network

Create bridge network:

```bash
docker network create app-network
```

Verify:

```bash
docker network ls
```

Expected:

```text
app-network
```

---

# 🔹 Step 3: Run Redis Container

```bash
docker run -d \
--name redis \
--network app-network \
-p 6379:6379 \
redis:7-alpine
```

Verify:

```bash
docker ps | grep redis
```

---

# 🔹 Step 4: Run API Container

```bash
docker run -d \
--name api \
--network app-network \
-p 5000:5000 \
-e REDIS_HOST=redis \
-e REDIS_PORT=6379 \
task-api:v1
```

Check logs:

```bash
docker logs api
```

---

# 🔹 Step 5: Run Worker Container

```bash
docker run -d \
--name worker \
--network app-network \
-e REDIS_HOST=redis \
-e REDIS_PORT=6379 \
task-worker:v1
```

Verify:

```bash
docker logs worker
```

Expected:

```text
Worker starting...
```

---

# ✅ Verification

---

# 🔹 Verify Running Containers

```bash
docker ps
```

Expected:

```text
redis
api
worker
```

All containers should show:

```text
STATUS: Up
```

---

# 🔹 Test Health Endpoint

```bash
curl http://localhost:5000/health
```

Expected:

```json
{
  "status": "healthy"
}
```

---

# 🔹 Test Task Processing

Submit task:

```bash
curl -X POST \
http://localhost:5000/task \
-H "Content-Type: application/json" \
-d '{"task_type":"process","data":{"value":42}}'
```

Response:

```json
{
  "task_id": "12345"
}
```

---

Check result:

```bash
curl http://localhost:5000/result/<task_id>
```

Expected:

```json
{
  "status": "completed"
}
```

---

# 🔹 Inspect Networking

```bash
docker network inspect app-network
```

Verify:

```text
redis
api
worker
```

are connected.

---

# 🔹 Inspect Logs

API:

```bash
docker logs api --tail 20
```

Worker:

```bash
docker logs worker --tail 20
```

Look for:

```text
Task received
Task processed
Result stored
```

---

# 📊 Container Architecture

```text
                 Client
                    │
                    ▼
          ┌─────────────────┐
          │   API Service   │
          │ Flask REST API  │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │      Redis      │
          │ Task Queue      │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Worker Service  │
          │ Task Processor  │
          └─────────────────┘
```

---

# 🛠 Troubleshooting

---

## ❌ Container Won't Start

Inspect logs:

```bash
docker logs <container-name>
```

Check:

* Dockerfile syntax
* Missing files
* Dependency installation

---

## ❌ Redis Connection Failed

Verify Redis:

```bash
docker ps
```

Inspect network:

```bash
docker network inspect app-network
```

Verify variables:

```bash
REDIS_HOST=redis
```

---

## ❌ Port Already In Use

Check:

```bash
sudo lsof -i :5000
```

Stop conflicting container:

```bash
docker stop <container>
```

Alternative:

```bash
-p 5001:5000
```

---

## ❌ Docker Build Failure

Verify:

```bash
requirements.txt
Dockerfile
COPY paths
```

Check working directory:

```bash
pwd
```

---

## ❌ Worker Not Processing Tasks

Check worker logs:

```bash
docker logs worker
```

Test Redis manually:

```bash
docker exec -it redis redis-cli
```

---

# 🧹 Cleanup

Stop containers:

```bash
docker stop api worker redis
```

Remove containers:

```bash
docker rm api worker redis
```

Remove network:

```bash
docker network rm app-network
```

Remove images:

```bash
docker rmi task-api:v1 task-worker:v1
```

---

# 🎓 Key Takeaways

✅ Dockerfiles create reproducible builds

✅ Containers run consistently across environments

✅ Docker networking enables service discovery

✅ Redis provides asynchronous communication

✅ Environment variables separate configuration from code

✅ Multi-container applications are foundation of microservices

---

# 🚀 Real-World Applications

These concepts are used in:

* 🔹 Kubernetes Deployments
* 🔹 Docker Compose Stacks
* 🔹 Microservices Platforms
* 🔹 CI/CD Pipelines
* 🔹 Cloud-Native Applications
* 🔹 Event-Driven Architectures

---

# 🏆 Lab Completed

You have successfully:

✔ Built API and Worker services

✔ Containerized applications using Docker

✔ Created production-ready Dockerfiles

✔ Implemented Redis-based communication

✔ Configured Docker networking

✔ Deployed a multi-container application

✔ Established a foundation for cloud-native development

---

<div align="center">

# 🌟 Build Once, Run Anywhere with Docker 🌟

### Happy Learning & Happy Containerizing 🐳🚀

</div>
