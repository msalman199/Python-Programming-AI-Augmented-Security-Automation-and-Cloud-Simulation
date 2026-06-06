# 🚀 Structured Logging and Correlation IDs

<div align="center">

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge&logo=flask)
![JSON](https://img.shields.io/badge/JSON-Structured%20Logs-000000?style=for-the-badge&logo=json)
![Logging](https://img.shields.io/badge/Logging-Observability-blue?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Monitoring-orange?style=for-the-badge)

# 📊 Structured Logging & Correlation IDs

### Observe • Trace • Debug • Analyze • Scale

Master modern observability practices by implementing structured logging and distributed request tracing using correlation IDs.

</div>

---

# 📖 Overview

Traditional text logs become difficult to analyze as applications grow into distributed systems and microservices.

Structured Logging and Correlation IDs solve this challenge by providing:

✅ Machine-readable logs

✅ Consistent log structure

✅ Cross-service request tracing

✅ Faster debugging

✅ Better observability

✅ Easier log aggregation and analysis

In this lab, you'll build a complete logging solution using JSON-formatted logs and correlation IDs that flow across multiple services.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- 🔹 Implement structured JSON logging
- 🔹 Generate and propagate correlation IDs
- 🔹 Improve traceability across services
- 🔹 Build centralized logging workflows
- 🔹 Analyze distributed application logs
- 🔹 Enhance debugging and observability

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- 🐧 Basic Linux command-line knowledge
- 🐍 Familiarity with Python programming
- 🌐 Understanding of HTTP APIs
- 📝 Knowledge of logging concepts
- 🚀 Experience with Flask or similar frameworks

---

# 🏗️ Environment Setup

You will use the Linux environment provided through the **Start Lab** button.

---

# 🔹 Install Required Tools

Update package manager:

```bash
sudo apt update
```

Install Python tools:

```bash
sudo apt install -y python3 python3-pip python3-venv
```

Create project directory:

```bash
mkdir -p ~/logging-lab

cd ~/logging-lab
```

Create virtual environment:

```bash
python3 -m venv venv

source venv/bin/activate
```

Install required packages:

```bash
pip install flask python-json-logger requests
```

---

# 🔍 Verify Installation

```bash
python --version

pip list
```

Verify installed packages:

```bash
pip show flask
pip show python-json-logger
pip show requests
```

---

# 📂 Project Structure

```text
logging-lab/
│
├── app.py
│
├── service_b.py
│
├── analyze_logs.py
│
├── logs/
│
└── venv/
```

---

# 🧩 Task 1: Implement Structured Logging

---

# 🔹 Step 1: Create Base Application

Create application file:

```bash
nano app.py
```

Purpose:

✅ Expose REST APIs

✅ Generate structured logs

✅ Attach correlation IDs

✅ Improve debugging capabilities

---

# 🔹 Structured Logging Benefits

Traditional log:

```text
User created order successfully
```

Structured JSON log:

```json
{
  "timestamp":"2025-01-01T12:00:00Z",
  "level":"INFO",
  "correlation_id":"abc123",
  "message":"Order created successfully"
}
```

Benefits:

- Machine-readable
- Searchable
- Queryable
- Easily indexed by ELK/Splunk

---

# 🔹 Step 2: Configure JSON Logger

Inside `app.py`:

```python
from pythonjsonlogger import jsonlogger
import logging
```

Create logger configuration:

```python
def setup_logging():
```

Responsibilities:

- JSON formatting
- Log level management
- Standardized output
- Centralized logging support

---

# 📊 Log Structure

Each log entry should contain:

| Field | Purpose |
|---------|----------|
| timestamp | Event time |
| level | Log severity |
| correlation_id | Request identifier |
| message | Log message |
| extra_fields | Contextual information |

---

# 🔹 Step 3: Implement Correlation ID Middleware

Create request middleware:

```python
@app.before_request
```

Responsibilities:

✅ Read incoming correlation ID

✅ Generate one if missing

✅ Store in request context

Expected header:

```http
X-Correlation-ID: abc123
```

Fallback:

```python
uuid.uuid4()
```

---

# 🔄 Correlation ID Lifecycle

```text
Incoming Request
       │
       ▼
Check Header
       │
 ┌─────┴─────┐
 │           │
Found      Missing
 │           │
 ▼           ▼
Use ID   Generate UUID
       │
       ▼
Store in Context
```

---

# 🔹 Step 4: Create Logging Helper

Implement:

```python
def log_with_context():
```

Purpose:

- Inject correlation ID
- Attach timestamps
- Include extra metadata
- Standardize logs

Example:

```python
log_with_context(
    "info",
    "User retrieved",
    endpoint="/api/users"
)
```

---

# 🔹 Step 5: Implement Users API

Endpoint:

```python
GET /api/users
```

Responsibilities:

✅ Log request arrival

✅ Simulate processing

✅ Log successful response

Return:

```json
[
  {
    "id":1,
    "name":"Alice"
  },
  {
    "id":2,
    "name":"Bob"
  }
]
```

---

# 🔹 Step 6: Implement Orders API

Endpoint:

```python
POST /api/orders
```

Responsibilities:

- Log request payload
- Validate input
- Handle errors
- Log order creation

Sample request:

```json
{
  "user_id":1,
  "amount":99.99
}
```

Sample response:

```json
{
  "order_id":"uuid",
  "user_id":1,
  "amount":99.99
}
```

---

# 🧪 Step 7: Test Structured Logging

Start application:

```bash
python app.py &
```

Wait:

```bash
sleep 2
```

Test users endpoint:

```bash
curl http://localhost:5000/api/users
```

Test order creation:

```bash
curl -X POST http://localhost:5000/api/orders \
-H "Content-Type: application/json" \
-d '{"user_id":1,"amount":99.99}'
```

---

# 📄 Expected JSON Logs

Example:

```json
{
  "timestamp":"2025-01-01T12:00:00Z",
  "level":"INFO",
  "correlation_id":"123abc",
  "message":"Users retrieved"
}
```

---

# 🧩 Task 2: Correlation ID Propagation Across Services

---

# 🔹 Step 1: Create Service B

Create:

```bash
nano service_b.py
```

Purpose:

- Simulate downstream service
- Receive correlation IDs
- Continue traceability chain

---

# 🏗️ Service Architecture

```text
Client
  │
  ▼
Service A (app.py)
  │
  ▼
Service B (service_b.py)
```

Correlation ID flows through every layer.

---

# 🔹 Step 2: Configure Logging in Service B

Implement:

```python
setup_logging()
```

Responsibilities:

✅ JSON logs

✅ Correlation ID extraction

✅ Request tracking

---

# 🔹 Step 3: Implement Inventory Endpoint

Endpoint:

```python
POST /api/inventory/check
```

Purpose:

- Check inventory
- Simulate downstream processing
- Generate logs

Response:

```json
{
  "product_id":"prod-001",
  "available":true,
  "quantity":50
}
```

---

# 🔹 Step 4: Update Main Service

Add:

```python
import requests
```

Create:

```python
POST /api/orders/full
```

Workflow:

```text
Receive Order
      │
      ▼
Call Inventory Service
      │
      ▼
Receive Response
      │
      ▼
Create Order
      │
      ▼
Return Result
```

---

# 🔹 Correlation Header Propagation

Example:

```python
headers = {
    "X-Correlation-ID": g.correlation_id
}
```

This ensures both services log the same request identifier.

---

# 🔹 Step 5: Test Correlation ID Propagation

Start Service B:

```bash
python service_b.py &
```

Wait:

```bash
sleep 2
```

Send request:

```bash
curl -X POST http://localhost:5000/api/orders/full \
-H "Content-Type: application/json" \
-H "X-Correlation-ID: test-12345" \
-d '{"product_id":"prod-001","user_id":1}'
```

Expected:

Both services should log:

```text
test-12345
```

---

# 🔄 Request Trace Example

```text
Client
  │
  ▼
Service A
  │ Correlation ID: test-12345
  ▼
Service B
  │ Correlation ID: test-12345
  ▼
Response
```

---

# 🧩 Task 3: Log Analysis and Traceability

---

# 🔹 Step 1: Create Analysis Script

Create:

```bash
nano analyze_logs.py
```

Purpose:

✅ Parse JSON logs

✅ Group by correlation ID

✅ Reconstruct request flow

✅ Simplify debugging

---

# 📊 Log Analysis Workflow

```text
Log File
    │
    ▼
Parse JSON
    │
    ▼
Group by Correlation ID
    │
    ▼
Build Request Timeline
    │
    ▼
Generate Trace Report
```

---

# 🔹 Step 2: Group Logs

Use:

```python
defaultdict(list)
```

Group entries:

```python
correlation_groups[correlation_id]
```

This allows viewing all events related to a single request.

---

# 🔹 Step 3: Display Request Flow

Output should show:

```text
Correlation ID: abc123

12:00:01 Service A Received Request

12:00:02 Service B Inventory Check

12:00:03 Service A Order Created
```

---

# 🧪 Verification

---

# 🔹 Verify Structured Logging

```bash
curl http://localhost:5000/api/users
```

Check output:

```bash
grep correlation_id
```

Expected fields:

```text
timestamp
level
correlation_id
message
```

---

# 🔹 Verify Correlation Propagation

Generate ID:

```bash
CORRELATION_ID="verify-$(date +%s)"
```

Send request:

```bash
curl -X POST http://localhost:5000/api/orders/full \
-H "Content-Type: application/json" \
-H "X-Correlation-ID: $CORRELATION_ID" \
-d '{"product_id":"test-prod","user_id":1}'
```

Expected:

Both services contain same correlation ID.

---

# 🔹 Verify Service Availability

Check running services:

```bash
ps aux | grep python
```

Verify ports:

```bash
netstat -tlnp | grep -E '5000|5001'
```

Expected:

```text
5000 LISTEN
5001 LISTEN
```

---

# 🔹 Verify Traceability

Generate requests:

```bash
for i in {1..3}; do
  curl -X POST \
  http://localhost:5000/api/orders/full \
  -H "Content-Type: application/json" \
  -d "{\"product_id\":\"prod-$i\",\"user_id\":$i}"
done
```

Expected:

Three unique correlation IDs.

---

# 📊 Expected Outcomes

After completing this lab, you should have:

### ✅ Structured JSON Logging

Machine-readable logs with consistent fields.

### ✅ Correlation ID System

Automatic ID generation and propagation.

### ✅ Request Traceability

Track requests across multiple services.

### ✅ Log Analysis Capability

Group and analyze logs using correlation IDs.

### ✅ Improved Observability

Faster debugging and troubleshooting.

---

# 🛠 Troubleshooting

---

## ❌ Logs Not JSON Formatted

Verify package:

```bash
pip show python-json-logger
```

Check formatter:

```python
jsonlogger.JsonFormatter()
```

---

## ❌ Correlation IDs Missing

Verify middleware:

```python
@app.before_request
```

Check header:

```http
X-Correlation-ID
```

Verify:

```python
g.correlation_id
```

---

## ❌ Service Communication Fails

Verify ports:

```bash
netstat -tlnp
```

Check services:

```bash
ps aux | grep python
```

---

## ❌ Missing Log Fields

Ensure:

```python
extra={}
```

contains:

```python
correlation_id
timestamp
```

---

## ❌ Service B Not Receiving Requests

Test manually:

```bash
curl http://localhost:5001/api/inventory/check
```

Verify:

```python
requests.post(...)
```

configuration.

---

# 🎓 Key Takeaways

✅ Structured logs are machine-readable and searchable

✅ Correlation IDs enable distributed tracing

✅ JSON logs improve observability

✅ Request tracking simplifies debugging

✅ Log analysis helps identify bottlenecks

✅ Distributed systems require consistent tracing strategies

✅ Modern DevOps relies heavily on structured telemetry

---

# 🚀 Real-World Applications

These practices are widely used in:

- 🔹 Kubernetes
- 🔹 Dockerized Applications
- 🔹 AWS CloudWatch
- 🔹 Azure Monitor
- 🔹 Google Cloud Logging
- 🔹 ELK Stack
- 🔹 Splunk
- 🔹 Datadog
- 🔹 OpenTelemetry
- 🔹 Jaeger

---

# 🏆 Lab Completed Successfully

You have successfully:

✔ Implemented structured JSON logging

✔ Built correlation ID middleware

✔ Propagated IDs across services

✔ Created distributed tracing capabilities

✔ Improved observability

✔ Enhanced debugging workflows

✔ Built log analysis tooling

✔ Applied production-grade logging best practices

---

<div align="center">

# 🌟 Observe Better • Trace Faster • Debug Smarter 🌟

### Happy Learning & Happy DevOps 🚀

</div>
