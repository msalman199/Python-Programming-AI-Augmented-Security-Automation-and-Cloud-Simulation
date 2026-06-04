# 🛡️ Safe Subprocess Runner Library 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Security-Command_Validation-red?style=for-the-badge&logo=shield" />
  <img src="https://img.shields.io/badge/Linux-CLI-black?style=for-the-badge&logo=linux" />
  <img src="https://img.shields.io/badge/Subprocess-Automation-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/DevOps-Secure_Execution-orange?style=for-the-badge" />
</p>

---

# 📖 Overview

In this lab, you will build a **Safe Subprocess Runner Library** using Python. The project focuses on secure command execution, command validation, timeout handling, logging, and protection against command injection attacks.

The final solution will provide a reusable library that can safely execute approved Linux commands while preventing dangerous operations.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Execute Linux commands securely using Python subprocess

✅ Prevent command injection attacks

✅ Implement command validation using whitelisting

✅ Handle execution timeouts

✅ Manage subprocess errors gracefully

✅ Create reusable automation libraries

✅ Implement structured logging and auditing

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming knowledge
- Understanding of Python functions and classes
- Familiarity with Linux commands
- Knowledge of subprocess execution concepts
- Basic understanding of cybersecurity principles

---

# 🖥️ Environment Setup

## 🔹 Step 1: Start Lab Environment

Launch your Linux machine using the **Start Lab** button.

---

## 🔹 Step 2: Prepare Development Environment

```bash
# Update package list
sudo apt update

# Install Python and virtual environment tools
sudo apt install -y python3 python3-pip python3-venv

# Create project directory
mkdir -p ~/subprocess-lab

cd ~/subprocess-lab

# Create virtual environment
python3 -m venv venv

# Activate environment
source venv/bin/activate
```

Verify installation:

```bash
python3 --version
pip3 --version
```

---

## 🔹 Step 3: Create Project Structure

```bash
touch safe_runner.py
touch test_runner.py

mkdir -p logs
```

Project layout:

```text
subprocess-lab/
│
├── safe_runner.py
├── test_runner.py
├── examples.py
├── verify_security.py
│
├── logs/
│   └── subprocess.log
│
└── venv/
```

---

# 🏗️ Task 1: Build the Safe Subprocess Runner

---

## 🔹 Step 1.1: Create Base Runner Class

Create:

```text
safe_runner.py
```

Core imports:

```python
import subprocess
import shlex
import logging

from typing import Optional
from typing import List
from typing import Dict
from typing import Union

from pathlib import Path
```

---

### 📋 Logging Configuration

Configure logging to:

- Store execution logs
- Display runtime messages
- Track security events

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/subprocess.log"),
        logging.StreamHandler()
    ]
)
```

---

### 🔒 Allowed Commands Whitelist

Use a whitelist approach:

```python
ALLOWED_COMMANDS = {
    "ls",
    "cat",
    "echo",
    "pwd",
    "whoami",
    "date",
    "df",
    "du",
    "grep",
    "wc"
}
```

Why whitelist?

✅ More secure than blacklisting

✅ Blocks unknown commands automatically

✅ Reduces attack surface

---

## 🔹 Step 1.2: Implement Command Validation

Complete:

```python
validate_command()
```

Responsibilities:

### ✅ Convert Strings Safely

Use:

```python
shlex.split()
```

Example:

```python
"ls -la"
```

Becomes:

```python
["ls", "-la"]
```

---

### ✅ Validate Empty Commands

Reject:

```python
""
```

```python
[]
```

---

### ✅ Extract Base Command

Example:

```python
ls -la
```

Base command:

```python
ls
```

---

### ✅ Check Whitelist

Allowed:

```python
ls
pwd
whoami
```

Blocked:

```python
rm
curl
wget
bash
```

---

### ✅ Detect Dangerous Patterns

Block:

```bash
;
&&
||
|
>
<
`
```

Examples:

```bash
ls; rm -rf /
```

```bash
echo test | grep test
```

```bash
cat file && whoami
```

All should fail validation.

---

### ✅ Detect Path Traversal

Reject:

```bash
../../../etc/passwd
```

```bash
../../secret.txt
```

Protect against:

- Sensitive file access
- Directory traversal attacks

---

## 🔹 Step 1.3: Implement Secure Command Execution

Complete:

```python
execute()
```

---

### Execution Flow

#### 1️⃣ Validate Command

```python
validate_command()
```

---

#### 2️⃣ Log Execution

Example:

```text
INFO Executing command: ls -la
```

---

#### 3️⃣ Execute Securely

Use:

```python
subprocess.run()
```

Recommended options:

```python
shell=False
```

```python
timeout=self.timeout
```

```python
capture_output=True
```

```python
text=True
```

```python
check=False
```

---

### Why shell=False?

❌ Dangerous

```python
shell=True
```

Allows:

```bash
ls; rm -rf /
```

---

✅ Secure

```python
shell=False
```

Treats arguments separately.

---

### Return Format

Success:

```python
{
    "success": True,
    "returncode": 0,
    "stdout": "...",
    "stderr": ""
}
```

Failure:

```python
{
    "success": False,
    "error": "Validation failed"
}
```

---

### Handle Timeouts

Catch:

```python
subprocess.TimeoutExpired
```

Return:

```python
{
    "success": False,
    "error": "Command timeout"
}
```

---

### Handle Unexpected Exceptions

Catch:

```python
Exception
```

Return:

```python
{
    "success": False,
    "error": str(exception)
}
```

---

## 🔹 Step 1.4: Implement Pipeline Execution (Challenge)

Complete:

```python
execute_pipeline()
```

Requirements:

### ✅ Validate All Commands

