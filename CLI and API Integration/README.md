
# 🖥️ CLI and API Integration 

<p align="center">

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![REST API](https://img.shields.io/badge/REST-API-00A8E8?style=for-the-badge)
![CLI](https://img.shields.io/badge/CLI-Command_Line-success?style=for-the-badge)
![Flask](https://img.shields.io/badge/Flask-API_Server-black?style=for-the-badge&logo=flask)
![Requests](https://img.shields.io/badge/Requests-HTTP_Client-orange?style=for-the-badge)
![DevOps](https://img.shields.io/badge/DevOps-Automation-blueviolet?style=for-the-badge)

</p>

---

# 📖 Overview

In this lab, you will build a **Command-Line Interface (CLI)** application that communicates with a REST API service.

The project demonstrates real-world DevOps practices used in:

✅ Infrastructure Automation

✅ Cloud Management Tools

✅ CI/CD Integrations

✅ Monitoring Systems

✅ Internal Engineering Platforms

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- Build a Python CLI using Click
- Connect CLI tools to REST APIs
- Implement Bearer Token Authentication
- Handle API errors gracefully
- Parse JSON responses
- Display data in formatted tables
- Store credentials securely

---

# 📋 Prerequisites

Before starting, ensure you have:

- Basic understanding of REST APIs
- Familiarity with Linux command line
- Knowledge of JSON
- Basic Python programming skills
- Understanding of authentication concepts

---

# 🛠️ Environment Setup

---

## 🔹 Step 1: Update System Packages

```bash
sudo apt update
```

---

## 🔹 Step 2: Install Python Tools

```bash
sudo apt install -y python3 python3-pip python3-venv
```

Verify installation:

```bash
python3 --version
pip3 --version
```

---

## 🔹 Step 3: Create Project Directory

```bash
mkdir -p ~/cli-api-lab

cd ~/cli-api-lab
```

---

## 🔹 Step 4: Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## 🔹 Step 5: Install Required Packages

```bash
pip install requests click tabulate
```

Verify:

```bash
pip list
```

Expected packages:

```text
requests
click
tabulate
```

---

# 🚀 Set Up Mock API Server

---

## Install Flask

```bash
pip install flask flask-httpauth
```

---

## Create API Server

```bash
touch api_server.py
```

---

## API Server Features

The mock API provides:

| Endpoint | Method | Authentication |
|-----------|----------|---------------|
| /api/health | GET | ❌ No |
| /api/users | GET | ✅ Yes |
| /api/users/<id> | GET | ✅ Yes |

---

## Authentication Token

```text
dev-token-12345
```

This token will be used throughout the lab.

---

## Start API Server

```bash
python3 api_server.py
```

Expected Output:

```text
* Running on http://127.0.0.1:5000
```

Keep this terminal running.

---

# 🚀 Task 1: Build CLI Application

---

## 🔹 Create CLI File

Open a new terminal:

```bash
cd ~/cli-api-lab

source venv/bin/activate

touch user_cli.py

chmod +x user_cli.py
```

---

# 📦 CLI Architecture

```text
CLI Application
       │
       ▼

 API Client Layer
       │
       ▼

 Authentication
       │
       ▼

 REST API Server
       │
       ▼

 JSON Response
       │
       ▼

 Formatted Output
```

---

# 🔹 Implement API Client

Create:

```python
class APIClient:
```

Responsibilities:

✅ Manage API requests

✅ Handle authentication

✅ Parse responses

✅ Handle failures

---

# 🌐 Health Check Endpoint

Endpoint:

```http
GET /api/health
```

Purpose:

Verify API availability.

Expected Response:

```json
{
  "status": "healthy",
  "service": "User API"
}
```

---

## Implement health_check()

Features:

- Send GET request
- Handle connection errors
- Parse JSON response
- Return health information

Example:

```python
response = self.session.get(
    f"{self.base_url}/health"
)
```

---

# 🔐 Authentication

API uses:

```http
Authorization: Bearer TOKEN
```

Example:

```http
Authorization: Bearer dev-token-12345
```

Added automatically:

```python
self.session.headers.update(
    {
        "Authorization":
        f"Bearer {self.token}"
    }
)
```

---

# 👥 Users Endpoint

Endpoint:

```http
GET /api/users
```

Requires:

```text
Bearer Authentication
```

Response:

```json
{
  "users": [...],
  "count": 3
}
```

---

## Implement get_users()

Responsibilities:

✅ Send authenticated request

✅ Handle 401 errors

✅ Parse user list

✅ Return results

---

# 👤 Single User Endpoint

Endpoint:

```http
GET /api/users/{id}
```

Example:

```http
GET /api/users/1
```

Response:

```json
{
  "id": 1,
  "name": "Alice Johnson",
  "role": "DevOps Engineer"
}
```

---

## Implement get_user_by_id()

Responsibilities:

✅ Request user by ID

✅ Handle 404 errors

✅ Return user information

---

# 🚀 Implement CLI Commands

---

## Health Command

```bash
python3 user_cli.py health
```

Expected Output:

```text
Status: healthy
Service: User API
```

---

## List Users Command

```bash
python3 user_cli.py list-users \
--token dev-token-12345
```

Display users using:

```python
tabulate()
```

Example Output:

```text
+----+---------------+------------------+
| ID | Name          | Role             |
+----+---------------+------------------+
| 1  | Alice Johnson | DevOps Engineer  |
| 2  | Bob Smith     | SRE              |
| 3  | Carol White   | Platform Engineer|
+----+---------------+------------------+
```

---

## Get User Command

```bash
python3 user_cli.py get-user 1 \
--token dev-token-12345
```

Expected:

```text
ID: 1
Name: Alice Johnson
Role: DevOps Engineer
```

---

# 🧪 Test Basic Functionality

---

## Health Check

```bash
python3 user_cli.py health
```

---

## List Users

```bash
python3 user_cli.py list-users \
--token dev-token-12345
```

---

## Get User

```bash
python3 user_cli.py get-user 1 \
--token dev-token-12345
```

---

## Invalid Token

```bash
python3 user_cli.py list-users \
--token invalid-token
```

Expected:

```text
Authentication Failed
```

---

## Missing User

```bash
python3 user_cli.py get-user 999 \
--token dev-token-12345
```

Expected:

```text
User not found
```

---

# 🚀 Task 2: Token Management

---

# 🔐 Secure Credential Storage

Instead of repeatedly typing tokens:

```bash
--token dev-token-12345
```

Store them securely.

---

## Token Storage Location

```text
~/.user_cli_token
```

---

# 📂 Save Token Function

Responsibilities:

✅ Create file

✅ Restrict permissions

✅ Save token securely

Permissions:

```bash
0600
```

Meaning:

```text
Owner Read/Write Only
```

---

# 📂 Load Token Function

Responsibilities:

✅ Read token file

✅ Return token

✅ Return None if missing

---

# 🗑️ Delete Token Function

Responsibilities:

✅ Remove token file

✅ Clear authentication

---

# 🚀 Authentication Commands

---

## Login

```bash
python3 user_cli.py login \
dev-token-12345
```

Actions:

✅ Validate token

✅ Save token

✅ Confirm success

---

## WhoAmI

```bash
python3 user_cli.py whoami
```

Expected:

```text
Authenticated
Token Found
```

---

## Logout

```bash
python3 user_cli.py logout
```

Expected:

```text
Authentication Removed
```

---

# 🔄 Updated Workflow

After login:

```bash
python3 user_cli.py login \
dev-token-12345
```

You can run:

```bash
python3 user_cli.py list-users
```

Without:

```bash
--token
```

---

# 🧪 Verification

---

## Test 1: API Connectivity

```bash
python3 user_cli.py health
```

Expected:

```text
Status: healthy
Service: User API
```

---

## Test 2: Login

```bash
python3 user_cli.py login \
dev-token-12345
```

Expected:

```text
Authentication Successful
```

---

## Test 3: List Users

```bash
python3 user_cli.py list-users
```

Expected:

Table of users.

---

## Test 4: Get User

```bash
python3 user_cli.py get-user 2
```

Expected:

```text
Bob Smith
SRE
```

---

## Test 5: Authentication Status

```bash
python3 user_cli.py whoami
```

Expected:

```text
Authenticated
```

---

## Test 6: Logout

```bash
python3 user_cli.py logout
```

Expected:

```text
Logged Out Successfully
```

---

# 📊 Complete Workflow

```text
Start API Server
       │
       ▼

Health Check
       │
       ▼

Login
       │
       ▼

Store Token
       │
       ▼

List Users
       │
       ▼

Get User Details
       │
       ▼

WhoAmI
       │
       ▼

Logout
```

---

# 🎯 Expected Outcomes

After completing this lab, you should have:

✅ Functional CLI Tool

✅ REST API Integration

✅ Authentication Support

✅ Secure Token Storage

✅ JSON Parsing

✅ Table Formatting

✅ Error Handling

---

# 🏆 Success Criteria

| Requirement | Status |
|------------|---------|
| API Connectivity | ✅ |
| Authentication | ✅ |
| User Listing | ✅ |
| User Lookup | ✅ |
| Token Storage | ✅ |
| Error Handling | ✅ |

---

# 📋 Verification Checklist

- [ ] Flask API running
- [ ] CLI application created
- [ ] APIClient implemented
- [ ] Health endpoint working
- [ ] Authentication working
- [ ] User listing working
- [ ] User lookup working
- [ ] Token storage implemented
- [ ] Login/logout commands working
- [ ] Error handling implemented

---

# 🛠️ Troubleshooting

---

## ❌ Connection Refused

Check server:

```bash
ps aux | grep api_server.py
```

Verify port:

```bash
netstat -tuln | grep 5000
```

Restart API:

```bash
python3 api_server.py
```

---

## ❌ Authentication Failed

Verify token:

```text
dev-token-12345
```

Check Authorization header:

```http
Bearer dev-token-12345
```

---

## ❌ Import Errors

Activate environment:

```bash
source venv/bin/activate
```

Reinstall:

```bash
pip install requests click tabulate flask flask-httpauth
```

---

## ❌ JSON Parsing Errors

Test API manually:

```bash
curl http://127.0.0.1:5000/api/health
```

Verify JSON response.

---

# 🎓 DevOps Best Practices

### ✅ Automate API Interactions

CLI tools reduce repetitive tasks.

---

### ✅ Use Token Authentication

More secure than username/password.

---

### ✅ Handle Errors Gracefully

Improve user experience.

---

### ✅ Store Credentials Securely

Use restricted file permissions.

---

### ✅ Format Output Clearly

Tables improve readability.

---

### ✅ Build Reusable Tools

CLI applications are valuable DevOps assets.

---

# 🚀 Conclusion

Congratulations! 🎉

You have successfully built a **CLI Application with API Integration**.

### Features Implemented

🔹 REST API Communication

🔹 Bearer Token Authentication

🔹 User Management Commands

🔹 Secure Token Storage

🔹 JSON Parsing

🔹 Error Handling

🔹 Formatted Table Output

### Real-World Applications

✅ Cloud Provider APIs

✅ Kubernetes Tooling

✅ CI/CD Automation

✅ Monitoring Platforms

✅ Internal Developer Platforms

✅ Infrastructure Management

### Key Takeaways

- CLI tools provide powerful automation interfaces.
- REST APIs are the backbone of modern platforms.
- Authentication is critical for security.
- Error handling improves reliability.
- Token storage must be secured properly.

These skills are essential for DevOps Engineers, Platform Engineers, SREs, and Cloud Automation Specialists.

---

# 🏆 Lab Completed Successfully

### CLI and API Integration Lab ✔️

🖥️ CLI • REST APIs • Authentication • DevOps Automation 🚀
````
