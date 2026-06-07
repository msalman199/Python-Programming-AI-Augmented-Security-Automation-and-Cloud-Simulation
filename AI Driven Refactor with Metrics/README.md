# 🤖 AI-Driven Refactor with Metrics

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge\&logo=ubuntu\&logoColor=white)
![Git](https://img.shields.io/badge/Git-Version%20Control-F05032?style=for-the-badge\&logo=git\&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-Testing-0A9EDC?style=for-the-badge\&logo=pytest\&logoColor=white)
![Radon](https://img.shields.io/badge/Radon-Code%20Metrics-4B8BBE?style=for-the-badge)
![Pylint](https://img.shields.io/badge/Pylint-Code%20Quality-2F8F4E?style=for-the-badge)
![Black](https://img.shields.io/badge/Black-Code%20Formatter-000000?style=for-the-badge)
![Aider](https://img.shields.io/badge/Aider-AI%20Refactoring-7B61FF?style=for-the-badge)

### 🚀 Measure • Refactor • Validate • Compare

</div>

---

## 📖 Overview

This lab demonstrates how to use **AI-assisted refactoring techniques** combined with **software quality metrics** to improve legacy Python code while maintaining correctness and performance.

You will:

* 📊 Measure code complexity
* 🤖 Use AI-assisted refactoring workflows
* 🧪 Validate functionality with automated testing
* ⚡ Benchmark performance
* 📈 Compare maintainability improvements
* 🔄 Build a metrics-driven improvement pipeline

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

✅ Use AI tools to safely refactor legacy code

✅ Measure code complexity before and after refactoring

✅ Track performance improvements through metrics

✅ Validate refactoring changes with automated tests

✅ Apply DevOps best practices for code quality monitoring

---

# 📚 Prerequisites

Before starting, ensure you have:

* Basic Python programming knowledge
* Understanding of code complexity concepts
* Familiarity with Linux command line
* Basic Git operations
* Understanding of software metrics

  * Cyclomatic Complexity
  * Maintainability Index
  * Halstead Metrics

---

# 🛠️ Environment Setup

## 🔹 Install Required Tools

```bash
# Update system
sudo apt update

# Install Python and pip
sudo apt install -y python3 python3-pip python3-venv git

# Create project directory
mkdir -p ~/ai-refactor-lab
cd ~/ai-refactor-lab

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required packages
pip install radon pylint pytest pytest-benchmark black isort aider-chat

# Verify installations
radon --version
pylint --version
pytest --version
```

---

# 📂 Project Structure

```text
ai-refactor-lab/
│
├── legacy_calculator.py
├── refactored_calculator.py
├── measure_metrics.py
├── compare_metrics.py
│
├── test_performance.py
├── test_refactored_performance.py
├── test_correctness.py
│
├── baseline_complexity.json
├── baseline_maintainability.json
│
├── refactored_complexity.json
├── refactored_maintainability.json
│
├── baseline_perf.json
├── refactored_perf.json
│
└── refactor_instructions.md
```

---

# 🚩 Task 1: Analyze Legacy Code Complexity

---

## 🔍 Step 1: Create Legacy Code Sample

Create the legacy application:

```bash
cat > legacy_calculator.py << 'EOF'
# Legacy code here
EOF
```

### 🎯 Goal

Create intentionally complex code that contains:

* Deep nesting
* Multiple condition branches
* High cyclomatic complexity
* Low maintainability

---

## 📊 Step 2: Measure Initial Complexity

Create the metrics collection script:

```bash
cat > measure_metrics.py << 'EOF'
# Metrics analyzer implementation
EOF
```

### 🔧 TODO

Implement:

```python
analyze_file()
save_metrics()
main()
```

### 📈 Metrics to Collect

| Metric                | Purpose                             |
| --------------------- | ----------------------------------- |
| Cyclomatic Complexity | Measures branching complexity       |
| Maintainability Index | Indicates code maintainability      |
| Halstead Difficulty   | Measures implementation complexity  |
| Halstead Effort       | Estimates effort to understand code |

---

### Run Initial Analysis

```bash
echo "=== Cyclomatic Complexity ==="
radon cc legacy_calculator.py -s

echo -e "\n=== Maintainability Index ==="
radon mi legacy_calculator.py -s

echo -e "\n=== Raw Metrics ==="
radon raw legacy_calculator.py
```

### Save Baseline Metrics

```bash
radon cc legacy_calculator.py -j > baseline_complexity.json
radon mi legacy_calculator.py -j > baseline_maintainability.json
```

---

## ⚡ Step 3: Create Performance Benchmark

Create benchmark tests:

```bash
cat > test_performance.py << 'EOF'
# Benchmark tests
EOF
```

### 🎯 Objectives

Benchmark:

* calculate_total()
* process_order()

Add:

* Edge case tests
* Performance measurements
* Repeatable benchmarks

---

# 🤖 Task 2: AI-Assisted Refactoring

---

## ⚙️ Step 1: Configure AI Refactoring Tool

Create Aider configuration:

```bash
cat > .aider.conf.yaml << 'EOF'
auto-commits: false
dirty-commits: false
attribute-author: true
attribute-committer: false
EOF
```

Initialize Git:

```bash
git init
git add legacy_calculator.py
git commit -m "Initial commit: legacy code baseline"
```

---

## 📝 Step 2: Create Refactoring Instructions

Create:

```bash
cat > refactor_instructions.md
```

### Refactoring Goals

✅ Complexity < 5 per function

✅ Extract nested conditionals

✅ Implement Strategy Pattern

✅ Improve readability

✅ Preserve behavior

---

## 🏗️ Step 3: Create Refactored Template

Create:

```bash
cat > refactored_calculator.py
```

### Required Components

#### Abstract Strategy

```python
class DiscountStrategy(ABC):
```

#### Strategy Implementations

```python
ElectronicsDiscountStrategy
ClothingDiscountStrategy
DefaultDiscountStrategy
```

#### Factory Pattern

```python
get_discount_strategy()
```

#### Refactored Functions

```python
calculate_total()
process_order()
```

---

## ✨ Step 4: Implement Refactoring

### Best Practices

✔ Use Strategy Pattern

✔ Add Type Hints

✔ Add Docstrings

✔ Use Early Returns

✔ Reduce Nesting

✔ Improve Readability

---

# 📈 Task 3: Measure and Compare Metrics

---

## 🔍 Step 1: Analyze Refactored Code

Run:

```bash
radon cc refactored_calculator.py -s
radon mi refactored_calculator.py -s
```

Save metrics:

```bash
radon cc refactored_calculator.py -j > refactored_complexity.json

radon mi refactored_calculator.py -j > refactored_maintainability.json
```

---

## 📊 Step 2: Create Comparison Report

Create:

```bash
cat > compare_metrics.py
```

### Implement

```python
load_metrics()
compare_complexity()
generate_report()
```

### Report Should Include

* Complexity reduction
* Maintainability increase
* Percentage improvement
* Function-by-function comparison

---

## 🚀 Step 3: Run Performance Comparison

Create:

```bash
cat > test_refactored_performance.py
```

Benchmark:

```python
calculate_total()
process_order()
```

Add:

```python
test_correctness_electronics_premium_holiday()
```

---

### Execute Benchmarks

```bash
pytest test_performance.py \
--benchmark-only \
--benchmark-json=baseline_perf.json

pytest test_refactored_performance.py \
--benchmark-only \
--benchmark-json=refactored_perf.json
```

Compare:

```bash
python3 -m pytest \
--benchmark-compare=baseline_perf.json \
--benchmark-compare-fail=mean:10%
```

---

# ✅ Verification

---

## 📉 Verify Complexity Reduction

```bash
baseline_cc=$(radon cc legacy_calculator.py -a | grep "Average complexity" | awk '{print $NF}')

refactored_cc=$(radon cc refactored_calculator.py -a | grep "Average complexity" | awk '{print $NF}')
```

Display:

```bash
echo "Baseline complexity: $baseline_cc"
echo "Refactored complexity: $refactored_cc"
```

---

## 🧪 Verify Functional Correctness

Create:

```bash
cat > test_correctness.py
```

Run:

```bash
pytest test_correctness.py -v
```

### Validation Goal

Ensure:

```text
Legacy Output == Refactored Output
```

for every test scenario.

---

# 🎯 Expected Outcomes

After successful completion:

| Metric                | Expected Improvement     |
| --------------------- | ------------------------ |
| Cyclomatic Complexity | ⬇ 50–70%                 |
| Maintainability Index | ⬆ 20–30 Points           |
| Functional Tests      | ✅ Pass                   |
| Performance           | ✅ Equal or Better        |
| Readability           | ✅ Significantly Improved |

---

# 🛡️ Troubleshooting

---

## ❌ Aider Not Working

```text
Use manual refactoring.
Follow the provided template.
```

---

## ❌ No Metrics Improvement

Check:

* Reduced nesting
* Smaller functions
* Strategy pattern implementation

---

## ❌ Tests Failing

Review:

* Discount logic
* Holiday logic
* VIP20 calculations
* Edge cases

Debug with:

```python
print()
```

comparisons.

---

## ❌ Performance Degraded

Profile:

```bash
python3 -m cProfile -s cumtime refactored_calculator.py
```

Optimization ideas:

* Cache strategy instances
* Reduce object creation
* Simplify branching

---

# 📊 Success Criteria Checklist

* [ ] Legacy metrics collected
* [ ] Baseline benchmarks executed
* [ ] Git repository initialized
* [ ] Refactoring instructions prepared
* [ ] Strategy Pattern implemented
* [ ] Complexity reduced
* [ ] Maintainability improved
* [ ] Tests passing
* [ ] Benchmarks compared
* [ ] Report generated

---

# 🎓 Conclusion

In this lab, you have:

✅ Measured software quality using Radon

✅ Applied AI-assisted refactoring techniques

✅ Reduced cyclomatic complexity

✅ Improved maintainability

✅ Preserved functionality using tests

✅ Compared performance before and after changes

✅ Built a repeatable metrics-driven improvement workflow

These techniques are essential for modern DevOps, Platform Engineering, and Software Engineering teams maintaining large production codebases.

---

# 💡 Key Takeaways

### 📏 Measure Before Refactoring

Data should guide improvements.

### 🧪 Test Everything

Refactoring without tests is risky.

### 📈 Track Metrics Continuously

Quality trends matter more than one-time measurements.

### 🤖 AI Assists, Humans Validate

AI accelerates refactoring but verification remains critical.

### 🏗️ Simpler Code Wins

Lower complexity leads to:

* Better maintainability
* Easier onboarding
* Faster debugging
* Safer deployments

---

<div align="center">

## 🚀 Happy Refactoring!

**Measure → Refactor → Test → Compare → Improve**

⭐ Don't forget to track your technical debt reduction journey.

</div>
