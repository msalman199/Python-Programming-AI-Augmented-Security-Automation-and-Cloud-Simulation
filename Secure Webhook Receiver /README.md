# 🔐 Secure Webhook Receiver 

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge\&logo=flask)
![JSONSchema](https://img.shields.io/badge/JSONSchema-Validation-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-HMAC--SHA256-red?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Webhooks-orange?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-yellow?style=for-the-badge\&logo=linux)

---

# 🎯 Secure Webhook Receiver

## 📖 Overview

In modern DevOps environments, webhooks enable real-time communication between systems such as GitHub, GitLab, Stripe, PagerDuty, and monitoring platforms.

This lab guides you through building a secure webhook receiver capable of:

* ✅ Verifying webhook signatures using HMAC-SHA256
* ✅ Validating incoming JSON payloads
* ✅ Logging webhook events securely
* ✅ Implementing webhook security best practices
* ✅ Handling invalid requests safely

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

* Basic understanding of HTTP and REST APIs
* Familiarity with Python programming
* Knowledge of HMAC and SHA256 hashing
* Linux command-line experience
* Understanding of JSON structures

---

# 🎯 Learning Objectives

By completing this lab, you will:

* Implement HMAC signature verification
* Validate payloads using JSON Schema
* Create secure webhook event logging
* Handle malformed or unauthorized requests
* Apply production-grade webhook security controls

---

# 🖥️ Environment Setup

## Step 1: Update System

```bash
sudo apt update
```

---

## Step 2: Install Python

```bash
sudo apt install -y python3 python3-pip python3-venv
```

---

## Step 3: Create Project Directory

```bash
mkdir -p ~/webhook-receiver
cd ~/webhook-receiver
```

---

## Step 4: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 5: Install Required Packages

```bash
pip install flask jsonschema
```

---

# 🏗️ Task 1: Build Secure Webhook Receiver

---

## 🔹 Step 1: Create Application Structure

Create the main webhook server:

```bash
touch webhook_server.py
```

---

## 🔹 Step 2: Configure Flask Application

The application will:

* Listen for webhook events
* Verify signatures
* Validate payloads
* Log events securely

Core components:

```python
from flask import Flask, request, jsonify
import hmac
import hashlib
import logging
from jsonschema import validate
```

---

## 🔹 Step 3: Configure Security Settings

```python
WEBHOOK_SECRET = "your-secret-key-change-this"
LOG_FILE = "webhook_events.log"
```

⚠️ Never hardcode secrets in production.

Use:

```bash
export WEBHOOK_SECRET=super-secret-key
```

---

# 🔐 Task 2: Implement HMAC Signature Verification

---

## Why Signature Verification?

Webhook signatures ensure:

* Request originated from trusted sender
* Payload was not modified in transit
* Protection against spoofed requests

---

## Expected Header Format

```http
X-Hub-Signature-256: sha256=<signature>
```

---

## HMAC Verification Logic

```python
expected_signature = hmac.new(
    key=WEBHOOK_SECRET.encode(),
    msg=payload_body,
    digestmod=hashlib.sha256
).hexdigest()
```

---

## Secure Comparison

Always use:

```python
hmac.compare_digest()
```

instead of:

```python
==
```

This prevents timing attacks.

---

# 📦 Task 3: Payload Validation

---

## Why Validate Payloads?

Protects against:

* Malformed requests
* Missing fields
* Unexpected structures
* Injection attempts

---

## Example Schema

```python
schema = {
    "type": "object",
    "properties": {
        "event": {"type": "string"},
        "timestamp": {"type": "string"},
        "data": {"type": "object"}
    },
    "required": ["event", "timestamp", "data"]
}
```

---

## Validation Example

```python
try:
    validate(instance=payload, schema=schema)
    return True
except ValidationError:
    return False
```

---

# 📝 Task 4: Secure Logging

---

## Logging Requirements

Store:

* Timestamp
* Event Type
* Status
* Non-sensitive metadata

Avoid:

* Passwords
* Tokens
* API Keys
* Authentication Headers

---

## Example Log Entry

```json
{
  "timestamp": "2026-06-05T12:00:00",
  "event_type": "user.created",
  "status": "success"
}
```

---

## Logging Configuration

```python
logging.basicConfig(
    filename="webhook_events.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```

---

# ⚙️ Task 5: Implement Webhook Handler

---

## Processing Workflow

```text
Receive Request
      │
      ▼
Verify Signature
      │
      ▼
Validate Payload
      │
      ▼
Process Event
      │
      ▼
Log Event
      │
      ▼
Return Response
```

---

## Success Response

```json
{
  "status": "success",
  "message": "Webhook received"
}
```

HTTP Status:

```http
200 OK
```

---

## Invalid Signature Response

```json
{
  "error": "Invalid signature"
}
```

HTTP Status:

```http
401 Unauthorized
```

---

## Invalid Payload Response

```json
{
  "error": "Invalid payload"
}
```

HTTP Status:

```http
400 Bad Request
```

---

# 🧪 Task 6: Create Test Client

---

## Create Testing Script

```bash
touch test_webhook.py
```

---

## Test Scenarios

### ✅ Test 1: Valid Webhook

```json
{
  "event": "user.created",
  "timestamp": "2026-06-05T12:00:00",
  "data": {
    "user_id": "12345"
  }
}
```

Expected:

```http
200 OK
```

---

### ❌ Test 2: Invalid Signature

Expected:

```http
401 Unauthorized
```

---

### ❌ Test 3: Invalid Payload

```json
{
  "wrong_field": "value"
}
```

Expected:

```http
400 Bad Request
```

---

# 🚀 Task 7: Run Webhook Server

## Terminal 1

```bash
cd ~/webhook-receiver
source venv/bin/activate
python3 webhook_server.py
```

Expected:

```text
* Running on http://0.0.0.0:5000
```

---

# 🧪 Task 8: Execute Tests

## Terminal 2

```bash
cd ~/webhook-receiver
source venv/bin/activate
python3 test_webhook.py
```

---

Expected Results:

| Test              | Expected Status |
| ----------------- | --------------- |
| Valid Webhook     | 200             |
| Invalid Signature | 401             |
| Invalid Payload   | 400             |

---

# 📊 Task 9: Verify Logs

View log entries:

```bash
cat webhook_events.log
```

Expected:

```text
INFO - user.created - success
ERROR - signature verification failed
ERROR - payload validation failed
```

---

# ✅ Verification

## Check 1: Health Endpoint

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

## Check 2: Signature Validation

```bash
curl -X POST http://localhost:5000/webhook \
-H "Content-Type: application/json" \
-d '{"event":"test"}'
```

Expected:

```http
401 Unauthorized
```

---

## Check 3: Log Verification

```bash
tail -n 20 webhook_events.log
```

Verify:

* Timestamp exists
* Event type exists
* Success/failure logged
* No sensitive information stored

---

## Check 4: Payload Validation

Verify:

* Required fields enforced
* Schema validation working
* Invalid requests rejected

---

# 📈 Security Best Practices

## ✅ Verify Every Webhook

Never trust incoming requests without validation.

---

## ✅ Use Constant-Time Comparison

```python
hmac.compare_digest()
```

Prevents timing attacks.

---

## ✅ Validate Input

Use JSON schemas to reject malformed payloads.

---

## ✅ Sanitize Logs

Never store:

* Passwords
* Secrets
* API Keys
* Tokens

---

## ✅ Return Proper Status Codes

| Status | Meaning           |
| ------ | ----------------- |
| 200    | Success           |
| 400    | Invalid Payload   |
| 401    | Invalid Signature |
| 500    | Internal Error    |

---

# 🛠️ Troubleshooting

## Issue: Signature Always Fails

### Verify Secret

Server:

```python
WEBHOOK_SECRET
```

Client:

```python
SECRET
```

Must match exactly.

---

## Issue: Missing Dependencies

```bash
source venv/bin/activate

pip install flask jsonschema
```

---

## Issue: Port Already In Use

Find process:

```bash
sudo lsof -i :5000
```

Kill process:

```bash
sudo kill -9 PID
```

Or use another port:

```python
app.run(port=5001)
```

---

## Issue: Log File Not Created

Verify permissions:

```bash
ls -l webhook_events.log
```

Check logging configuration.

---

# 🎯 Expected Outcomes

After completing this lab you should have:

✅ Working Flask webhook server

✅ HMAC-SHA256 signature verification

✅ JSON schema validation

✅ Structured security-focused logging

✅ Secure webhook processing pipeline

✅ Automated webhook testing client

---

# 📚 Real-World Use Cases

## GitHub Webhooks

```text
Push Events
Pull Requests
Issue Tracking
CI/CD Triggers
```

---

## Payment Providers

```text
Stripe
PayPal
Square
```

---

## Monitoring Systems

```text
PagerDuty
Datadog
Prometheus Alertmanager
```

---

## CI/CD Platforms

```text
GitLab
Jenkins
Azure DevOps
GitHub Actions
```

---

# 🎓 Key Takeaways

### Security First

Always verify signatures before processing data.

### Validate Everything

External input should never be trusted.

### Log Safely

Maintain audit trails while protecting sensitive information.

### Use Proper HTTP Responses

Clear status codes improve reliability and troubleshooting.

### Design for Production

Webhook endpoints are critical integration points and must be secured.

---

# 🚀 Next Steps

### Advanced Security

* Replay attack prevention
* Timestamp validation
* Nonce tracking

### Reliability Improvements

* Retry queues
* Dead-letter processing
* Persistent storage

### Scalability

* Async webhook processing
* Message queues
* Worker-based architecture

### Monitoring

* Prometheus metrics
* Grafana dashboards
* Alerting rules

---

# 🏆 Lab Completion Checklist

* [ ] Flask webhook server created
* [ ] Signature verification implemented
* [ ] JSON schema validation added
* [ ] Secure logging configured
* [ ] Test client developed
* [ ] Successful webhook processed
* [ ] Invalid signature rejected
* [ ] Invalid payload rejected
* [ ] Logs verified
* [ ] Security best practices followed

---

## 🎉 Congratulations!

You have successfully built a **Secure Webhook Receiver** capable of authenticating, validating, logging, and processing webhook events securely—an essential skill for modern DevOps, Platform Engineering, and Cloud Security roles.
