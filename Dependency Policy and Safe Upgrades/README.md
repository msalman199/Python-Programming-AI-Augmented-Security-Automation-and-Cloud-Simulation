# 🔐 Dependency Policy and Safe Upgrades 

![DevOps](https://img.shields.io/badge/DevOps-Dependency%20Management-blue)
![Python](https://img.shields.io/badge/Python-3.x-green)
![Node.js](https://img.shields.io/badge/Node.js-18.x-brightgreen)
![Security](https://img.shields.io/badge/Security-Vulnerability%20Scanning-red)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Automation-orange)
![License](https://img.shields.io/badge/License-Educational-lightgrey)

---

# 📦 Dependency Policy and Safe Upgrades

## 📖 Overview

Modern applications depend heavily on third-party libraries and packages. While dependencies accelerate development, they also introduce risks such as:

* Security vulnerabilities
* Breaking changes
* License compliance issues
* Supply chain attacks
* Compatibility conflicts

In this lab, you'll learn how to create dependency governance policies, safely test upgrades, automate security scanning, and implement rollback strategies.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Define dependency upgrade policies

✅ Implement dependency security scanning

✅ Safely test package upgrades

✅ Create rollback strategies

✅ Automate dependency validation workflows

✅ Compare dependency management in Python and Node.js

---

# 🛠️ Prerequisites

Before starting this lab, you should have:

* Basic Linux command line knowledge
* Familiarity with Python or Node.js
* Understanding of package managers (pip, npm)
* Knowledge of Semantic Versioning (SemVer)
* Basic Git experience

---

# 🏗️ Environment Setup

## Step 1: Install Required Tools

```bash
sudo apt update

sudo apt install -y \
python3 \
python3-pip \
python3-venv \
git
```

Install Node.js:

```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -

sudo apt install -y nodejs
```

Verify installations:

```bash
python3 --version
pip3 --version
node --version
npm --version
```

Expected output:

```text
Python 3.x
pip 23.x
Node 18.x
npm 9.x
```

---

# 📂 Task 1: Define Upgrade Policies

## Step 1: Create Project Structure

```bash
mkdir -p ~/dependency-lab
cd ~/dependency-lab

mkdir python-app
cd python-app

python3 -m venv venv

source venv/bin/activate
```

Create requirements files:

```bash
touch requirements.txt
touch requirements-dev.txt
```

---

## Step 2: Create Dependency Policy

Create:

```bash
dependency-policy.yaml
```

### Policy Goals

| Update Type | Schedule  | Approval            |
| ----------- | --------- | ------------------- |
| Security    | Immediate | Auto                |
| Minor       | Weekly    | Team Lead           |
| Major       | Quarterly | Architecture Review |

### Allowed Licenses

```yaml
MIT
Apache-2.0
BSD-3-Clause
ISC
```

### Blocked Packages

```yaml
example-malicious-package
```

---

## Step 3: Create Sample Application

Create:

```bash
app.py
```

Application features:

* Flask API
* Health endpoint
* External API requests
* Dependency validation target

### Endpoints

```text
/health
/fetch
```

---

## Step 4: Define Initial Dependencies

Create:

```txt
requirements.txt
```

```txt
flask==2.3.0
requests==2.28.0
werkzeug==2.3.0
```

Development dependencies:

```txt
pytest==7.3.0
pytest-cov==4.0.0
safety==2.3.0
pip-audit==2.5.0
```

Install packages:

```bash
pip install -r requirements-dev.txt
```

---

# 🔎 Task 2: Dependency Security Scanning

## Step 1: Create Dependency Checker

Create:

```bash
check_dependencies.py
```

Responsibilities:

### 🔐 Safety Scan

Checks:

* Known vulnerabilities
* CVE exposure
* Insecure package versions

Command:

```bash
safety check --json
```

---

### 🛡️ Pip Audit

Checks:

* Public vulnerability databases
* Dependency trees
* Security advisories

Command:

```bash
pip-audit --desc
```

---

### 📜 License Compliance

Verify:

* Allowed licenses
* Blocked licenses
* Organizational policies

Examples:

```text
MIT
Apache-2.0
BSD-3-Clause
ISC
```

---

### 📈 Upgrade Report

Generate recommendations:

```text
Patch Updates
Minor Updates
Major Updates
Security Updates
```

---

## Step 2: Run Initial Scan

```bash
python3 check_dependencies.py
```

Check outdated packages:

```bash
pip list --outdated
```

Expected:

```text
Security Scan Complete
No Critical Vulnerabilities
Upgrade Recommendations Generated
```

---

# 🧪 Task 3: Build Upgrade Testing Framework

## Step 1: Create Test Suite

Create directory:

```bash
mkdir tests
```

Create:

```bash
tests/test_app.py
```

Required tests:

### Health Endpoint Test

Verify:

```text
Status Code = 200
Response = healthy
```

---

### Fetch Endpoint Test

Validate:

* API response
* Timeout handling
* Error handling

---

### Dependency Version Test

Verify:

* Installed versions
* Policy compliance
* Version constraints

---

## Step 2: Run Tests

```bash
pytest tests/ -v
```

Expected:

```text
PASSED
PASSED
PASSED
```

---

# 🔄 Task 4: Safe Upgrade Workflow

## Step 1: Create Upgrade Script

Create:

```bash
test_upgrade.sh
```

Workflow:

```text
Backup Environment
Run Baseline Tests
Upgrade Packages
Run Tests Again
Security Scan
Rollback If Needed
```

---

## Step 2: Backup Current Environment

```bash
pip freeze > frozen_requirements.txt
```

Create backup:

```bash
backup_YYYYMMDD_HHMMSS
```

---

## Step 3: Run Baseline Tests

```bash
pytest
```

Capture:

* Pass rate
* Coverage
* Performance metrics

---

## Step 4: Perform Upgrade

Example:

```bash
pip install --upgrade requests
```

Record:

```text
Current Version
New Version
Upgrade Type
```

---

## Step 5: Run Post-Upgrade Validation

Execute:

```bash
pytest
```

Verify:

* No regressions
* All endpoints functional
* Dependencies compatible

---

## Step 6: Security Scan

```bash
python3 check_dependencies.py
```

Confirm:

✅ No new vulnerabilities

✅ License compliance maintained

✅ Policy requirements satisfied

---

## Step 7: Rollback Strategy

If tests fail:

```bash
pip install -r backup/frozen_requirements.txt
```

Verify:

```bash
pytest
```

Expected:

```text
Environment Restored Successfully
```

---

# 🤖 Task 5: Automated Upgrade Workflow

Create:

```bash
upgrade_workflow.py
```

Capabilities:

---

## 📦 Check Outdated Packages

```bash
pip list --outdated --format=json
```

Produces:

```json
[
  {
    "name":"requests",
    "current":"2.28.0",
    "latest":"2.31.0"
  }
]
```

---

## 🏷️ Classify Update Type

| Current | Latest | Type  |
| ------- | ------ | ----- |
| 2.28.0  | 2.28.1 | Patch |
| 2.28.0  | 2.29.0 | Minor |
| 2.28.0  | 3.0.0  | Major |

---

## 📝 Apply Policy Rules

Example:

```text
Patch → Auto Approve
Minor → Team Lead Approval
Major → Architecture Review
```

---

## 🌿 Create Git Upgrade Branch

Example:

```bash
git checkout -b upgrade-requests-2.31.0
```

---

## 🧪 Execute Test Suite

Run:

```bash
pytest --cov
```

Run:

```bash
pip-audit
```

Run:

```bash
safety check
```

---

## 📄 Generate Upgrade Report

Output:

```markdown
Upgrade Summary
Security Findings
Test Results
Approval Requirements
Recommendations
```

---

# 🌐 Task 6: Node.js Dependency Management

## Step 1: Create Project

```bash
mkdir nodejs-app

cd nodejs-app

npm init -y
```

---

## Step 2: Install Dependencies

```bash
npm install express axios
```

Install development tools:

```bash
npm install --save-dev jest npm-check-updates
```

---

## Step 3: Security Audit

```bash
npm audit
```

Fix vulnerabilities:

```bash
npm audit fix
```

---

## Step 4: Check Outdated Packages

```bash
npm outdated
```

Example:

```text
Package  Current  Wanted  Latest
axios    1.3.0    1.3.5   1.6.0
```

---

# 📊 Task 7: Generate Dependency Report

Create:

```bash
generate_report.sh
```

Generate:

```text
Installed Packages
Outdated Packages
Security Findings
Upgrade Recommendations
```

Run:

```bash
./generate_report.sh
```

Expected output:

```text
report.md created
```

---

# ✅ Verification

## Verify Policy

```bash
test -f dependency-policy.yaml
```

Expected:

```text
✓ Policy file created
```

---

## Verify Security Tools

```bash
safety --version
pip-audit --version
```

Expected:

```text
✓ Safety installed
✓ Pip-Audit installed
```

---

## Verify Tests

```bash
pytest tests/ -v
```

Expected:

```text
PASSED
PASSED
PASSED
```

---

## Verify Upgrade Workflow

```bash
./test_upgrade.sh
```

Expected:

```text
Backup Complete
Tests Passed
Security Scan Passed
Upgrade Successful
```

---

## Verify Report Generation

```bash
cat report.md
```

Expected:

```text
Python Dependency Summary
Node.js Dependency Summary
Upgrade Recommendations
```

---

# 🛠️ Troubleshooting

## Issue: safety Not Found

Activate virtual environment:

```bash
source venv/bin/activate
```

Install:

```bash
pip install safety
```

---

## Issue: pip-audit Missing

```bash
pip install pip-audit
```

---

## Issue: Test Import Errors

Run tests from project root:

```bash
pytest tests/
```

Verify:

```bash
PYTHONPATH
```

---

## Issue: npm Audit Reports Vulnerabilities

Run:

```bash
npm audit fix
```

Review breaking changes before applying:

```bash
npm audit fix --force
```

---

## Issue: Permission Denied

```bash
chmod +x *.sh
```

---

# 🎯 Expected Outcomes

After completing this lab, you should have:

✅ Dependency policy framework

✅ Security scanning automation

✅ Safe upgrade workflow

✅ Rollback strategy

✅ Python dependency governance

✅ Node.js dependency governance

✅ Automated reporting system

---

# 🏆 Key Takeaways

### 🔐 Security First

Always scan dependencies before deployment.

### 🧪 Test Before Upgrade

Every update must pass validation.

### 📦 Follow Semantic Versioning

Understand risk differences:

* Patch = Low Risk
* Minor = Medium Risk
* Major = High Risk

### 🔄 Maintain Rollback Capability

Every upgrade should be reversible.

### 🤖 Automate Everything

Dependency management should be part of CI/CD pipelines.

---

# 🎉 Conclusion

You have successfully built a complete **Dependency Policy and Safe Upgrades Framework** capable of:

* Defining upgrade governance rules
* Detecting vulnerable dependencies
* Testing upgrades safely
* Automating approval workflows
* Rolling back failed changes
* Managing dependencies across Python and Node.js ecosystems

These practices are essential for modern DevOps teams operating secure, reliable, and maintainable production environments.

---

## ⏱ Estimated Completion Time

**90 – 120 Minutes**

**Difficulty:** Intermediate ⭐⭐⭐☆☆

**Category:** DevSecOps • Dependency Management • Software Supply Chain Security
