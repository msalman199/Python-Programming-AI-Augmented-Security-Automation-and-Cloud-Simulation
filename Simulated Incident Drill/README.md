# 🚨 Simulated Incident Drill 

![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?logo=linux)
![Nginx](https://img.shields.io/badge/Nginx-Web%20Server-green?logo=nginx)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue?logo=postgresql)
![Python](https://img.shields.io/badge/Python-Automation-yellow?logo=python)
![DevOps](https://img.shields.io/badge/DevOps-Incident%20Response-red)

---

# 📖 Overview

This lab provides hands-on experience with **Incident Response and Troubleshooting Workflows** by simulating common production outages. You will create incident scenarios, follow structured runbooks, document investigations, and restore services using industry-standard response procedures.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

✅ Practice structured incident response procedures

✅ Trigger and diagnose common system failures

✅ Follow runbook procedures for incident resolution

✅ Document incident response activities professionally

✅ Develop muscle memory for troubleshooting workflows

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

* Basic Linux command-line proficiency
* Understanding of system services and processes
* Familiarity with log file locations
* Basic Bash or Python scripting knowledge
* Understanding of web servers and databases

---

# 🖥️ Environment Setup

## Install Required Tools

```bash
# Update package manager
sudo apt update

# Install web server
sudo apt install -y nginx

# Install database
sudo apt install -y postgresql postgresql-contrib

# Install monitoring tools
sudo apt install -y sysstat htop

# Install Python
sudo apt install -y python3 python3-pip

# Create working directory
mkdir -p ~/incident-drill
cd ~/incident-drill
```

---

## Verify Installations

```bash
nginx -v
psql --version
python3 --version
```

Expected Output:

```text
nginx version: nginx/1.x.x
psql (PostgreSQL) xx.x
Python 3.x.x
```

---

# 🛠️ Task 1: Create Incident Scenarios and Runbooks

---

## Step 1: Configure Baseline Services

### Create Sample Web Application

```bash
sudo mkdir -p /var/www/incident-app
sudo chown $USER:$USER /var/www/incident-app
```

Create web page:

```html
<!DOCTYPE html>
<html>
<head>
<title>Incident Drill App</title>
</head>
<body>
<h1>Application Running</h1>
<p>Status: Operational</p>
</body>
</html>
```

---

### Configure Nginx

```nginx
server {
    listen 8080;
    server_name localhost;

    root /var/www/incident-app;
    index index.html;

    access_log /var/log/nginx/incident-app-access.log;
    error_log /var/log/nginx/incident-app-error.log;
}
```

Enable configuration:

```bash
sudo nginx -t
sudo systemctl restart nginx
```

---

## Step 2: Create Incident Trigger Scripts

These scripts intentionally create failure scenarios for practice.

---

### 💽 Disk Space Exhaustion

```bash
#!/bin/bash

FILL_DIR="/tmp/disk-fill-test"

mkdir -p $FILL_DIR

echo "Triggering disk space incident..."

# TODO:
# Create large files using dd
# Stop at 90% utilization or 2GB

echo "Disk space incident triggered"

df -h
```

---

### ❌ Service Failure Simulation

```bash
#!/bin/bash

echo "Triggering service crash incident..."

# TODO:
# Stop nginx
# Corrupt configuration file

echo "Service crash incident triggered"
```

---

### 🔥 CPU Spike Simulation

```bash
#!/bin/bash

echo "Triggering CPU spike incident..."

# TODO:
# Launch CPU-intensive processes
# Run 4 workers for 300 seconds

echo "CPU spike incident triggered"
```

---

# 📘 Step 3: Create Incident Runbooks

---

## General Incident Response Runbook

### Initial Assessment

```text
[ ] Verify incident

[ ] Check monitoring dashboards

[ ] Identify impacted services

[ ] Determine user impact
```

### Investigation Checklist

```text
1. Check service status

2. Review recent changes

3. Examine logs

4. Inspect system resources
```

### Resolution Verification

```text
[ ] Service responding

[ ] Metrics normal

[ ] No critical errors

[ ] Users can access application
```

---

## Disk Space Runbook

### Detection

```bash
df -h

du -sh /* 2>/dev/null | sort -hr | head -10

df -i
```

### Investigation

```bash
# TODO

du -ah /

find / -type f -size +500M

lsof | grep deleted
```

### Resolution

```bash
# TODO

sudo journalctl --vacuum-time=7d

sudo apt autoremove

sudo rm -rf /tmp/*
```

---

## Service Failure Runbook

### Detection

```bash
systemctl status nginx

sudo netstat -tlnp | grep :8080
```

### Investigation

```bash
sudo journalctl -u nginx -n 50

sudo nginx -t

df -h

free -m
```

### Resolution

```bash
sudo nginx -t

sudo systemctl restart nginx

curl -I http://localhost:8080
```

---

# 🚀 Task 2: Execute Incident Response Drill

---

## Step 1: Build Incident Documentation System

### Incident Logger Features

The Incident Logger should:

* Generate Incident IDs
* Create JSON incident files
* Record response actions
* Calculate incident duration
* Generate final reports

Example structure:

```json
{
  "incident_id": "INC-20260101-120000",
  "severity": "high",
  "status": "investigating",
  "actions": [],
  "start_time": "2026-01-01T12:00:00"
}
```

---

## Step 2: Create Drill Execution Framework

### System State Capture

Capture:

```bash
uptime

free -h

df -h

systemctl status nginx

top -bn1 | head
```

---

### Drill Workflow

```text
1. Capture baseline

2. Trigger incident

3. Detect issue

4. Follow runbook

5. Resolve incident

6. Verify restoration

7. Document findings
```

---

# 🧪 Step 3: Perform Full Incident Drill

---

## Baseline Snapshot

```bash
echo "=== Baseline Check ==="

date

df -h

systemctl status nginx

top -bn1 | head -20
```

---

## Trigger Incident

Choose one:

```bash
./trigger-disk-full.sh
```

or

```bash
./trigger-service-crash.sh
```

or

```bash
./trigger-cpu-spike.sh
```

---

## Detection Phase

Check:

```bash
top

htop

df -h

systemctl status nginx

journalctl -xe
```

---

## Investigation Phase

Collect evidence:

```bash
journalctl -u nginx

tail -f /var/log/nginx/error.log

free -h

netstat -tlnp
```

---

## Resolution Phase

Apply remediation steps from the appropriate runbook.

Verify:

```bash
curl -I http://localhost:8080

systemctl status nginx

df -h

top -bn1 | head
```

---

# 📝 Task 3: Post-Incident Analysis

---

## Incident Timeline

| Time  | Event                 |
| ----- | --------------------- |
| 10:00 | Incident triggered    |
| 10:02 | Issue detected        |
| 10:05 | Investigation started |
| 10:12 | Root cause identified |
| 10:18 | Fix applied           |
| 10:20 | Service restored      |
| 10:25 | Incident closed       |

---

## Root Cause Analysis Template

### What Happened

Describe the failure.

### Why It Happened

Identify root cause.

### Contributing Factors

* Factor 1
* Factor 2
* Factor 3

---

## Lessons Learned

```text
1. Monitoring alerts should be improved.

2. Runbooks require additional detail.

3. Recovery procedures need automation.
```

---

# ✅ Verification

---

## Verify Scripts

```bash
ls -l ~/incident-drill/*.sh
```

Expected:

```text
-rwxr-xr-x trigger-disk-full.sh
-rwxr-xr-x trigger-service-crash.sh
-rwxr-xr-x trigger-cpu-spike.sh
```

---

## Verify Services

```bash
systemctl status nginx

curl -I http://localhost:8080
```

Expected:

```text
HTTP/1.1 200 OK
```

---

## Verify Incident Logs

```bash
ls -lh ~/incident-drill/drill-*.log
```

---

## Verify Documentation

```bash
ls -l ~/incident-drill/runbook-*.md

ls -l ~/incident-drill/incident-logs/
```

---

# ✔️ Completion Checklist

* [ ] Baseline environment configured
* [ ] Incident trigger scripts created
* [ ] Runbooks documented
* [ ] Incident logger implemented
* [ ] Full incident drill executed
* [ ] Resolution completed successfully
* [ ] Incident report generated
* [ ] Lessons learned documented

---

# 🔧 Troubleshooting

---

## Permission Errors

```bash
chmod +x ~/incident-drill/*.sh

ls -l ~/incident-drill
```

---

## Nginx Not Starting

```bash
sudo nginx -t

sudo journalctl -u nginx -n 50
```

---

## Disk Completely Full

```bash
pkill -f disk-fill

sudo rm -rf /tmp/disk-fill-test
```

---

## Missing Logs

```bash
sudo journalctl -xe

sudo tail -f /var/log/nginx/error.log
```

---

# 🎓 Conclusion

Congratulations! 🎉

You have successfully completed the **Simulated Incident Drill Lab** and gained practical experience with real-world incident response workflows.

You learned how to:

* Build realistic outage scenarios
* Detect and investigate production issues
* Follow structured runbooks
* Restore services safely
* Document incidents professionally
* Perform post-incident reviews

These skills are essential for DevOps Engineers, SREs, Platform Engineers, and Cloud Operations teams responsible for maintaining reliable production systems.

---

# 📚 Key Takeaways

✅ Structured runbooks reduce response time

✅ Documentation is critical during incidents

✅ Practice builds troubleshooting confidence

✅ Post-mortems drive operational improvement

✅ Repeated drills improve team readiness

---

## 🚀 Next Steps

* Build additional incident scenarios
* Implement Prometheus alerts
* Integrate Grafana dashboards
* Practice team-based game day exercises
* Develop an internal incident response knowledge base

**Estimated Completion Time:** 90–120 Minutes ⏱️
