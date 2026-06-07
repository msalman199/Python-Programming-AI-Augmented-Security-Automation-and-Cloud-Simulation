# 🏭 Manufacturing Pack: Telemetry Collector and Downtime Alerts

<div align="center">

![Manufacturing](https://img.shields.io/badge/Domain-Manufacturing-blue?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge\&logo=python)
![InfluxDB](https://img.shields.io/badge/InfluxDB-Time--Series_DB-green?style=for-the-badge\&logo=influxdb)
![Telegraf](https://img.shields.io/badge/Telegraf-Telemetry-orange?style=for-the-badge)
![Monitoring](https://img.shields.io/badge/Monitoring-Real_Time-success?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Industrial_IoT-red?style=for-the-badge)

# 📡 Manufacturing Telemetry Collector & Downtime Alerts

### Real-Time Equipment Monitoring • Automated Downtime Detection • Production Alerting

</div>

---

# 📖 Overview

This lab demonstrates how to build a complete manufacturing telemetry and downtime monitoring platform using open-source technologies.

The solution includes:

✅ Equipment Telemetry Simulator

✅ InfluxDB Time-Series Storage

✅ Downtime Detection Engine

✅ Alert Generation System

✅ Optional HTTP Webhook Receiver

---

# 🎯 Learning Objectives

By completing this lab, you will:

* 📡 Implement telemetry collection for manufacturing equipment
* 🚨 Detect downtime using threshold monitoring
* 🔔 Generate alerts for production failures
* 🏭 Deploy an industrial monitoring architecture

---

# 📋 Prerequisites

* 🐧 Linux command-line knowledge
* ⚙️ Understanding of services and processes
* 🐍 Python programming basics
* 🌐 Networking fundamentals
* 📝 Familiarity with text editors

---

# ⚙️ Environment Setup

## Install Packages

```bash
sudo apt update

sudo apt install -y python3 python3-pip python3-venv

wget -q https://repos.influxdata.com/influxdata-archive_compat.key

echo '393e8779c89ac8d958f81f942f9ad7fb82a25e133faddaf92e15b16e6ac9ce4c influxdata-archive_compat.key' | sha256sum -c

cat influxdata-archive_compat.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg > /dev/null

echo 'deb [signed-by=/etc/apt/trusted.gpg.d/influxdata-archive_compat.gpg] https://repos.influxdata.com/debian stable main' | sudo tee /etc/apt/sources.list.d/influxdata.list

sudo apt update

sudo apt install -y influxdb

sudo apt install -y telegraf
```

## Start InfluxDB

```bash
sudo systemctl start influxdb
sudo systemctl enable influxdb
```

## Create Project

```bash
mkdir -p ~/manufacturing-monitor

cd ~/manufacturing-monitor

python3 -m venv venv

source venv/bin/activate

pip install influxdb-client requests
```

---

# 🗄️ Create Database

```bash
influx -execute 'CREATE DATABASE manufacturing'

influx -execute 'CREATE USER admin WITH PASSWORD "admin123" WITH ALL PRIVILEGES'
```

---

# 📁 Project Structure

```text
manufacturing-monitor/
├── equipment_simulator.py
├── downtime_monitor.py
├── alert_webhook.py
├── requirements.txt
└── README.md
```

---

# 📄 requirements.txt

```txt
influxdb-client
requests
```

---

# 📄 equipment_simulator.py

```python
#!/usr/bin/env python3

import time
import random
from datetime import datetime

from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS


class EquipmentSimulator:

    def __init__(self, equipment_id, equipment_type):

        self.equipment_id = equipment_id
        self.equipment_type = equipment_type

        self.client = InfluxDBClient(
            url="http://localhost:8086",
            token="-",
            org="-"
        )

        self.write_api = self.client.write_api(
            write_options=SYNCHRONOUS
        )

        self.bucket = "manufacturing"

    def generate_telemetry(self):

        status = random.choices(
            ["running", "idle", "error"],
            weights=[80, 15, 5],
            k=1
        )[0]

        telemetry = {
            "temperature": round(random.uniform(60, 95), 2),
            "pressure": round(random.uniform(20, 50), 2),
            "speed": round(random.uniform(0, 100), 2),
            "status": status
        }

        if status == "error":
            telemetry["speed"] = 0

        return telemetry

    def send_telemetry(self, telemetry_data):

        point = (
            Point("equipment_metrics")
            .tag("equipment_id", self.equipment_id)
            .tag("equipment_type", self.equipment_type)
            .field("temperature", telemetry_data["temperature"])
            .field("pressure", telemetry_data["pressure"])
            .field("speed", telemetry_data["speed"])
            .field("status", telemetry_data["status"])
        )

        self.write_api.write(
            bucket=self.bucket,
            org="-",
            record=point
        )

    def run(self, duration=300):

        start = time.time()

        while time.time() - start < duration:

            telemetry = self.generate_telemetry()

            self.send_telemetry(telemetry)

            print(
                f"[{datetime.now()}] "
                f"{self.equipment_id} -> {telemetry}"
            )

            time.sleep(5)


if __name__ == "__main__":

    simulator = EquipmentSimulator(
        "MACHINE-001",
        "CNC_MILL"
    )

    simulator.run()
```

---

# 📄 downtime_monitor.py

```python
#!/usr/bin/env python3

import time
from datetime import datetime

from influxdb_client import InfluxDBClient


class DowntimeMonitor:

    def __init__(self, check_interval=10):

        self.check_interval = check_interval

        self.alert_cooldown = {}

        self.client = InfluxDBClient(
            url="http://localhost:8086",
            token="-",
            org="-"
        )

        self.query_api = self.client.query_api()

        self.bucket = "manufacturing"

    def query_equipment_status(self, equipment_id):

        query = f'''
from(bucket:"{self.bucket}")
  |> range(start:-1m)
  |> filter(fn:(r)=>r._measurement=="equipment_metrics")
  |> filter(fn:(r)=>r.equipment_id=="{equipment_id}")
  |> filter(fn:(r)=>r._field=="status")
  |> last()
'''

        try:

            result = self.query_api.query(query)

            statuses = []

            for table in result:
                for record in table.records:
                    statuses.append(record.get_value())

            return statuses

        except Exception as e:

            print(e)

            return []

    def detect_downtime(self, equipment_id):

        statuses = self.query_equipment_status(
            equipment_id
        )

        if not statuses:
            return True, "No telemetry received"

        latest = statuses[-1]

        if latest == "error":
            return True, "Machine error detected"

        return False, "Healthy"

    def send_alert(self, equipment_id, reason):

        now = time.time()

        cooldown = 300

        last = self.alert_cooldown.get(
            equipment_id,
            0
        )

        if now - last < cooldown:
            return

        self.alert_cooldown[equipment_id] = now

        message = (
            f"{datetime.now().isoformat()},"
            f"{equipment_id},"
            f"{reason}\n"
        )

        with open(
            "/tmp/manufacturing_alerts.log",
            "a"
        ) as f:
            f.write(message)

        print("ALERT:", message)

    def monitor(self, equipment_list):

        while True:

            for equipment in equipment_list:

                down, reason = self.detect_downtime(
                    equipment
                )

                if down:
                    self.send_alert(
                        equipment,
                        reason
                    )

            time.sleep(
                self.check_interval
            )


if __name__ == "__main__":

    monitor = DowntimeMonitor(
        check_interval=10
    )

    monitor.monitor(
        [
            "MACHINE-001",
            "MACHINE-002"
        ]
    )
```

---

# 📄 alert_webhook.py

```python
#!/usr/bin/env python3

from http.server import (
    HTTPServer,
    BaseHTTPRequestHandler
)

import json


class AlertHandler(BaseHTTPRequestHandler):

    def do_POST(self):

        length = int(
            self.headers["Content-Length"]
        )

        body = self.rfile.read(length)

        try:

            data = json.loads(
                body.decode()
            )

            print("\n=== ALERT RECEIVED ===")

            print(
                json.dumps(
                    data,
                    indent=2
                )
            )

        except Exception as e:
            print(e)

        self.send_response(200)

        self.send_header(
            "Content-Type",
            "application/json"
        )

        self.end_headers()

        self.wfile.write(
            b'{"status":"received"}'
        )


if __name__ == "__main__":

    server = HTTPServer(
        ("localhost", 8080),
        AlertHandler
    )

    print(
        "Alert webhook listening on port 8080..."
    )

    server.serve_forever()
```

---

# 🚀 Running the Lab

## Terminal 1

```bash
source venv/bin/activate

python3 equipment_simulator.py
```

---

## Terminal 2

```bash
influx -database manufacturing \
-execute 'SELECT * FROM equipment_metrics ORDER BY time DESC LIMIT 10'
```

---

## Terminal 3

```bash
source venv/bin/activate

python3 downtime_monitor.py
```

---

## Terminal 4

```bash
tail -f /tmp/manufacturing_alerts.log
```

---

# 🧪 Force Downtime Test

Inside `generate_telemetry()` temporarily replace:

```python
status = "error"
```

Restart simulator.

Expected result:

```text
ALERT:
2026-01-01T10:15:00,
MACHINE-001,
Machine error detected
```

---

# ✅ Verification Checklist

```bash
sudo systemctl status influxdb
```

```bash
influx -execute 'SHOW DATABASES'
```

```bash
influx -database manufacturing \
-execute 'SELECT COUNT(*) FROM equipment_metrics'
```

```bash
tail -f /tmp/manufacturing_alerts.log
```

---

# 📊 Expected Outcomes

| Component       | Result                              |
| --------------- | ----------------------------------- |
| 📡 Simulator    | Generates telemetry every 5 seconds |
| 🗄️ InfluxDB    | Stores manufacturing metrics        |
| 🚨 Monitor      | Detects downtime automatically      |
| 🔔 Alerts       | Writes incidents to alert log       |
| 🏭 Architecture | Supports multiple machines          |

---

# 🎓 Conclusion

You have successfully built a manufacturing telemetry collection and downtime alerting system using Python, InfluxDB, and open-source monitoring tools.

## Key Skills Learned

* 📡 Telemetry Collection
* 🗄️ Time-Series Databases
* 🚨 Downtime Detection
* 🔔 Alerting Systems
* 🏭 Industrial IoT Monitoring

## 🚀 Next Steps

* 📊 Grafana Dashboards
* 🤖 Predictive Maintenance
* ☁️ Cloud Monitoring
* 🎫 Automated Ticket Creation
* 📱 Slack / Teams Notifications

---

<div align="center">

# 🏆 Lab Complete

### Monitor • Detect • Alert • Optimize

Built for Modern Manufacturing Operations 🚀

</div>
