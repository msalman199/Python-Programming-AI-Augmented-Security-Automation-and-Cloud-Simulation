# 🚦 Multi-Profile Policy Gate

<p align="center">

![Policy Engine](https://img.shields.io/badge/Policy-Engine-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge\&logo=python)
![YAML](https://img.shields.io/badge/Configuration-YAML-red?style=for-the-badge)
![REST API](https://img.shields.io/badge/API-REST-green?style=for-the-badge)
![Compliance](https://img.shields.io/badge/Compliance-Multi--Profile-purple?style=for-the-badge)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge\&logo=linux)

</p>

---

# 📖 Overview

The **Multi-Profile Policy Gate** is a dynamic compliance enforcement platform that supports multiple industry profiles within a single policy engine.

The system allows runtime switching between:

🏥 Healthcare (HIPAA)

💳 Finance (PCI-DSS)

🛒 Retail (General Commerce)

without restarting services.

---

# 🎯 Learning Objectives

By completing this lab you will learn:

✅ Build a policy enforcement engine

✅ Implement multiple compliance profiles

✅ Dynamically switch active policies

✅ Create REST-based policy enforcement APIs

✅ Manage compliance requirements centrally

✅ Build reusable policy-as-code architectures

---

# 🛠 Prerequisites

* Linux CLI Basics
* YAML & JSON Knowledge
* REST API Fundamentals
* Python Programming Basics
* Text Editor (nano/vim)

---

# ⚙️ Environment Setup

## Update Packages

```bash
sudo apt update
```

## Install Python

```bash
sudo apt install -y python3 python3-pip python3-venv
```

## Install Utilities

```bash
sudo apt install -y curl jq git
```

## Create Lab Directory

```bash
mkdir -p ~/policy-gate-lab
cd ~/policy-gate-lab
```

---

# 📂 Project Structure

```text
policy-gate-lab/
│
├── config/
│   ├── active_profile.json
│   └── profiles/
│       ├── healthcare.yaml
│       ├── finance.yaml
│       └── retail.yaml
│
├── policy_gate.py
├── config_manager.py
├── api_gateway.py
├── test_client.py
│
└── verify_switching.sh
```

---

# 🏥 Healthcare Policy Profile

## config/profiles/healthcare.yaml

```yaml
profile:
  name: healthcare
  industry: HIPAA-compliant

  rules:
    - id: data_encryption
      enabled: true
      severity: critical
      requirement: "All PHI must be encrypted"

    - id: access_logging
      enabled: true
      severity: high
      requirement: "Log all data access"

    - id: data_retention
      enabled: true
      severity: medium
      max_days: 2555
```

---

# 💳 Finance Policy Profile

## config/profiles/finance.yaml

```yaml
profile:
  name: finance
  industry: PCI-DSS-compliant

  rules:
    - id: data_encryption
      enabled: true
      severity: critical
      requirement: "Encrypt cardholder data"

    - id: network_segmentation
      enabled: true
      severity: critical
      requirement: "Isolate payment networks"

    - id: access_control
      enabled: true
      severity: high
      min_password_length: 12
```

---

# 🛒 Retail Policy Profile

## config/profiles/retail.yaml

```yaml
profile:
  name: retail
  industry: general-commerce

  rules:
    - id: data_encryption
      enabled: true
      severity: medium
      requirement: "Encrypt customer PII"

    - id: rate_limiting
      enabled: true
      severity: low
      max_requests: 1000
```

---

# 🚦 Policy Engine

## policy_gate.py

```python
#!/usr/bin/env python3

import yaml
from dataclasses import dataclass
from typing import Dict, Optional, List

@dataclass
class PolicyRule:
    id: str
    enabled: bool
    severity: str
    requirement: str = ""
    metadata: Dict = None

class PolicyProfile:

    def __init__(self, profile_data):

        profile = profile_data["profile"]

        self.name = profile["name"]
        self.industry = profile["industry"]

        self.rules = {}

        for rule in profile["rules"]:
            self.rules[rule["id"]] = PolicyRule(
                id=rule["id"],
                enabled=rule["enabled"],
                severity=rule["severity"],
                requirement=rule.get("requirement", ""),
                metadata=rule
            )

    def get_rule(self, rule_id):
        return self.rules.get(rule_id)

    def get_enabled_rules(self):
        return [
            rule
            for rule in self.rules.values()
            if rule.enabled
        ]

class PolicyGate:

    def __init__(self):

        self.profiles = {}
        self.active_profile = None

    def load_profile(self, profile_path):

        with open(profile_path) as f:
            data = yaml.safe_load(f)

        profile = PolicyProfile(data)

        self.profiles[profile.name] = profile

    def switch_profile(self, profile_name):

        if profile_name not in self.profiles:
            return False

        self.active_profile = self.profiles[profile_name]

        return True

    def enforce_policy(self, request_data):

        if not self.active_profile:
            return {
                "allowed": False,
                "reason": "No active profile"
            }

        violations = []

        for rule in self.active_profile.get_enabled_rules():

            if rule.id == "data_encryption":
                if not request_data.get("encrypted", False):
                    violations.append(
                        f"{rule.id} violation"
                    )

            if rule.id == "access_logging":
                if not request_data.get(
                    "access_logged",
                    False
                ):
                    violations.append(
                        f"{rule.id} violation"
                    )

            if rule.id == "network_segmentation":
                if not request_data.get(
                    "network_segmented",
                    False
                ):
                    violations.append(
                        f"{rule.id} violation"
                    )

            if rule.id == "access_control":
                if request_data.get(
                    "password_length",
                    0
                ) < 12:
                    violations.append(
                        f"{rule.id} violation"
                    )

            if rule.id == "rate_limiting":
                if request_data.get(
                    "requests",
                    0
                ) > 1000:
                    violations.append(
                        f"{rule.id} violation"
                    )

        return {
            "allowed": len(violations) == 0,
            "violations": violations
        }

    def get_active_profile_info(self):

        if not self.active_profile:
            return {}

        return {
            "profile":
                self.active_profile.name,

            "industry":
                self.active_profile.industry,

            "rules":
                len(
                    self.active_profile.rules
                )
        }
```

---

# ⚙️ Configuration Manager

## config_manager.py

```python
#!/usr/bin/env python3

import os
import json
from datetime import datetime

class ConfigManager:

    def __init__(
        self,
        config_dir="config"
    ):

        self.config_dir = config_dir

        self.current_config_file = \
            os.path.join(
                config_dir,
                "active_profile.json"
            )

    def set_active_profile(
        self,
        profile_name
    ):

        with open(
            self.current_config_file,
            "w"
        ) as f:

            json.dump(
                {
                    "profile":
                        profile_name,

                    "timestamp":
                        datetime.now().isoformat()
                },
                f,
                indent=2
            )

    def get_active_profile(self):

        if not os.path.exists(
            self.current_config_file
        ):
            return None

        with open(
            self.current_config_file
        ) as f:

            return json.load(f)["profile"]

    def list_available_profiles(self):

        profile_dir = \
            os.path.join(
                self.config_dir,
                "profiles"
            )

        return [
            f.replace(".yaml", "")
            for f in os.listdir(profile_dir)
            if f.endswith(".yaml")
        ]
```

---

# 🌐 API Gateway

## api_gateway.py

```python
#!/usr/bin/env python3

from http.server import HTTPServer
from http.server import BaseHTTPRequestHandler

import json

class PolicyGateHandler(
    BaseHTTPRequestHandler
):

    gate = None
    config_mgr = None

    def _send_json(self, data):

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.end_headers()

        self.wfile.write(
            json.dumps(data).encode()
        )

    def do_GET(self):

        if self.path == "/status":

            self._send_json(
                self.gate.get_active_profile_info()
            )

        elif self.path == "/profiles":

            self._send_json(
                {
                    "profiles":
                    self.config_mgr
                        .list_available_profiles()
                }
            )

    def do_POST(self):

        length = int(
            self.headers[
                "Content-Length"
            ]
        )

        body = self.rfile.read(
            length
        )

        data = json.loads(body)

        if self.path == "/switch-profile":

            profile = data["profile"]

            success = \
                self.gate.switch_profile(
                    profile
                )

            if success:
                self.config_mgr.set_active_profile(
                    profile
                )

            self._send_json(
                {
                    "success": success
                }
            )

        elif self.path == "/enforce":

            result = \
                self.gate.enforce_policy(
                    data
                )

            self._send_json(result)
```

---

# 🧪 Test Client

## test_client.py

```python
#!/usr/bin/env python3

import requests

BASE_URL = "http://localhost:8080"

def switch_profile(profile):

    response = requests.post(
        f"{BASE_URL}/switch-profile",
        json={
            "profile": profile
        }
    )

    return response.json()

def enforce(data):

    response = requests.post(
        f"{BASE_URL}/enforce",
        json=data
    )

    return response.json()

print(
    switch_profile("healthcare")
)

print(
    enforce(
        {
            "encrypted": False,
            "access_logged": True
        }
    )
)
```

---

# 🔄 Verification Script

## verify_switching.sh

```bash
#!/bin/bash

echo "Testing profile switching"

for profile in healthcare finance retail
do

curl -X POST \
http://localhost:8080/switch-profile \
-H "Content-Type: application/json" \
-d "{\"profile\":\"$profile\"}"

echo ""

curl http://localhost:8080/status

echo ""
echo "--------------------"

done
```

---

# 🚀 Run the Lab

## Start API Gateway

```bash
python3 api_gateway.py
```

---

## Check Profiles

```bash
curl http://localhost:8080/profiles
```

---

## Switch Profile

```bash
curl -X POST http://localhost:8080/switch-profile \
-H "Content-Type: application/json" \
-d '{"profile":"healthcare"}'
```

---

## Verify Status

```bash
curl http://localhost:8080/status
```

---

## Test Enforcement

```bash
curl -X POST http://localhost:8080/enforce \
-H "Content-Type: application/json" \
-d '{
  "encrypted": false,
  "access_logged": true
}'
```

---

# ✅ Expected Outcomes

✔ Dynamic Profile Switching

✔ Healthcare HIPAA Enforcement

✔ Finance PCI-DSS Enforcement

✔ Retail Policy Enforcement

✔ API-based Compliance Validation

✔ Runtime Policy Changes

✔ Multi-Tenant Policy Architecture

---

# 🏆 Skills Gained

* Policy-as-Code
* Compliance Automation
* API Gateway Development
* Multi-Tenant Architecture
* Configuration Management
* YAML Processing
* Python Backend Development
* DevSecOps Governance

---

# 🎉 Conclusion

You have successfully built a **Multi-Profile Policy Gate** capable of enforcing multiple industry compliance frameworks through a single API-driven policy engine.

The solution demonstrates modern DevSecOps patterns used in:

* Healthcare Platforms (HIPAA)
* Financial Services (PCI-DSS)
* Retail Systems
* SaaS Multi-Tenant Products
* Enterprise Governance Platforms

The architecture enables dynamic policy switching, centralized enforcement, and reusable compliance automation across multiple industries.
