# ⚡ Energy Pack: Ingestion and Threshold Detection

<div align="center">

# ⚡ Energy Monitoring Pipeline with Threshold-Based Alerting

![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu)
![InfluxDB](https://img.shields.io/badge/InfluxDB-TimeSeries_DB-22ADF6?style=for-the-badge\&logo=influxdb)
![Telegraf](https://img.shields.io/badge/Telegraf-Metrics_Collector-green?style=for-the-badge)
![Kapacitor](https://img.shields.io/badge/Kapacitor-Alerting-red?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Monitoring-blue?style=for-the-badge)

### Real-Time Energy Monitoring • Threshold Detection • Automated Alerting

</div>

---

# 📖 Overview

This lab demonstrates how to build a complete energy monitoring and alerting pipeline using the TICK Stack:

* 📊 Telegraf for metric collection
* 🗄️ InfluxDB for time-series storage
* 🚨 Kapacitor for threshold detection and alerting

The solution simulates energy consumption data and automatically generates alerts whenever configured thresholds are exceeded.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Ingest energy consumption metrics

✅ Store metrics in InfluxDB

✅ Configure threshold-based detection rules

✅ Generate automated alerts

✅ Build a production-style monitoring pipeline

---

# 📋 Prerequisites

* 🐧 Linux Command Line
* 📈 Monitoring Concepts
* 📝 Nano/Vim Editor
* ⚙️ Configuration Management
* 🚨 Alerting Fundamentals

---

# 🏗️ Architecture

```text
Energy Simulator
        │
        ▼
     Telegraf
        │
        ▼
     InfluxDB
        │
        ▼
    Kapacitor
        │
        ▼
 Alert Generation
```

---

# ⚙️ Environment Setup

## Install InfluxDB

```bash
wget https://dl.influxdata.com/influxdb/releases/influxdb2-2.7.4-amd64.deb

sudo dpkg -i influxdb2-2.7.4-amd64.deb

sudo systemctl start influxdb

sudo systemctl enable influxdb
```

---

## Initialize InfluxDB

```bash
influx setup \
  --username admin \
  --password adminpassword123 \
  --org energyorg \
  --bucket energy_metrics \
  --retention 168h \
  --force
```

> ⚠️ Save the generated API token.

---

## Install Telegraf

```bash
wget https://dl.influxdata.com/telegraf/releases/telegraf_1.29.1-1_amd64.deb

sudo dpkg -i telegraf_1.29.1-1_amd64.deb
```

---

# 📄 /etc/telegraf/telegraf.conf

```toml
[agent]
  interval = "10s"
  round_interval = true
  metric_batch_size = 1000
  metric_buffer_limit = 10000
  collection_jitter = "0s"
  flush_interval = "10s"
  flush_jitter = "0s"

[[outputs.influxdb_v2]]
  urls = ["http://localhost:8086"]
  token = "YOUR_API_TOKEN_HERE"
  organization = "energyorg"
  bucket = "energy_metrics"

[[inputs.cpu]]
  percpu = true
  totalcpu = true
  collect_cpu_time = false
  report_active = true

[[inputs.mem]]

[[inputs.diskio]]

[[inputs.system]]

[[inputs.file]]
  files = ["/var/log/energy_data.log"]
  data_format = "influx"
  name_override = "energy_consumption"
```

---

# 📄 energy_simulator.sh

```bash
#!/bin/bash

LOG_FILE="/var/log/energy_data.log"

sudo touch $LOG_FILE
sudo chmod 666 $LOG_FILE

while true
do
    POWER_WATTS=$((50 + RANDOM % 100))

    VOLTAGE=$((110 + RANDOM % 15))

    CURRENT=$(echo "scale=2; $POWER_WATTS / $VOLTAGE" | bc)

    TIMESTAMP=$(date +%s%N)

    echo "energy_consumption,location=datacenter,rack=A1 power_watts=${POWER_WATTS}i,voltage=${VOLTAGE}i,current=${CURRENT} ${TIMESTAMP}" >> $LOG_FILE

    sleep 5
done
```

---

## Make Executable

```bash
sudo chmod +x /usr/local/bin/energy_simulator.sh

nohup sudo /usr/local/bin/energy_simulator.sh > /dev/null 2>&1 &
```

---

# 🚀 Start Telegraf

```bash
sudo systemctl start telegraf

sudo systemctl enable telegraf

sudo systemctl status telegraf
```

---

# 📥 Verify Data Ingestion

```bash
influx query '
from(bucket: "energy_metrics")
  |> range(start: -5m)
  |> filter(fn: (r) => r._measurement == "energy_consumption")
  |> limit(n: 10)
'
```

---

# 🚨 Install Kapacitor

```bash
wget https://dl.influxdata.com/kapacitor/releases/kapacitor_1.7.0_amd64.deb

sudo dpkg -i kapacitor_1.7.0_amd64.deb
```

---

# 📄 /etc/kapacitor/kapacitor.conf

```toml
[[influxdb]]
  enabled = true
  name = "energydb"
  urls = ["http://localhost:8086"]
  token = "YOUR_API_TOKEN_HERE"
  organization = "energyorg"
  default = true
```

---

# 📄 energy_threshold_alert.tick

```javascript
stream
    |from()
        .measurement('energy_consumption')
        .groupBy('location', 'rack')

    |window()
        .period(30s)
        .every(10s)

    |mean('power_watts')
        .as('avg_power')

    |alert()
        .id('energy-threshold-alert')
        .message('High energy consumption detected: {{ .Level }} - Average Power: {{ index .Fields "avg_power" }} watts in {{ index .Tags "location" }}/{{ index .Tags "rack" }}')
        .warn(lambda: "avg_power" > 100)
        .crit(lambda: "avg_power" > 120)
        .log('/var/log/kapacitor/energy_alerts.log')
```

---

# 🔧 Enable Alert Task

```bash
kapacitor define energy_alert \
  -tick ~/energy_threshold_alert.tick \
  -type stream \
  -dbrp energyorg.autogen

kapacitor enable energy_alert

kapacitor show energy_alert
```

---

# 🧪 Generate Test Alert

```bash
for i in {1..10}
do
    TIMESTAMP=$(date +%s%N)

    echo "energy_consumption,location=datacenter,rack=A1 power_watts=135i,voltage=120i,current=1.125 ${TIMESTAMP}" \
    | sudo tee -a /var/log/energy_data.log

    sleep 2
done
```

---

# 👀 Monitor Alerts

```bash
tail -f /var/log/kapacitor/energy_alerts.log
```

---

# ✅ Verification Script

```bash
#!/bin/bash

echo "=== Energy Pack Verification ==="

systemctl is-active influxdb && echo "✓ InfluxDB Running"

systemctl is-active telegraf && echo "✓ Telegraf Running"

systemctl is-active kapacitor && echo "✓ Kapacitor Running"

pgrep -f energy_simulator.sh > /dev/null \
&& echo "✓ Energy Simulator Running"

echo "Verification Complete"
```

---

# 🎯 Expected Outcomes

✅ Energy metrics continuously generated

✅ Data stored inside InfluxDB

✅ Telegraf forwarding metrics

✅ Kapacitor evaluating thresholds

✅ Alerts generated when power exceeds 100W and 120W

---

# 🚑 Troubleshooting

## Telegraf Not Collecting

```bash
telegraf --config /etc/telegraf/telegraf.conf --test
```

## Kapacitor Logs

```bash
sudo journalctl -u kapacitor -n 100
```

## Verify InfluxDB

```bash
sudo systemctl status influxdb

sudo netstat -tlnp | grep 8086
```

---

# 🎓 Conclusion

You have successfully implemented an Energy Monitoring Pipeline using:

* 📊 Telegraf
* 🗄️ InfluxDB
* 🚨 Kapacitor

This architecture is widely used in:

* Energy Monitoring Systems
* Data Centers
* Industrial IoT
* SRE Platforms
* Cloud Infrastructure Monitoring

### Key Takeaways

* Time-series databases excel at metric storage.
* Real-time stream processing enables rapid anomaly detection.
* Automated alerting improves operational reliability.
* The TICK Stack provides a powerful open-source observability solution.

🚀 Congratulations on building a production-style energy monitoring and threshold detection platform!
