# 🚨 CI Failure Triage Assistant

![DevOps](https://img.shields.io/badge/DevOps-CI%2FCD-blue)
![Python](https://img.shields.io/badge/Python-3.x-yellow)
![Automation](https://img.shields.io/badge/Automation-Log%20Analysis-green)
![YAML](https://img.shields.io/badge/YAML-Configuration-red)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange)
![Status](https://img.shields.io/badge/Lab-Complete-success)

---

# 📖 Overview

Modern CI/CD pipelines generate large amounts of logs whenever builds, tests, deployments, or security checks fail. Manually investigating these logs consumes valuable engineering time.

In this lab, you will build a **CI Failure Triage Assistant** that automatically analyzes CI/CD logs, identifies common failure patterns, extracts relevant error context, and provides actionable troubleshooting suggestions.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Build an automated CI log analysis tool

✅ Implement pattern matching for common build failures

✅ Create a triage system that suggests likely root causes

✅ Extract useful error context automatically

✅ Perform batch analysis of multiple CI logs

✅ Extend the system with custom failure patterns

✅ Accelerate build failure diagnosis using automation

---

# 🏗 Architecture

```text
                 ┌─────────────────────┐
                 │   CI/CD Pipeline    │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │    Build Logs       │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ CI Triage Assistant │
                 └──────────┬──────────┘
                            │
           ┌────────────────┼────────────────┐
           ▼                ▼                ▼
   Pattern Matching   Error Extraction   Severity Analysis
           │                │                │
           └────────────────┼────────────────┘
                            ▼
                 ┌─────────────────────┐
                 │ Triage Report       │
                 │ Root Cause          │
                 │ Suggestions         │
                 └─────────────────────┘
```

---

# 🛠 Prerequisites

Before starting this lab, ensure you have:

* Basic Linux command-line knowledge
* Understanding of Git and version control
* Familiarity with CI/CD concepts
* Basic Python programming skills
* Experience reading log files

---

# ⚙️ Environment Setup

## 📦 Install Required Tools

```bash
sudo apt update

sudo apt install -y python3 python3-pip git

pip3 install pyyaml colorama
```

---

## 📁 Create Project Structure

```bash
mkdir -p ~/ci-triage-lab
cd ~/ci-triage-lab

mkdir -p logs patterns output
```

---

# 🚀 Task 1: Build the CI Log Analyzer

---

## Step 1: Create Sample CI Logs

Create sample failure logs for testing.

### Network Failure Log

```bash
cat > logs/build_failure_1.log << 'EOF'
[2024-01-15 10:23:45] INFO: Starting build process
[2024-01-15 10:23:46] INFO: Checking out repository
[2024-01-15 10:23:50] INFO: Installing dependencies
[2024-01-15 10:24:15] ERROR: npm ERR! code ENOTFOUND
[2024-01-15 10:24:15] ERROR: npm ERR! network request to https://registry.npmjs.org/express failed
[2024-01-15 10:24:15] ERROR: npm ERR! network This is a problem related to network connectivity
[2024-01-15 10:24:15] FATAL: Build failed with exit code 1
EOF
```

### Test Failure Log

```bash
cat > logs/test_failure_2.log << 'EOF'
[2024-01-15 11:15:30] INFO: Running test suite
[2024-01-15 11:15:35] INFO: Test: user_authentication_test
[2024-01-15 11:15:36] PASS: test_valid_login
[2024-01-15 11:15:37] FAIL: test_invalid_password
[2024-01-15 11:15:37] ERROR: AssertionError: Expected status code 401, got 500
[2024-01-15 11:15:37] ERROR: at UserAuthTest.test_invalid_password (auth_test.py:45)
[2024-01-15 11:15:38] INFO: Tests completed: 1 passed, 1 failed
EOF
```

### Compilation Failure Log

```bash
cat > logs/compile_error_3.log << 'EOF'
[2024-01-15 14:20:10] INFO: Compiling Java sources
[2024-01-15 14:20:15] ERROR: src/main/java/com/example/Service.java:23: error: cannot find symbol
[2024-01-15 14:20:15] ERROR:   symbol:   class DatabaseConnection
[2024-01-15 14:20:15] ERROR:   location: class Service
[2024-01-15 14:20:15] ERROR: 1 error
[2024-01-15 14:20:15] FATAL: Compilation failed
EOF
```

---

## Step 2: Create Failure Pattern Database

Create:

```bash
patterns/failure_patterns.yaml
```

The YAML file contains:

* Network Failures
* Test Assertion Failures
* Compilation Errors
* Resource Exhaustion Errors

Each pattern includes:

* Keywords
* Severity
* Suggested remediation actions

---

## Step 3: Implement CI Triage Assistant

Create:

```bash
ci_triage.py
```

### Features

✅ Load failure patterns from YAML

✅ Analyze CI logs

✅ Match known failure signatures

✅ Score confidence levels

✅ Extract error context

✅ Generate colored reports

### Core Components

```python
class CITriageAssistant:
```

Methods:

```python
_load_patterns()
analyze_log()
extract_error_lines()
generate_report()
_get_severity_color()
```

---

## Step 4: Test the Analyzer

Analyze individual logs:

```bash
python3 ci_triage.py logs/build_failure_1.log

python3 ci_triage.py logs/test_failure_2.log

python3 ci_triage.py logs/compile_error_3.log
```

---

# 📊 Task 2: Batch Analysis

---

## Step 1: Create Batch Analyzer

Create:

```bash
batch_triage.py
```

### Capabilities

* Scan entire log directories
* Process multiple files
* Summarize findings
* Highlight top issues

---

## Step 2: Execute Batch Mode

```bash
python3 batch_triage.py logs
```

Expected output:

```text
BATCH ANALYSIS SUMMARY

build_failure_1.log
  Top Issue: Network/Dependency Download Failure

test_failure_2.log
  Top Issue: Test Assertion Failure

compile_error_3.log
  Top Issue: Compilation Error
```

---

## Step 3: Add Custom Failure Patterns

Extend:

```yaml
patterns/failure_patterns.yaml
```

Example:

```yaml
- name: "Docker Build Failure"
```

Keywords:

```yaml
docker
image not found
pull access denied
manifest unknown
```

---

### Create Docker Failure Test Log

```bash
cat > logs/docker_failure_4.log << 'EOF'
[2024-01-15 16:30:00] INFO: Building Docker image
[2024-01-15 16:30:05] ERROR: Error response from daemon: pull access denied for myapp/backend
[2024-01-15 16:30:05] ERROR: repository does not exist or may require 'docker login'
[2024-01-15 16:30:05] FATAL: Docker build failed
EOF
```

Test:

```bash
python3 ci_triage.py logs/docker_failure_4.log
```

---

# 🔍 Verification

---

## Verify Single Log Analysis

```bash
python3 ci_triage.py logs/build_failure_1.log
```

Expected:

```text
CI FAILURE TRIAGE REPORT
```

---

## Verify Pattern Detection

```bash
python3 ci_triage.py logs/test_failure_2.log
```

Expected:

```text
Test Assertion Failure
```

---

## Verify Batch Processing

```bash
python3 batch_triage.py logs
```

Expected:

```text
BATCH ANALYSIS SUMMARY
```

---

## Verify Custom Pattern

```bash
python3 ci_triage.py logs/docker_failure_4.log
```

Expected:

```text
Docker Build Failure
```

---

# 📂 Project Structure

```text
ci-triage-lab/
│
├── logs/
│   ├── build_failure_1.log
│   ├── test_failure_2.log
│   ├── compile_error_3.log
│   └── docker_failure_4.log
│
├── patterns/
│   └── failure_patterns.yaml
│
├── output/
│
├── ci_triage.py
├── batch_triage.py
│
└── README.md
```

---

# 🧪 Example Output

```text
====================================================
CI FAILURE TRIAGE REPORT
====================================================

Detected Failure Patterns

1. Network/Dependency Download Failure

Severity: HIGH

Confidence Score: 4

Suggested Actions:

- Check network connectivity
- Verify registry access
- Review proxy settings
- Check authentication issues
```

---

# 🛡 Troubleshooting

## ModuleNotFoundError

Install dependencies:

```bash
pip3 install pyyaml colorama --user
```

---

## No Patterns Detected

Verify:

```bash
cat patterns/failure_patterns.yaml
```

Ensure keywords match log content.

---

## Permission Denied

```bash
chmod +x *.py
```

---

## Colors Not Displaying

```bash
export TERM=xterm-256color
```

---

# ✅ Complete Lab Checklist

* [ ] Project structure created
* [ ] Sample CI logs generated
* [ ] Failure pattern database created
* [ ] Log analyzer implemented
* [ ] Error extraction working
* [ ] Colored reporting enabled
* [ ] Batch analyzer created
* [ ] Custom pattern added
* [ ] Verification tests completed
* [ ] Troubleshooting validated

---

# 🎓 Conclusion

In this lab you successfully built a **CI Failure Triage Assistant** capable of automatically diagnosing common CI/CD pipeline failures.

You implemented:

* Automated log analysis
* YAML-based pattern matching
* Error context extraction
* Severity classification
* Batch processing workflows
* Custom failure signatures

These techniques are commonly used by DevOps, Platform Engineering, and Site Reliability Engineering (SRE) teams to reduce Mean Time To Resolution (MTTR) and improve CI/CD reliability.

---

# 🚀 Key Takeaways

✅ Log parsing automation accelerates troubleshooting

✅ Pattern matching identifies recurring issues quickly

✅ Structured YAML configurations simplify maintenance

✅ Batch analysis improves operational efficiency

✅ Automated triage reduces manual investigation effort

✅ CI/CD observability is a critical DevOps skill

---

**Estimated Completion Time:** **60–90 Minutes** ⏱️

**Difficulty Level:** **Intermediate** 🔥

**Category:** CI/CD • DevOps • Automation • Python • Troubleshooting
