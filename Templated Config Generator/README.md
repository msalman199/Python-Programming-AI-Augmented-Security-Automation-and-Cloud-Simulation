# 🚀 Templated Config Generator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Jinja2](https://img.shields.io/badge/Jinja2-Templates-red?style=for-the-badge)
![YAML](https://img.shields.io/badge/YAML-Configuration-orange?style=for-the-badge)
![JSON Schema](https://img.shields.io/badge/JSON-Schema-green?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Automation-purple?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-black?style=for-the-badge\&logo=linux)

# 📦 Templated Configuration Generator

### Generate • Validate • Standardize • Automate

Reusable configuration management using **Jinja2 Templates**, **YAML Data Files**, and **JSON Schema Validation**.

</div>

---

# 📖 Overview

Modern DevOps environments require consistent and repeatable configuration management across multiple environments.

This lab demonstrates how to build a complete **Templated Configuration Generator** capable of:

✅ Creating reusable configuration templates

✅ Generating environment-specific configurations

✅ Validating generated outputs

✅ Automating configuration workflows

✅ Reducing configuration drift and human errors

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

* 🔹 Create reusable Jinja2 templates
* 🔹 Generate standardized configurations
* 🔹 Separate configuration data from templates
* 🔹 Validate configurations using JSON Schema
* 🔹 Build a practical DevOps configuration workflow

---

# 📋 Prerequisites

Before starting, ensure you have:

* 🐧 Basic Linux command-line knowledge
* 📄 Understanding of YAML and JSON
* 🐍 Basic Python knowledge
* 📝 Experience using text editors
* ⚙️ Basic configuration management concepts

---

# 🏗️ Environment Setup

After launching the lab environment, install required tools.

---

## 📦 Install Required Packages

```bash
sudo apt update

sudo apt install -y \
    python3 \
    python3-pip \
    python3-venv
```

---

## 📂 Create Project Directory

```bash
mkdir -p ~/config-generator

cd ~/config-generator
```

---

## 🐍 Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 📥 Install Python Dependencies

```bash
pip install \
    jinja2 \
    pyyaml \
    jsonschema
```

---

# 🧩 Task 1: Build Template-Based Configuration Generator

---

# 🔹 Step 1: Create Project Structure

```bash
cd ~/config-generator

mkdir -p \
    templates \
    configs \
    data \
    schemas

touch generator.py validator.py
```

---

## 📁 Project Structure

```text
config-generator/
│
├── templates/
│   ├── nginx.conf.j2
│   └── app_config.yaml.j2
│
├── configs/
│
├── data/
│   ├── dev_config.yaml
│   └── prod_config.yaml
│
├── schemas/
│   └── app_config_schema.json
│
├── generator.py
├── validator.py
└── verify_lab.sh
```

---

# 🔹 Step 2: Create Configuration Templates

Templates allow dynamic configuration generation.

---

## 🌐 Nginx Template

Create:

```bash
templates/nginx.conf.j2
```

Features:

* Load balancing
* SSL support
* Dynamic backends
* Custom headers
* Environment awareness

Key Jinja2 Concepts Used:

```jinja2
{{ variable }}

{% if condition %}

{% for item in list %}

{% endif %}
```

---

## ⚙️ Application Configuration Template

Create:

```bash
templates/app_config.yaml.j2
```

Features:

* Application settings
* Database settings
* Cache configuration
* Logging configuration
* Environment-specific options

---

# 🔹 Step 3: Create Environment Data Files

---

## 🧪 Development Configuration

Create:

```bash
data/dev_config.yaml
```

Characteristics:

```yaml
environment: development
ssl_enabled: false
log_level: DEBUG
```

Development focuses on:

* Local testing
* Debug logging
* Reduced resource usage

---

## 🏭 Production Configuration

Create:

```bash
data/prod_config.yaml
```

Characteristics:

```yaml
environment: production
ssl_enabled: true
log_level: INFO
```

Production focuses on:

* Security
* Performance
* High availability

---

# 🔹 Step 4: Implement Configuration Generator

Create:

```bash
generator.py
```

---

## 🚀 Generator Features

The ConfigGenerator class should support:

### 📥 Loading YAML Data

```python
yaml.safe_load()
```

### 📄 Loading Jinja2 Templates

```python
Environment(
    loader=FileSystemLoader(),
    trim_blocks=True,
    lstrip_blocks=True
)
```

### ⚡ Rendering Templates

```python
template.render(**data)
```

### 💾 Saving Generated Configurations

```python
configs/
├── nginx.conf
└── app_config.yaml
```

---

## 🔐 Make Executable

```bash
chmod +x generator.py
```

---

# 🔹 Step 5: Create Validation Schema

Create:

```bash
schemas/app_config_schema.json
```

Purpose:

✅ Enforce required fields

✅ Validate data types

✅ Validate version format

✅ Validate environments

✅ Prevent invalid configurations

---

## Example Validation Rules

```json
{
  "environment": {
    "enum": [
      "development",
      "staging",
      "production"
    ]
  }
}
```

---

# 🔹 Step 6: Implement Configuration Validator

Create:

```bash
validator.py
```

---

## 🔍 Validator Features

### YAML Validation

Uses:

```python
jsonschema.validate()
```

Checks:

* Required fields
* Correct types
* Value ranges
* Pattern matching

---

### Nginx Validation

Checks:

✅ Balanced braces

✅ Required blocks

✅ Directive syntax

✅ Server block existence

---

## 🔐 Make Executable

```bash
chmod +x validator.py
```

---

# 🧩 Task 2: Test and Validate Configuration Generation

---

# 🔹 Step 1: Complete Generator Implementation

Implement all TODO sections.

---

## 💡 Helpful Hints

### Initialize Jinja2

```python
Environment(
    loader=FileSystemLoader(self.template_dir),
    trim_blocks=True,
    lstrip_blocks=True
)
```

---

### Load YAML

```python
yaml.safe_load(file)
```

---

### Render Template

```python
template.render(**data)
```

---

### List Templates

```python
os.listdir(self.template_dir)
```

---

# 🔹 Step 2: Complete Validator Implementation

Implement all TODO sections.

---

## 💡 Helpful Hints

### Load Schema

```python
json.load(file)
```

### Validate

```python
validate(instance, schema)
```

### Check Nginx Braces

```python
config.count("{")
config.count("}")
```

---

# 🔹 Step 3: Generate Development Configurations

Generate all configurations:

```bash
python3 generator.py data/dev_config.yaml
```

---

## Verify Output

```bash
ls -lh configs/
```

View generated files:

```bash
cat configs/nginx.conf

cat configs/app_config.yaml
```

---

# 🔹 Step 4: Generate Production Configurations

```bash
python3 generator.py data/prod_config.yaml
```

---

## Compare Environments

```bash
diff configs/nginx.conf \
<(python3 generator.py data/dev_config.yaml nginx.conf.j2 2>/dev/null && cat configs/nginx.conf)
```

Expected Differences:

* SSL enabled
* Backend servers
* Logging levels
* Cache settings

---

# 🔹 Step 5: Validate Generated Configurations

---

## Validate Application Config

```bash
python3 validator.py \
configs/app_config.yaml \
app_config_schema.json
```

---

## Validate Nginx Config

```bash
python3 validator.py \
configs/nginx.conf \
nginx
```

---

# 🔹 Step 6: Test Edge Cases

Create invalid configuration:

```bash
data/invalid_config.yaml
```

Example:

```yaml
app_name: testapp
environment: development

db_host: localhost
db_port: 5432
```

Missing:

```yaml
version:
```

---

## Test Validation Failure

```bash
python3 generator.py \
data/invalid_config.yaml \
app_config.yaml.j2

python3 validator.py \
configs/app_config.yaml \
app_config_schema.json
```

Expected:

❌ Validation Error

---

# ✅ Verification

---

## Verify Generated Files

```bash
test -f configs/nginx.conf \
&& echo "Nginx config: OK"

test -f configs/app_config.yaml \
&& echo "App config: OK"
```

---

## Verify Content

```bash
grep "myapp" configs/nginx.conf

grep "environment: production" \
configs/app_config.yaml
```

Expected:

```text
App name found: OK
Environment set: OK
```

---

# 🔍 Verify Validator

```bash
python3 validator.py \
configs/app_config.yaml \
app_config_schema.json
```

Check exit code:

```bash
echo $?
```

Expected:

```text
0
```

---

## Verify Nginx Structure

```bash
grep -c "server {" configs/nginx.conf

grep -c "location" configs/nginx.conf
```

Expected:

```text
1
1+
```

---

# 🤖 Create Verification Script

Create:

```bash
verify_lab.sh
```

Purpose:

✅ Verify generator

✅ Verify validator

✅ Verify output files

✅ Verify Nginx structure

Run:

```bash
chmod +x verify_lab.sh

./verify_lab.sh
```

---

# 📊 Configuration Generation Workflow

```text
          YAML DATA
               │
               ▼
     ┌─────────────────┐
     │ Jinja2 Template │
     └────────┬────────┘
              │
              ▼
     ┌─────────────────┐
     │ Config Generator│
     └────────┬────────┘
              │
              ▼
      Generated Configs
              │
              ▼
     ┌─────────────────┐
     │ Config Validator│
     └────────┬────────┘
              │
              ▼
         Deployment
```

---

# 🛠 Troubleshooting

---

## ❌ Template Not Found

Verify:

```bash
ls templates/
```

Ensure:

```text
*.j2
```

files exist.

---

## ❌ YAML Parsing Errors

Validate:

```bash
python3 -c \
"import yaml; yaml.safe_load(open('data/dev_config.yaml'))"
```

Check:

* Proper indentation
* Spaces instead of tabs
* Correct key:value syntax

---

## ❌ Validation Failure

Debug configuration:

```python
print(
    yaml.safe_load(
        open('configs/app_config.yaml')
    )
)
```

Verify:

* Schema path
* Generated YAML
* Required fields

---

## ❌ Extra Whitespace

Use:

```python
trim_blocks=True
lstrip_blocks=True
```

Inside templates:

```jinja2
{%- %}
```

for whitespace control.

---

# 🎓 Key Takeaways

✅ Jinja2 enables reusable configuration templates

✅ YAML separates data from logic

✅ JSON Schema catches configuration errors early

✅ Environment-specific configs become easy to manage

✅ Template-driven workflows reduce manual mistakes

✅ This approach scales to enterprise DevOps environments

---

# 🚀 Real-World Applications

The same concepts power:

* 🔹 Ansible Templates
* 🔹 Helm Charts
* 🔹 Terraform Modules
* 🔹 Kubernetes Manifests
* 🔹 GitOps Workflows
* 🔹 CI/CD Pipelines

---

# 🏆 Lab Completed

You have successfully built a complete **Templated Configuration Generator** that:

✔ Creates reusable templates

✔ Generates development and production configs

✔ Validates configurations automatically

✔ Supports scalable environment management

✔ Implements industry-standard DevOps practices

✔ Reduces configuration drift and deployment failures

---

<div align="center">

## 🌟 Infrastructure as Code Starts with Consistent Configuration 🌟

### Happy Learning & Happy Automating 🚀

</div>
