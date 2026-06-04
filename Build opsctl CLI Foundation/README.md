# 🚀 Build opsctl CLI Foundation 

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/CLI-Development-green?style=for-the-badge&logo=gnubash" />
  <img src="https://img.shields.io/badge/Argparse-Framework-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Linux-Terminal-black?style=for-the-badge&logo=linux" />
  <img src="https://img.shields.io/badge/Git-Version_Control-red?style=for-the-badge&logo=git" />
</p>

---

# 📖 Overview

In this lab, you will build **opsctl**, a modular command-line interface (CLI) tool for operational management. The project demonstrates professional CLI architecture, argument parsing, command routing, configuration persistence, version management, and extensibility.

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Design and implement a structured CLI architecture

✅ Parse and validate command-line arguments

✅ Build modular command implementations

✅ Implement version and help management

✅ Create persistent configuration storage

✅ Apply CLI development best practices

✅ Handle errors gracefully

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming knowledge
- Familiarity with Linux terminal commands
- Understanding of Git version control
- Experience using command-line tools
- Knowledge of Python functions and modules

---

# 🖥️ Environment Setup

## 🔹 Step 1: Install Required Tools

```bash
# Update package manager
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip python3-venv

# Verify installation
python3 --version
pip3 --version
```

Expected Output:

```bash
Python 3.x.x
pip x.x.x
```

---

## 🔹 Step 2: Create Project Structure

```bash
mkdir -p ~/opsctl-project
cd ~/opsctl-project

python3 -m venv venv
source venv/bin/activate

mkdir -p opsctl/{commands,utils}

touch opsctl/__init__.py
touch opsctl/commands/__init__.py
touch opsctl/utils/__init__.py

touch opsctl/cli.py
touch opsctl/version.py
touch setup.py
touch README.md
```

Project Structure:

```text
opsctl-project/
│
├── opsctl/
│   ├── __init__.py
│   ├── cli.py
│   ├── version.py
│   │
│   ├── commands/
│   │   ├── __init__.py
│   │   ├── status.py
│   │   ├── deploy.py
│   │   └── config.py
│   │
│   └── utils/
│       ├── __init__.py
│       └── helpers.py
│
├── setup.py
├── README.md
└── venv/
```

---

# 🏗️ Task 1: Design CLI Structure and Argument Handling

---

## 🔹 Step 1: Create Version Module

Create:

```text
opsctl/version.py
```

```python
"""Version information for opsctl."""

__version__ = "0.1.0"
__author__ = "DevOps Team"
__description__ = "Operational CLI tool for system management"
```

---

## 🔹 Step 2: Implement Core CLI Framework

Create:

```text
opsctl/cli.py
```

Responsibilities:

### ✅ Global Arguments

```bash
opsctl --version
opsctl --verbose
```

### ✅ Subcommands

```bash
opsctl status
opsctl deploy
opsctl config
```

### ✅ Argument Parser

Use:

```python
argparse.ArgumentParser()
```

### ✅ Subparsers

```python
subparsers = parser.add_subparsers(
    dest="command",
    help="Available commands"
)
```

### ✅ Command Routing

```python
if hasattr(args, "func"):
    return args.func(args)
```

---

## 🔹 Step 3: Implement Command Modules

Create:

```text
opsctl/commands/__init__.py
```

```python
"""Command modules for opsctl."""

from . import status
from . import deploy
from . import config

__all__ = [
    "status",
    "deploy",
    "config"
]
```

---

### 📊 Status Command

Create:

```text
opsctl/commands/status.py
```

Responsibilities:

- Service health checks
- Resource usage display
- Deployment information
- JSON/Text output

Supported Usage:

```bash
opsctl status

opsctl status --service nginx

opsctl status --format json
```

Arguments:

| Argument | Description |
|-----------|------------|
| --service | Specific service |
| --format | text/json |

---

### 🚀 Deploy Command

Create:

```text
opsctl/commands/deploy.py
```

Responsibilities:

- Validate application
- Validate environment
- Simulate deployment
- Display progress

Supported Usage:

```bash
opsctl deploy --app myapp --env dev

opsctl deploy --app webapp --env prod --version 1.2.3
```

Arguments:

| Argument | Required |
|-----------|-----------|
| --app | Yes |
| --env | Yes |
| --version | No |

Valid Environments:

```text
dev
staging
prod
```

---

### ⚙️ Config Command

Create:

```text
opsctl/commands/config.py
```

Configuration File:

```bash
~/.opsctl/config.json
```

Supported Commands:

```bash
opsctl config set api_endpoint https://api.example.com

opsctl config get api_endpoint
```

Responsibilities:

- Read configuration
- Write configuration
- Create directories automatically
- Handle missing keys

---

## 🔹 Step 4: Create Utility Functions

Create:

```text
opsctl/utils/helpers.py
```

Functions:

### ✅ Success Output

```python
print_success("Deployment successful")
```

Output:

```text
[SUCCESS] Deployment successful
```

---

### ❌ Error Output

```python
print_error("Invalid environment")
```

Output:

```text
[ERROR] Invalid environment
```

---

### ℹ️ Info Output

```python
print_info("Starting deployment")
```

Output:

```text
[INFO] Starting deployment
```

---

### 🌍 Environment Validation

Valid values:

```python
[
    "dev",
    "staging",
    "prod"
]
```

---

## 🔹 Step 5: Create Setup Configuration

