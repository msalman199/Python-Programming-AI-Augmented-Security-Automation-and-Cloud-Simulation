# 🔍 Configuration Drift Scanner

<div align="center">

![DevOps](https://img.shields.io/badge/DevOps-Configuration%20Management-blue?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Bash](https://img.shields.io/badge/Bash-Scripting-green?style=for-the-badge&logo=gnu-bash)
![YAML](https://img.shields.io/badge/YAML-Configuration-red?style=for-the-badge)
![JSON](https://img.shields.io/badge/JSON-Reports-black?style=for-the-badge)
![DeepDiff](https://img.shields.io/badge/DeepDiff-Drift%20Detection-purple?style=for-the-badge)

### 🚀 Detect • Monitor • Prevent Configuration Drift

</div>

---

# 📖 Overview

Configuration drift occurs when systems gradually deviate from their intended configuration state due to manual changes, software updates, or unauthorized modifications.

This lab guides you through building a complete **Configuration Drift Scanner** capable of:

✅ Capturing baseline configurations

✅ Detecting configuration changes

✅ Comparing YAML configurations

✅ Generating detailed drift reports

✅ Automating configuration compliance checks

---

# 🎯 Learning Objectives

By completing this lab, you will:

- 🔹 Understand configuration drift and its impact on reliability
- 🔹 Capture baseline configurations
- 🔹 Build a drift detection engine
- 🔹 Generate JSON and text-based reports
- 🔹 Automate compliance scanning
- 🔹 Apply DevOps configuration management practices

---

# 📋 Prerequisites

Before starting, ensure you have:

- 🐧 Basic Linux command-line skills
- 📂 Understanding of file operations
- 📄 Familiarity with JSON/YAML formats
- ⚙️ Basic system configuration knowledge
- 🖥️ Shell scripting fundamentals

---

# 🏗️ Environment Setup

The lab uses a Linux machine provided through the **Start Lab** environment.

---

## 📦 Install Required Tools

```bash
sudo apt update

sudo apt install -y \
    python3 \
    python3-pip \
    jq \
    git

pip3 install pyyaml deepdiff
```

---

## ✅ Verify Installation

```bash
python3 --version
jq --version
```

Expected output:

```text
Python 3.x.x
jq-1.x
```

---

# 🧩 Task 1: Create Baseline Configuration Capture System

---

## 🔹 Step 1: Create Project Structure

```bash
mkdir -p ~/config-drift-scanner/{baselines,current,reports,scripts}

cd ~/config-drift-scanner
```

Project Layout:

```text
config-drift-scanner/
├── baselines/
├── current/
├── reports/
└── scripts/
```

---

## 🔹 Step 2: Create Baseline Capture Script

Create the script:

```bash
nano scripts/capture_baseline.sh
```

---

### 📝 Baseline Capture Script

```bash
#!/bin/bash

BASELINE_DIR="$HOME/config-drift-scanner/baselines"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BASELINE_DIR"

capture_system_config() {
    echo "Capturing baseline configuration..."

    cp /etc/hosts "$BASELINE_DIR/hosts.baseline"

    dpkg -l > "$BASELINE_DIR/packages.baseline"

    systemctl list-units --type=service --state=running \
        > "$BASELINE_DIR/services.baseline"

    ip addr show > "$BASELINE_DIR/network.baseline"

    env | sort > "$BASELINE_DIR/environment.baseline"

    echo "Baseline captured successfully at: $BASELINE_DIR"
}

capture_system_config
```

---

### ▶️ Execute Script

```bash
chmod +x scripts/capture_baseline.sh

./scripts/capture_baseline.sh
```

---

## 🔹 Step 3: Create Application Configuration Baseline

Create directory:

```bash
mkdir -p ~/config-drift-scanner/app-configs
```

Create configuration file:

```bash
nano ~/config-drift-scanner/app-configs/app-config.yaml
```

---

### 📝 Sample Application Configuration

```yaml
application:
  name: "WebApp"
  version: "1.0.0"
  port: 8080
  environment: "production"

database:
  host: "localhost"
  port: 5432
  name: "appdb"
  max_connections: 100

security:
  ssl_enabled: true
  token_expiry: 3600
  allowed_origins:
    - "https://example.com"
    - "https://app.example.com"
```

---

### 📦 Save Baseline Copy

```bash
cp \
~/config-drift-scanner/app-configs/app-config.yaml \
~/config-drift-scanner/baselines/app-config.baseline.yaml
```

---

# 🧩 Task 2: Build Configuration Drift Detection System

---

## 🔹 Step 1: Create Python Drift Scanner

Create file:

```bash
nano scripts/drift_scanner.py
```

---

## 🔹 Step 2: Complete Drift Scanner

Replace contents with the complete implementation provided in the lab.

The scanner performs:

### 🔍 Features

- SHA256 Hash Validation
- Line-by-Line Text Comparison
- YAML Deep Comparison
- JSON Report Generation
- Text Report Generation
- Drift Statistics Collection

---

### Make Executable

```bash
chmod +x scripts/drift_scanner.py
```

---

## 🔹 Step 3: Create Current Configuration Capture Script

Create file:

```bash
nano scripts/capture_current.sh
```

Add:

```bash
#!/bin/bash

CURRENT_DIR="$HOME/config-drift-scanner/current"

mkdir -p "$CURRENT_DIR"

echo "Capturing current configuration..."

cp /etc/hosts "$CURRENT_DIR/hosts.current"

dpkg -l > "$CURRENT_DIR/packages.current"

systemctl list-units --type=service --state=running \
    > "$CURRENT_DIR/services.current"

ip addr show > "$CURRENT_DIR/network.current"

cp \
~/config-drift-scanner/app-configs/app-config.yaml \
"$CURRENT_DIR/app-config.current.yaml"

echo "Current configuration captured at: $CURRENT_DIR"
```

---

### Make Executable

```bash
chmod +x scripts/capture_current.sh
```

---

# ⚠️ Step 4: Simulate Configuration Drift

Modify:

```bash
nano ~/config-drift-scanner/app-configs/app-config.yaml
```

---

### Updated Configuration

```yaml
application:
  name: "WebApp"
  version: "1.1.0"
  port: 8080
  environment: "staging"

database:
  host: "localhost"
  port: 5432
  name: "appdb"
  max_connections: 150

security:
  ssl_enabled: true
  token_expiry: 7200
  allowed_origins:
    - "https://example.com"
    - "https://app.example.com"
    - "https://new.example.com"
```

---

### Capture Current State

```bash
./scripts/capture_current.sh
```

---

# 🔍 Step 5: Run Drift Detection

Execute scanner:

```bash
python3 scripts/drift_scanner.py
```

---

## View JSON Report

```bash
cat reports/drift_report_*.json | jq '.'
```

---

## View Text Report

```bash
cat reports/drift_report_*.txt
```

---

# ✅ Verification

---

## Verify Baseline Files

```bash
ls -lh ~/config-drift-scanner/baselines/
```

Check content:

```bash
head -5 ~/config-drift-scanner/baselines/hosts.baseline
```

---

## Verify Drift Reports

```bash
ls -lh ~/config-drift-scanner/reports/
```

---

## Verify YAML Drift Detection

```bash
cat reports/drift_report_*.json | jq \
'.findings[] |
select(.file=="app-config.baseline.yaml")'
```

Expected:

```json
{
  "drift_detected": true
}
```

Detected changes:

- version
- environment
- max_connections
- token_expiry
- allowed_origins

---

# 🤖 Automated Drift Scanning

Create automation script:

```bash
nano scripts/automated_scan.sh
```

---

### Script

```bash
#!/bin/bash

echo "Running automated drift scan..."

./scripts/capture_current.sh

python3 scripts/drift_scanner.py

DRIFT_COUNT=$(cat reports/drift_report_*.json \
| tail -1 \
| jq '.drifts_detected')

if [ "$DRIFT_COUNT" -gt 0 ]; then
    echo "WARNING: $DRIFT_COUNT configuration drift(s) detected!"
    exit 1
else
    echo "No configuration drift detected."
    exit 0
fi
```

---

### Execute

```bash
chmod +x scripts/automated_scan.sh

./scripts/automated_scan.sh
```

---

# 🛠 Troubleshooting

---

## ❌ Permission Denied

### Cause

Restricted system files.

### Solution

```bash
sudo ./script.sh
```

or monitor only user-accessible files.

---

## ❌ DeepDiff Module Missing

### Solution

```bash
pip3 install --user deepdiff
```

---

## ❌ YAML Parsing Errors

Validate YAML:

```bash
python3 -c \
"import yaml; yaml.safe_load(open('file.yaml'))"
```

---

## ❌ Drift Not Detected

Verify current files were captured:

```bash
ls -lt current/
```

Run capture script again after making modifications.

---

# 📊 Architecture Flow

```text
          ┌──────────────┐
          │ Baseline     │
          │ Configs      │
          └──────┬───────┘
                 │
                 ▼
       ┌──────────────────┐
       │ Drift Scanner    │
       │ (Python Engine)  │
       └──────┬───────────┘
              │
              ▼
       ┌───────────────┐
       │ Comparison    │
       │ Engine        │
       └──────┬────────┘
              │
              ▼
     ┌──────────────────┐
     │ Drift Reports    │
     │ JSON / TXT       │
     └──────────────────┘
```

---

# 🎓 Key Takeaways

✅ Configuration drift is a major source of production incidents

✅ Baseline snapshots create auditable configuration history

✅ DeepDiff enables structured YAML comparison

✅ Automated scanning helps maintain compliance

✅ CI/CD integration enables continuous monitoring

✅ Early detection prevents outages and security risks

---

# 🚀 Next Steps

Enhance the scanner by adding:

- 📄 JSON Configuration Support
- 📄 INI File Support
- 📄 TOML File Support
- 📧 Email Notifications
- 📢 Slack Alerts
- ☁️ Cloud Configuration Monitoring
- 🔄 CI/CD Pipeline Integration
- 📈 Grafana Dashboard Reporting

---

# 🏆 Lab Completed

You have successfully built a **Configuration Drift Scanner** that:

✔ Captures baseline configurations

✔ Detects unauthorized changes

✔ Compares YAML and system configurations

✔ Generates compliance reports

✔ Supports automation for DevOps workflows

✔ Provides a foundation for enterprise configuration governance

---

<div align="center">

### 🌟 Configuration Consistency = Reliable Infrastructure 🌟

**Happy Learning & Happy Automating! 🚀**

</div>