Before execution starts.

---

### ✅ Execute Sequentially

Example:

```python
[
    "pwd",
    "ls",
    "whoami"
]
```

---

### ✅ Stop on Failure

If one command fails:

```python
break
```

---

### ✅ Return Combined Results

Example:

```python
{
    "success": True,
    "results": [...]
}
```

---

# 🧪 Task 2: Test and Validate the Runner

---

## 🔹 Step 2.1: Create Test Script

Create:

```text
test_runner.py
```

Test Categories:

### ✅ Basic Execution

Commands:

```bash
ls -la
```

```bash
echo "Hello World"
```

```bash
pwd
```

---

### ✅ Validation Testing

Attempt:

```bash
ls; rm -rf /
```

```bash
echo test | grep test
```

```bash
rm -rf /
```

Expected:

```text
Blocked
```

---

### ✅ Timeout Testing

Create:

```python
runner = SafeSubprocessRunner(timeout=2)
```

Execute:

```bash
sleep 5
```

Expected:

```text
Command timeout
```

---

### ✅ Error Handling

Example:

```bash
cat missing_file.txt
```

Expected:

```text
No such file
```

---

## 🔹 Step 2.2: Execute Test Suite

Run:

```bash
python3 test_runner.py
```

Expected:

```text
Basic execution tests passed
Validation tests passed
Timeout tests passed
Error handling tests passed
```

---

# 🌍 Task 3: Create Real-World Examples

---

## 🔹 Example 1: System Information Collector

Create:

```text
examples.py
```

Gather:

### Current User

```bash
whoami
```

---

### Current Directory

```bash
pwd
```

---

### Disk Usage

```bash
df -h
```

Display results in structured format.

---

## 🔹 Example 2: File Operations

Operations:

### List Files

```bash
ls -la
```

---

### Count Lines

```bash
wc -l filename
```

---

### Search Content

```bash
grep keyword filename
```

---

# ✅ Verification

---

## Step 1: Verify Security Controls

Create:

```bash
verify_security.py
```

Test dangerous commands:

```python
dangerous_commands = [
    "ls; rm -rf /tmp/test",
    "cat /etc/passwd && echo hacked",
    "echo test | grep test",
    "rm -rf /",
    "cat /etc/passwd"
]
```

Run:

```bash
python3 verify_security.py
```

Expected:

```text
Blocked: True
Blocked: True
Blocked: True
Blocked: True
Blocked: True
```

---

## Step 2: Verify Timeout Handling

Run:

```bash
python3
```

```python
from safe_runner import SafeSubprocessRunner

runner = SafeSubprocessRunner(timeout=2)

result = runner.execute("sleep 5")
```

Expected:

```text
Timeout handled successfully
```

---

## Step 3: Verify Logging

View log file:

```bash
cat logs/subprocess.log
```

Expected:

```text
INFO Executing command: pwd
INFO Executing command: ls -la
WARNING Blocked dangerous command
```

---

## Step 4: Run Complete Test Suite

```bash
python3 test_runner.py
```

Expected:

### Allowed Commands

```text
SUCCESS
```

---

### Dangerous Commands

```text
BLOCKED
```

---

### Timeout Events

```text
HANDLED
```

---

### Error Scenarios

```text
GRACEFULLY MANAGED
```

---

# 🛠️ Troubleshooting

---

## Issue: Module Not Found

Activate virtual environment:

```bash
source venv/bin/activate
```

---

## Issue: Permission Denied

Make scripts executable:

```bash
chmod +x test_runner.py
```

---

## Issue: Timeout Not Triggering

Verify:

```python
timeout=self.timeout
```

exists in:

```python
subprocess.run()
```

---

## Issue: Dangerous Commands Execute

Check:

### Whitelist Validation

```python
ALLOWED_COMMANDS
```

### Injection Detection

```python
;
&&
||
|
>
<
`
```

---

## Issue: Logging Missing

Create log directory:

```bash
mkdir -p logs
```

Verify:

```python
logging.FileHandler()
```

---

# 🔐 Security Best Practices Learned

### Never Trust User Input

❌ Dangerous:

```python
subprocess.run(user_input, shell=True)
```

---

### Use Whitelisting

✅ Safe:

```python
if command not in allowed_commands:
    reject()
```

---

### Disable Shell Execution

✅ Safe:

```python
shell=False
```

---

### Apply Timeouts

✅ Prevents:

- Infinite loops
- Hanging processes
- Resource exhaustion

---

### Log Security Events

Track:

- Executed commands
- Validation failures
- Timeout events
- Exceptions

---

# 🎓 Conclusion

Congratulations! 🎉

You have successfully built a **Secure Subprocess Runner Library** capable of:

✅ Secure command execution

✅ Command whitelist enforcement

✅ Injection attack prevention

✅ Timeout management

✅ Structured error handling

✅ Execution auditing and logging

✅ Reusable DevOps automation functionality

---

# 🚀 Key Takeaways

- Never trust external input.
- Whitelisting is safer than blacklisting.
- Always disable shell execution when possible.
- Every subprocess should have a timeout.
- Security-relevant actions should be logged.
- Structured error handling improves reliability.

---

# 📈 Next Steps

- Add configuration-based command policies
- Implement environment variable validation
- Add command output sanitization
- Create YAML/JSON configuration support
- Add metrics collection and monitoring
- Integrate with CI/CD pipelines
- Build a REST API around the runner
- Package and publish to PyPI

---

# 🧹 Cleanup

Deactivate environment:

```bash
deactivate
```

Optional cleanup:

```bash
cd ~

rm -rf subprocess-lab
```

---

**🏆 Lab Completed Successfully!**
