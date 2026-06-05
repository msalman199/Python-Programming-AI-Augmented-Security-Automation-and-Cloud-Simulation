 
# 🌐 Resilient HTTP Client Library 

<p align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-HTTP_Client-2CA5E0?style=for-the-badge)
![REST API](https://img.shields.io/badge/REST-API_Integration-009688?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![DevOps](https://img.shields.io/badge/DevOps-Reliability-blueviolet?style=for-the-badge)
![Circuit Breaker](https://img.shields.io/badge/Circuit_Breaker-Pattern-success?style=for-the-badge)

</p>

---

# 📖 Overview

In this lab, you will build a **Production-Ready Resilient HTTP Client Library** using Python.

The client will include:

✅ Retry Logic

✅ Exponential Backoff

✅ Timeout Handling

✅ Error Classification

✅ Circuit Breaker Pattern

✅ Production-Grade Reliability Features

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- Implement retry logic for failed requests
- Configure exponential backoff strategies
- Handle timeouts effectively
- Classify retryable vs non-retryable errors
- Build a reusable HTTP client wrapper
- Implement Circuit Breaker protection

---

# 📋 Prerequisites

Before starting, ensure you have:

- Basic Python programming knowledge
- Understanding of HTTP requests and responses
- Familiarity with Linux commands
- Basic REST API knowledge
- Understanding of Python exceptions

---

# 🛠️ Environment Setup

---

## 🔹 Step 1: Verify Python Installation

```bash
python3 --version
```

Expected Output:

```text
Python 3.8+
```

---

## 🔹 Step 2: Install Required Package

```bash
pip3 install requests
```

Verify Installation:

```bash
pip3 show requests
```

---

## 🔹 Step 3: Create Project Workspace

```bash
mkdir -p ~/resilient-http-lab

cd ~/resilient-http-lab
```

---

# 🚀 Task 1: Build the Resilient HTTP Client

---

## 🔹 Step 1: Create Base Client

Create:

```bash
nano resilient_client.py
```

---

## 📦 Client Features

The client should provide:

| Feature | Description |
|----------|-------------|
| Retry Logic | Automatic retry on failures |
| Backoff Strategy | Exponential delay increase |
| Timeout Protection | Prevent hanging requests |
| Error Classification | Retry only appropriate failures |
| Session Reuse | Better performance |
| Circuit Breaker Ready | Future integration |

---

## 🔹 Client Skeleton

```python
import requests
import time
from typing import Optional, Dict, Any
from requests.exceptions import RequestException, Timeout, ConnectionError

class ResilientHTTPClient:
    """
    Production-ready resilient HTTP client.
    """

    def __init__(
        self,
        max_retries: int = 3,
        base_timeout: int = 5,
        backoff_factor: float = 2.0
    ):
        self.max_retries = max_retries
        self.base_timeout = base_timeout
        self.backoff_factor = backoff_factor
        self.session = requests.Session()
```

---

## 🔹 Implement Exponential Backoff

### Formula

```python
delay = base_delay * (backoff_factor ** attempt)
```

Where:

```text
Attempt 0 = 1 second
Attempt 1 = 2 seconds
Attempt 2 = 4 seconds
Attempt 3 = 8 seconds
```

---

## 🔹 Retry Rules

Retry On:

✅ Timeout

✅ ConnectionError

✅ HTTP 429

✅ HTTP 500

✅ HTTP 502

✅ HTTP 503

✅ HTTP 504

Do Not Retry:

❌ HTTP 400

❌ HTTP 401

❌ HTTP 403

❌ HTTP 404

❌ Successful Responses

---

## 🔹 Request Workflow

```text
Request
   │
   ▼
Success?
   │
 ┌─┴─┐
 │Yes│
 └─┬─┘
   ▼
 Return Response

No
 │
 ▼
Retry Allowed?
 │
 ┌─┴─┐
 │Yes│
 └─┬─┘
   ▼
Backoff Delay
   │
   ▼
Retry

No
 │
 ▼
Raise Exception
```

---

# 🧪 Step 2: Create Test Client

Create:

```bash
nano test_client.py
```

---

## Test Scenarios

### ✅ Successful Request

Endpoint:

```text
https://httpbin.org/get
```

Verify:

- Status code
- JSON response
- Headers

---

### ✅ Timeout Handling

Endpoint:

```text
https://httpbin.org/delay/5
```

Client:

```python
base_timeout=1
```

Observe:

- Timeout exception
- Retry attempts
- Backoff delays

---

### ✅ Retry on Failure

Endpoint:

```text
http://invalid-domain-12345.com
```

Observe:

- Connection errors
- Retry logic
- Final failure

---

### ✅ POST Request Testing

Endpoint:

```text
https://httpbin.org/post
```

Payload:

```json
{
  "service": "devops",
  "status": "active"
}
```

Verify:

- Request succeeds
- JSON echoed back

---

# 📚 Implementation Hints

---

## Exponential Backoff

```python
delay = 1 * (2 ** attempt)
```

Produces:

```text
1s
2s
4s
8s
```

---

## Retry Loop

```python
for attempt in range(self.max_retries + 1):
    try:
        ...
    except Exception as e:
        ...
```

---

## Timeout Usage

```python
response = self.session.get(
    url,
    timeout=self.base_timeout
)
```

---

# 🚀 Task 2: Add Advanced Features

---

# 🔥 Circuit Breaker Pattern

---

## 🔹 Create Circuit Breaker

Create:

```bash
nano circuit_breaker.py
```

---

## Circuit States

```text
CLOSED
│
├── Normal Operation

OPEN
│
├── Reject Requests

HALF_OPEN
│
└── Recovery Testing
```

---

## State Diagram

```text
          Failure Threshold
      ┌──────────────────────┐
      ▼                      │

   CLOSED ───────────────► OPEN
      ▲                      │
      │                      │
      │ Recovery Timeout     │
      │                      ▼

      └──────── HALF_OPEN ◄──┘
                 │
          Success Threshold
                 │
                 ▼

               CLOSED
```

---

## Circuit Breaker Responsibilities

### CLOSED

✔ Allow Requests

✔ Track Failures

---

### OPEN

❌ Reject Requests

❌ Prevent Service Overload

---

### HALF_OPEN

✔ Allow Limited Requests

✔ Test Recovery

---

# 🔗 Integrate Circuit Breaker

Update:

```python
from circuit_breaker import CircuitBreaker
```

Initialize:

```python
self.circuit_breaker = CircuitBreaker()
```

Wrap Calls:

```python
self.circuit_breaker.call(...)
```

---

# 🧪 Create Advanced Tests

Create:

```bash
nano test_advanced.py
```

---

## Test Circuit Breaker

Verify:

- Failure threshold reached
- Circuit opens
- Requests blocked
- Recovery timeout respected
- Circuit closes after recovery

---

## Test Rate Limiting

Simulate:

```text
HTTP 429
```

Verify:

- Retries occur
- Backoff applied
- Eventual success/failure

---

# ✅ Verification

---

## Run Main Tests

```bash
python3 test_client.py
```

Expected:

```text
Test 1 → Success (200)

Test 2 → Retry + Timeout

Test 3 → Retry + Failure

Test 4 → Successful POST
```

---

## Create Verification Script

```bash
nano verify.py
```

Example:

```python
from resilient_client import ResilientHTTPClient

client = ResilientHTTPClient(
    max_retries=3,
    base_timeout=2
)

print("Backoff delays:")

for i in range(4):
    print(client._calculate_backoff(i))
```

---

## Run Verification

```bash
python3 verify.py
```

Expected:

```text
Attempt 0: 1s

Attempt 1: 2s

Attempt 2: 4s

Attempt 3: 8s
```

---

## Run Advanced Tests

```bash
python3 test_advanced.py
```

Verify:

✅ Backoff delays

✅ Circuit breaker transitions

✅ Timeout enforcement

✅ Error handling

---

# 📊 Client Architecture

```text
                Application
                      │
                      ▼

        Resilient HTTP Client Wrapper
                      │
      ┌───────────────┼───────────────┐
      │               │               │

      ▼               ▼               ▼

 Retry Logic     Timeouts      Error Handling

      │               │               │
      └───────────────┼───────────────┘
                      │

                      ▼

             Circuit Breaker

                      │

                      ▼

                External API
```

---

# 🎯 Expected Outcomes

After completing this lab you should have:

✅ Resilient HTTP Client

✅ Retry Logic

✅ Exponential Backoff

✅ Timeout Management

✅ Circuit Breaker Integration

✅ Production-Ready API Wrapper

---

# 🏆 Success Criteria

| Requirement | Target |
|------------|---------|
| Retry Logic | Implemented |
| Backoff Strategy | Exponential |
| Timeout Handling | Configurable |
| Error Classification | Working |
| Circuit Breaker | Functional |
| Tests Passing | Yes |

---

# 📋 Verification Checklist

- [ ] requests package installed
- [ ] resilient_client.py created
- [ ] retry logic implemented
- [ ] exponential backoff implemented
- [ ] timeout handling working
- [ ] POST requests supported
- [ ] circuit_breaker.py created
- [ ] circuit breaker integrated
- [ ] verification script passing
- [ ] advanced tests passing

---

# 🛠️ Troubleshooting

---

## ❌ Import Errors

Verify files exist:

```bash
ls -la ~/resilient-http-lab/
```

Expected:

```text
resilient_client.py
circuit_breaker.py
test_client.py
test_advanced.py
```

---

## ❌ Requests Timeout Immediately

Increase timeout:

```python
base_timeout=10
```

Check connectivity:

```bash
curl https://httpbin.org/get
```

Check DNS:

```bash
nslookup httpbin.org
```

---

## ❌ Circuit Breaker Not Triggering

Add debug output:

```python
print(f"State={self.state}")
```

Verify:

- Failure threshold reached
- Recovery timeout elapsed

---

## ❌ Backoff Not Exponential

Verify:

```python
delay = 1 * (2 ** attempt)
```

Output:

```text
1
2
4
8
16
```

---

# 🎓 DevOps Best Practices

### ✅ Retry Intelligently

Not every error should be retried.

---

### ✅ Use Exponential Backoff

Prevents overwhelming services.

---

### ✅ Set Timeouts

Never wait indefinitely.

---

### ✅ Implement Circuit Breakers

Protect systems from cascading failures.

---

### ✅ Monitor Failures

Track retries and exceptions.

---

### ✅ Design for Failure

Network failures are normal in distributed systems.

---

# 🚀 Conclusion

Congratulations! 🎉

You have successfully built a **Production-Ready Resilient HTTP Client Library**.

### Features Implemented

🔹 Retry Logic

🔹 Exponential Backoff

🔹 Timeout Handling

🔹 Error Classification

🔹 Circuit Breaker Pattern

🔹 API Reliability Controls

### Real-World Applications

✅ Microservices Communication

✅ Cloud Automation

✅ CI/CD Pipelines

✅ Infrastructure Monitoring

✅ External API Integrations

✅ DevOps Automation Tools

### Key Takeaways

- Network failures are inevitable
- Retries improve reliability
- Exponential backoff protects services
- Circuit breakers prevent cascading failures
- Timeouts improve responsiveness

These patterns are foundational building blocks for modern distributed systems and production-grade DevOps automation.

---

# 🏆 Lab Completed Successfully

### Resilient HTTP Client Library Lab ✔️

🌐 Reliable Requests • Resilient Systems • Better Automation 🚀
````
