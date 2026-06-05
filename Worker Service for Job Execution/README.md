# 🚀 Worker Service for Job Execution

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-API-black?style=for-the-badge\&logo=flask)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge\&logo=sqlite)
![REST\_API](https://img.shields.io/badge/REST-API-green?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Automation-orange?style=for-the-badge)

---

# 📖 Overview

In this lab, you will build a **Worker Service Architecture** that processes jobs asynchronously using a REST API and SQLite database.

The worker continuously polls for pending jobs, executes them, updates status throughout the lifecycle, and stores execution results.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Implement a worker service that executes jobs asynchronously

✅ Fetch jobs from a queue and process them

✅ Update job status throughout execution lifecycle

✅ Understand worker service patterns for DevOps automation

✅ Build REST APIs for job management

✅ Store and retrieve job execution results

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

* Basic Linux command-line skills
* Familiarity with Python programming
* Knowledge of REST APIs and HTTP methods
* Understanding of background processes and services
* Basic database concepts (SQLite)

---

# 🛠️ Environment Setup

## Step 1: Update Package Repository

```bash
sudo apt update
```

---

## Step 2: Install Python

```bash
sudo apt install -y python3 python3-pip python3-venv
```

---

## Step 3: Install SQLite

```bash
sudo apt install -y sqlite3
```

---

## Step 4: Create Project Directory

```bash
mkdir -p ~/worker-service-lab
cd ~/worker-service-lab
```

---

## Step 5: Create Python Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 6: Install Required Packages

```bash
pip install flask requests
```

---

## Step 7: Verify Installation

```bash
python3 --version
sqlite3 --version
```

Expected output:

```text
Python 3.x.x
SQLite 3.x.x
```

---

# 🗄️ Task 1: Create Job Queue Database and API

---

## Step 1: Initialize SQLite Database

Create the job queue database:

```bash
sqlite3 jobs.db << 'EOF'
CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_type TEXT NOT NULL,
    payload TEXT,
    status TEXT DEFAULT 'pending',
    result TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO jobs (job_type, payload, status) VALUES
('backup', '{"path": "/var/log", "destination": "/backup"}', 'pending'),
('cleanup', '{"directory": "/tmp", "days": 7}', 'pending'),
('report', '{"type": "system", "format": "json"}', 'pending');

.quit
EOF
```

---

## Step 2: Create API Server

```bash
touch api_server.py
```

The API server provides:

* GET /jobs
* GET /jobs/<id>
* POST /jobs
* PUT /jobs/<id>/status

---

### Implement Status Update Endpoint

Features:

✔ Validate status values

✔ Update timestamps

✔ Store execution results

✔ Return updated job data

Valid statuses:

```python
['pending', 'processing', 'completed', 'failed']
```

---

### Implement Job Creation Endpoint

Responsibilities:

* Accept JSON payload
* Insert new job into database
* Return created job ID
* Set default status to pending

---

## Step 3: Start API Server

```bash
python3 api_server.py &
```

Wait for startup:

```bash
sleep 3
```

---

## Step 4: Verify API

Retrieve all jobs:

```bash
curl http://localhost:5000/jobs
```

Retrieve pending jobs:

```bash
curl http://localhost:5000/jobs?status=pending
```

---

# ⚙️ Task 2: Implement Worker Service

---

## Step 1: Create Worker Service

```bash
touch worker_service.py
```

Worker configuration:

```python
API_BASE_URL = 'http://localhost:5000'
POLL_INTERVAL = 5
```

---

# 🏗️ Worker Architecture

```text
+----------------+
| Pending Jobs   |
+--------+-------+
         |
         v
+----------------+
| Worker Service |
+--------+-------+
         |
         v
+----------------+
| Job Execution  |
+--------+-------+
         |
         v
+----------------+
| Status Update  |
+----------------+
```

---

## Step 2: Implement Core Methods

### fetch_pending_jobs()

Responsibilities:

* Call API endpoint
* Fetch pending jobs
* Handle connection errors
* Return empty list on failure

Example:

```python
requests.get(
    f"{self.api_url}/jobs?status=pending"
)
```

---

### update_job_status()

Responsibilities:

* Update processing state
* Update completed state
* Update failed state
* Store execution results

Example payload:

```json
{
  "status": "completed",
  "result": "Backup successful"
}
```

---

### execute_backup_job()

Tasks:

* Parse JSON payload
* Create backup archive
* Return execution result

Example payload:

```json
{
  "path": "/etc",
  "destination": "/tmp/backup"
}
```

Possible implementation:

```python
subprocess.run(
    ["tar", "-czf", archive_name, source]
)
```

---

### execute_cleanup_job()

Tasks:

* Parse cleanup criteria
* Scan directory
* Remove old files
* Return processed file count

Example payload:

```json
{
  "directory": "/tmp",
  "days": 30
}
```

---

### execute_report_job()

Tasks:

* Gather system information
* Generate report
* Return report data

Useful commands:

```bash
df -h
free -m
uptime
```

Python example:

```python
subprocess.check_output(["df", "-h"])
```

---

# 🔄 Job Lifecycle

```text
Pending
   |
   v
Processing
   |
   +------------+
   |            |
   v            v
Completed    Failed
```

---

## Step 3: Process Jobs

Processing workflow:

```python
1. Fetch Pending Job
2. Mark Processing
3. Execute Task
4. Save Results
5. Mark Completed
```

Error flow:

```python
1. Exception Occurs
2. Capture Error
3. Store Error Message
4. Mark Failed
```

---

## Step 4: Start Worker

```bash
python3 worker_service.py
```

Expected output:

```text
Worker service started.
Found 3 pending jobs
Processing job 1
Job 1 completed successfully
```

---

# 🧪 Create Additional Test Jobs

---

## Create Backup Job

```bash
curl -X POST http://localhost:5000/jobs \
-H "Content-Type: application/json" \
-d '{
  "job_type": "backup",
  "payload": "{\"path\":\"/etc/hostname\",\"destination\":\"/tmp/backup\"}"
}'
```

---

## Create Cleanup Job

```bash
curl -X POST http://localhost:5000/jobs \
-H "Content-Type: application/json" \
-d '{
  "job_type": "cleanup",
  "payload": "{\"directory\":\"/tmp\",\"days\":30}"
}'
```

---

## Check Job Status

```bash
curl http://localhost:5000/jobs
```

---

# ✅ Verification

---

## Verify API Functionality

List all jobs:

```bash
curl http://localhost:5000/jobs | python3 -m json.tool
```

Completed jobs:

```bash
curl http://localhost:5000/jobs?status=completed \
| python3 -m json.tool
```

Specific job:

```bash
curl http://localhost:5000/jobs/1 \
| python3 -m json.tool
```

---

## Verify Worker Processing

Inspect database:

```bash
sqlite3 jobs.db \
"SELECT id, job_type, status, result FROM jobs;"
```

Check pending jobs:

```bash
sqlite3 jobs.db \
"SELECT COUNT(*) FROM jobs WHERE status='pending';"
```

Expected:

```text
0
```

---

## Verify Backup Output

```bash
ls -la /tmp/backup/
```

---

## Verify Worker Logs

Review terminal output:

```text
Processing job 4 (backup)
Job 4 completed successfully

Processing job 5 (cleanup)
Job 5 completed successfully
```

---

# 📊 Expected Results

After successful completion:

✔ Worker continuously polls API

✔ Pending jobs are processed automatically

✔ Job statuses update correctly

✔ Results stored in SQLite

✔ Failed jobs record error details

✔ No jobs remain pending

---

# 🛠️ Troubleshooting

## API Server Not Responding

Check process:

```bash
ps aux | grep api_server
```

Check port:

```bash
netstat -tlnp | grep 5000
```

Restart server:

```bash
python3 api_server.py
```

---

## Worker Not Fetching Jobs

Verify endpoint:

```bash
curl http://localhost:5000/jobs?status=pending
```

Check configuration:

```python
API_BASE_URL = "http://localhost:5000"
```

---

## Jobs Stuck in Processing

Reset manually:

```bash
sqlite3 jobs.db \
"UPDATE jobs
 SET status='pending'
 WHERE status='processing';"
```

---

## Permission Errors

Use writable directories:

```bash
/tmp
/home/$USER
```

Avoid:

```bash
/root
/etc
/usr
```

---

# 🎯 Success Criteria

You have successfully completed the lab if:

* API endpoints function correctly
* Worker processes all pending jobs
* Job statuses update automatically
* Results are stored successfully
* Error handling works properly
* No pending jobs remain in queue

---

# 🚀 Real-World DevOps Use Cases

This architecture is commonly used for:

### CI/CD Pipelines

* Build jobs
* Deployment jobs
* Automated testing

### Infrastructure Automation

* Server backups
* Cleanup tasks
* Patch management

### Monitoring Systems

* Log processing
* Alert generation
* Report creation

### Platform Engineering

* Scheduled maintenance
* Compliance scans
* Health checks

---

# 📚 Key Takeaways

✅ Worker services enable asynchronous processing

✅ Job queues improve scalability

✅ Status tracking provides visibility

✅ REST APIs simplify orchestration

✅ Error handling improves reliability

✅ This pattern forms the foundation of modern DevOps automation systems

---

# 🧹 Cleanup Resources

Stop API server:

```bash
pkill -f api_server.py
```

Stop worker service:

```bash
Ctrl + C
```

Deactivate virtual environment:

```bash
deactivate
```

---

# 🎉 Conclusion

You have successfully built a **Worker Service for Job Execution** using:

* Python
* Flask REST API
* SQLite Database
* Background Worker Architecture

This pattern is widely used in production systems such as:

* Jenkins
* GitLab CI/CD
* Airflow
* Celery Workers
* Kubernetes Job Controllers

Mastering worker-based architectures is an essential skill for DevOps, Platform, and Cloud Engineers building scalable automation systems.
