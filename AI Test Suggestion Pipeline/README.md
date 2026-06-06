# 🤖 AI Test Suggestion Pipeline

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Git](https://img.shields.io/badge/Git-Version%20Control-orange?logo=git)
![Ollama](https://img.shields.io/badge/Ollama-Local%20AI-green)
![AST](https://img.shields.io/badge/AST-Code%20Analysis-purple)
![DevOps](https://img.shields.io/badge/DevOps-Automation-red)
![CI/CD](https://img.shields.io/badge/CI%2FCD-Testing-yellow)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-black?logo=linux)

---

# 📖 Overview

Modern development teams often struggle to maintain adequate test coverage as code evolves. This lab demonstrates how to build an **AI-powered Test Suggestion Pipeline** that automatically analyzes code changes, identifies testing gaps, and generates intelligent test recommendations using local AI models.

The pipeline combines:

- 🔍 Static Code Analysis (AST)
- 📂 Git Change Detection
- 🧠 AI-Based Test Generation
- 📊 Complexity Analysis
- 🚀 CI/CD Integration

---

# 🎯 Learning Objectives

By completing this lab, you will learn how to:

✅ Analyze source code changes using Git

✅ Extract functions and metadata using Python AST

✅ Measure function complexity

✅ Integrate local AI models using Ollama

✅ Generate intelligent unit test recommendations

✅ Create automated test coverage reports

✅ Build reusable DevOps automation workflows

---

# 📋 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming knowledge
- Familiarity with Git workflows
- Understanding of unit testing concepts
- Linux command-line experience
- Basic knowledge of REST APIs and JSON

---

# 🛠 Environment Setup

## Step 1: Update System

```bash
sudo apt update
```

---

## Step 2: Install Python & Git

```bash
sudo apt install -y python3 python3-pip python3-venv git
```

---

## Step 3: Create Project Workspace

```bash
mkdir -p ~/ai-test-pipeline
cd ~/ai-test-pipeline
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
pip install openai gitpython ast-parser
```

---

# 📁 Project Structure

Create the project layout:

```bash
cd ~/ai-test-pipeline

mkdir -p src tests sample_project

touch src/code_analyzer.py
touch src/test_suggester.py
touch src/pipeline.py
```

Expected structure:

```text
ai-test-pipeline/
│
├── src/
│   ├── code_analyzer.py
│   ├── test_suggester.py
│   └── pipeline.py
│
├── tests/
│
├── sample_project/
│
└── venv/
```

---

# 🔍 Task 1 — Build Code Change Analyzer

## 🎯 Goal

Analyze Python code changes and extract useful information for AI-generated test suggestions.

---

## Step 1: Create Code Analyzer

Create:

```bash
nano src/code_analyzer.py
```

Key responsibilities:

- Initialize Git repository
- Detect changed files
- Parse Python AST
- Extract function metadata
- Measure complexity

---

### Important Methods

### get_changed_files()

```python
def get_changed_files(self, commit_range="HEAD~1..HEAD"):
```

Responsibilities:

- Execute git diff
- Detect modified files
- Filter Python files only

---

### extract_functions()

```python
def extract_functions(self, file_path):
```

Extract:

- Function names
- Parameters
- Docstrings
- Complexity metrics

---

### analyze_complexity()

```python
def analyze_complexity(self, function_node):
```

Calculate:

- Conditional branches
- Loops
- Cyclomatic complexity estimate

---

# 🧪 Task 2 — Create Sample Project

Create:

```bash
nano sample_project/calculator.py
```

Example functions:

```python
def add(a, b):
    return a + b

def divide(a, b):
    if b == 0:
        raise ValueError()
    return a / b

def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError()

    return price - (
        price * discount_percent / 100
    )
```

---

## Initialize Git Repository

```bash
cd sample_project

git init

git add .

git commit -m "Initial calculator implementation"
```

---

# 🧪 Task 3 — Test Analyzer

Create:

```bash
nano tests/test_analyzer.py
```

Purpose:

- Verify AST parsing
- Verify function extraction
- Verify complexity calculations

Run:

```bash
python3 tests/test_analyzer.py
```

Expected output:

```text
Found 3 functions

Function: add
Parameters: ['a', 'b']

Function: divide
Parameters: ['a', 'b']

Function: calculate_discount
Parameters: ['price', 'discount_percent']
```

---

# 🤖 Task 4 — Install Local AI Model

## Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

## Pull Code Model

```bash
ollama pull codellama:7b
```

---

## Verify Installation

```bash
ollama list
```

Expected:

```text
NAME
codellama:7b
```

---

# 🧠 Task 5 — Build AI Test Suggester

Create:

```bash
nano src/test_suggester.py
```

---

## Responsibilities

The module should:

### Generate Prompt

Include:

- Function signature
- Parameters
- Complexity score
- Request for edge cases

Example:

```text
Analyze the following function:

Function:
calculate_discount(price, discount)

Complexity:
3

Generate:
1. Happy path tests
2. Edge cases
3. Error handling tests
4. Boundary conditions
```

---

### Call Ollama

Example:

```python
subprocess.run(
    ["ollama", "run", model, prompt]
)
```

---

### Parse Suggestions

Convert AI response into:

```json
{
  "test_type": "edge_case",
  "description": "Discount equals 100"
}
```

---

# 🚀 Task 6 — Build Pipeline Orchestrator

Create:

```bash
nano src/pipeline.py
```

Pipeline workflow:

```text
Git Changes
      │
      ▼
Code Analyzer
      │
      ▼
AST Extraction
      │
      ▼
Complexity Analysis
      │
      ▼
AI Test Generator
      │
      ▼
JSON Report
      │
      ▼
Markdown Report
```

---

## Pipeline Responsibilities

### Step 1

Detect changed files

```python
changed_files = analyzer.get_changed_files()
```

---

### Step 2

Extract functions

```python
functions = analyzer.extract_functions()
```

---

### Step 3

Generate AI suggestions

```python
suggestions = suggester.suggest_tests()
```

---

### Step 4

Save results

```bash
suggestions/test_suggestions.json
```

---

### Step 5

Generate Markdown report

```bash
suggestions/report.md
```

---

# 📝 Task 7 — Run Pipeline

Activate environment:

```bash
source venv/bin/activate
```

Run:

```bash
python3 src/pipeline.py \
--repo ./sample_project \
--output ./suggestions
```

---

# 📊 Sample Output

## JSON

```json
{
  "function": "divide",
  "tests": [
    {
      "type": "happy_path",
      "description": "Divide 10 by 2"
    },
    {
      "type": "error",
      "description": "Divide by zero"
    }
  ]
}
```

---

## Markdown Report

```markdown
# Test Suggestion Report

## divide()

Priority: High

Recommended Tests:

- Divide valid numbers
- Divide negative numbers
- Divide by zero
```

---

# 🧪 Task 8 — Add New Code Change

Append:

```python
def calculate_tax(amount, tax_rate, region):

    if region == "US":
        if amount > 1000:
            return amount * (tax_rate * 1.1)

    elif region == "EU":
        if amount > 500:
            return amount * (tax_rate * 1.2)

    return amount * tax_rate
```

Commit:

```bash
git add .

git commit -m "Add tax calculation"
```

---

## Run Pipeline Again

```bash
python3 src/pipeline.py \
--repo ./sample_project \
--commit-range HEAD~1..HEAD
```

---

# ✅ Verification

## Verify AST Analysis

```bash
python3 tests/test_analyzer.py
```

Expected:

```text
Functions detected
Parameters extracted
Complexity metrics generated
```

---

## Verify Ollama

```bash
ollama list
```

Expected:

```text
codellama:7b
```

---

## Verify Suggestions

```bash
cat suggestions/test_suggestions.json
```

Look for:

- Happy-path tests
- Edge cases
- Boundary tests
- Error handling tests

---

## Verify Reports

```bash
cat suggestions/report.md
```

Expected:

```text
Function summaries
Complexity scores
Suggested test cases
Risk prioritization
```

---

# 🔍 Suggested Tests for calculate_tax()

AI should recommend:

### Region Coverage

- US region
- EU region
- Unknown region

### Boundary Values

- Amount = 1000
- Amount = 1001
- Amount = 500
- Amount = 501

### Invalid Inputs

- Negative amount
- Invalid tax rate
- Empty region

### Parameterized Tests

```python
@pytest.mark.parametrize(...)
```

---

# 🚨 Troubleshooting

## Ollama Not Responding

Check service:

```bash
systemctl status ollama
```

Restart:

```bash
sudo systemctl restart ollama
```

---

## Git Errors

Verify repository:

```bash
git status
```

Initialize if necessary:

```bash
git init
```

---

## Import Errors

Check virtual environment:

```bash
which python3
```

Reinstall:

```bash
pip install --force-reinstall openai gitpython
```

---

## AST Parsing Errors

Check:

- Syntax validity
- UTF-8 encoding
- Indentation issues

---

# 🎯 Real-World DevOps Use Cases

This pipeline can be integrated into:

- GitHub Actions
- GitLab CI/CD
- Jenkins Pipelines
- Azure DevOps
- Argo Workflows

Benefits:

✅ Better test coverage

✅ Faster code reviews

✅ Automated quality checks

✅ Reduced manual effort

✅ Improved deployment confidence

---

# 🏆 Conclusion

In this lab, you successfully built an **AI Test Suggestion Pipeline** capable of:

- Detecting code changes using Git
- Parsing source code with AST
- Measuring function complexity
- Leveraging local AI models through Ollama
- Generating intelligent test recommendations
- Producing actionable reports for developers

This approach combines **static analysis**, **AI-assisted reasoning**, and **DevOps automation** to improve software quality while reducing the manual effort required to maintain comprehensive test coverage.

---

# 🚀 Next Steps

- Integrate with GitHub Pull Requests
- Add code coverage analysis
- Implement risk-based test prioritization
- Generate actual pytest test cases automatically
- Support multiple programming languages
- Integrate with CI/CD pipelines
- Use larger coding models for improved suggestions

---

## 🎓 Lab Complete

You now have a working foundation for building **AI-powered testing assistants** that help development teams maintain high-quality software through intelligent automation.
