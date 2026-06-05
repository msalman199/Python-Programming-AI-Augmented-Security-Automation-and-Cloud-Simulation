# 🚀 Queryable Job History API with Tests

<div align="center">

# 📊 Queryable Job History API with Tests

### Build a Production-Ready Job Audit & History Tracking Service with Flask, SQLAlchemy, SQLite, and Pytest

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge\&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web_API-black?style=for-the-badge\&logo=flask)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-red?style=for-the-badge)
![SQLite](https://img.shields.io/badge/SQLite-Database-blue?style=for-the-badge\&logo=sqlite)
![Pytest](https://img.shields.io/badge/Pytest-Testing-green?style=for-the-badge\&logo=pytest)
![REST API](https://img.shields.io/badge/REST-API-orange?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Auditability-purple?style=for-the-badge)

</div>

---

# 📖 Overview

In modern DevOps environments, maintaining a complete audit trail of automated jobs is critical for:

* 🔍 Compliance & Auditing
* 📊 Operational Visibility
* ⚡ Troubleshooting
* 📈 Performance Analysis
* 🚀 CI/CD Monitoring

This lab guides you through building a fully queryable Job History API with filtering, statistics, database persistence, and comprehensive automated testing.

---

# 🎯 Learning Objectives

After completing this lab, you will be able to:

✅ Build a REST API for job execution history

✅ Store and retrieve job execution metadata

✅ Implement advanced filtering capabilities

✅ Create job audit trails for DevOps workflows

✅ Develop automated API tests using Pytest

✅ Generate test coverage reports

✅ Query historical job execution data

---

# 📚 Prerequisites

Before starting, ensure you have:

* Basic understanding of REST APIs
* Familiarity with Flask framework
* Python programming fundamentals
* SQL database knowledge
* Experience with pytest
* Linux command-line skills

---

# 🛠 Environment Setup

## Step 1: Update System

```bash
sudo apt update
```

---

## Step 2: Install Python

```bash
sudo apt install -y python3 python3-pip python3-venv
```

---

## Step 3: Create Project Workspace

```bash
mkdir -p ~/job-history-api
cd ~/job-history-api
```

---

## Step 4: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 5: Install Dependencies

```bash
pip install flask flask-sqlalchemy pytest pytest-flask requests
```

---

# 📂 Project Structure

```text
job-history-api/
│
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   └── routes.py
│
├── tests/
│   ├── __init__.py
│   └── test_api.py
│
├── populate_data.py
├── run.py
├── requirements.txt
│
└── job_history.db
```

Create structure:

```bash
mkdir -p app tests

touch app/__init__.py
touch app/models.py
touch app/routes.py
touch app/config.py

touch tests/__init__.py
touch tests/test_api.py

touch run.py
touch requirements.txt
```

---

# 🏗 Architecture Overview

```text
          ┌─────────────────┐
          │     Client      │
          └────────┬────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │     Flask API        │
        └────────┬─────────────┘
                 │
     ┌───────────┼───────────┐
     ▼           ▼           ▼
 Create       Query       Update
 Jobs         Jobs        Jobs
     │           │           │
     └───────────┼───────────┘
                 ▼
        ┌─────────────────┐
        │ SQLite Database │
        └─────────────────┘
```

---

# 🧱 Task 1 — Configure Database Models

## 📄 app/models.py

Create JobHistory model:

```python
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class JobHistory(db.Model):
    __tablename__ = "job_history"

    id = db.Column(db.Integer, primary_key=True)
    job_name = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), nullable=False)

    start_time = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    end_time = db.Column(db.DateTime)

    duration = db.Column(db.Integer)

    user = db.Column(db.String(50))

    environment = db.Column(db.String(20))

    error_message = db.Column(db.Text)

    def to_dict(self):
        return {
            "id": self.id,
            "job_name": self.job_name,
            "status": self.status,
            "start_time": self.start_time.isoformat(),
            "end_time":
                self.end_time.isoformat()
                if self.end_time else None,
            "duration": self.duration,
            "user": self.user,
            "environment": self.environment,
            "error_message": self.error_message
        }
```

---

# ⚙ Task 2 — Configure Application Settings

## 📄 app/config.py

```python
class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///job_history.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = False


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///test_job_history.db"
    TESTING = True
```

---

# 🚀 Task 3 — Initialize Flask Application

## 📄 app/**init**.py

```python
from flask import Flask
from app.models import db
from app.config import Config

def create_app(config_class=Config):

    app = Flask(__name__)

    app.config.from_object(config_class)

    db.init_app(app)

    from app.routes import api

    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    return app
```

---

# 🌐 Task 4 — Build REST API Routes

## Endpoints

| Method | Endpoint    | Description |
| ------ | ----------- | ----------- |
| POST   | /jobs       | Create Job  |
| GET    | /jobs       | List Jobs   |
| GET    | /jobs/<id>  | Get Job     |
| PUT    | /jobs/<id>  | Update Job  |
| GET    | /jobs/stats | Statistics  |

---

## 🔍 Filtering Supported

```text
/jobs?status=success

/jobs?environment=prod

/jobs?user=admin

/jobs?job_name=backup-db

/jobs?status=success&environment=prod
```

---

# 📊 Job Statistics Endpoint

Example Response:

```json
{
  "status_counts": {
    "success": 15,
    "failed": 4,
    "running": 2
  },
  "environment_counts": {
    "dev": 8,
    "staging": 5,
    "prod": 8
  }
}
```

---

# 🧪 Task 5 — Populate Sample Data

## 📄 populate_data.py

Generate:

* 20–30 jobs
* Multiple environments
* Random users
* Various statuses
* Execution durations

Run:

```bash
python3 populate_data.py
```

Expected:

```text
Created sample job history entries
```

---

# 🧪 Task 6 — Build Automated Tests

## Testing Categories

### ✅ Create Job

```python
def test_create_job():
    pass
```

---

### ✅ Retrieve Jobs

```python
def test_get_all_jobs():
    pass
```

---

### ✅ Retrieve Job By ID

```python
def test_get_job_by_id():
    pass
```

---

### ✅ Update Job

```python
def test_update_job():
    pass
```

---

### ✅ Filter By Status

```python
def test_filter_by_status():
    pass
```

---

### ✅ Filter By Environment

```python
def test_filter_by_environment():
    pass
```

---

### ✅ Filter By User

```python
def test_filter_by_user():
    pass
```

---

### ✅ Multiple Filters

```python
def test_multiple_filters():
    pass
```

---

### ✅ Statistics Endpoint

```python
def test_get_statistics():
    pass
```

---

# ▶ Run Application

```bash
python3 run.py
```

Server:

```text
http://localhost:5000
```

---

# 🔍 Manual API Verification

## Create Job

```bash
curl -X POST http://localhost:5000/jobs \
-H "Content-Type: application/json" \
-d '{
"job_name":"test-job",
"status":"running",
"user":"testuser",
"environment":"dev"
}'
```

---

## Get All Jobs

```bash
curl http://localhost:5000/jobs
```

---

## Filter Successful Jobs

```bash
curl "http://localhost:5000/jobs?status=success"
```

---

## Filter Production Jobs

```bash
curl "http://localhost:5000/jobs?environment=prod"
```

---

## View Statistics

```bash
curl http://localhost:5000/jobs/stats
```

---

# 🧪 Run Tests

## Run All Tests

```bash
pytest tests/ -v
```

---

## Run Specific Test

```bash
pytest tests/test_api.py::test_filter_by_status -v
```

---

## Run Coverage

```bash
pip install pytest-cov

pytest tests/ \
--cov=app \
--cov-report=term-missing
```

---

# 📈 Generate HTML Coverage Report

```bash
pytest tests/ \
--cov=app \
--cov-report=html
```

Serve report:

```bash
python3 -m http.server 8080 --directory htmlcov
```

Open:

```text
http://localhost:8080
```

---

# ✅ Verification Checklist

| Check                     | Status |
| ------------------------- | ------ |
| Flask API Running         | ✅      |
| Database Created          | ✅      |
| Jobs Persisted            | ✅      |
| Filtering Works           | ✅      |
| Statistics Endpoint Works | ✅      |
| Tests Pass                | ✅      |
| Coverage > 80%            | ✅      |
| CRUD Operations Working   | ✅      |

---

# 🎯 Expected Outcomes

After completing this lab:

* ✅ RESTful Job History API
* ✅ Persistent SQLite Storage
* ✅ Queryable Audit Trails
* ✅ Filtering by User, Status & Environment
* ✅ Job Statistics Dashboard Endpoint
* ✅ Automated Testing Suite
* ✅ Coverage Reporting
* ✅ DevOps Auditability Foundation

---

# 🛠 Troubleshooting Guide

## Database Locked

```bash
rm job_history.db
python3 populate_data.py
```

---

## Import Errors

```bash
source venv/bin/activate

pip install -r requirements.txt
```

---

## Routes Returning 404

Verify:

```python
app.register_blueprint(api)
```

exists in:

```python
app/__init__.py
```

---

## Empty Filter Results

Verify:

```bash
python3 populate_data.py
```

has been executed.

---

## Coverage Too Low

Run:

```bash
pytest tests/ \
--cov=app \
--cov-report=term-missing
```

Review uncovered lines and create additional tests.

---

# 💡 DevOps Use Cases

### CI/CD Audit Logs

Track:

* Deployments
* Rollbacks
* Pipeline Runs

### Compliance Reporting

Generate:

* Historical Reports
* Change Records
* Execution Evidence

### Monitoring

Analyze:

* Failure Rates
* Runtime Trends
* Environment Health

### Incident Response

Quickly identify:

* Failed Jobs
* User Activity
* Production Events

---

# 🏆 Skills Gained

* Flask API Development
* SQLAlchemy ORM
* SQLite Database Management
* REST API Design
* API Filtering Techniques
* Automated Testing with Pytest
* Coverage Reporting
* DevOps Audit Trail Engineering

---

# 🎓 Conclusion

You have successfully built a **Queryable Job History API** capable of storing, querying, filtering, auditing, and analyzing job execution history.

This architecture forms the foundation of enterprise-grade:

* 🚀 CI/CD Monitoring Systems
* 📊 Operational Dashboards
* 🔍 Compliance Reporting Platforms
* 🛠 Job Scheduling Frameworks
* 📈 Observability Pipelines

The testing and filtering techniques learned in this lab are directly applicable to production DevOps platforms where reliability, traceability, and auditability are essential.
