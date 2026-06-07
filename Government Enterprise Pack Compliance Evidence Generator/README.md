# 🏛️ Government Enterprise Pack – Compliance Evidence Generator

<p align="center">

![Government](https://img.shields.io/badge/Domain-Government%20Enterprise-blue?style=for-the-badge)
![Compliance](https://img.shields.io/badge/Compliance-NIST%20800--53-green?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-yellow?style=for-the-badge&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![JSON](https://img.shields.io/badge/Reports-JSON%20HTML%20CSV-red?style=for-the-badge)
![Audit](https://img.shields.io/badge/Audit-Logging-purple?style=for-the-badge)

</p>

---

# 📖 Overview

The **Compliance Evidence Generator** automates evidence collection, report generation, and audit logging for government and regulated enterprise environments.

This project demonstrates how DevOps engineers can automate compliance workflows using:

✅ System Evidence Collection  
✅ Audit Trail Generation  
✅ Compliance Reporting  
✅ Structured Logging  
✅ NIST 800-53 Alignment  
✅ Automated Evidence Workflows

---

# 🎯 Learning Objectives

By completing this lab you will learn how to:

- Generate compliance evidence automatically
- Build auditable reporting workflows
- Collect system logs and access logs
- Create JSON, HTML, and CSV compliance reports
- Implement audit logging for evidence tracking
- Produce compliance artifacts suitable for government environments

---

# 🛠️ Environment Setup

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
sudo apt install -y jq git curl
```

## Create Project

```bash
mkdir -p ~/compliance-lab
cd ~/compliance-lab
```

## Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

## Install Python Dependencies

```bash
pip install pyyaml jinja2 python-dateutil
```

---

# 📂 Project Structure

```text
compliance-lab/
│
├── config/
│   └── compliance_config.yaml
│
├── output/
│   ├── compliance_report.json
│   ├── compliance_report.html
│   └── compliance_report.csv
│
├── logs/
│   ├── audit.log
│   └── audit.json
│
├── templates/
│
└── scripts/
    ├── evidence_collector.py
    ├── report_generator.py
    ├── audit_logger.py
    ├── compliance_workflow.py
    └── generate_sample_data.sh
```

---

# ⚙️ Configuration File

## config/compliance_config.yaml

```yaml
organization:
  name: "Federal Agency Demo"
  department: "IT Operations"
  compliance_framework: "NIST 800-53"

evidence_types:
  - system_logs
  - access_logs
  - configuration_snapshots
  - security_events

report_formats:
  - json
  - html
  - csv
```

---

# 🔍 Evidence Collection Module

## scripts/evidence_collector.py

```python
#!/usr/bin/env python3

import json
import yaml
import subprocess
from datetime import datetime
from pathlib import Path


class EvidenceCollector:

    def __init__(self, config_path):

        with open(config_path, "r") as f:
            self.config = yaml.safe_load(f)

        self.output_dir = Path("../output")
        self.output_dir.mkdir(exist_ok=True)

    def run_command(self, command):

        try:
            result = subprocess.run(
                command,
                shell=True,
                capture_output=True,
                text=True
            )

            return result.stdout

        except Exception as e:
            return str(e)

    def collect_system_logs(self):

        return {
            "timestamp": datetime.now().isoformat(),
            "evidence_type": "system_logs",
            "data": {
                "journal_logs":
                    self.run_command(
                        "journalctl -n 100 --no-pager"
                    ),

                "running_services":
                    self.run_command(
                        "systemctl list-units --type=service --state=running"
                    )
            }
        }

    def collect_access_logs(self):

        return {
            "timestamp": datetime.now().isoformat(),
            "evidence_type": "access_logs",
            "data": {
                "last_logins":
                    self.run_command("last -n 50"),

                "current_users":
                    self.run_command("who"),

                "failed_logins":
                    self.run_command("lastb -n 20")
            }
        }

    def collect_configuration_snapshot(self):

        return {
            "timestamp": datetime.now().isoformat(),
            "evidence_type": "configuration_snapshot",
            "data": {
                "network":
                    self.run_command("ip addr"),

                "firewall":
                    self.run_command("iptables -L -n"),

                "packages":
                    self.run_command("dpkg -l | head -50")
            }
        }


if __name__ == "__main__":

    collector = EvidenceCollector(
        "../config/compliance_config.yaml"
    )

    print(
        json.dumps(
            collector.collect_system_logs(),
            indent=2
        )
    )
```

---

# 📊 Report Generator

## scripts/report_generator.py

```python
#!/usr/bin/env python3

import json
import csv

from pathlib import Path
from datetime import datetime


class ComplianceReportGenerator:

    def __init__(
        self,
        evidence_data,
        output_dir="../output"
    ):

        self.evidence_data = evidence_data

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)

    def generate_json_report(
        self,
        filename="compliance_report.json"
    ):

        report = {
            "report_metadata": {
                "generated_at":
                    datetime.now().isoformat(),

                "report_type":
                    "compliance_evidence",

                "version":
                    "1.0"
            },

            "evidence_summary": {
                "total_evidence":
                    len(self.evidence_data)
            },

            "evidence_items":
                self.evidence_data
        }

        file_path = self.output_dir / filename

        with open(file_path, "w") as f:
            json.dump(report, f, indent=2)

        return str(file_path)

    def generate_html_report(
        self,
        filename="compliance_report.html"
    ):

        file_path = self.output_dir / filename

        html = f"""
        <html>
        <head>
        <title>Compliance Report</title>
        </head>
        <body>
        <h1>Compliance Evidence Report</h1>
        <p>Generated:
        {datetime.now()}</p>

        <h2>Total Evidence:
        {len(self.evidence_data)}</h2>

        </body>
        </html>
        """

        with open(file_path, "w") as f:
            f.write(html)

        return str(file_path)

    def generate_csv_report(
        self,
        filename="compliance_report.csv"
    ):

        file_path = self.output_dir / filename

        with open(
            file_path,
            "w",
            newline=""
        ) as f:

            writer = csv.writer(f)

            writer.writerow([
                "timestamp",
                "evidence_type"
            ])

            for item in self.evidence_data:

                writer.writerow([
                    item["timestamp"],
                    item["evidence_type"]
                ])

        return str(file_path)
```

---

# 📝 Audit Logger

## scripts/audit_logger.py

```python
#!/usr/bin/env python3

import json
import logging

from pathlib import Path
from datetime import datetime


class AuditLogger:

    def __init__(
        self,
        log_dir="../logs"
    ):

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        self.log_file = self.log_dir / "audit.log"

        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(message)s"
        )

    def log_evidence_collection(
        self,
        evidence_type,
        status,
        details=None
    ):

        entry = {
            "timestamp":
                datetime.now().isoformat(),

            "event_type":
                "evidence_collection",

            "evidence_type":
                evidence_type,

            "status":
                status,

            "details":
                details or {}
        }

        logging.info(
            json.dumps(entry)
        )

    def log_report_generation(
        self,
        report_type,
        output_path,
        status
    ):

        entry = {
            "timestamp":
                datetime.now().isoformat(),

            "event_type":
                "report_generation",

            "report_type":
                report_type,

            "output":
                output_path,

            "status":
                status
        }

        logging.info(
            json.dumps(entry)
        )
```

---

# 🚀 Compliance Workflow

## scripts/compliance_workflow.py

```python
#!/usr/bin/env python3

from evidence_collector import EvidenceCollector
from report_generator import ComplianceReportGenerator
from audit_logger import AuditLogger


class ComplianceWorkflow:

    def __init__(
        self,
        config_path
    ):

        self.collector = EvidenceCollector(
            config_path
        )

        self.logger = AuditLogger()

    def run_full_compliance_cycle(self):

        evidence = []

        system_logs = \
            self.collector.collect_system_logs()

        access_logs = \
            self.collector.collect_access_logs()

        config_snapshot = \
            self.collector.collect_configuration_snapshot()

        evidence.extend([
            system_logs,
            access_logs,
            config_snapshot
        ])

        for item in evidence:

            self.logger.log_evidence_collection(
                item["evidence_type"],
                "SUCCESS"
            )

        reporter = \
            ComplianceReportGenerator(
                evidence
            )

        json_report = \
            reporter.generate_json_report()

        html_report = \
            reporter.generate_html_report()

        csv_report = \
            reporter.generate_csv_report()

        self.logger.log_report_generation(
            "json",
            json_report,
            "SUCCESS"
        )

        self.logger.log_report_generation(
            "html",
            html_report,
            "SUCCESS"
        )

        self.logger.log_report_generation(
            "csv",
            csv_report,
            "SUCCESS"
        )

        return {
            "evidence_count":
                len(evidence),

            "reports": [
                json_report,
                html_report,
                csv_report
            ]
        }


def main():

    workflow = ComplianceWorkflow(
        "../config/compliance_config.yaml"
    )

    results = \
        workflow.run_full_compliance_cycle()

    print("\n========== SUMMARY ==========")

    print(
        f"Evidence Collected: "
        f"{results['evidence_count']}"
    )

    print("\nGenerated Reports:")

    for report in results["reports"]:
        print(f"  ✓ {report}")

    print("\nCompliance workflow completed!")


if __name__ == "__main__":
    main()
```

---

# 🧪 Sample Data Generator

## scripts/generate_sample_data.sh

```bash
#!/bin/bash

echo "Generating sample activity..."

logger -t compliance-test \
"Sample security event: User authentication"

logger -t compliance-test \
"Sample system event: Service started"

logger -t compliance-test \
"Sample access event: File accessed"

cat > ../output/sample_config.txt << EOF
Sample System Configuration
Generated: $(date)
Hostname: $(hostname)
Kernel: $(uname -r)
EOF

echo "Sample data generated successfully"
```

---

# ▶️ Execute the Lab

## Generate Sample Data

```bash
cd ~/compliance-lab/scripts

chmod +x generate_sample_data.sh

./generate_sample_data.sh
```

---

## Run Compliance Workflow

```bash
python3 compliance_workflow.py
```

---

# ✅ Verification

## Verify Reports

```bash
ls -lh ../output
```

Expected:

```text
compliance_report.json
compliance_report.html
compliance_report.csv
```

---

## Validate JSON Report

```bash
jq '.report_metadata' \
output/compliance_report.json
```

---

## Check Audit Logs

```bash
tail -10 logs/audit.log
```

---

## Count Evidence Records

```bash
jq '.evidence_items | length' \
output/compliance_report.json
```

---

# 🎯 Expected Outcomes

✅ System Logs Collected

✅ Access Logs Collected

✅ Configuration Snapshots Generated

✅ JSON Compliance Report

✅ HTML Compliance Report

✅ CSV Compliance Report

✅ Structured Audit Trail

✅ Automated Compliance Workflow

---

# 🏆 Skills Gained

- Compliance Automation
- NIST 800-53 Evidence Collection
- Audit Trail Generation
- DevSecOps Reporting
- Linux System Auditing
- Structured Logging
- JSON & YAML Processing
- Government Enterprise Compliance

---

# 🎉 Conclusion

You have successfully built a **Government Enterprise Compliance Evidence Generator** capable of:

✔ Collecting compliance evidence automatically

✔ Generating JSON, HTML, and CSV reports

✔ Maintaining auditable records

✔ Supporting government compliance workflows

✔ Creating reusable compliance automation pipelines

This project demonstrates real-world DevSecOps and Governance practices used across government agencies, regulated enterprises, FedRAMP environments, and NIST-aligned infrastructures.
