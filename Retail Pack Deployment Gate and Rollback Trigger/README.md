# 🛍️ Retail Pack: Deployment Gate and Rollback Trigger

<div align="center">

![Retail](https://img.shields.io/badge/Domain-Retail-blue?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=for-the-badge\&logo=docker)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_API-black?style=for-the-badge\&logo=flask)
![CI/CD](https://img.shields.io/badge/CI/CD-Deployment_Gates-success?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Automated_Rollback-red?style=for-the-badge)

# 🚀 Retail Deployment Gate & Automatic Rollback System

### Safe Deployments • Health Validation • Zero-Downtime Recovery

</div>

---

# 📖 Overview

Retail and e-commerce platforms require highly reliable deployment strategies because service interruptions directly impact revenue and customer trust.

This lab demonstrates how to build a deployment pipeline with:

✅ Health Gates

✅ Readiness Gates

✅ Automated Validation

✅ Automatic Rollback

✅ Docker-Based Deployments

---

# 🎯 Learning Objectives

By completing this lab, you will:

* 🛡️ Implement deployment gates for production systems
* ❤️ Configure automated health checks
* 🔄 Build automatic rollback mechanisms
* 🚀 Create a safe deployment pipeline

---

# 📋 Prerequisites

* 🐧 Linux command line knowledge
* 🌳 Git fundamentals
* 🐳 Docker basics
* 🐍 Python scripting
* ⚙️ CI/CD concepts

---

# 🏗️ Architecture

```text
Developer
    │
    ▼
Deployment Gate
    │
    ▼
Health Check
    │
    ▼
Readiness Check
    │
    ├── PASS ──► Production
    │
    └── FAIL ──► Rollback Trigger
                     │
                     ▼
             Previous Stable Version
```

---

# ⚙️ Environment Setup

## Install Dependencies

```bash
sudo apt update

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

sudo usermod -aG docker $USER
newgrp docker

sudo apt install -y git

sudo apt install -y python3 python3-pip

pip3 install flask requests pyyaml
```

---

# 📁 Project Structure

```text
retail-deployment-lab/
├── app/
│   ├── retail_app.py
│   ├── retail_app_faulty.py
│   └── Dockerfile
│
├── config/
│   └── deployment.yaml
│
├── deployment-scripts/
│   ├── deploy_with_gate.py
│   └── manual_rollback.py
│
└── logs/
```

---

# 📄 app/retail_app.py

```python
from flask import Flask, jsonify
import time
import os

app = Flask(__name__)

app_state = {
    "version": os.getenv("APP_VERSION", "1.0.0"),
    "start_time": time.time(),
    "healthy": True,
    "ready": True
}

@app.route("/")
def home():
    return jsonify({
        "service": "Retail Pack API",
        "version": app_state["version"],
        "status": "running"
    })

@app.route("/health")
def health():
    if not app_state["healthy"]:
        return jsonify({"status":"unhealthy"}),503

    return jsonify({
        "status":"healthy",
        "version":app_state["version"]
    }),200

@app.route("/ready")
def ready():
    uptime = time.time() - app_state["start_time"]

    if uptime < 5:
        return jsonify({
            "status":"warming_up"
        }),503

    if not app_state["ready"]:
        return jsonify({
            "status":"not ready"
        }),503

    return jsonify({
        "status":"ready",
        "uptime":uptime
    }),200

@app.route("/products")
def products():
    return jsonify({
        "products":[
            {
                "id":1,
                "name":"Laptop",
                "price":999.99
            },
            {
                "id":2,
                "name":"Mouse",
                "price":29.99
            }
        ]
    })

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000
    )
```

---

# 📄 app/Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

RUN pip install flask requests

COPY retail_app.py .

ENV APP_VERSION=1.0.0

EXPOSE 5000

CMD ["python","retail_app.py"]
```

---

# 📄 config/deployment.yaml

```yaml
deployment:
  app_name: retail-app

  port: 5000

  health_check:
    endpoint: /health
    timeout: 5
    retries: 3
    interval: 2

  readiness_check:
    endpoint: /ready
    timeout: 5
    retries: 5
    interval: 3

  rollback:
    enabled: true
    on_failure: true
    keep_previous: true
```

---

# 🚀 Deployment Flow

```text
Build Image
    │
    ▼
Start Container
    │
    ▼
Health Check
    │
    ▼
Readiness Check
    │
 ┌──┴─────┐
 │        │
PASS    FAIL
 │        │
 ▼        ▼
Deploy  Rollback
```

---

# 🧪 Verification

## Deploy Healthy Version

```bash
python3 deployment-scripts/deploy_with_gate.py 1.0.0
```

Verify:

```bash
curl http://localhost:5000/

curl http://localhost:5000/health

curl http://localhost:5000/products
```

---

## Deploy Faulty Version

```bash
python3 deployment-scripts/deploy_with_gate.py 2.0.0
```

Expected:

* ❌ Health Gate Fails
* 🔄 Rollback Triggered
* ✅ Version 1.0.0 Restored

---

# 🎓 Conclusion

You have successfully implemented a production-grade deployment gate system with automated rollback capabilities.

### Key Skills Learned

* 🛡️ Deployment Gates
* ❤️ Health Checks
* 🚀 Readiness Validation
* 🔄 Automated Rollback
* 🏪 Retail Production Safety

### Next Steps

* 📊 Monitoring Integration
* 🔵🟢 Blue-Green Deployments
* 🧪 Smoke Tests
* ☁️ CI/CD Automation
* 🚨 Alerting & Incident Management

</div>
