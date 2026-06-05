# 🚀 FastAPI Status and Policy Service 

<p align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-E92063?style=for-the-badge)
![Uvicorn](https://img.shields.io/badge/Uvicorn-ASGI_Server-4B8BBE?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![DevOps](https://img.shields.io/badge/DevOps-Monitoring-blueviolet?style=for-the-badge)

</p>

---

# 📖 Overview

In this hands-on lab, you will build a **FastAPI Status and Policy Service** that provides:

✅ Health Monitoring

✅ System Resource Status

✅ Policy Enforcement

✅ Request Validation

✅ Middleware Logging

✅ REST API Endpoints

This project demonstrates common DevOps and Cloud-Native patterns used in API gateways, service meshes, monitoring services, and microservice architectures.

---

# 🎯 Learning Objectives

By completing this lab, you will:

- Build a FastAPI service with multiple endpoints
- Monitor system resources using psutil
- Create policy enforcement mechanisms
- Validate HTTP requests and payloads
- Apply middleware for request logging
- Test APIs using curl and Python clients
- Understand health monitoring patterns

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming knowledge
- Understanding of REST APIs
- Familiarity with JSON
- Linux command-line experience
- Basic knowledge of monitoring concepts

---

# 🛠️ Environment Setup

---

## 🔹 Step 1: Update System Packages

```bash
sudo apt update
```

---

## 🔹 Step 2: Install Python & Tools

```bash
sudo apt install -y python3 python3-pip python3-venv
```

Verify Installation:

```bash
python3 --version
pip3 --version
```

---

## 🔹 Step 3: Create Project Workspace

```bash
mkdir -p ~/fastapi-policy-service

cd ~/fastapi-policy-service
```

---

## 🔹 Step 4: Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 🔹 Step 5: Install Dependencies

```bash
pip install fastapi uvicorn pydantic psutil
```

Verify:

```bash
pip list
```

Expected packages:

```text
fastapi
uvicorn
pydantic
psutil
```

---

# 🚀 Task 1: Build the FastAPI Service

---

# 📁 Project Structure

Create the application files:

```bash
touch main.py
touch models.py
touch policies.py
touch config.py
```

Project Layout:

```text
fastapi-policy-service/
│
├── main.py
├── models.py
├── policies.py
├── config.py
│
├── venv/
│
└── README.md
```

---

# ⚙️ Step 1: Create Configuration Settings

Create:

```bash
nano config.py
```

Purpose:

✅ Centralized configuration

✅ Policy settings

✅ Resource thresholds

✅ API metadata

---

## Resource Limits

```python
RESOURCE_LIMITS = {
    "cpu_percent": 80.0,
    "memory_percent": 85.0,
    "disk_percent": 90.0
}
```

---

## Policy Rules

```python
POLICY_RULES = {
    "max_request_size": 1048576,
    "allowed_methods": [
        "GET",
        "POST",
        "PUT",
        "DELETE"
    ],
    "rate_limit_per_minute": 100
}
```

---

## API Configuration

```python
API_CONFIG = {
    "title": "Status and Policy Service",
    "version": "1.0.0",
    "description": "System monitoring and policy enforcement API"
}
```

---

# 📦 Step 2: Create Data Models

Create:

```bash
nano models.py
```

---

## Available Models

### ✅ SystemStatus

Tracks:

- CPU Usage
- Memory Usage
- Disk Usage
- Overall Health Status

---

### ✅ PolicyCheckRequest

Required Fields:

```python
request_size: int
method: str
user_id: str
```

---

### ✅ PolicyCheckResponse

Required Fields:

```python
allowed: bool
reason: str
policy_name: str
```

---

### ✅ HealthResponse

Provides:

```python
status
timestamp
service_name
```

---

# 🛡️ Step 3: Implement Policy Logic

Create:

```bash
nano policies.py
```

---

# 🔹 System Health Monitoring

Use:

```python
psutil.cpu_percent()
```

```python
psutil.virtual_memory().percent
```

```python
psutil.disk_usage('/').percent
```

---

## Health Classification Logic

```text
CPU > Limit
OR
Memory > Limit
OR
Disk > Limit

= CRITICAL
```

---

```text
Resource Usage > 70%

= WARNING
```

---

```text
Below Thresholds

= HEALTHY
```

---

# 🔹 Request Size Validation

Policy:

```python
POLICY_RULES["max_request_size"]
```

Allowed:

```text
<= 1 MB
```

Denied:

```text
> 1 MB
```

---

# 🔹 HTTP Method Validation

Allowed Methods:

```text
GET
POST
PUT
DELETE
```

Denied:

```text
PATCH
OPTIONS
TRACE
```

---

# 🔹 Rate Limit Enforcement

Policy:

```python
100 requests/minute
```

Logic:

```text
Request Count <= Limit

ALLOW
```

```text
Request Count > Limit

DENY
```

---

# 🚀 Step 4: Build FastAPI Application

Create:

```bash
nano main.py
```

---

## FastAPI Initialization

```python
app = FastAPI(
    title=API_CONFIG["title"],
    version=API_CONFIG["version"],
    description=API_CONFIG["description"]
)
```

---

# 🌐 API Endpoints

---

## 🏠 Root Endpoint

```http
GET /
```

Purpose:

Basic service health response.

Returns:

```json
{
  "status": "ok"
}
```

---

## ❤️ Health Endpoint

```http
GET /health
```

Returns:

```json
{
  "status": "ok",
  "timestamp": "2026-06-04T10:00:00"
}
```

---

## 📊 System Status Endpoint

```http
GET /status
```

Returns:

```json
{
  "cpu_percent": 20.5,
  "memory_percent": 45.2,
  "disk_percent": 30.1,
  "status": "healthy"
}
```

---

## 🛡️ Policy Validation Endpoint

```http
POST /policy/check
```

Request:

```json
{
  "request_size": 1024,
  "method": "GET",
  "user_id": "user123"
}
```

Response:

```json
{
  "allowed": true,
  "reason": "Request allowed",
  "policy_name": "combined_policy"
}
```

---

## 📋 Policies Endpoint

```http
GET /policies
```

Returns:

```json
{
  "max_request_size": 1048576,
  "allowed_methods": [
    "GET",
    "POST",
    "PUT",
    "DELETE"
  ]
}
```

---

## ⚙️ Resource Limits Endpoint

```http
GET /limits
```

Returns:

```json
{
  "cpu_percent": 80,
  "memory_percent": 85,
  "disk_percent": 90
}
```

---

# 🔍 Step 5: Middleware Logging

Middleware should:

✅ Log HTTP Method

✅ Log Request Path

✅ Log Status Code

---

## Request Flow

```text
Client Request
      │
      ▼

Middleware Logging
      │
      ▼

Endpoint Processing
      │
      ▼

Response Generated
      │
      ▼

Status Logged
      │
      ▼

Client Response
```

---

# 🚀 Task 2: Run the Service

---

## Activate Virtual Environment

```bash
source ~/fastapi-policy-service/venv/bin/activate
```

---

## Start FastAPI Service

```bash
python3 main.py
```

Expected:

```text
INFO: Uvicorn running on http://0.0.0.0:8000
```

---

# 🧪 API Testing

---

## Test Health Endpoint

```bash
curl http://localhost:8000/health
```

---

## Test System Status

```bash
curl http://localhost:8000/status
```

---

## Test Valid Policy Request

```bash
curl -X POST http://localhost:8000/policy/check \
-H "Content-Type: application/json" \
-d '{
  "request_size": 1024,
  "method": "GET",
  "user_id": "user123"
}'
```

Expected:

```json
{
  "allowed": true
}
```

---

## Test Oversized Request

```bash
curl -X POST http://localhost:8000/policy/check \
-H "Content-Type: application/json" \
-d '{
  "request_size": 2000000,
  "method": "GET",
  "user_id": "user123"
}'
```

Expected:

```json
{
  "allowed": false
}
```

---

## Test Invalid HTTP Method

```bash
curl -X POST http://localhost:8000/policy/check \
-H "Content-Type: application/json" \
-d '{
  "request_size": 1000,
  "method": "PATCH",
  "user_id": "user123"
}'
```

Expected:

```json
{
  "allowed": false
}
```

---

## List Policies

```bash
curl http://localhost:8000/policies
```

---

## Resource Limits

```bash
curl http://localhost:8000/limits
```

---

# 📚 Interactive API Documentation

FastAPI automatically generates Swagger UI.

Open:

```text
http://localhost:8000/docs
```

Features:

✅ Interactive Testing

✅ Request Validation

✅ Schema Documentation

✅ Endpoint Discovery

---

# ✅ Verification

---

## Health Check

```bash
curl http://localhost:8000/health | jq
```

Expected:

```json
{
  "status": "ok"
}
```

---

## System Status

```bash
curl http://localhost:8000/status | jq
```

Expected:

```json
{
  "cpu_percent": 25.1,
  "memory_percent": 40.5,
  "disk_percent": 31.2,
  "status": "healthy"
}
```

---

## Policy Validation

Valid:

```json
{
  "allowed": true
}
```

Invalid:

```json
{
  "allowed": false
}
```

---

# 🎯 Expected Outcomes

After completing this lab, you should have:

✅ FastAPI REST Service

✅ Health Monitoring API

✅ Resource Usage Monitoring

✅ Policy Enforcement Engine

✅ Middleware Logging

✅ Request Validation

✅ Interactive API Documentation

---

# 🏆 Success Criteria

| Requirement | Status |
|------------|---------|
| FastAPI Running | ✅ |
| Health Endpoint Working | ✅ |
| Status Endpoint Working | ✅ |
| Policy Checks Working | ✅ |
| Middleware Logging Working | ✅ |
| Swagger Documentation Available | ✅ |

---

# 📋 Verification Checklist

- [ ] FastAPI installed
- [ ] Uvicorn installed
- [ ] psutil installed
- [ ] Configuration created
- [ ] Models implemented
- [ ] Policies implemented
- [ ] Middleware implemented
- [ ] Health endpoint working
- [ ] Status endpoint working
- [ ] Policy validation working
- [ ] Swagger docs accessible

---

# 🛠️ Troubleshooting

---

## ❌ Service Won't Start

Check port:

```bash
sudo lsof -i :8000
```

Kill process:

```bash
sudo kill -9 <PID>
```

---

## ❌ Import Errors

Verify dependencies:

```bash
pip list | grep -E "fastapi|uvicorn|pydantic|psutil"
```

Reinstall:

```bash
pip install --upgrade fastapi uvicorn pydantic psutil
```

---

## ❌ Policy Validation Fails

Verify:

```python
PolicyCheckRequest
```

Matches:

```json
{
  "request_size": 100,
  "method": "GET",
  "user_id": "abc"
}
```

---

## ❌ psutil Errors

Test manually:

```bash
python3 -c "import psutil; print(psutil.cpu_percent())"
```

---

## ❌ Middleware Not Logging

Add debugging:

```python
print(request.method)
print(request.url.path)
```

---

# 🎓 DevOps Best Practices

### ✅ Monitor Resource Usage

Track CPU, memory, and disk continuously.

---

### ✅ Enforce Policies Centrally

Keep business and operational rules in one location.

---

### ✅ Log All Requests

Essential for observability and troubleshooting.

---

### ✅ Validate Inputs

Prevent invalid data from entering the system.

---

### ✅ Expose Health Endpoints

Required for Kubernetes and cloud-native deployments.

---

### ✅ Use Configuration Files

Avoid hardcoding operational values.

---

# 🚀 Conclusion

Congratulations! 🎉

You have successfully built a **FastAPI Status and Policy Service**.

### Features Implemented

🔹 FastAPI REST Endpoints

🔹 System Health Monitoring

🔹 Resource Usage Tracking

🔹 Request Policy Validation

🔹 Middleware Logging

🔹 Swagger API Documentation

### Real-World Applications

✅ API Gateways

✅ Service Meshes

✅ Cloud Monitoring Services

✅ Kubernetes Health Checks

✅ DevOps Observability Platforms

✅ Microservice Architectures

### Key Takeaways

- FastAPI enables rapid API development.
- Health endpoints improve service reliability.
- Policy enforcement protects systems.
- Middleware enhances observability.
- Monitoring is a core DevOps practice.

These patterns are widely used in production environments for scalable and reliable cloud-native applications.

---

# 🏆 Lab Completed Successfully

### FastAPI Status and Policy Service ✔️

🚀 FastAPI • Monitoring • Policy Enforcement • DevOps Excellence
