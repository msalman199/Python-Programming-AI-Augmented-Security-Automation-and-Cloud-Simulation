# 📊 Grafana Dashboard Evidence 

<div align="center">

# 🚀 Grafana Dashboard Evidence & Monitoring Lab

### Build Dashboards • Visualize Metrics • Capture Evidence • Monitor Infrastructure

![Grafana](https://img.shields.io/badge/Grafana-F46800?style=for-the-badge\&logo=grafana\&logoColor=white)
![Prometheus](https://img.shields.io/badge/Prometheus-E6522C?style=for-the-badge\&logo=prometheus\&logoColor=white)
![Node Exporter](https://img.shields.io/badge/Node_Exporter-000000?style=for-the-badge\&logo=prometheus\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge\&logo=linux\&logoColor=black)
![Monitoring](https://img.shields.io/badge/Monitoring-4285F4?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-326CE5?style=for-the-badge\&logo=kubernetes\&logoColor=white)

</div>

---

# 📖 Overview

Modern DevOps environments require real-time visibility into infrastructure and application performance.

In this lab, you will build a complete monitoring stack using:

* 📊 Grafana
* 🔥 Prometheus
* 🖥️ Node Exporter

You will create operational dashboards, visualize key infrastructure metrics, capture screenshots as evidence, and generate audit-ready dashboard documentation.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Install and configure Grafana

✅ Configure Prometheus as a metrics source

✅ Install Node Exporter for system metrics

✅ Build operational monitoring dashboards

✅ Visualize CPU, Memory, Disk, and Network usage

✅ Capture dashboard screenshots and evidence

✅ Export dashboard configurations

✅ Generate compliance documentation

---

# 🛠️ Prerequisites

Before starting this lab, you should have:

* 🐧 Basic Linux command-line knowledge
* 📈 Understanding of CPU, Memory, and Disk metrics
* 🌐 Familiarity with web browsers
* 🔍 Basic monitoring knowledge
* 🔐 Sudo access

---

# 🏗️ Environment Setup

## ☁️ Lab Environment

You will use the Al Nafi Linux cloud machine provided through the **Start Lab** button.

### Required Components

| Component     | Purpose            |
| ------------- | ------------------ |
| Grafana       | Visualization      |
| Prometheus    | Metrics Collection |
| Node Exporter | System Metrics     |
| Linux VM      | Monitoring Target  |

---

# 🚀 Task 1: Install Monitoring Stack

---

# 🔹 Step 1.1 Install Prometheus

## Download Prometheus

```bash
cd /tmp

wget https://github.com/prometheus/prometheus/releases/download/v2.47.0/prometheus-2.47.0.linux-amd64.tar.gz
```

## Extract Package

```bash
tar xvfz prometheus-2.47.0.linux-amd64.tar.gz
```

## Move Installation

```bash
sudo mv prometheus-2.47.0.linux-amd64 /opt/prometheus
```

---

# 🔹 Step 1.2 Configure Prometheus

Create configuration file:

```bash
sudo nano /opt/prometheus/prometheus.yml
```

Paste:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: "prometheus"
    static_configs:
      - targets:
          - localhost:9090

  - job_name: "node"
    static_configs:
      - targets:
          - localhost:9100
```

---

# 🔹 Step 1.3 Install Node Exporter

## Download

```bash
cd /tmp

wget https://github.com/prometheus/node_exporter/releases/download/v1.6.1/node_exporter-1.6.1.linux-amd64.tar.gz
```

## Extract

```bash
tar xvfz node_exporter-1.6.1.linux-amd64.tar.gz
```

## Move Files

```bash
sudo mv node_exporter-1.6.1.linux-amd64 /opt/node_exporter
```

---

# 🔹 Step 1.4 Create Systemd Services

## Node Exporter Service

```bash
sudo tee /etc/systemd/system/node_exporter.service > /dev/null <<EOF
[Unit]
Description=Node Exporter
After=network.target

[Service]
Type=simple
ExecStart=/opt/node_exporter/node_exporter
Restart=always

[Install]
WantedBy=multi-user.target
EOF
```

---

## Prometheus Service

```bash
sudo tee /etc/systemd/system/prometheus.service > /dev/null <<EOF
[Unit]
Description=Prometheus
After=network.target

[Service]
Type=simple
ExecStart=/opt/prometheus/prometheus \
--config.file=/opt/prometheus/prometheus.yml \
--storage.tsdb.path=/opt/prometheus/data

Restart=always

[Install]
WantedBy=multi-user.target
EOF
```

---

# 🔹 Step 1.5 Start Services

```bash
sudo systemctl daemon-reload

sudo systemctl start node_exporter
sudo systemctl start prometheus

sudo systemctl enable node_exporter
sudo systemctl enable prometheus
```

Verify:

```bash
sudo systemctl status node_exporter --no-pager

sudo systemctl status prometheus --no-pager
```

---

# 🔹 Step 1.6 Install Grafana

## Install Dependencies

```bash
sudo apt-get update

sudo apt-get install -y software-properties-common wget
```

## Add Repository

```bash
wget -q -O - https://packages.grafana.com/gpg.key | sudo apt-key add -
```

```bash
echo "deb https://packages.grafana.com/oss/deb stable main" | \
sudo tee /etc/apt/sources.list.d/grafana.list
```

## Install Grafana

```bash
sudo apt-get update

sudo apt-get install -y grafana
```

## Start Service

```bash
sudo systemctl start grafana-server

sudo systemctl enable grafana-server
```

---

# 🔹 Step 1.7 Verify Installation

```bash
echo "=== Service Status ==="

sudo systemctl is-active node_exporter
sudo systemctl is-active prometheus
sudo systemctl is-active grafana-server
```

Check ports:

```bash
sudo netstat -tlnp | grep -E '9090|9100|3000'
```

### Expected

✅ Grafana → Port 3000

✅ Prometheus → Port 9090

✅ Node Exporter → Port 9100

---

# 🚀 Task 2: Build Operational Dashboards

---

# 🔹 Step 2.1 Access Grafana

Open:

```text
http://localhost:3000
```

### Default Login

```text
Username: admin
Password: admin
```

Change password when prompted.

---

# 🔹 Step 2.2 Add Prometheus Data Source

Navigate:

```text
Configuration
→ Data Sources
→ Add Data Source
→ Prometheus
```

Configure:

```text
Name: Prometheus
URL: http://localhost:9090
```

Click:

```text
Save & Test
```

Expected:

```text
Data source is working
```

---

# 🔹 Step 2.3 Create System Performance Dashboard

Navigate:

```text
+ → Dashboard → Add New Panel
```

---

## 📈 Panel 1: CPU Usage

### Query

```promql
100 - (
avg by(instance)
(irate(node_cpu_seconds_total{mode="idle"}[5m]))
* 100
)
```

Settings:

```text
Title: CPU Usage (%)
Visualization: Time Series
Unit: Percent
Legend: {{instance}}
```

---

## 🧠 Panel 2: Memory Usage

### Used Memory

```promql
node_memory_MemTotal_bytes
-
node_memory_MemAvailable_bytes
```

### Total Memory

```promql
node_memory_MemTotal_bytes
```

Settings:

```text
Visualization: Time Series
Unit: Bytes (IEC)
```

---

## 💾 Panel 3: Disk Usage

### Query

```promql
100 - (
(node_filesystem_avail_bytes{fstype!="tmpfs"}
/
node_filesystem_size_bytes{fstype!="tmpfs"})
*100
)
```

Settings:

```text
Visualization: Bar Gauge
Unit: Percent
Legend: {{mountpoint}}
```

---

## 🌐 Panel 4: Network Traffic

### Receive

```promql
rate(node_network_receive_bytes_total{device!="lo"}[5m])
```

### Transmit

```promql
rate(node_network_transmit_bytes_total{device!="lo"}[5m])
```

Settings:

```text
Visualization: Time Series
Unit: Bytes/sec
```

---

# 🔹 Step 2.4 Save Dashboard

Dashboard Name:

```text
System Performance Overview
```

Arrange panels in a clean 2×2 layout.

---

# 🔹 Step 2.5 Create Monitoring Health Dashboard

Create another dashboard.

---

## 🟢 Panel 5: Target Status

### Query

```promql
up
```

Visualization:

```text
Stat
```

Mappings:

```text
0 = Down 🔴
1 = Up 🟢
```

---

## 📊 Panel 6: Prometheus Query Rate

### Query

```promql
rate(prometheus_http_requests_total[5m])
```

Visualization:

```text
Time Series
```

Unit:

```text
requests/sec
```

Save dashboard as:

```text
Monitoring Health
```

---

# 🔹 Step 2.6 Configure Dashboard Settings

Dashboard Settings:

```text
Time Range: Last 15 Minutes
Refresh: Every 30 Seconds
```

Save dashboard.

---

# 🚀 Task 3: Capture Dashboard Evidence

---

# 🔹 Step 3.1 Create Evidence Directory

```bash
mkdir -p ~/grafana-evidence

cd ~/grafana-evidence
```

---

# 🔹 Step 3.2 Generate System Load

### CPU Load

```bash
stress-ng --cpu 2 --timeout 60s &
```

### Disk Activity

```bash
dd if=/dev/zero of=/tmp/testfile bs=1M count=1024
```

### Monitor

```bash
watch -n 1 'uptime; free -h'
```

---

# 🔹 Step 3.3 Capture Screenshots

Install Firefox:

```bash
sudo apt-get install -y firefox
```

Take screenshot:

```bash
firefox --screenshot \
~/grafana-evidence/system-performance.png \
http://localhost:3000
```

Alternative:

```bash
sudo apt-get install -y scrot

sleep 5 && scrot \
~/grafana-evidence/dashboard-fullscreen.png
```

---

# 🔹 Step 3.4 Create Evidence Report

```bash
nano ~/grafana-evidence/dashboard-evidence.md
```

Document:

* Dashboard Names
* Metrics
* Screenshots
* Data Sources
* Verification Results

---

# 🔹 Step 3.5 Export Dashboard JSON

```bash
curl -u admin:admin \
http://localhost:3000/api/dashboards/uid/YOUR_DASHBOARD_UID \
> ~/grafana-evidence/system-performance-dashboard.json
```

---

# 🔹 Step 3.6 Generate Evidence Summary

```bash
cat > ~/grafana-evidence/metrics-summary.txt
```

Include:

* Timestamp
* Active Services
* Dashboard Count
* CPU Usage
* Memory Usage
* Disk Usage
* Active Targets

---

# 🔹 Step 3.7 Package Evidence

```bash
cd ~

tar -czf grafana-lab-evidence.tar.gz grafana-evidence/
```

Verify:

```bash
tar -tzf grafana-lab-evidence.tar.gz
```

---

# ✅ Verification

---

## Verify Grafana

```bash
grafana-server -v
```

```bash
sudo systemctl status grafana-server
```

Expected:

```text
active (running)
```

---

## Verify Prometheus Targets

```bash
curl -s \
http://localhost:9090/api/v1/targets \
| jq '.data.activeTargets[]'
```

Expected:

```text
health: up
```

---

## Verify Dashboards

```bash
curl -s \
-u admin:admin \
http://localhost:3000/api/search?type=dash-db
```

Expected:

```text
At least 2 dashboards
```

---

## Verify Evidence Files

```bash
ls -lh ~/grafana-evidence/
```

Expected:

✅ Screenshots

✅ JSON Exports

✅ Markdown Documentation

✅ Metrics Summary

---

# 🛠️ Troubleshooting

---

## ❌ Grafana Won't Start

Check logs:

```bash
sudo journalctl -u grafana-server -n 50
```

Verify port:

```bash
sudo netstat -tlnp | grep 3000
```

---

## ❌ No Dashboard Data

Check Prometheus:

```bash
curl http://localhost:9090/api/v1/targets
```

Check Node Exporter:

```bash
curl http://localhost:9100/metrics | head
```

---

## ❌ Cannot Connect Data Source

Verify:

```bash
curl http://localhost:9090/api/v1/query?query=up
```

Restart:

```bash
sudo systemctl restart prometheus

sudo systemctl restart grafana-server
```

---

## ❌ Screenshots Missing

Use Grafana Export:

```text
Dashboard
→ Share
→ Export
→ Save File
```

---

# 🎉 Lab Completion Summary

Congratulations!

You have successfully:

✅ Installed Grafana

✅ Installed Prometheus

✅ Installed Node Exporter

✅ Configured Metrics Collection

✅ Created Infrastructure Dashboards

✅ Visualized CPU, Memory, Disk, and Network Usage

✅ Built Monitoring Health Dashboard

✅ Captured Dashboard Evidence

✅ Exported Dashboard Configurations

✅ Generated Audit Documentation

---

# 💡 Key Takeaways

### 📊 Grafana

Transforms raw metrics into meaningful visualizations.

### 🔥 Prometheus

Collects and stores time-series metrics.

### 🖥️ Node Exporter

Provides host-level infrastructure metrics.

### 📸 Evidence Collection

Supports:

* Audits
* Compliance
* Reporting
* Operational Reviews

### 🚀 Dashboard Design

Best practices:

* Clear naming
* Consistent units
* Proper panel sizing
* Meaningful visualizations

---

# 🌟 Real-World DevOps Applications

* Production Monitoring
* Infrastructure Health Checks
* Capacity Planning
* Incident Response
* Compliance Reporting
* Executive Dashboards
* SRE Observability Platforms

---

# 📦 Evidence Package Location

```bash
~/grafana-lab-evidence.tar.gz
```

Contains:

✅ Dashboard Screenshots

✅ Dashboard JSON Exports

✅ Evidence Documentation

✅ Metrics Summaries

✅ Verification Results

---

# 🏆 Lab Completed Successfully

### Grafana Dashboard Evidence → Monitoring Visibility → Production Observability

**A critical DevOps and SRE skill for modern cloud-native infrastructure.**
