
# 🤖 AI-Assisted Runbook Generator 

<div align="center">

# 🚀 AI-Powered DevOps Documentation Automation

![AI](https://img.shields.io/badge/AI-Ollama-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![DevOps](https://img.shields.io/badge/DevOps-Runbooks-green?style=for-the-badge)
![Automation](https://img.shields.io/badge/Automation-Documentation-orange?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-System_Admin-black?style=for-the-badge&logo=linux)

### Build Intelligent Operational Documentation Using Local AI Models

</div>

---

# 📖 Overview

Modern DevOps teams rely on runbooks to standardize incident response and operational procedures. Writing and maintaining these documents manually can be time-consuming and inconsistent.

In this lab, you will build an **AI-Assisted Runbook Generator** that automatically collects system information, sends structured context to a local AI model using **Ollama**, and generates professional runbooks for common operational incidents.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Automate runbook generation using AI language models

✅ Collect and structure system context programmatically

✅ Integrate local AI models through Ollama

✅ Generate standardized operational procedures

✅ Create reusable runbook templates

✅ Export documentation in Markdown and YAML formats

✅ Build foundations for AI-powered DevOps automation

---

# 📚 Prerequisites

Before starting this lab, you should have:

- Basic Linux command-line knowledge
- Understanding of system administration concepts
- Familiarity with Python programming
- Knowledge of JSON and YAML formats
- Understanding of DevOps documentation practices

---

# 🏗️ Environment Setup

## Step 1: Update System Packages

```bash
sudo apt update
```

---

## Step 2: Install Python Environment

```bash
sudo apt install -y python3 python3-pip python3-venv
```

---

## Step 3: Install System Monitoring Tools

```bash
sudo apt install -y sysstat net-tools curl jq
```

---

## Step 4: Create Project Workspace

```bash
mkdir -p ~/runbook-generator
cd ~/runbook-generator
```

---

## Step 5: Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Step 6: Install Python Dependencies

```bash
pip install ollama requests pyyaml jinja2
```

---

# 🧠 Install Ollama Local AI Model

---

## Step 1: Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## Step 2: Start Ollama Service

```bash
ollama serve &
```

---

## Step 3: Wait for Startup

```bash
sleep 5
```

---

## Step 4: Download Lightweight Model

```bash
ollama pull llama3.2:1b
```

---

## Step 5: Verify Installation

```bash
ollama list
```

Expected Output:

```text
NAME
llama3.2:1b
```

---

# 📦 Task 1: Build System Context Collector

The context collector gathers system information that will be provided to the AI model for runbook generation.

---

# 📝 Step 1.1 Create Context Collection Script

Create:

```bash
nano collect_context.py
```

---

## Core Class Structure

```python
#!/usr/bin/env python3

import subprocess
import json
import socket
from datetime import datetime

class SystemContextCollector:

    def __init__(self):
        self.context = {
            "timestamp": datetime.now().isoformat(),
            "hostname": socket.gethostname(),
            "system_info": {},
            "services": [],
            "network": {},
            "disk": {}
        }
```

---

# ⚙️ Step 1.2 Collect System Information

Implement:

```python
def collect_system_info(self):

    os_release = {}

    with open("/etc/os-release") as f:
        for line in f:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                os_release[key] = value.replace('"', '')

    kernel = subprocess.run(
        ["uname", "-r"],
        capture_output=True,
        text=True
    ).stdout.strip()

    memory = subprocess.run(
        ["free", "-h"],
        capture_output=True,
        text=True
    ).stdout

    self.context["system_info"] = {
        "os": os_release.get("PRETTY_NAME"),
        "kernel": kernel,
        "memory": memory
    }
```

---

# 🔧 Step 1.3 Collect Service Status

```python
def collect_service_status(self, services):

    for service in services:

        result = subprocess.run(
            ["systemctl", "is-active", service],
            capture_output=True,
            text=True
        )

        self.context["services"].append({
            "name": service,
            "status": result.stdout.strip()
        })
```

---

# 🌐 Step 1.4 Collect Network Information

```python
def collect_network_info(self):

    interfaces = subprocess.run(
        ["ip", "addr"],
        capture_output=True,
        text=True
    ).stdout

    ports = subprocess.run(
        ["ss", "-tulpn"],
        capture_output=True,
        text=True
    ).stdout

    self.context["network"] = {
        "interfaces": interfaces,
        "ports": ports
    }
```

---

# 💾 Step 1.5 Collect Disk Information

```python
def collect_disk_info(self):

    disk_usage = subprocess.run(
        ["df", "-h"],
        capture_output=True,
        text=True
    ).stdout

    self.context["disk"] = {
        "usage": disk_usage
    }
```

---

# 📤 Step 1.6 Export Context

```python
collector = SystemContextCollector()

collector.collect_system_info()
collector.collect_service_status([
    "ssh",
    "cron",
    "networking"
])

collector.collect_network_info()
collector.collect_disk_info()

collector.export_context()

print("Context collection complete")
```

---

# ▶️ Step 1.7 Test Collector

```bash
chmod +x collect_context.py

python3 collect_context.py
```

---

# 🔍 Verify Context Output

```bash
cat system_context.json | jq .
```

Expected Output:

```json
{
  "hostname": "server01",
  "system_info": {},
  "network": {},
  "disk": {}
}
```

---

# 🤖 Task 2: Build AI Runbook Generator

---

# 📝 Step 2.1 Create Generator Script

Create:

```bash
nano runbook_generator.py
```

---

## Initialize Generator

```python
class RunbookGenerator:

    def __init__(self):
        self.ollama_url = "http://localhost:11434"
        self.model = "llama3.2:1b"
```

---

# 🧠 Step 2.2 Create AI Prompt

```python
def create_prompt(self, context, scenario):

    prompt = f"""
You are a Senior DevOps Engineer.

System Information:
{json.dumps(context, indent=2)}

Incident Scenario:
{scenario}

Generate a professional runbook containing:

1. Investigation Steps
2. Resolution Steps
3. Verification Steps
4. Rollback Steps

Use numbered lists.
Provide Linux commands where applicable.
"""

    return prompt
```

---

# 🚀 Step 2.3 Call Ollama API

```python
def generate_with_ai(self, prompt):

    payload = {
        "model": self.model,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(
        f"{self.ollama_url}/api/generate",
        json=payload
    )

    response.raise_for_status()

    return response.json()["response"]
```

---

# 📑 Step 2.4 Format Runbook

```python
def format_runbook(self,
                   ai_output,
                   context,
                   scenario):

    return {
        "title": f"Runbook - {scenario}",
        "created": datetime.now().isoformat(),
        "scenario": scenario,
        "system": context["system_info"],
        "procedure": ai_output
    }
```

---

# 📤 Step 2.5 Export Markdown

```python
def export_runbook(self, runbook):

    filename = (
        f"runbook_"
        f"{runbook['scenario']}.md"
    )

    with open(filename, "w") as f:
        f.write(f"# {runbook['title']}\n\n")
        f.write(runbook["procedure"])

    return filename
```

---

# 📄 Step 2.6 Create Markdown Template

Create:

```bash
nano runbook_template.md
```

Template:

```markdown
# {{ title }}

**Generated:** {{ created }}

**Hostname:** {{ hostname }}

**Scenario:** {{ scenario }}

## System Information

- OS: {{ os_version }}
- Kernel: {{ kernel }}

## Procedure

{{ procedure }}

## Verification

{{ verification }}

## Rollback

{{ rollback }}

---
Auto-generated by AI Runbook Generator
```

---

# 🔄 Task 3: Create Complete Workflow

---

# 📝 Step 3.1 Create Main Workflow

Create:

```bash
nano generate_runbook.py
```

---

## Workflow Implementation

```python
from collect_context import SystemContextCollector
from runbook_generator import RunbookGenerator

collector = SystemContextCollector()

collector.collect_system_info()
collector.collect_network_info()
collector.collect_disk_info()

collector.export_context()

generator = RunbookGenerator()

context = generator.load_context(
    "system_context.json"
)

scenario = (
    "CPU usage is at 95% "
    "and application is slow"
)

prompt = generator.create_prompt(
    context,
    scenario
)

response = generator.generate_with_ai(
    prompt
)

runbook = generator.format_runbook(
    response,
    context,
    scenario
)

generator.export_runbook(runbook)

print("Runbook generated successfully")
```

---

# 🎯 Available Incident Scenarios

```python
scenarios = {
    "high_cpu":
        "CPU usage is at 95% and application is slow",

    "disk_full":
        "Root filesystem is 98% full",

    "service_down":
        "Web service is not responding"
}
```

---

# ▶️ Step 3.2 Generate Runbook

```bash
python3 generate_runbook.py
```

Expected Output:

```text
Runbook generated successfully
```

---

# ✅ Verification

---

## Verify Context Collection

```bash
python3 collect_context.py
```

Inspect:

```bash
cat system_context.json | jq .
```

---

## Verify Ollama API

```bash
curl http://localhost:11434/api/generate \
-d '{
"model":"llama3.2:1b",
"prompt":"List 3 CPU troubleshooting steps",
"stream":false
}'
```

Expected:

```json
{
  "response":"..."
}
```

---

## Verify Runbook Generation

```bash
python3 generate_runbook.py high_cpu
```

---

## Verify Files Created

```bash
ls -lh runbook_*.md
```

Expected:

```text
runbook_high_cpu.md
```

---

## Review Generated Runbook

```bash
cat runbook_high_cpu.md
```

Verify:

✅ System Context Included

✅ Numbered Investigation Steps

✅ Resolution Procedures

✅ Verification Instructions

✅ Rollback Guidance

---

# 📊 Project Structure

```text
runbook-generator/
│
├── collect_context.py
├── runbook_generator.py
├── generate_runbook.py
├── runbook_template.md
├── system_context.json
│
├── runbook_high_cpu.md
├── runbook_high_cpu.yaml
│
└── venv/
```

---

# 🛠 Troubleshooting

---

## Ollama Not Running

Check:

```bash
ps aux | grep ollama
```

Restart:

```bash
pkill ollama

ollama serve &
```

---

## Model Missing

List models:

```bash
ollama list
```

Download:

```bash
ollama pull llama3.2:1b
```

---

## Context Collection Errors

Install required packages:

```bash
sudo apt install -y sysstat procps
```

Check permissions:

```bash
ls -l /proc/cpuinfo
ls -l /etc/os-release
```

---

## Poor AI Output

Improve prompt quality:

- Add examples
- Add formatting requirements
- Add troubleshooting expectations

Or use larger model:

```bash
ollama pull llama3.2:3b
```

---

# 🎯 Expected Outcomes

After completing this lab, you will have:

✅ Automated system context collection

✅ Local AI-powered runbook generation

✅ Standardized documentation templates

✅ Markdown and YAML exports

✅ Reusable operational documentation workflows

✅ AI-assisted DevOps automation framework

---

# 🏁 Conclusion

Congratulations! 🎉

You have successfully built an **AI-Assisted Runbook Generator** capable of:

- Gathering live system information
- Understanding operational context
- Generating runbooks using local AI models
- Producing standardized operational documentation
- Reducing manual documentation effort

This approach enables DevOps teams to create consistent and scalable incident response documentation while leveraging AI safely within their own infrastructure.

---

# 🚀 Next Steps

- Integrate with Grafana alerts
- Connect to incident management systems
- Generate runbooks automatically from monitoring events
- Add support for Kubernetes clusters
- Store generated runbooks in Git repositories
- Build approval workflows for generated documentation

---

## ⏱ Estimated Completion Time

**90–120 Minutes**

---

## 📁 Lab Directory

```bash
~/runbook-generator
```

---

# 🤖 AI + DevOps + Automation = Faster Incident Response 🚀
````
