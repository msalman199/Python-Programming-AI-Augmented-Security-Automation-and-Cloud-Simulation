# 🏗️ Build and Version Artifacts

<div align="center">

![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge&logo=git)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=linux)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash)
![JSON](https://img.shields.io/badge/JSON-Metadata-black?style=for-the-badge&logo=json)
![DevOps](https://img.shields.io/badge/DevOps-Release%20Management-blue?style=for-the-badge)
![Semantic Versioning](https://img.shields.io/badge/SemVer-Versioning-success?style=for-the-badge)

# 🚀 Build and Version Artifacts 

### Version • Build • Tag • Track • Verify

Master artifact versioning, release automation, metadata generation, and build traceability for modern DevOps pipelines.

</div>

---

# 📖 Overview

In modern DevOps workflows, every software artifact must be:

✅ Versioned

✅ Traceable

✅ Reproducible

✅ Verifiable

✅ Auditable

This lab teaches how to implement semantic versioning, automate release workflows, generate metadata, create Git tags, and verify artifact integrity.

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

- 🔹 Implement Semantic Versioning (SemVer)
- 🔹 Automate version management
- 🔹 Create and manage Git release tags
- 🔹 Generate build metadata
- 🔹 Track artifact provenance
- 🔹 Verify artifact integrity using checksums
- 🔹 Build automated release workflows

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- 🐧 Basic Linux command-line knowledge
- 🌳 Understanding of Git fundamentals
- 🛠️ Familiarity with software build processes
- 📜 Basic Bash scripting knowledge
- 🔢 Understanding of Semantic Versioning

---

# 🏗️ Environment Setup

---

# 🔹 Install Required Tools

Update package manager:

```bash
sudo apt update
```

Install Git:

```bash
sudo apt install -y git
```

Install jq:

```bash
sudo apt install -y jq
```

Install Build Tools:

```bash
sudo apt install -y build-essential
```

Verify installation:

```bash
git --version
jq --version
```

Expected:

```text
git version 2.x.x
jq-1.x
```

---

# 🔹 Create Lab Workspace

```bash
mkdir -p ~/artifact-lab

cd ~/artifact-lab
```

Initialize Git repository:

```bash
git init

git config user.name "DevOps Student"

git config user.email "student@example.com"
```

---

# 📂 Project Structure

```text
artifact-lab/
│
├── src/
│   └── app.sh
│
├── builds/
│
├── metadata/
│
├── VERSION
│
├── CHANGELOG.md
│
├── version-manager.sh
│
├── build.sh
│
├── release.sh
│
├── query-artifacts.sh
│
└── verify-lab.sh
```

---

# 🧩 Task 1: Implement Semantic Versioning System

---

# 🔹 Step 1: Create Sample Application

Create source directory:

```bash
mkdir -p src
```

Create application:

```bash
nano src/app.sh
```

Paste:

```bash
#!/bin/bash

VERSION="0.0.0"

calculate() {
    echo "Calculator v${VERSION}"
    echo "Result: $(($1 + $2))"
}

calculate "$@"
```

Make executable:

```bash
chmod +x src/app.sh
```

---

## 📌 What is Semantic Versioning?

Semantic Versioning follows:

```text
MAJOR.MINOR.PATCH
```

Example:

```text
1.4.7
```

Meaning:

| Component | Purpose |
|------------|----------|
| MAJOR | Breaking changes |
| MINOR | New features |
| PATCH | Bug fixes |

Examples:

```text
0.1.0
0.1.1
0.2.0
1.0.0
```

---

# 🔹 Step 2: Create Version Management Script

Create:

```bash
nano version-manager.sh
```

Responsibilities:

✅ Initialize version

✅ Read current version

✅ Bump versions

✅ Manage changelog

---

## Version Workflow

```text
Current Version
       │
       ▼
 Version Bump
       │
       ▼
Update VERSION
       │
       ▼
Update CHANGELOG
```

---

### Supported Commands

Initialize:

```bash
./version-manager.sh init
```

Get Version:

```bash
./version-manager.sh get
```

Patch Release:

```bash
./version-manager.sh bump patch
```

Minor Release:

```bash
./version-manager.sh bump minor
```

Major Release:

```bash
./version-manager.sh bump major
```

---

# 🔹 Step 3: Initialize Versioning

Initialize version:

```bash
./version-manager.sh init
```

Expected:

```text
Version initialized to 0.1.0
```

Create initial commit:

```bash
git add .

git commit -m "Initial commit"
```

Test version bumping:

```bash
./version-manager.sh bump patch

./version-manager.sh bump minor

./version-manager.sh bump major
```

Check version:

```bash
./version-manager.sh get
```

---

# 🧩 Task 2: Tag Builds and Store Metadata

---

# 🔹 Step 1: Create Build Script

Create:

```bash
nano build.sh
```

Make executable:

```bash
chmod +x build.sh
```

---

## Build Script Responsibilities

The script will:

✅ Build artifacts

✅ Generate metadata

✅ Calculate checksums

✅ Create Git tags

✅ Record build information

---

## Artifact Naming Convention

Format:

```text
app-VERSION-BUILDNUMBER.tar.gz
```

Example:

```text
app-1.0.0-1712345678.tar.gz
```

---

## Build Metadata

Each build generates:

```json
{
  "artifact": {},
  "build": {},
  "source": {}
}
```

Contains:

- Artifact details
- Version
- Checksum
- Build timestamp
- Git commit
- Git branch

---

# 🔹 Step 2: Generate Build Metadata

Example Metadata:

```json
{
  "artifact": {
    "version": "1.0.0"
  },
  "build": {
    "number": "1712345678"
  },
  "source": {
    "commit": "abc123"
  }
}
```

---

## Why Metadata Matters

Metadata provides:

✅ Traceability

✅ Auditability

✅ Reproducibility

✅ Compliance support

---

# 🔹 Step 3: Create Git Tags

Git Tags represent releases.

Example:

```text
v1.0.0
```

Create tag:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
```

List tags:

```bash
git tag
```

Show tag details:

```bash
git show v1.0.0
```

---

# 🔹 Step 4: Build Artifact

Run build:

```bash
./build.sh
```

Expected:

```text
=== Starting Build Process ===
Version: 1.0.0
Build Number: XXXXX
```

Generated:

```text
builds/
metadata/
git tag
```

---

# 🧩 Task 3: Release Workflow Automation

---

# 🔹 Step 1: Create Release Script

Create:

```bash
nano release.sh
```

Make executable:

```bash
chmod +x release.sh
```

---

## Release Process

```text
Check Git Status
        │
        ▼
Version Bump
        │
        ▼
Update Changelog
        │
        ▼
Commit Changes
        │
        ▼
Build Artifact
        │
        ▼
Generate Metadata
        │
        ▼
Create Git Tag
```

---

# 🔹 Step 2: Execute Release

Patch release:

```bash
./release.sh patch "Bug fixes and improvements"
```

Expected:

```text
=== Release Complete ===
Version: 1.0.1
Tag: v1.0.1
```

---

# 🔹 Step 3: View Release Information

List tags:

```bash
git tag -l
```

Show tag:

```bash
git show v$(cat VERSION)
```

List builds:

```bash
ls -lh builds/
```

View metadata:

```bash
cat metadata/*.json | jq '.'
```

---

# 🧩 Task 4: Artifact Query Tool

---

# 🔹 Create Query Script

Create:

```bash
nano query-artifacts.sh
```

Make executable:

```bash
chmod +x query-artifacts.sh
```

---

## Features

### List Artifacts

```bash
./query-artifacts.sh list
```

Output:

```text
Version: 1.0.1
Artifact: app-1.0.1-123456.tar.gz
```

---

### Show Artifact Details

```bash
./query-artifacts.sh info 1.0.1
```

Displays:

- Version
- Checksum
- Build Date
- Git Commit
- Source Branch

---

### Verify Integrity

```bash
./query-artifacts.sh verify builds/app-1.0.1.tar.gz
```

Expected:

```text
Verification PASSED
```

---

# 🔍 Verification

---

# 🔹 Verify Semantic Versioning

Check VERSION:

```bash
cat VERSION
```

Validate:

```bash
grep -E '^[0-9]+\.[0-9]+\.[0-9]+$' VERSION
```

Expected:

```text
1.0.1
```

---

# 🔹 Verify Build Artifacts

List builds:

```bash
ls -lh builds/
```

Check naming convention:

```bash
ls builds/ | grep -E 'app-[0-9]+\.[0-9]+\.[0-9]+-[0-9]+\.tar\.gz'
```

Expected:

```text
Artifact naming correct
```

---

# 🔹 Verify Metadata

List metadata:

```bash
ls -lh metadata/
```

Validate JSON:

```bash
jq empty metadata/*.json
```

Verify fields:

```bash
jq '.artifact.version' metadata/*.json
```

---

# 🔹 Verify Git Tags

List tags:

```bash
git tag
```

Expected:

```text
v1.0.0
v1.0.1
```

Validate format:

```bash
git tag | grep -E '^v[0-9]+\.[0-9]+\.[0-9]+$'
```

---

# 🔹 Verify Artifact Integrity

```bash
artifact=$(ls builds/*.tar.gz | head -1)

./query-artifacts.sh verify "$artifact"
```

Expected:

```text
Verification PASSED
```

---

# 📊 Release Architecture

```text
Developer
    │
    ▼
Git Commit
    │
    ▼
Version Manager
    │
    ▼
Release Script
    │
    ▼
Build Artifact
    │
    ▼
Metadata Generation
    │
    ▼
Git Tag Creation
    │
    ▼
Artifact Repository
```

---

# 🛠 Troubleshooting

---

## ❌ Version Bump Fails

Verify VERSION file:

```bash
cat VERSION
```

Check permissions:

```bash
chmod 644 VERSION
```

---

## ❌ Build Script Fails

Verify source exists:

```bash
ls src/
```

Check tar:

```bash
which tar
```

---

## ❌ Git Tag Creation Fails

Check repository:

```bash
git status
```

Check existing tags:

```bash
git tag -l
```

---

## ❌ Invalid Metadata JSON

Validate:

```bash
jq empty metadata/*.json
```

---

## ❌ Checksum Verification Fails

Verify artifact not modified:

```bash
sha256sum builds/*.tar.gz
```

Compare with metadata checksum.

---

# 🎓 Key Takeaways

✅ Semantic Versioning communicates release impact

✅ Git Tags create immutable release points

✅ Build Metadata improves traceability

✅ Checksums verify artifact integrity

✅ Automated Releases reduce human error

✅ Provenance tracking supports compliance

✅ Reproducible builds improve reliability

---

# 🚀 Real-World DevOps Applications

These practices are used in:

- 🔹 Jenkins Pipelines
- 🔹 GitHub Actions
- 🔹 GitLab CI/CD
- 🔹 Azure DevOps
- 🔹 Artifact Registry
- 🔹 Nexus Repository
- 🔹 JFrog Artifactory
- 🔹 Kubernetes Release Pipelines

---

# 🏆 Lab Completed

You have successfully:

✔ Implemented Semantic Versioning

✔ Automated Version Management

✔ Generated Build Artifacts

✔ Created Git Release Tags

✔ Generated Build Metadata

✔ Verified Artifact Integrity

✔ Built a Complete Release Workflow

✔ Improved Software Traceability

---

<div align="center">

# 🌟 Version Everything • Track Everything • Verify Everything 🌟

### Happy Learning & Happy DevOps 🚀

</div>
