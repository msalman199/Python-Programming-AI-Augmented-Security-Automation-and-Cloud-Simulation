# 🚀 Job Registry with PostgreSQL

<div align="center">

# 📋 Job Metadata Persistence & Tracking System

### Build a Production-Ready Job Registry using PostgreSQL and Python

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-blue?style=for-the-badge&logo=postgresql)
![Python](https://img.shields.io/badge/Python-3.10+-yellow?style=for-the-badge&logo=python)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu)
![SQL](https://img.shields.io/badge/SQL-Database-orange?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Automation-success?style=for-the-badge)
![JSONB](https://img.shields.io/badge/PostgreSQL-JSONB-blueviolet?style=for-the-badge)

</div>

---

# 📖 Overview

In this lab, you will build a **Job Registry System** that stores and tracks job execution metadata using PostgreSQL.

The registry will support:

✅ Job Creation

✅ Status Tracking

✅ Execution Timestamps

✅ Result Storage

✅ Error Logging

✅ Historical Analysis

This architecture is commonly used in:

- CI/CD Pipelines
- Workflow Orchestration Platforms
- ETL Systems
- Data Processing Frameworks
- Automation Platforms
- DevOps Job Schedulers

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

- 🏗️ Design PostgreSQL schemas for job persistence
- 📊 Track job lifecycle states
- ⏱️ Store execution timestamps
- 📦 Save job execution results using JSONB
- ❌ Capture and analyze failures
- 🔍 Query historical job executions
- 📈 Calculate execution durations
- 🚀 Build production-ready job tracking systems

---

# 🛠️ Prerequisites

Before starting, ensure you have:

- Basic Linux command-line skills
- Understanding of SQL fundamentals
- Familiarity with Python programming
- Basic database concepts
- Understanding of job scheduling systems

---

# 🖥️ Environment Setup

---

## 🔄 Step 1: Update System Packages

```bash
sudo apt update
```

---

## 🐘 Step 2: Install PostgreSQL

```bash
sudo apt install -y postgresql postgresql-contrib
```

Verify installation:

```bash
psql --version
```

---

## 🐍 Step 3: Install Python Dependencies

```bash
sudo apt install -y python3 python3-pip
pip3 install psycopg2-binary
```

Verify:

```bash
python3 --version
pip3 list | grep psycopg2
```

---

## ▶️ Step 4: Start PostgreSQL Service

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

Verify:

```bash
sudo systemctl status postgresql
```

---

## 🔐 Step 5: Configure Database Access

Set PostgreSQL password:

```bash
sudo -u postgres psql -c "ALTER USER postgres PASSWORD 'labpassword';"
```

Create database:

```bash
sudo -u postgres psql -c "CREATE DATABASE job_registry;"
```

Verify:

```bash
sudo -u postgres psql -l
```

---

# 📚 Task 1: Design Job Registry Schema

---

## 🏗️ Step 1: Create Schema File

Create:

```bash
nano schema.sql
```

Add:

```sql
CREATE TABLE jobs (
    job_id SERIAL PRIMARY KEY,
    job_name VARCHAR(255) NOT NULL,

    status VARCHAR(20) NOT NULL
        CHECK (status IN ('pending','running','completed','failed')),

    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,

    started_at TIMESTAMP NULL,

    completed_at TIMESTAMP NULL,

    result_data JSONB NULL,

    error_message TEXT NULL
);

CREATE INDEX idx_jobs_name
ON jobs(job_name);

CREATE INDEX idx_jobs_status
ON jobs(status);

CREATE INDEX idx_jobs_created
ON jobs(created_at);
```

---

## 🚀 Step 2: Apply Schema

```bash
sudo -u postgres psql -d job_registry -f schema.sql
```

Expected:

```text
CREATE TABLE
CREATE INDEX
CREATE INDEX
CREATE INDEX
```

---

## 🔍 Step 3: Verify Schema

```bash
sudo -u postgres psql -d job_registry -c "\d jobs"
```

Expected columns:

| Column | Type |
|----------|----------|
| job_id | SERIAL |
| job_name | VARCHAR |
| status | VARCHAR |
| created_at | TIMESTAMP |
| started_at | TIMESTAMP |
| completed_at | TIMESTAMP |
| result_data | JSONB |
| error_message | TEXT |

---

# 📚 Task 2: Implement Job Registry Manager

---

## 📄 Step 1: Create Job Manager

```bash
nano job_manager.py
```

---

### 🏗️ Database Connection

```python
import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime
import json
```

---

### 🔌 Connect to PostgreSQL

```python
self.conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

self.conn.autocommit = False

self.cursor = self.conn.cursor(
    cursor_factory=RealDictCursor
)
```

---

## ➕ Create Job

```python
def create_job(self, job_name):
    query = """
    INSERT INTO jobs
    (job_name,status,created_at)
    VALUES (%s,%s,%s)
    RETURNING job_id;
    """

    self.cursor.execute(
        query,
        (
            job_name,
            "pending",
            datetime.now()
        )
    )

    job_id = self.cursor.fetchone()["job_id"]

    self.conn.commit()

    return job_id
```

---

## ▶️ Start Job

```python
def start_job(self, job_id):
    query = """
    UPDATE jobs
    SET status='running',
        started_at=%s
    WHERE job_id=%s;
    """

    self.cursor.execute(
        query,
        (datetime.now(), job_id)
    )

    self.conn.commit()

    return True
```

---

## ✅ Complete Job

```python
def complete_job(
    self,
    job_id,
    result_data
):
    query = """
    UPDATE jobs
    SET status='completed',
        completed_at=%s,
        result_data=%s
    WHERE job_id=%s;
    """

    self.cursor.execute(
        query,
        (
            datetime.now(),
            json.dumps(result_data),
            job_id
        )
    )

    self.conn.commit()

    return True
```

---

## ❌ Fail Job

```python
def fail_job(
    self,
    job_id,
    error_message
):
    query = """
    UPDATE jobs
    SET status='failed',
        completed_at=%s,
        error_message=%s
    WHERE job_id=%s;
    """

    self.cursor.execute(
        query,
        (
            datetime.now(),
            error_message,
            job_id
        )
    )

    self.conn.commit()

    return True
```

---

## 🔍 Get Job Status

```python
def get_job_status(self, job_id):

    self.cursor.execute(
        """
        SELECT *
        FROM jobs
        WHERE job_id=%s
        """,
        (job_id,)
    )

    return self.cursor.fetchone()
```

---

## 📊 Query Jobs By Status

```python
def get_jobs_by_status(self, status):

    self.cursor.execute(
        """
        SELECT *
        FROM jobs
        WHERE status=%s
        ORDER BY created_at DESC
        """,
        (status,)
    )

    return self.cursor.fetchall()
```

---

## ⏱️ Calculate Job Duration

```python
def get_job_duration(self, job_id):

    self.cursor.execute(
        """
        SELECT
        started_at,
        completed_at
        FROM jobs
        WHERE job_id=%s
        """,
        (job_id,)
    )

    job = self.cursor.fetchone()

    if (
        not job
        or not job["started_at"]
        or not job["completed_at"]
    ):
        return None

    duration = (
        job["completed_at"]
        - job["started_at"]
    )

    return duration.total_seconds()
```

---

## 🔒 Close Connection

```python
def close(self):
    self.cursor.close()
    self.conn.close()
```

---

# 🧪 Step 2: Create Test Script

```bash
nano test_job_registry.py
```

---

## 🔄 Test Complete Lifecycle

```python
job_id = manager.create_job(
    "data_processing_job"
)

manager.start_job(job_id)

time.sleep(2)

manager.complete_job(
    job_id,
    {
        "records_processed": 1500,
        "errors": 0
    }
)

status = manager.get_job_status(job_id)

print(status)

duration = manager.get_job_duration(job_id)

print(duration)
```

---

## ❌ Test Failed Job

```python
job_id = manager.create_job(
    "failing_job"
)

manager.start_job(job_id)

manager.fail_job(
    job_id,
    "Unable to connect to API"
)

print(
    manager.get_job_status(job_id)
)
```

---

## 📊 Query By Status

```python
completed_jobs = manager.get_jobs_by_status(
    "completed"
)

failed_jobs = manager.get_jobs_by_status(
    "failed"
)

print(completed_jobs)
print(failed_jobs)
```

---

# 🚀 Execute Tests

```bash
chmod +x test_job_registry.py

python3 test_job_registry.py
```

Expected:

```text
Testing Job Lifecycle...

Job Created: 1
Status: completed

Duration: 2.01 seconds

Testing Failed Job...

Status: failed

Testing Query by Status...

Completed Jobs: 1
Failed Jobs: 1
```

---

# ✅ Verification

---

## 🔍 View All Jobs

```bash
sudo -u postgres psql -d job_registry -c "
SELECT
job_id,
job_name,
status,
created_at
FROM jobs
ORDER BY job_id;"
```

---

## ⏱️ Verify Durations

```bash
sudo -u postgres psql -d job_registry -c "
SELECT
job_id,
job_name,
started_at,
completed_at,
(completed_at-started_at) AS duration
FROM jobs;"
```

---

## 📦 Verify Result Storage

```bash
sudo -u postgres psql -d job_registry -c "
SELECT
job_id,
job_name,
result_data
FROM jobs
WHERE status='completed';"
```

---

## ❌ Verify Error Storage

```bash
sudo -u postgres psql -d job_registry -c "
SELECT
job_id,
job_name,
error_message
FROM jobs
WHERE status='failed';"
```

---

# 🎯 Expected Outcomes

After completing this lab:

✅ PostgreSQL job registry deployed

✅ Job lifecycle management implemented

✅ JSONB results persisted

✅ Failure tracking enabled

✅ Historical queries operational

✅ Duration calculations available

✅ Audit trail maintained

---

# 📋 Success Checklist

- [ ] PostgreSQL Installed
- [ ] Database Created
- [ ] Jobs Table Created
- [ ] Indexes Added
- [ ] JobManager Implemented
- [ ] Jobs Can Be Created
- [ ] Jobs Can Be Started
- [ ] Jobs Can Be Completed
- [ ] Failed Jobs Logged
- [ ] JSONB Results Stored
- [ ] Durations Calculated
- [ ] Test Script Executed Successfully

---

# 🛠️ Troubleshooting

---

## ❌ Connection Refused

```bash
sudo systemctl restart postgresql

sudo systemctl status postgresql
```

---

## ❌ Authentication Failed

```bash
sudo -u postgres psql -c "
ALTER USER postgres
PASSWORD 'labpassword';
"
```

---

## ❌ psycopg2 Missing

```bash
pip3 install --user psycopg2-binary
```

---

## ❌ Permission Denied

```bash
sudo -u postgres psql -d job_registry -c "
GRANT ALL PRIVILEGES
ON ALL TABLES
IN SCHEMA public
TO postgres;
"
```

---

## 🔍 Count Existing Jobs

```bash
sudo -u postgres psql -d job_registry -c "
SELECT COUNT(*) FROM jobs;
"
```

---

# 🏆 Conclusion

You have successfully built a **PostgreSQL Job Registry System** capable of:

- 📋 Tracking job metadata
- ⏱️ Recording execution timestamps
- 📊 Measuring performance
- 📦 Storing execution results
- ❌ Capturing failures
- 🔍 Querying historical records

This architecture is widely used in:

- Jenkins Pipelines
- GitLab CI/CD
- Apache Airflow
- Prefect
- Argo Workflows
- Kubernetes Jobs
- Enterprise Automation Platforms

The concepts learned here form the foundation for building scalable workflow orchestration and production-grade DevOps automation systems.

---

<div align="center">

### 🎉 Congratulations!

You have completed the Job Registry with PostgreSQL Lab 🚀

**Happy Learning & Keep Building!**

</div>
