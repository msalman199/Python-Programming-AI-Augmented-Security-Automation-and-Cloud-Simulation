# 🚀 Pre-commit Quality Gate Setup 

<p align="center">

![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pre-commit](https://img.shields.io/badge/Pre--Commit-Automation-FAB040?style=for-the-badge&logo=pre-commit&logoColor=black)
![Black](https://img.shields.io/badge/Black-Code%20Formatter-000000?style=for-the-badge)
![Flake8](https://img.shields.io/badge/Flake8-Linting-4B8BBE?style=for-the-badge)
![Bandit](https://img.shields.io/badge/Bandit-Security%20Scanner-FF6B6B?style=for-the-badge)
![YAML](https://img.shields.io/badge/YAML-Configuration-CB171E?style=for-the-badge&logo=yaml&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

</p>

---

# 📖 Overview

This lab demonstrates how to implement a **Pre-commit Quality Gate System** that automatically checks code quality before commits are accepted into a Git repository.

By the end of this lab, you will have:

✅ Automated Code Formatting  
✅ Linting Enforcement  
✅ Security Scanning  
✅ File Validation Checks  
✅ Custom Quality Gates  
✅ DevOps Best Practices

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

- ✅ Configure pre-commit hooks
- ✅ Enforce code quality standards
- ✅ Implement automated linting
- ✅ Configure code formatting validation
- ✅ Perform security scanning before commits
- ✅ Understand DevOps Quality Gates

---

# 📋 Prerequisites

Before starting, ensure you have:

- Basic Git knowledge
- Python fundamentals
- Linux command-line experience
- Understanding of linting and formatting
- Familiarity with YAML files
- Ubuntu/Linux machine with sudo privileges

---

# 🛠️ Environment Setup

## 🔹 Step 1: Update System

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
```

### Verify Installation

```bash
python3 --version
git --version
pip3 --version
```

---

## 🔹 Step 2: Create Lab Workspace

```bash
mkdir ~/precommit-lab
cd ~/precommit-lab

git init

git config user.name "Lab User"
git config user.email "labuser@example.com"
```

---

# 🚀 Task 1: Install and Configure Pre-commit Framework

---

## 🔹 Step 1: Install Pre-commit

```bash
pip3 install pre-commit
```

Verify:

```bash
pre-commit --version
```

---

## 🔹 Step 2: Create Sample Python Project

Create `app.py`

```bash
cat > app.py << 'EOF'
import os
import sys

def calculate_sum(a,b):
    password = "hardcoded_password123"
    result=a+b
    return result

def process_data( x ):
    if x>0:
        print("Positive")
    else:
        print("Negative")

if __name__=="__main__":
    print(calculate_sum(5,10))
EOF
```

---

## 🔹 Step 3: Create Pre-commit Configuration

Create `.pre-commit-config.yaml`

```bash
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.5.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: ['--maxkb=500']
      - id: check-json
      - id: pretty-format-json
        args: ['--autofix']

  - repo: https://github.com/psf/black
    rev: 23.12.1
    hooks:
      - id: black
        language_version: python3

  - repo: https://github.com/PyCQA/flake8
    rev: 7.0.0
    hooks:
      - id: flake8
        args: ['--max-line-length=88', '--extend-ignore=E203']

  - repo: https://github.com/PyCQA/bandit
    rev: 1.7.6
    hooks:
      - id: bandit
        args: ['-ll', '-i']
EOF
```

---

## 🔹 Step 4: Install Git Hooks

```bash
pre-commit install
```

Expected Output:

```text
pre-commit installed at .git/hooks/pre-commit
```

---

## 🔹 Step 5: Run Hooks Manually

```bash
pre-commit run --all-files
```

Expected detections:

- ❌ Formatting issues
- ❌ Linting problems
- ❌ Hardcoded password
- ❌ Style violations

---

# 🔧 Task 2: Configure Quality Rules

---

## 🔹 Step 1: Configure Flake8

Create `.flake8`

```bash
cat > .flake8 << 'EOF'
[flake8]
max-line-length = 88
extend-ignore = E203, W503
exclude =
    .git,
    __pycache__,
    .venv,
    venv
per-file-ignores =
    __init__.py:F401
EOF
```

---

## 🔹 Step 2: Configure Bandit

Create `.bandit`

```bash
cat > .bandit << 'EOF'
[bandit]
exclude_dirs = ['/test', '.venv', 'venv']
skips = B101,B601
EOF
```

---

## 🔹 Step 3: Fix Code Quality Issues

Update `app.py`

```python
import os
import sys


def calculate_sum(a, b):
    """
    Calculate sum of two numbers.

    Args:
        a: First number
        b: Second number

    Returns:
        Sum of a and b
    """
    pass


def process_data(x):
    """
    Process data and print result.

    Args:
        x: Number to process
    """
    pass


if __name__ == "__main__":
    pass
```

---

## 🔹 Step 4: Corrected Solution

Create `app_fixed.py`

```bash
cat > app_fixed.py << 'EOF'
import os
import sys


def calculate_sum(a, b):
    """Calculate sum of two numbers."""
    result = a + b
    return result


def process_data(x):
    """Process data based on value."""
    if x > 0:
        print("Positive")
    else:
        print("Negative")


if __name__ == "__main__":
    print(calculate_sum(5, 10))
EOF
```

---

## 🔹 Step 5: Re-run Quality Checks

```bash
cp app_fixed.py app.py

pre-commit run --all-files
```

Expected:

```text
All checks passed.
```

---

## 🔹 Step 6: Add Custom TODO Hook

Append this to `.pre-commit-config.yaml`

```yaml
  - repo: local
    hooks:
      - id: check-todos
        name: Check for TODO comments
        entry: bash -c 'if grep -r "TODO" --include="*.py" .; then echo "TODO comments found. Please resolve before committing."; exit 1; fi'
        language: system
        pass_filenames: false
```

---

## 🔹 Step 7: Create Test Files

### JSON File

```bash
cat > config.json << 'EOF'
{"name":"test","value":123,"nested":{"key":"value"}}
EOF
```

### YAML File

```bash
cat > config.yaml << 'EOF'
application:
  name: precommit-lab
  version: 1.0
  settings:
    debug: true
    timeout: 30
EOF
```

---

# ✅ Verification

---

## 🔹 Step 1: Commit Files

```bash
git add .pre-commit-config.yaml .flake8 .bandit app.py config.json config.yaml

git commit -m "Add pre-commit configuration and sample files"
```

Hooks execute automatically.

Expected:

```text
All checks passed.
```

---

## 🔹 Step 2: Test Hook Enforcement

Create intentionally bad code:

```bash
cat > bad_code.py << 'EOF'
def bad_function(x,y):
    password="secret123"
    return x+y
EOF
```

Attempt commit:

```bash
git add bad_code.py
git commit -m "Test bad code"
```

Expected failures:

❌ Black

❌ Flake8

❌ Bandit

Commit blocked.

---

## 🔹 Step 3: Emergency Bypass

```bash
git commit -m "Emergency commit" --no-verify
```

> ⚠️ Use only in emergencies.

---

## 🔹 Step 4: Verify Hook Installation

```bash
pre-commit run --all-files

ls -la .git/hooks/

cat .git/hooks/pre-commit | head -20
```

---

## 🔹 Step 5: Update Hook Versions

```bash
pre-commit autoupdate
```

Updates hook versions automatically.

---

# 🎯 Expected Outcomes

After completing this lab you should have:

✅ Pre-commit installed

✅ Black formatting enabled

✅ Flake8 linting configured

✅ Bandit security scanning enabled

✅ JSON validation hooks

✅ YAML validation hooks

✅ File size enforcement

✅ Custom TODO validation

---

# 📋 Verification Checklist

| Check | Status |
|---------|---------|
| Pre-commit Installed | ✅ |
| Git Hooks Configured | ✅ |
| Black Working | ✅ |
| Flake8 Working | ✅ |
| Bandit Working | ✅ |
| JSON Validation | ✅ |
| YAML Validation | ✅ |
| Commit Blocking Enabled | ✅ |
| Custom TODO Hook Added | ✅ |

---

# 🛠️ Troubleshooting Guide

---

## ❌ Pre-commit Command Not Found

```bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc

source ~/.bashrc
```

---

## ❌ Hooks Not Running

```bash
pre-commit uninstall

pre-commit install
```

---

## ❌ Black and Flake8 Conflicts

Ensure `.flake8` contains:

```ini
extend-ignore = E203, W503
```

---

## ❌ Bandit Too Strict

Modify:

```yaml
args: ['-ll']
```

Only high-severity issues reported.

---

## ❌ Hooks Running Slowly

Run specific hooks:

```bash
pre-commit run black --all-files

pre-commit run flake8 --all-files
```

---

# 🏗️ DevOps Quality Gate Architecture

```text
Developer
    │
    ▼
Git Commit
    │
    ▼
Pre-commit Hook
    │
    ├── Black
    ├── Flake8
    ├── Bandit
    ├── JSON Validation
    ├── YAML Validation
    └── Custom TODO Check
    │
    ▼
Pass ✅
    │
    ▼
Commit Accepted

Fail ❌
    │
    ▼
Commit Blocked
```

---

# 🎓 Conclusion

Congratulations! 🎉

You have successfully implemented a **Pre-commit Quality Gate System** that enforces quality standards before code enters your repository.

### Key Components Implemented

🔹 Black — Automated Formatting

🔹 Flake8 — Code Quality Enforcement

🔹 Bandit — Security Vulnerability Detection

🔹 JSON/YAML Validation

🔹 File Size Protection

🔹 Custom TODO Detection

### DevOps Benefits

✅ Faster Code Reviews

✅ Consistent Coding Standards

✅ Early Security Detection

✅ Reduced Technical Debt

✅ Improved Team Collaboration

✅ Stronger CI/CD Pipelines

Pre-commit hooks serve as the **first line of defense** in modern DevOps workflows and are commonly paired with CI/CD pipelines to create multiple layers of quality assurance across enterprise environments.

---

## 🏆 Lab Completed Successfully

**Pre-commit Quality Gate Setup Lab** ✔️

🚀 Happy Coding & Secure Committing!
