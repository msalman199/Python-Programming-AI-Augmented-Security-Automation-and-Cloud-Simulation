# 🛡️ Golden Config Enforcement

<div align="center">

![DevOps](https://img.shields.io/badge/DevOps-Configuration%20Compliance-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge\&logo=python)
![YAML](https://img.shields.io/badge/YAML-Configuration-red?style=for-the-badge)
![JSON Schema](https://img.shields.io/badge/JSON-Schema-green?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?style=for-the-badge\&logo=git)
![Security](https://img.shields.io/badge/Security-Enforcement-purple?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-black?style=for-the-badge\&logo=linux)

# 🔒 Golden Configuration Enforcement System

### Validate • Enforce • Protect • Automate

Ensure every infrastructure configuration follows approved organizational standards.

</div>

---

# 📖 Overview

Configuration drift and security misconfigurations are among the leading causes of outages and security incidents.

This lab demonstrates how to build a complete **Golden Configuration Enforcement System** that:

✅ Defines approved configuration standards

✅ Detects configuration drift

✅ Identifies security violations

✅ Blocks non-compliant deployments

✅ Generates compliance reports

✅ Creates audit trails for governance

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

* 🔹 Define Golden Configuration Standards
* 🔹 Implement automated configuration validation
* 🔹 Detect configuration drift
* 🔹 Enforce security requirements
* 🔹 Block unsafe deployments
* 🔹 Generate compliance reports

---

# 📋 Prerequisites

Before starting, ensure you have:

* 🐧 Basic Linux command line knowledge
* 📄 Understanding of YAML and JSON
* 🌳 Familiarity with Git basics
* 🐍 Basic Python scripting experience
* ⚙️ Understanding of configuration management concepts

---

# 🏗️ Environment Setup

---

# 🔹 Step 1: Install Required Tools

Update packages:

```bash
sudo apt update
```

Install required software:

```bash
sudo apt install -y \
    python3 \
    python3-pip \
    git
```

Install Python libraries:

```bash
pip3 install \
    pyyaml \
    jsonschema \
    deepdiff
```

---

# 🔹 Step 2: Create Lab Directory Structure

```bash
mkdir -p ~/golden-config-lab/{golden,current,scripts,logs}

cd ~/golden-config-lab
```

---

## 📁 Project Structure

```text
golden-config-lab/
│
├── golden/
│   ├── webserver_golden.yaml
│   ├── ssh_golden.yaml
│   └── config_schema.json
│
├── current/
│   ├── webserver_compliant.yaml
│   └── ssh_violation.yaml
│
├── scripts/
│   ├── config_enforcer.py
│   ├── pre_deploy_check.sh
│   └── compliance_report.py
│
└── logs/
```

---

# 🧩 Task 1: Create Golden Configuration Standards

Golden Configurations act as the **single source of truth** for infrastructure settings.

---

# 🔹 Step 1.1: Define Golden Web Server Configuration

Create:

```bash
golden/webserver_golden.yaml
```

Purpose:

✅ Standardize Nginx settings

✅ Enforce SSL

✅ Define approved logging

✅ Define firewall requirements

---

### Golden Configuration Components

```yaml
service:
security:
network:
logging:
```

---

### Security Controls

```yaml
firewall:
ssl:
```

Mandatory:

* Port 80
* Port 443
* TLS 1.2+
* Logging enabled

---

# 🔹 Step 1.2: Define Golden SSH Configuration

Create:

```bash
golden/ssh_golden.yaml
```

Security Requirements:

✅ Root login disabled

✅ Password authentication disabled

✅ Public key authentication enabled

✅ SSH hardening applied

---

### SSH Security Baseline

```yaml
permit_root_login: false
password_authentication: false
pubkey_authentication: true
```

---

# 🔹 Step 1.3: Create Validation Schema

Create:

```bash
golden/config_schema.json
```

Purpose:

* Enforce required sections
* Validate configuration structure
* Prevent malformed configs

---

## Example Requirements

```json
{
  "required": [
    "service",
    "security"
  ]
}
```

---

# 🧩 Task 2: Build Configuration Comparison and Enforcement System

---

# 🔹 Step 2.1: Create Configuration Validator Script

Create:

```bash
scripts/config_enforcer.py
```

---

## 🚀 Enforcer Features

The ConfigEnforcer class should support:

### 📥 YAML Loading

```python
yaml.safe_load()
```

---

### 🔍 Configuration Comparison

Using:

```python
DeepDiff()
```

Detect:

* Missing values
* Modified values
* Added fields
* Removed fields

---

### 🛡️ Security Violation Detection

Checks:

```yaml
permit_root_login
password_authentication
ssl
timeouts
```

---

### 📋 Compliance Logging

Generate:

```text
logs/violations_*.log
```

---

### 🚫 Deployment Blocking

If violations exist:

```python
block_deployment()
```

Deployment immediately fails.

---

## Make Script Executable

```bash
chmod +x scripts/config_enforcer.py
```

---

# 🔹 Step 2.2: Create Current Configurations

---

## ✅ Compliant Configuration

Create:

```bash
current/webserver_compliant.yaml
```

Expected Result:

✔ Passes validation

✔ No violations

✔ Deployment allowed

---

## ❌ Non-Compliant Configuration

Create:

```bash
current/ssh_violation.yaml
```

Contains:

```yaml
permit_root_login: true
password_authentication: true
max_auth_tries: 10
```

Expected Result:

🚫 Deployment blocked

🚫 Violations reported

---

# 🔹 Step 2.3: Implement Enforcement Logic

Complete all TODO sections.

---

## Required Methods

### Load YAML

```python
def load_yaml():
```

Responsibilities:

* Open files
* Parse YAML
* Handle errors

---

### Compare Configurations

```python
def compare_configs():
```

Use:

```python
DeepDiff(
    golden_config,
    current_config
)
```

Detect:

* values_changed
* dictionary_item_added
* dictionary_item_removed

---

### Security Validation

```python
def check_security_violations():
```

Checks:

| Validation     | Expected |
| -------------- | -------- |
| Root Login     | Disabled |
| Password Auth  | Disabled |
| TLS Enabled    | Yes      |
| Timeout Values | Secure   |

---

### Enforcement

```python
def enforce_config():
```

Responsibilities:

* Load configs
* Compare against golden baseline
* Detect violations
* Log findings
* Block deployment

---

# 🔹 Step 2.4: Create Pre-Deployment Hook

Create:

```bash
scripts/pre_deploy_check.sh
```

Purpose:

Run enforcement before deployment begins.

---

## Workflow

```text
Deployment Request
        │
        ▼
Pre-Deployment Check
        │
        ▼
Config Enforcer
        │
 ┌──────┴──────┐
 │             │
 ▼             ▼
PASS         FAIL
 │             │
 ▼             ▼
Deploy      Block
```

---

## Make Executable

```bash
chmod +x scripts/pre_deploy_check.sh
```

---

# 🔹 Step 2.5: Create Compliance Dashboard

Create:

```bash
scripts/compliance_report.py
```

Purpose:

Generate:

* Compliance metrics
* Violation summaries
* Security trends
* Audit reports

---

## Report Statistics

Track:

```text
Total Checks
Compliant Systems
Failed Checks
Top Violations
Compliance Rate
```

---

## Make Executable

```bash
chmod +x scripts/compliance_report.py
```

---

# ✅ Verification

---

# 🔹 Step 1: Test Compliant Configuration

```bash
cd ~/golden-config-lab

python3 scripts/config_enforcer.py
```

Expected:

```text
No violations found
Exit Code: 0
```

Check:

```bash
echo $?
```

Expected:

```text
0
```

---

# 🔹 Step 2: Test Violation Detection

Rename:

```bash
mv current/ssh_violation.yaml \
current/ssh_current.yaml
```

Run:

```bash
python3 scripts/config_enforcer.py
```

Expected:

```text
DEPLOYMENT BLOCKED
```

Exit Code:

```text
1
```

---

# 🔹 Step 3: Review Violation Logs

```bash
ls -la logs/

cat logs/violations_*.log
```

Expected:

```text
Timestamp
Configuration Name
Violation Type
Severity
Details
```

---

# 🔹 Step 4: Test Pre-Deployment Hook

Execute:

```bash
./scripts/pre_deploy_check.sh
```

Expected:

```text
Configuration violations detected.
Deployment blocked.
```

---

# 🔹 Step 5: Generate Compliance Report

Run:

```bash
python3 scripts/compliance_report.py
```

Expected Output:

```text
Total Checks: XX
Compliant: XX
Failed: XX
Compliance Rate: XX%
```

---

# 📊 Enforcement Architecture

```text
                  Golden Config
                        │
                        ▼
              ┌─────────────────┐
              │ Config Enforcer │
              └────────┬────────┘
                       │
         ┌─────────────┴─────────────┐
         │                           │
         ▼                           ▼
 Compare Configs          Security Checks
         │                           │
         └─────────────┬─────────────┘
                       ▼
                Violations Found?
                       │
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
       No Issues              Violations
          │                         │
          ▼                         ▼
     Allow Deploy           Block Deploy
```

---

# 📈 Expected Outcomes

After completing this lab, you will have:

### 🏆 Golden Configuration Repository

Approved configuration standards.

---

### 🏆 Automated Enforcement Engine

Python-based compliance validation.

---

### 🏆 Security Compliance Checks

Detection of risky settings.

---

### 🏆 Deployment Protection

Unsafe configurations blocked automatically.

---

### 🏆 Audit Trail

Historical records of all violations.

---

### 🏆 Compliance Reporting

Visibility into organizational compliance.

---

# 🛠 Troubleshooting

---

## ❌ Import Errors

Reinstall dependencies:

```bash
pip3 install --upgrade \
    pyyaml \
    jsonschema \
    deepdiff
```

---

## ❌ YAML Parsing Errors

Validate:

```bash
python3 -c \
"import yaml; yaml.safe_load(open('file.yaml'))"
```

Check:

* Proper indentation
* Spaces only
* Valid YAML structure

---

## ❌ Permission Denied

Fix permissions:

```bash
chmod +x scripts/*.py scripts/*.sh
```

---

## ❌ No Violations Detected

Verify:

* Current config differs from golden config
* Correct file paths
* DeepDiff logic implemented
* Enforcement method called

---

# 🎓 Key Takeaways

✅ Golden Configurations provide a single source of truth

✅ Automated enforcement eliminates manual review errors

✅ Security validation catches dangerous settings early

✅ Pre-deployment hooks prevent production incidents

✅ Audit logs support governance and compliance

✅ Configuration as Code enables version control and review

---

# 🚀 Real-World Applications

This same approach is used in:

* 🔹 Kubernetes Admission Controllers
* 🔹 Open Policy Agent (OPA)
* 🔹 HashiCorp Sentinel
* 🔹 GitOps Pipelines
* 🔹 Enterprise Security Compliance
* 🔹 Infrastructure Governance Platforms

---

# 🏆 Lab Completed

You have successfully built a complete **Golden Configuration Enforcement System** that:

✔ Defines approved configuration standards

✔ Detects configuration drift

✔ Identifies security violations

✔ Blocks non-compliant deployments

✔ Generates compliance reports

✔ Provides audit-ready enforcement logs

✔ Implements enterprise-grade configuration governance

---

<div align="center">

# 🌟 Secure Infrastructure Begins with Enforced Standards 🌟

### Happy Learning & Happy Automating 🚀

</div>
