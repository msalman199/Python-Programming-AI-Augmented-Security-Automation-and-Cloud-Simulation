# 🚀 Typed Configuration Loader

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Pydantic](https://img.shields.io/badge/Pydantic-Validation-green?style=for-the-badge)
![YAML](https://img.shields.io/badge/YAML-Config-red?style=for-the-badge&logo=yaml)
![JSON](https://img.shields.io/badge/JSON-Configuration-black?style=for-the-badge&logo=json)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![DevOps](https://img.shields.io/badge/DevOps-Configuration_Management-purple?style=for-the-badge)

---

# 📖 Overview

In modern software systems, configuration management is critical for reliability, maintainability, and security. This lab demonstrates how to build a **Typed Configuration Loader** using Python and Pydantic to ensure configuration files are validated before applications start.

You will implement:

✅ Type-safe configuration loading  
✅ JSON and YAML configuration support  
✅ Schema validation using Pydantic  
✅ Default value handling  
✅ Configuration reloading  
✅ Production-grade error handling  

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

- 🔹 Implement type-safe configuration loading mechanisms
- 🔹 Validate configuration data against expected schemas
- 🔹 Apply default values for missing configuration entries
- 🔹 Detect and handle invalid configuration values
- 🔹 Build robust configuration management systems
- 🔹 Support JSON and YAML configuration formats
- 🔹 Reload configurations dynamically

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming knowledge
- Understanding of dictionaries and classes
- Familiarity with JSON/YAML formats
- Linux command-line experience
- Text editor (VS Code, Vim, Nano)

---

# 🖥️ Environment Setup

## 📦 Install Required Packages

```bash
sudo apt update

sudo apt install -y \
python3 \
python3-pip \
python3-venv
```

---

## 📁 Create Project Directory

```bash
mkdir -p ~/config-loader-lab
cd ~/config-loader-lab
```

---

## 🐍 Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 📥 Install Dependencies

```bash
pip install pyyaml pydantic
```

---

# 🏗️ Project Structure

Create the following directory layout:

```text
config-loader-lab/
│
├── configs/
│   ├── valid_config.yaml
│   ├── minimal_config.json
│   └── invalid_config.yaml
│
├── tests/
│
├── config_loader.py
├── test_configs.py
├── app_example.py
│
└── venv/
```

Create directories:

```bash
mkdir -p configs tests

touch config_loader.py
touch test_configs.py
```

---

# 🛠️ Task 1: Build Configuration Schema and Validator

---

## 📝 Step 1: Create Configuration Models

Inside:

```bash
config_loader.py
```

Create the following models:

### 🗄️ DatabaseConfig

Responsible for database connection settings.

Fields:

| Field | Type | Default |
|---------|---------|---------|
| host | str | localhost |
| port | int | 5432 |
| username | str | Required |
| password | str | Required |
| database | str | Required |
| max_connections | int | 10 |

Validation:

✅ Host cannot be empty  
✅ Port must be between 1 and 65535

---

### ⚡ CacheConfig

Fields:

| Field | Type | Default |
|---------|---------|---------|
| enabled | bool | True |
| ttl_seconds | int | 300 |
| max_size_mb | int | 100 |

Validation:

✅ max_size_mb ≤ 1024

---

### 📜 LoggingConfig

Fields:

| Field | Type | Default |
|---------|---------|---------|
| level | str | INFO |
| format | str | json |
| output_path | str | /var/log/app.log |

Valid log levels:

```text
DEBUG
INFO
WARNING
ERROR
CRITICAL
```

Convert values to uppercase before validation.

---

### 🌍 AppConfig

Main application configuration model.

Fields:

```text
app_name
environment
debug
database
cache
logging
```

Valid environments:

```text
development
staging
production
```

---

# ⚙️ Step 2: Build ConfigLoader Class

The ConfigLoader class should provide:

### 📥 load()

Responsibilities:

- Verify file exists
- Detect YAML or JSON
- Parse configuration
- Validate against AppConfig
- Return validated configuration

---

### 📄 _load_json()

Responsibilities:

- Open file
- Parse JSON
- Return dictionary

---

### 📄 _load_yaml()

Responsibilities:

- Open file
- Parse YAML
- Return dictionary

---

### ✔️ validate_config()

Responsibilities:

- Instantiate AppConfig
- Handle validation errors
- Return validated object

---

### 🔄 reload()

Responsibilities:

- Reload configuration file
- Refresh object
- Return updated configuration

---

# 📂 Step 3: Create Configuration Files

---

## ✅ Valid YAML Configuration

File:

```bash
configs/valid_config.yaml
```

```yaml
app_name: "MyApp"
environment: "production"
debug: false

database:
  host: "db.example.com"
  port: 5432
  username: "app_user"
  password: "secure_password"
  database: "app_db"
  max_connections: 20

cache:
  enabled: true
  ttl_seconds: 600
  max_size_mb: 256

logging:
  level: "INFO"
  format: "json"
  output_path: "/var/log/myapp.log"
```

---

## 🟡 Minimal JSON Configuration

File:

```bash
configs/minimal_config.json
```

```json
{
  "app_name": "MinimalApp",
  "database": {
    "username": "user",
    "password": "pass",
    "database": "testdb"
  }
}
```

---

## ❌ Invalid Configuration

File:

```bash
configs/invalid_config.yaml
```

```yaml
app_name: "InvalidApp"

environment: "testing"

database:
  host: ""
  port: 99999
  username: "user"
  password: "pass"
  database: "db"
```

---

# 🧪 Task 2: Testing and Validation

---

## 🔬 Create Test Suite

File:

```bash
test_configs.py
```

Implement tests for:

### ✅ test_valid_yaml_config()

Verify:

- Configuration loads successfully
- Values match expected data
- Types are correct

---

### ✅ test_minimal_config_with_defaults()

Verify defaults:

```text
database.host
database.port
cache settings
logging settings
```

---

### ❌ test_invalid_config_detection()

Verify:

- Invalid environment rejected
- Invalid host rejected
- Invalid port rejected

---

### ❌ test_missing_required_fields()

Verify:

Missing:

```text
app_name
database.username
```

Raises validation errors.

---

### 🔄 test_config_reload()

Verify:

- Modify config
- Reload configuration
- New values are reflected

---

# ▶️ Run Test Suite

```bash
python3 test_configs.py
```

---

# 💻 Task 3: Practical Application Example

Create:

```bash
app_example.py
```

Application should:

### 1️⃣ Accept Config Path

Example:

```bash
python3 app_example.py configs/valid_config.yaml
```

---

### 2️⃣ Load Configuration

Using:

```python
ConfigLoader()
```

---

### 3️⃣ Print Configuration Summary

Example output:

```text
Application: MyApp
Environment: production
Database Host: db.example.com
Database Port: 5432
Cache Enabled: True
Log Level: INFO
```

---

### 4️⃣ Handle Errors Gracefully

Examples:

```text
Configuration file not found
Validation failed
Invalid environment value
```

---

# 🔍 Verification

---

## ✔️ Test Valid Configuration

```bash
python3 -c "
from config_loader import ConfigLoader
loader = ConfigLoader('configs/valid_config.yaml')
config = loader.load()

assert config.app_name == 'MyApp'
assert config.database.port == 5432

print('Valid config works')
"
```

---

## ✔️ Test Default Values

```bash
python3 -c "
from config_loader import ConfigLoader

loader = ConfigLoader('configs/minimal_config.json')
config = loader.load()

assert config.database.host == 'localhost'
assert config.cache.enabled == True

print('Defaults applied successfully')
"
```

---

## ✔️ Test Validation Errors

```bash
python3 -c "
from config_loader import ConfigLoader

try:
    ConfigLoader('configs/invalid_config.yaml').load()
except Exception:
    print('Validation working correctly')
"
```

---

## ✔️ Execute Full Test Suite

```bash
python3 test_configs.py
```

---

# 🎯 Expected Outcomes

After completing this lab you should have:

✅ Typed configuration models

✅ JSON configuration support

✅ YAML configuration support

✅ Automatic default values

✅ Strong validation rules

✅ Runtime configuration reload capability

✅ Clear validation error reporting

---

# 🚨 Troubleshooting

---

## Issue: Validation Errors Are Hard To Read

### Solution

Catch:

```python
ValidationError
```

And print:

```python
for error in e.errors():
    print(error)
```

---

## Issue: Configuration File Not Found

### Solution

Verify file exists:

```bash
ls -lh configs/
```

Use absolute paths if needed.

---

## Issue: YAML Parsing Errors

### Solution

Validate syntax:

```bash
python3 -c "
import yaml
yaml.safe_load(open('configs/valid_config.yaml'))
"
```

---

## Issue: Missing Dependencies

### Solution

```bash
source venv/bin/activate

pip install pyyaml pydantic
```

---

# 🏆 Key Takeaways

- Type validation prevents runtime failures
- Pydantic simplifies configuration management
- Defaults reduce operational complexity
- YAML and JSON are common production formats
- Validation creates self-documenting configuration schemas
- Robust configuration management is a core DevOps practice

---

# 🚀 Next Steps

Enhance this project by adding:

### 🔐 Environment Variable Overrides

```bash
DB_PASSWORD=mysecret
```

Override config file values dynamically.

---

### 🔒 Configuration Encryption

Protect sensitive values:

```text
passwords
tokens
API keys
```

---

### 📚 Configuration Documentation Generator

Generate documentation automatically from Pydantic schemas.

---

### 🔄 Configuration Versioning

Support:

```text
v1
v2
v3
```

with migration capabilities.

---

# 🎉 Conclusion

You have successfully built a **Typed Configuration Loader** capable of:

✔ Loading JSON and YAML files

✔ Applying default values automatically

✔ Enforcing strict schema validation

✔ Detecting invalid configurations before runtime

✔ Supporting configuration reloads

✔ Improving reliability of production systems

This pattern is widely used in modern DevOps, Cloud, Platform Engineering, MLOps, and Software Engineering environments to ensure applications start with valid and predictable configurations.

Happy Coding! 🚀
