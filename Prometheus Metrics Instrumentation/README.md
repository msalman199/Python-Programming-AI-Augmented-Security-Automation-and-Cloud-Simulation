# 📊 Prometheus Metrics Instrumentation 

<div align="center">

# 🚀 Prometheus Observability & Monitoring

### Instrument Applications • Collect Metrics • Analyze Performance • Build Production-Grade Monitoring

![Prometheus](https://img.shields.io/badge/Prometheus-FE7A16?style=for-the-badge&logo=prometheus&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Monitoring](https://img.shields.io/badge/Monitoring-FF6B35?style=for-the-badge&logo=datadog&logoColor=white)
![DevOps](https://img.shields.io/badge/DevOps-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white)

</div>

---

# 📖 Overview

Prometheus is the industry-standard monitoring and observability platform used by DevOps, SRE, and Cloud Engineers to collect, store, query, and visualize metrics.

In this lab, you will install Prometheus, instrument a Python application with custom metrics, configure metric scraping, and use PromQL to analyze application health and performance.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Understand Prometheus metric types and formats

✅ Instrument a service to expose custom metrics

✅ Configure Prometheus scraping targets

✅ Query metrics using PromQL

✅ Monitor application health and performance

✅ Apply Prometheus metric naming best practices

✅ Generate real-time application traffic

✅ Analyze latency, throughput, and health metrics

---

# 🛠️ Prerequisites

Before starting this lab, ensure you have:

- 🐧 Basic Linux command-line knowledge
- 🌐 Familiarity with HTTP APIs
- 🐍 Basic Python programming skills
- 📈 Understanding of monitoring concepts
- 🔐 Root or sudo access

---

# 🏗️ Environment Setup

## 📦 System Requirements

| Requirement | Value |
|------------|--------|
| OS | Ubuntu 20.04+ |
| RAM | Minimum 2 GB |
| Internet | Required |
| Access | Root / Sudo |

---

# 🚀 Task 1: Install and Configure Prometheus

---

## 🔹 Step 1.1 — Download and Install Prometheus

### 👤 Create Prometheus User

```bash
sudo useradd --no-create-home --shell /bin/false prometheus
```

### 📁 Create Required Directories

```bash
sudo mkdir -p /etc/prometheus
sudo mkdir -p /var/lib/prometheus
```

### 📥 Download Prometheus

```bash
cd /tmp

wget https://github.com/prometheus/prometheus/releases/download/v2.47.0/prometheus-2.47.0.linux-amd64.tar.gz
```

### 📦 Extract Package

```bash
tar -xvf prometheus-2.47.0.linux-amd64.tar.gz

cd prometheus-2.47.0.linux-amd64
```

### 📋 Copy Binaries

```bash
sudo cp prometheus promtool /usr/local/bin/

sudo cp -r consoles console_libraries /etc/prometheus/
```

### 🔐 Set Ownership

```bash
sudo chown -R prometheus:prometheus \
/etc/prometheus \
/var/lib/prometheus

sudo chown prometheus:prometheus \
/usr/local/bin/prometheus \
/usr/local/bin/promtool
```

---

## 🔹 Step 1.2 — Configure Prometheus

### 📝 Create Configuration File

```bash
sudo nano /etc/prometheus/prometheus.yml
```

### 📄 prometheus.yml

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets:
          - localhost:9090

  - job_name: 'instrumented_app'
    static_configs:
      - targets:
          - localhost:8000
```

---

## 🔹 Step 1.3 — Create Systemd Service

### 📝 Create Service File

```bash
sudo nano /etc/systemd/system/prometheus.service
```

### 📄 prometheus.service

```ini
[Unit]
Description=Prometheus
Wants=network-online.target
After=network-online.target

[Service]
User=prometheus
Group=prometheus
Type=simple

ExecStart=/usr/local/bin/prometheus \
  --config.file=/etc/prometheus/prometheus.yml \
  --storage.tsdb.path=/var/lib/prometheus/ \
  --web.console.templates=/etc/prometheus/consoles \
  --web.console.libraries=/etc/prometheus/console_libraries

[Install]
WantedBy=multi-user.target
```

---

### ▶️ Start Prometheus

```bash
sudo systemctl daemon-reload

sudo systemctl start prometheus

sudo systemctl enable prometheus

sudo systemctl status prometheus
```

---

## 🔹 Step 1.4 — Verify Installation

### Check Metrics Endpoint

```bash
curl http://localhost:9090/metrics
```

### Display Prometheus URL

```bash
echo "Access Prometheus at: http://$(hostname -I | awk '{print $1}'):9090"
```

---

# 🚀 Task 2: Instrument a Python Application

---

## 🔹 Step 2.1 — Install Dependencies

### Install Python

```bash
sudo apt update

sudo apt install -y python3 python3-pip
```

### Install Prometheus Client

```bash
pip3 install prometheus-client flask
```

---

## 🔹 Step 2.2 — Create Application Directory

```bash
mkdir -p ~/prometheus-lab

cd ~/prometheus-lab
```

---

## 🔹 Step 2.3 — Create Instrumented Application

### 📝 Create app.py

```bash
nano app.py
```

---

### 📄 Application Code

```python
from flask import Flask, Response
from prometheus_client import Counter, Histogram, Gauge, generate_latest, REGISTRY
import time
import random

app = Flask(__name__)

# Total HTTP Requests
http_requests = Counter(
    'http_requests_total',
    'Total HTTP requests',
    ['method', 'endpoint', 'status_code']
)

# Request Duration
request_duration = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

# Active Connections
active_connections = Gauge(
    'active_connections',
    'Number of active connections'
)

# Health Score
health_score = Gauge(
    'system_health_score',
    'Current system health score'
)

@app.route('/')
def home():

    active_connections.inc()

    start_time = time.time()

    time.sleep(random.uniform(0.1, 0.5))

    duration = time.time() - start_time

    request_duration.labels(
        method='GET',
        endpoint='/'
    ).observe(duration)

    http_requests.labels(
        method='GET',
        endpoint='/',
        status_code='200'
    ).inc()

    active_connections.dec()

    return "Hello from Instrumented App!"


@app.route('/api/data')
def api_data():

    active_connections.inc()

    start_time = time.time()

    time.sleep(random.uniform(0.2, 0.8))

    duration = time.time() - start_time

    request_duration.labels(
        method='GET',
        endpoint='/api/data'
    ).observe(duration)

    http_requests.labels(
        method='GET',
        endpoint='/api/data',
        status_code='200'
    ).inc()

    active_connections.dec()

    return {
        "status": "success",
        "data": [1,2,3,4,5]
    }


@app.route('/health')
def health():

    score = random.randint(50,100)

    health_score.set(score)

    return {
        "health": "ok",
        "score": score
    }


@app.route('/metrics')
def metrics():
    return Response(
        generate_latest(REGISTRY),
        mimetype='text/plain'
    )


if __name__ == '__main__':

    health_score.set(100)

    app.run(
        host='0.0.0.0',
        port=8000
    )
```

---

## 🔹 Step 2.4 — Run Application

```bash
python3 app.py &
```

Store PID:

```bash
APP_PID=$!

echo $APP_PID
```

---

## 🔹 Step 2.5 — Generate Test Traffic

```bash
for i in {1..10}; do
    curl http://localhost:8000/
    curl http://localhost:8000/api/data
    curl http://localhost:8000/health
    sleep 1
done
```

---

### 📊 View Metrics

```bash
curl http://localhost:8000/metrics
```

---

# 🚀 Task 3: Query Metrics with PromQL

---

## 🔹 Step 3.1 — Open Prometheus UI

Open browser:

```text
http://<SERVER-IP>:9090
```

---

## 🔹 Step 3.2 — Execute PromQL Queries

---

### 📈 Total HTTP Requests

```promql
http_requests_total
```

---

### ⚡ Request Rate

```promql
rate(http_requests_total[1m])
```

---

### ⏱️ Average Request Duration

```promql
rate(http_request_duration_seconds_sum[5m])
/
rate(http_request_duration_seconds_count[5m])
```

---

### 🚀 95th Percentile Latency

```promql
histogram_quantile(
  0.95,
  rate(http_request_duration_seconds_bucket[5m])
)
```

---

### ❤️ Health Score

```promql
system_health_score
```

---

### 📊 Requests by Endpoint

```promql
sum by (endpoint)(
  rate(http_requests_total[1m])
)
```

---

# 🚀 Task 4: Create Load Generator

---

## 🔹 Create Script

```bash
nano load_generator.sh
```

---

### 📄 load_generator.sh

```bash
#!/bin/bash

ENDPOINTS=(
"/"
"/api/data"
"/health"
)

for i in {1..100}
do

  ENDPOINT=${ENDPOINTS[$RANDOM % ${#ENDPOINTS[@]}]}

  curl -s http://localhost:8000$ENDPOINT > /dev/null

  sleep 0.$((RANDOM % 5))

done

echo "Load generation complete"
```

---

### Make Executable

```bash
chmod +x load_generator.sh
```

### Run Generator

```bash
./load_generator.sh &
```

---

# 🔍 Verification

---

## ✅ Verify Prometheus Targets

```bash
curl http://localhost:9090/api/v1/targets \
| python3 -m json.tool
```

---

## ✅ Verify Scrape Status

```bash
curl -s \
'http://localhost:9090/api/v1/query?query=up' \
| python3 -m json.tool
```

---

## ✅ Verify Metrics Endpoint

```bash
curl http://localhost:8000/metrics | grep -E \
"http_requests_total|http_request_duration|active_connections|system_health_score"
```

---

## ✅ Verify Request Counter

```bash
curl -s http://localhost:8000/metrics \
| grep "http_requests_total" | head -5

sleep 5

curl http://localhost:8000/

curl -s http://localhost:8000/metrics \
| grep "http_requests_total" | head -5
```

---

# 🎯 Expected Results

You should observe:

✅ Prometheus running on port 9090

✅ Instrumented application on port 8000

✅ Metrics endpoint exposing Prometheus format

✅ Request counters increasing

✅ Histograms tracking latency

✅ Gauges reporting health status

✅ Real-time graphs in Prometheus UI

✅ Targets marked as UP

---

# 🛠️ Troubleshooting Guide

---

## ❌ Prometheus Not Starting

### Check Logs

```bash
sudo journalctl -u prometheus -n 50 --no-pager
```

### Validate Config

```bash
promtool check config \
/etc/prometheus/prometheus.yml
```

---

## ❌ Application Metrics Missing

### Verify Process

```bash
ps aux | grep python3
```

### Verify Port

```bash
sudo netstat -tlnp | grep 8000
```

### Test Endpoint

```bash
curl -v http://localhost:8000/metrics
```

---

## ❌ Metrics Not Updating

### Check Targets

```bash
curl http://localhost:9090/api/v1/targets
```

### Verify Scrape Interval

```bash
cat /etc/prometheus/prometheus.yml \
| grep scrape_interval
```

---

# 🧹 Cleanup

## Stop Application

```bash
kill $APP_PID
```

---

## Stop Load Generator

```bash
pkill -f load_generator.sh
```

---

## Stop Prometheus

```bash
sudo systemctl stop prometheus
```

---

# 🏆 Lab Completion Summary

Congratulations! 🎉

You have successfully:

✅ Installed Prometheus

✅ Configured scrape targets

✅ Instrumented a Python application

✅ Implemented Counter metrics

✅ Implemented Histogram metrics

✅ Implemented Gauge metrics

✅ Exposed Prometheus metrics endpoint

✅ Generated application traffic

✅ Queried metrics using PromQL

✅ Analyzed application performance

---

# 💡 Key Takeaways

### 🔢 Counter

Used for cumulative values:

```text
http_requests_total
```

---

### 📊 Gauge

Used for current values:

```text
active_connections
system_health_score
```

---

### 📈 Histogram

Used for latency and distribution analysis:

```text
http_request_duration_seconds
```

---

### 🏷️ Labels

Provide dimensional data:

```text
method
endpoint
status_code
```

---

### 🔍 PromQL

Powerful language for:

- Aggregation
- Filtering
- Alerting
- Forecasting
- Capacity Planning

---

# 🚀 Next Steps

- 📊 Integrate Grafana Dashboards
- 🚨 Create Alertmanager Rules
- ☁️ Monitor Kubernetes Clusters
- 📦 Instrument Microservices
- 📈 Add Business KPIs
- 🔍 Build Full Observability Stack

---

## ⭐ Lab Completed Successfully

**Prometheus Metrics Instrumentation → Production Monitoring → Observability Engineering**

🎯 *A critical DevOps and SRE skill for modern cloud-native systems.*
