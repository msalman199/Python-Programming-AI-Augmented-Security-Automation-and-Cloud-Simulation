# 🚀 Smoke Test Pipeline

<div align="center">

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git)
![Node.js](https://img.shields.io/badge/Node.js-18.x-339933?style=for-the-badge&logo=node.js)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash)
![CI/CD](https://img.shields.io/badge/CI/CD-Automation-blue?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Pipeline-orange?style=for-the-badge)

# 🔥 Smoke Test Pipeline Lab

### Deploy • Validate • Report • Notify • Automate

Build a complete deployment validation pipeline with automated smoke testing, reporting, and failure notifications.

</div>

---

# 📖 Overview

In modern DevOps environments, successful deployment does not guarantee a working application.

Smoke Tests provide a fast and reliable way to verify that:

✅ Applications start successfully

✅ Critical APIs are available

✅ Core functionality works

✅ Response times remain acceptable

✅ Deployment health is validated automatically

This lab demonstrates how to build a complete smoke testing pipeline that validates deployments immediately after release.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- 🔹 Implement automated smoke tests
- 🔹 Create deployment validation pipelines
- 🔹 Test API health and functionality
- 🔹 Generate deployment reports
- 🔹 Configure failure notifications
- 🔹 Integrate smoke tests into DevOps workflows

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- 🐧 Basic Linux command-line knowledge
- 🌳 Understanding of Git basics
- 📝 Familiarity with Shell Scripting
- 🔄 Basic CI/CD concepts
- 🌐 Experience with Web Applications

---

# 🏗️ Environment Setup

You will use the Linux machine provided by Al Nafi through the **Start Lab** button.

---

# 🔹 Install Required Tools

Update packages:

```bash
sudo apt update
```

Install Git:

```bash
sudo apt install -y git
```

Install Curl & jq:

```bash
sudo apt install -y curl jq
```

Install Node.js:

```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

sudo apt install -y nodejs
```

Verify installation:

```bash
git --version
curl --version
node --version
npm --version
```

Expected:

```text
git version 2.x.x
curl 8.x.x
v18.x.x
9.x.x
```

---

# 📂 Project Structure

```text
smoke-test-lab/
│
├── app/
│   └── server.js
│
├── tests/
│   ├── smoke_tests.sh
│   ├── smoke_tests_complete.sh
│   └── notify_failure.sh
│
├── reports/
│
├── deploy.sh
│
├── pipeline.sh
│
└── pipeline_complete.sh
```

---

# 🧩 Task 1: Create Sample Application and Deployment Script

---

# 🔹 Step 1: Create Project Structure

```bash
mkdir -p ~/smoke-test-lab

cd ~/smoke-test-lab

mkdir -p app
mkdir -p tests
mkdir -p reports
```

Verify:

```bash
tree .
```

Expected:

```text
app/
tests/
reports/
```

---

# 🔹 Step 2: Create Web Application

Create application:

```bash
nano app/server.js
```

Paste:

```javascript
const http = require('http');

const PORT = 3000;
let appStatus = 'healthy';

const server = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'application/json');

  if (req.url === '/health') {
    res.writeHead(200);
    res.end(JSON.stringify({
      status: 'ok',
      timestamp: new Date().toISOString()
    }));
  }

  else if (req.url === '/api/data') {
    res.writeHead(200);
    res.end(JSON.stringify({
      message: 'Data endpoint',
      version: '1.0.0'
    }));
  }

  else if (req.url === '/api/status') {
    res.writeHead(200);
    res.end(JSON.stringify({
      status: appStatus,
      uptime: process.uptime()
    }));
  }

  else {
    res.writeHead(404);
    res.end(JSON.stringify({
      error: 'Not found'
    }));
  }
});

server.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
```

---

# 🌐 Application Endpoints

| Endpoint | Purpose |
|-----------|----------|
| `/health` | Health Check |
| `/api/data` | Sample API Data |
| `/api/status` | Application Status |

---

# 🔹 Step 3: Create Deployment Script

Create deployment script:

```bash
nano deploy.sh
```

Paste:

```bash
#!/bin/bash

echo "Starting deployment..."

pkill -f "node app/server.js" 2>/dev/null || true

sleep 2

cd ~/smoke-test-lab

nohup node app/server.js > app.log 2>&1 &

sleep 3

echo "Deployment completed"

echo "Application PID: $(pgrep -f 'node app/server.js')"
```

Make executable:

```bash
chmod +x deploy.sh
```

---

# 🚀 Deployment Workflow

```text
Stop Old Process
        │
        ▼
Start New Application
        │
        ▼
Wait For Startup
        │
        ▼
Verify Process Running
```

---

# 🧩 Task 2: Implement Smoke Test Suite

---

# 🔹 Step 1: Create Smoke Test Script

Create:

```bash
nano tests/smoke_tests.sh
```

Purpose:

✅ Validate deployment

✅ Verify endpoints

✅ Measure response time

✅ Generate reports

---

# 🔥 Smoke Test Coverage

| Test | Description |
|--------|-------------|
| Health Check | Endpoint availability |
| API Validation | API functionality |
| Response Time | Performance validation |
| Status Check | Service health |

---

# 🔹 Step 2: Health Endpoint Test

Verify:

```bash
curl http://localhost:3000/health
```

Expected:

```json
{
  "status":"ok"
}
```

Validation:

- HTTP Status 200
- Contains "ok"

---

# 🔹 Step 3: API Endpoint Test

Verify:

```bash
curl http://localhost:3000/api/data
```

Expected:

```json
{
  "message":"Data endpoint",
  "version":"1.0.0"
}
```

Validation:

- Response exists
- Contains version field

---

# 🔹 Step 4: Response Time Test

Measure performance:

```bash
curl -o /dev/null -s -w "%{time_total}" \
http://localhost:3000/health
```

Expected:

```text
< 2 seconds
```

Validation Threshold:

```text
PASS  < 2.0 sec
FAIL >= 2.0 sec
```

---

# 🔹 Step 5: Application Status Test

Verify:

```bash
curl http://localhost:3000/api/status
```

Expected:

```json
{
  "status":"healthy",
  "uptime":123.45
}
```

Validation:

- Status = healthy
- Uptime > 0

---

# 📄 Smoke Test Report Structure

Example:

```text
=== Smoke Test Report ===

Test 1: PASS
Test 2: PASS
Test 3: PASS
Test 4: PASS

=== Summary ===

Passed: 4
Failed: 0
```

---

# 🔹 Step 6: Complete Smoke Test Implementation

Create:

```bash
nano tests/smoke_tests_complete.sh
```

This implementation:

✅ Executes all tests

✅ Logs results

✅ Tracks pass/fail counts

✅ Produces reports

✅ Returns proper exit codes

---

# 📊 Exit Code Logic

```text
0 = Success

1 = Failure
```

Used by CI/CD systems for deployment decisions.

---

# 🔹 Step 7: Create Notification Script

Create:

```bash
nano tests/notify_failure.sh
```

Purpose:

- Log notifications
- Store deployment outcomes
- Simulate alerting

Future integrations:

- Slack
- Microsoft Teams
- Email
- PagerDuty
- OpsGenie

---

# 🔔 Notification Flow

```text
Smoke Test Result
        │
        ▼
Generate Report
        │
        ▼
Send Notification
        │
        ▼
Log Outcome
```

---

# 🧩 Task 3: Build Automated Pipeline

---

# 🔹 Step 1: Create Pipeline Script

Create:

```bash
nano pipeline.sh
```

Pipeline stages:

```text
Pre-Checks
    │
    ▼
Deploy
    │
    ▼
Smoke Tests
    │
    ▼
Notifications
    │
    ▼
Success / Failure
```

---

# 🔹 Step 2: Pre-Deployment Checks

Verify:

```bash
lsof -i:3000
```

Check:

- Port availability
- Required files
- Environment readiness

---

# 🔹 Step 3: Deploy Application

Execute:

```bash
./deploy.sh
```

Verify:

```bash
pgrep -f "node app/server.js"
```

Expected:

```text
PID Returned
```

---

# 🔹 Step 4: Run Smoke Tests

Execute:

```bash
./tests/smoke_tests_complete.sh
```

Capture:

```bash
$?
```

Expected:

```text
0
```

---

# 🔹 Step 5: Process Results

Pipeline actions:

✅ Locate latest report

✅ Trigger notifications

✅ Decide rollback actions

✅ Store logs

---

# 🔹 Step 6: Complete Pipeline

Create:

```bash
nano pipeline_complete.sh
```

Capabilities:

- Full deployment
- Validation
- Reporting
- Notification
- Failure handling

---

# 🔍 Verification

---

# 🔹 Verify Deployment

Deploy application:

```bash
./deploy.sh
```

Check process:

```bash
pgrep -f "node app/server.js"
```

Expected:

```text
PID
```

---

# 🔹 Verify Health Endpoint

```bash
curl http://localhost:3000/health
```

Expected:

```json
{
  "status":"ok"
}
```

---

# 🔹 Verify Smoke Tests

Run:

```bash
./tests/smoke_tests_complete.sh
```

Expected:

```text
ALL SMOKE TESTS PASSED
```

---

# 🔹 Verify Reports

List reports:

```bash
ls -lh reports/
```

Expected:

```text
smoke_test_report_YYYYMMDD_HHMMSS.txt
```

View report:

```bash
cat reports/smoke_test_report_*.txt
```

---

# 🔹 Verify Pipeline

Execute:

```bash
./pipeline_complete.sh
```

Expected:

```text
Pipeline completed successfully
```

---

# 🔹 Verify Notifications

View logs:

```bash
cat reports/notifications.log
```

Expected:

```text
Deployment PASSED
```

or

```text
Deployment FAILED
```

---

# 🧪 Test Failure Scenario

---

## Stop Application

```bash
pkill -f "node app/server.js"
```

Verify stopped:

```bash
pgrep -f "node app/server.js"
```

Expected:

```text
No output
```

---

## Run Smoke Tests Again

```bash
./tests/smoke_tests_complete.sh
```

Expected:

```text
SMOKE TESTS FAILED
```

Check exit code:

```bash
echo $?
```

Expected:

```text
1
```

---

## Restart Application

```bash
./deploy.sh
```

---

# 📊 Smoke Testing Architecture

```text
Developer
    │
    ▼
Deployment
    │
    ▼
Application Start
    │
    ▼
Smoke Tests
    │
 ┌──┴─────┐
 │        │
PASS    FAIL
 │        │
 ▼        ▼
Release  Alert
Success  Rollback
```

---

# 🛠 Troubleshooting

---

## ❌ Application Won't Start

Check logs:

```bash
cat app.log
```

Verify Node:

```bash
node --version
```

Check port:

```bash
lsof -i:3000
```

---

## ❌ Smoke Tests Fail

Verify service:

```bash
pgrep -f "node app/server.js"
```

Manual health check:

```bash
curl -v http://localhost:3000/health
```

---

## ❌ Port Already In Use

Find process:

```bash
sudo lsof -i :3000
```

Kill process:

```bash
sudo kill -9 PID
```

---

## ❌ Pipeline Errors

Review logs:

```bash
cat reports/pipeline_*.log
```

Verify permissions:

```bash
chmod +x *.sh tests/*.sh
```

---

## ❌ Response Time Test Fails

Install bc:

```bash
sudo apt install -y bc
```

Verify timing:

```bash
curl -w "%{time_total}" \
-o /dev/null \
-s http://localhost:3000/health
```

---

# 🎓 Key Takeaways

✅ Smoke tests validate deployments quickly

✅ Health endpoints are critical for automation

✅ Exit codes integrate with CI/CD systems

✅ Reports simplify troubleshooting

✅ Notifications improve operational awareness

✅ Automated validation reduces production risk

✅ Fast feedback accelerates software delivery

---

# 🚀 Real-World DevOps Usage

These techniques are used in:

- 🔹 Jenkins Pipelines
- 🔹 GitHub Actions
- 🔹 GitLab CI/CD
- 🔹 Azure DevOps
- 🔹 ArgoCD
- 🔹 Kubernetes Deployments
- 🔹 AWS CodePipeline
- 🔹 Google Cloud Build

---

# 🏆 Lab Completed Successfully

You have successfully:

✔ Built a Node.js application

✔ Automated deployment workflows

✔ Created smoke test suites

✔ Implemented health checks

✔ Generated deployment reports

✔ Added failure notifications

✔ Built an end-to-end deployment pipeline

✔ Applied DevOps deployment validation best practices

---

<div align="center">

# 🌟 Deploy Fast • Validate Automatically • Release Safely 🌟

### Happy Learning & Happy DevOps 🚀

</div>
