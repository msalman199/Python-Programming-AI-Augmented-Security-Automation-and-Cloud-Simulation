# 🚀 Migration and Rollback Runbook 

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16+-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-Migrations-blue?style=for-the-badge&logo=postgresql)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![DevOps](https://img.shields.io/badge/DevOps-Database_Operations-blueviolet?style=for-the-badge)
![Runbook](https://img.shields.io/badge/Runbook-Production_Ready-success?style=for-the-badge)

---

# 📚 Migration and Rollback Runbook

A comprehensive hands-on DevOps lab focused on building a production-ready database migration framework with rollback procedures, validation checks, backup automation, and operational runbooks.

---

# 🎯 Learning Objectives

By completing this lab, you will:

✅ Create structured database migration procedures

✅ Develop comprehensive rollback strategies

✅ Implement validation checks for database changes

✅ Document migration workflows for production environments

✅ Practice safe database change management

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic understanding of relational databases (SQL)
- Familiarity with Linux command line
- Basic knowledge of Git
- Understanding of database schema concepts
- Experience with shell scripting basics

---

# 🏗️ Architecture Overview

```text
                ┌─────────────────────┐
                │   Migration Script  │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Migration Framework │
                └──────────┬──────────┘
                           │
      ┌────────────────────┼────────────────────┐
      ▼                    ▼                    ▼
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│ Validation  │    │ PostgreSQL  │    │ Rollback    │
│ Framework   │    │ Database    │    │ Procedures  │
└─────────────┘    └─────────────┘    └─────────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Migration History   │
                │ Tracking System     │
                └─────────────────────┘
```

---

# 🛠️ Environment Setup

## 🔹 Update System Packages

```bash
sudo apt update
```

---

## 🔹 Install Required Tools

```bash
sudo apt install -y postgresql postgresql-contrib git
```

---

## 🔹 Start PostgreSQL Service

```bash
sudo systemctl start postgresql
sudo systemctl enable postgresql
```

---

## 🔹 Create Working Directory

```bash
mkdir -p ~/migration-lab
cd ~/migration-lab
```

---

## 🔹 Initialize Git Repository

```bash
git init

git config user.name "Lab User"
git config user.email "lab@example.com"
```

---

# 🚀 Task 1: Create Migration Framework

---

## 📌 Step 1: Setup Database Environment

### Create Database

```bash
sudo -u postgres psql -c "CREATE DATABASE inventory_db;"
```

### Create User

```bash
sudo -u postgres psql -c "CREATE USER labuser WITH PASSWORD 'labpass123';"
```

### Grant Permissions

```bash
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE inventory_db TO labuser;"
```

---

### Create Configuration File

```bash
cat > db_config.sh << 'EOF'
#!/bin/bash

export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=inventory_db
export PGUSER=labuser
export PGPASSWORD=labpass123
EOF
```

Make executable:

```bash
chmod +x db_config.sh
source db_config.sh
```

---

## 📌 Step 2: Create Migration Structure

```bash
mkdir -p migrations/{up,down,validation}
mkdir -p logs
```

Result:

```text
migration-lab/
│
├── migrations/
│   ├── up/
│   ├── down/
│   └── validation/
│
└── logs/
```

---

## 📌 Step 3: Build Migration Framework

Create migration engine:

```bash
touch migrate.sh
chmod +x migrate.sh
```

### Features To Implement

✅ Database configuration loading

✅ Logging framework

✅ Migration execution

✅ Rollback execution

✅ Migration tracking

✅ Error handling

---

## 📌 Step 4: Create Migration Tracking System

### Forward Migration

File:

```text
migrations/up/000_init_tracking.sql
```

Creates:

```sql
migration_history
```

Stores:

| Column | Purpose |
|----------|---------|
| id | Unique record |
| migration_name | Migration identifier |
| executed_at | Execution timestamp |
| status | Success/Failure |
| executed_by | User |
| rollback_at | Rollback time |
| notes | Additional notes |

---

### Rollback Migration

```text
migrations/down/000_init_tracking.sql
```

Drops tracking table if rollback required.

---

## 📌 Step 5: Create Products Migration

File:

```text
migrations/up/001_create_products.sql
```

Creates:

```sql
products
```

Columns:

- id
- name
- sku
- price
- stock_quantity
- created_at
- updated_at

Indexes:

```sql
idx_products_sku
idx_products_name
```

---

### Rollback

```text
migrations/down/001_create_products.sql
```

Drops:

```sql
products
```

---

## 📌 Step 6: Create Validation Scripts

File:

```text
migrations/validation/001_validate_products.sql
```

Validation Areas:

✅ Table existence

✅ Column types

✅ Constraints

✅ Indexes

---

# 🚀 Task 2: Create Comprehensive Runbook

---

## 📌 Step 1: Build Pre-Migration Checklist

Create:

```bash
pre_migration_check.sh
```

Checks:

### 🔹 Database Connectivity

```bash
psql
```

---

### 🔹 Backup Verification

Checks backups created within 24 hours.

---

### 🔹 Disk Space Validation

Ensures sufficient free space.

---

### 🔹 Active Connections

Queries:

```sql
pg_stat_activity
```

---

### 🔹 Lock Detection

Queries:

```sql
pg_locks
```

---

# 💾 Backup Strategy

---

## 📌 Create Backup Script

File:

```bash
backup_database.sh
```

Responsibilities:

✅ Create backups

✅ Timestamp files

✅ Validate backup integrity

✅ Compress backups

---

### Example Backup

```bash
./backup_database.sh
```

Output:

```text
backups/inventory_db_20260605_120000.sql
```

---

## 📌 Create Restore Script

File:

```bash
restore_database.sh
```

Capabilities:

✅ Verify backup

✅ Disconnect active users

✅ Restore schema

✅ Restore data

✅ Validate restoration

---

# 🔄 Rollback Runbook

File:

```text
ROLLBACK_RUNBOOK.md
```

---

## Rollback Workflow

### 1️⃣ Assess Current State

```sql
SELECT * FROM migration_history;
```

---

### 2️⃣ Create Emergency Backup

```bash
./backup_database.sh
```

---

### 3️⃣ Execute Rollback

```bash
./migrate.sh down migration_name
```

---

### 4️⃣ Validate Rollback

Checks:

✅ Schema state

✅ Data integrity

✅ Application connectivity

---

### 5️⃣ Update Documentation

Record:

- Cause
- Timestamp
- Outcome
- Lessons learned

---

# 📘 Migration Execution Runbook

File:

```text
MIGRATION_RUNBOOK.md
```

---

## Pre-Migration Phase

### T-24 Hours

- Review scripts
- Test in staging
- Schedule maintenance
- Verify rollback plan

---

### T-1 Hour

Run:

```bash
./pre_migration_check.sh
```

Create backup:

```bash
./backup_database.sh
```

---

## Execution Phase

```bash
source db_config.sh
./migrate.sh up migration_name
```

Monitor:

```bash
tail -f logs/migration_*.log
```

---

## Validation Phase

Run:

```bash
psql -f migrations/validation/migration.sql
```

Verify:

```sql
SELECT * FROM migration_history;
```

---

## Monitoring Phase

Monitor:

✅ Query performance

✅ Application logs

✅ Health checks

✅ User testing

---

# 🧪 Validation Framework

Create:

```bash
validate_migration.sh
```

---

## Validation Categories

### 🔹 Schema Validation

Checks:

- Tables
- Columns
- Data types

---

### 🔹 Constraint Validation

Checks:

- Primary Keys
- Foreign Keys
- Check Constraints

---

### 🔹 Index Validation

Checks:

- Existence
- Definitions

---

### 🔹 Data Validation

Checks:

- Row counts
- Integrity
- Sample queries

---

### 🔹 Performance Validation

Checks:

- Query execution times
- Baseline comparison

---

# ✅ Verification

---

## Verify Database Connection

```bash
source db_config.sh

psql -c "SELECT version();"
```

---

## Initialize Tracking System

```bash
psql -f migrations/up/000_init_tracking.sql
```

Verify:

```bash
psql -c "SELECT * FROM migration_history;"
```

---

## Test Backup Script

```bash
./backup_database.sh
```

Verify:

```bash
ls -lh backups/
```

---

## Execute Sample Migration

```bash
psql -f migrations/up/001_create_products.sql
```

Verify:

```bash
psql -c "\d products"
```

---

## Test Rollback

```bash
psql -f migrations/down/001_create_products.sql
```

Verify:

```bash
psql -c "\d products"
```

---

# 🎯 Expected Outcomes

After completing this lab you should have:

✅ Migration directory structure

✅ Migration tracking system

✅ Backup automation

✅ Restore automation

✅ Rollback procedures

✅ Validation framework

✅ Migration runbooks

✅ Production-ready migration process

---

# 📊 Success Criteria

| Check | Status |
|---------|---------|
| PostgreSQL Running | ✅ |
| Migration Tracking Active | ✅ |
| Backup Script Functional | ✅ |
| Restore Script Functional | ✅ |
| Validation Framework Working | ✅ |
| Rollback Runbook Complete | ✅ |
| Migration Runbook Complete | ✅ |

---

# 🛠️ Troubleshooting

---

## PostgreSQL Connection Failed

Check service:

```bash
sudo systemctl status postgresql
```

Restart:

```bash
sudo systemctl restart postgresql
```

---

## Authentication Errors

Reset password:

```bash
sudo -u postgres psql

ALTER USER postgres PASSWORD 'labpassword';
```

---

## Script Permission Denied

```bash
chmod +x *.sh
```

Verify:

```bash
ls -l
```

---

## Migration Syntax Errors

Validate SQL:

```bash
psql -f migration.sql
```

Check:

- Missing semicolons
- Incorrect quotes
- Invalid SQL syntax

---

## Backup Not Created

Verify disk space:

```bash
df -h
```

Check backup folder:

```bash
ls -lh backups/
```

---

# 🎓 Conclusion

In this lab, you successfully built a complete **Database Migration and Rollback Framework** used in real-world DevOps environments.

You implemented:

- 📦 Structured migration workflows
- 🔄 Safe rollback procedures
- 📝 Migration history tracking
- 💾 Automated backup and restore processes
- 🧪 Validation frameworks
- 📘 Production-grade runbooks

These skills are fundamental for managing database changes safely in CI/CD pipelines, cloud platforms, enterprise applications, and large-scale production environments.

---

# 🌟 Key Takeaways

✅ Always backup before migrating

✅ Every migration must have a rollback plan

✅ Validate changes before and after deployment

✅ Track migration history centrally

✅ Automate repetitive database operations

✅ Documentation is as important as automation

---

**Happy Learning & Safe Database Deployments! 🚀**