Create:

```text
setup.py
```

Features:

- Package metadata
- Entry point registration
- Version management
- Python requirement specification

Console Entry Point:

```python
entry_points={
    'console_scripts': [
        'opsctl=opsctl.cli:main',
    ],
}
```

---

# 🛠️ Task 2: Implement and Test CLI Commands

---

## 🔹 Step 1: Complete All TODO Sections

Implement functionality for:

### cli.py

✔ Global arguments

✔ Subparsers

✔ Command routing

✔ Help handling

✔ Version handling

---

### status.py

✔ Status checks

✔ JSON output

✔ Exit codes

---

### deploy.py

✔ Deployment simulation

✔ Environment validation

✔ Progress output

✔ Error handling

---

### config.py

✔ Read JSON config

✔ Write JSON config

✔ Create config directory

✔ Handle missing values

---

## 🔹 Step 2: Install the CLI Tool

Activate virtual environment:

```bash
source ~/opsctl-project/venv/bin/activate
```

Install package:

```bash
cd ~/opsctl-project

pip install -e .
```

Expected:

```text
Successfully installed opsctl
```

---

## 🔹 Step 3: Test Basic Functionality

### Version

```bash
opsctl --version
```

Expected:

```text
opsctl 0.1.0
```

---

### Help

```bash
opsctl --help
```

```bash
opsctl status --help
```

```bash
opsctl deploy --help
```

```bash
opsctl config --help
```

---

## 🔹 Step 4: Test Commands

### Status Command

```bash
opsctl status
```

```bash
opsctl status --format json
```

---

### Config Commands

```bash
opsctl config set api_endpoint https://api.example.com
```

```bash
opsctl config get api_endpoint
```

Expected:

```text
https://api.example.com
```

---

### Deploy Command

```bash
opsctl deploy --app myapp --env dev
```

Example Output:

```text
[INFO] Starting deployment
[INFO] Validating application
[INFO] Deploying...
[SUCCESS] Deployment completed
```

---

## 🔹 Step 5: Add Error Handling

### Invalid Environment

```bash
opsctl deploy --app test --env invalid
```

Expected:

```text
[ERROR] Invalid environment
```

---

### Missing Argument

```bash
opsctl deploy --app test
```

Expected:

```text
error: the following arguments are required: --env
```

---

### Missing Configuration Key

```bash
opsctl config get nonexistent_key
```

Expected:

```text
Configuration key not found
```

---

# ✅ Verification

---

## Verify Installation

```bash
which opsctl
```

Expected:

```text
~/opsctl-project/venv/bin/opsctl
```

---

## Verify Version

```bash
opsctl --version | grep "0.1.0"
```

---

## Verify Commands

```bash
opsctl --help | grep -E "(status|deploy|config)"
```

Expected:

```text
status
deploy
config
```

---

## Verify Configuration Persistence

```bash
opsctl config set test_key test_value
```

```bash
opsctl config get test_key
```

Expected:

```text
test_value
```

---

## Verify Config File

```bash
ls -la ~/.opsctl/config.json
```

```bash
cat ~/.opsctl/config.json
```

Example:

```json
{
  "test_key": "test_value",
  "api_endpoint": "https://api.example.com"
}
```

---

## Verify Status Command

```bash
opsctl status
echo $?
```

Expected:

```text
0
```

---

## Verify Deploy Command

```bash
opsctl deploy --app testapp --env dev
echo $?
```

Expected:

```text
0
```

---

# 🧪 Error Handling Tests

---

### Invalid Command

```bash
opsctl invalid_command
```

Expected:

```text
invalid choice
```

---

### Missing Required Argument

```bash
opsctl deploy
```

Expected:

```text
required argument missing
```

---

# 🛠️ Troubleshooting

## Issue: Command Not Found

```bash
source ~/opsctl-project/venv/bin/activate
```

Reinstall:

```bash
pip install -e .
```

---

## Issue: Import Errors

Verify package files:

```bash
find opsctl -name "__init__.py"
```

Check Python path:

```bash
python3 -c "import sys; print(sys.path)"
```

---

## Issue: Config Permission Problems

Check permissions:

```bash
ls -la ~/.opsctl/
```

Create manually:

```bash
mkdir -p ~/.opsctl
chmod 755 ~/.opsctl
```

---

## Issue: Argument Parsing Errors

Verify:

```python
dest="command"
```

And:

```python
set_defaults(func=execute)
```

for every subcommand parser.

---

# 🎓 Conclusion

Congratulations! 🎉

You have successfully built a professional CLI foundation using Python.

The completed **opsctl** project includes:

✅ Structured CLI architecture

✅ Modular command system

✅ Status command

✅ Deploy command

✅ Configuration management

✅ Help documentation

✅ Version management

✅ Persistent settings

✅ Error handling

✅ Extensible project design

---

# 🚀 Key Takeaways

- CLI tools benefit from clear command hierarchies.
- argparse simplifies argument parsing.
- Modular architecture improves maintainability.
- Configuration persistence enhances usability.
- Good help documentation improves user experience.
- Error handling is essential for production tools.

---

# 📈 Next Steps

- Add structured logging
- Implement authentication
- Add YAML output support
- Create automated tests
- Add command aliases
- Integrate with real infrastructure APIs
- Support Kubernetes and Docker operations
- Publish opsctl to PyPI

---

**🏆 Lab Completed Successfully!**
