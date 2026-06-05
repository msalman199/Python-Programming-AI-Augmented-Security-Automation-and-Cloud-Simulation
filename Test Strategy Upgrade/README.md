
# 🧪 Test Strategy Upgrade

<p align="center">

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTest](https://img.shields.io/badge/PyTest-Testing-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white)
![Coverage](https://img.shields.io/badge/Test_Coverage-80%25+-success?style=for-the-badge)
![Git](https://img.shields.io/badge/Git-Version_Control-F05032?style=for-the-badge&logo=git&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![DevOps](https://img.shields.io/badge/DevOps-Quality_Assurance-blueviolet?style=for-the-badge)

</p>

---

# 📖 Overview

In this lab, you will implement a **multi-layered testing strategy** for a Python-based e-commerce order processing application.

The lab covers:

✅ Unit Testing

✅ Integration Testing

✅ Test Coverage Reporting

✅ Improved Assertions

✅ Test Organization

✅ DevOps Testing Best Practices

---

# 🎯 Learning Objectives

By completing this lab, you will be able to:

- Implement a multi-layered testing strategy
- Create unit tests for individual components
- Build integration tests for workflows
- Improve assertions for better diagnostics
- Generate test coverage reports
- Understand testing within DevOps pipelines

---

# 📋 Prerequisites

Before starting, ensure you have:

- Basic Python knowledge
- Git and version control experience
- Understanding of unit testing concepts
- Linux command-line familiarity
- Knowledge of software development lifecycle

---

# 🛠️ Environment Setup

After launching the lab environment:

---

## 🔹 Step 1: Install Required Packages

```bash
sudo apt update

sudo apt install -y python3 python3-pip python3-venv
```

---

## 🔹 Step 2: Create Project Workspace

```bash
mkdir -p ~/test-strategy-lab

cd ~/test-strategy-lab
```

---

## 🔹 Step 3: Create Virtual Environment

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 🔹 Step 4: Install Testing Tools

```bash
pip install pytest pytest-cov pytest-mock
```

---

# 🚀 Task 1: Define Test Layers and Create Application Structure

---

## 🔹 Step 1: Create Project Structure

```bash
mkdir -p src/order_system tests/{unit,integration}

touch src/__init__.py
touch src/order_system/__init__.py

touch tests/__init__.py
touch tests/unit/__init__.py
touch tests/integration/__init__.py
```

---

## 📂 Expected Structure

```text
test-strategy-lab/
│
├── src/
│   └── order_system/
│       ├── __init__.py
│       ├── models.py
│       ├── inventory.py
│       └── processor.py
│
├── tests/
│   ├── unit/
│   └── integration/
│
├── pytest.ini
├── run_tests.sh
└── venv/
```

---

# 🏗️ Step 2: Create Application Components

---

## 📦 models.py

Create:

```bash
nano src/order_system/models.py
```

Paste:

```python
from dataclasses import dataclass
from typing import List
from decimal import Decimal

@dataclass
class Product:
    id: str
    name: str
    price: Decimal
    stock: int

@dataclass
class OrderItem:
    product: Product
    quantity: int

    def get_subtotal(self) -> Decimal:
        """Calculate subtotal for this order item"""
        # TODO
        pass

@dataclass
class Order:
    order_id: str
    items: List[OrderItem]
    discount_percent: Decimal = Decimal('0')

    def calculate_total(self) -> Decimal:
        """Calculate order total"""
        # TODO
        pass
```

---

## 📦 inventory.py

```bash
nano src/order_system/inventory.py
```

```python
from typing import Dict, Optional
from .models import Product

class InventoryManager:
    def __init__(self):
        self.products: Dict[str, Product] = {}

    def add_product(self, product: Product) -> None:
        # TODO
        pass

    def get_product(self, product_id: str) -> Optional[Product]:
        # TODO
        pass

    def check_availability(self, product_id: str, quantity: int) -> bool:
        # TODO
        pass

    def reduce_stock(self, product_id: str, quantity: int) -> bool:
        # TODO
        pass
```

---

## 📦 processor.py

```bash
nano src/order_system/processor.py
```

```python
from typing import List, Tuple
from .models import Order
from .inventory import InventoryManager

class OrderProcessor:
    def __init__(self, inventory_manager: InventoryManager):
        self.inventory = inventory_manager
        self.processed_orders: List[Order] = []

    def validate_order(self, order: Order) -> Tuple[bool, str]:
        # TODO
        pass

    def process_order(self, order: Order) -> Tuple[bool, str]:
        # TODO
        pass
```

---

# ⚙️ Step 3: Configure PyTest

Create:

```bash
nano pytest.ini
```

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

addopts =
    -v
    --tb=short
    --strict-markers

markers =
    unit: Unit tests
    integration: Integration tests
    slow: Slow tests
```

---

# 🧪 Task 2: Implement Unit Tests

---

## 🔹 Create Model Tests

File:

```bash
nano tests/unit/test_models.py
```

### Test Areas

### Product Tests

✔ Product Creation

✔ Price Type Validation

### OrderItem Tests

✔ Subtotal Calculation

✔ Quantity Handling

### Order Tests

✔ No Discount Total

✔ Discount Total

✔ Empty Order

---

## 🔹 Create Inventory Tests

File:

```bash
nano tests/unit/test_inventory.py
```

### Test Scenarios

| Test | Purpose |
|--------|----------|
| Add Product | Verify storage |
| Get Product | Verify retrieval |
| Missing Product | Handle invalid ID |
| Availability Check | Stock validation |
| Reduce Stock | Inventory update |
| Failure Cases | Edge conditions |

---

# 🧩 Task 3: Implement Integration Tests

---

## 🔹 Create Integration Test File

```bash
nano tests/integration/test_order_processing.py
```

---

## Integration Workflow Tests

### ✔ Successful Order Processing

Validate:

- Order accepted
- Stock reduced
- Order saved

---

### ✔ Out-of-Stock Validation

Validate:

- Order rejected
- Error returned

---

### ✔ Inventory Consistency

Validate:

- Failed order doesn't alter inventory

---

### ✔ Multiple Sequential Orders

Validate:

- All orders processed
- Inventory updated correctly

---

### ✔ Discount Processing

Validate:

- Discount applied correctly
- Final total accurate

---

# 📊 Coverage Testing

---

## 🔹 Create Test Runner Script

```bash
nano run_tests.sh
```

```bash
#!/bin/bash

echo "Running Unit Tests..."
pytest tests/unit -m unit -v

echo -e "\nRunning Integration Tests..."
pytest tests/integration -m integration -v

echo -e "\nRunning All Tests with Coverage..."
pytest tests/ \
--cov=src/order_system \
--cov-report=html \
--cov-report=term

echo -e "\nCoverage report generated in htmlcov/index.html"
```

---

## Make Script Executable

```bash
chmod +x run_tests.sh
```

---

# ✅ Verification

---

## 🔹 Step 1: Complete All TODO Sections

Implement:

- Order subtotal logic
- Order total logic
- Inventory management
- Order processing
- Test assertions

---

## 🔹 Step 2: Run Unit Tests

```bash
pytest tests/unit -v
```

Expected:

```text
10+ tests passed
```

---

## 🔹 Step 3: Run Integration Tests

```bash
pytest tests/integration -v
```

Expected:

```text
5+ tests passed
```

---

## 🔹 Step 4: Generate Coverage Report

```bash
pytest tests/ \
--cov=src/order_system \
--cov-report=term-missing
```

Target:

```text
Coverage > 80%
```

---

## 🔹 Step 5: Test Quality Review

Verbose output:

```bash
pytest tests/ -v --tb=long
```

Run markers:

```bash
pytest -m unit

pytest -m integration
```

---

## 🔹 Step 6: HTML Coverage Report

Generate:

```bash
pytest tests/ \
--cov=src/order_system \
--cov-report=html
```

Serve report:

```bash
python3 -m http.server 8000 --directory htmlcov
```

Open:

```text
http://localhost:8000
```

---

# 📈 Coverage Architecture

```text
                    Application
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         ▼               ▼               ▼

     Models         Inventory       Processor
         │               │               │
         └───────────────┼───────────────┘
                         │
                         ▼

                 Unit Tests Layer
                         │
                         ▼

              Integration Tests Layer
                         │
                         ▼

               Coverage Analysis Layer
                         │
                         ▼

                    Quality Report
```

---

# 🎯 Expected Outcomes

After completing this lab you should have:

✅ Organized test structure

✅ Unit test suite

✅ Integration test suite

✅ Coverage reporting

✅ Assertion best practices

✅ Working order processing application

---

# 🏆 Success Criteria

| Requirement | Target |
|------------|---------|
| Unit Tests | ≥ 10 |
| Integration Tests | ≥ 5 |
| Coverage | > 80% |
| Test Layers | Unit + Integration |
| Assertions | Descriptive |
| Organization | Clean Structure |

---

# 📋 Verification Checklist

- [ ] Virtual environment created
- [ ] PyTest installed
- [ ] pytest-cov installed
- [ ] pytest-mock installed
- [ ] Models implemented
- [ ] Inventory manager implemented
- [ ] Order processor implemented
- [ ] Unit tests passing
- [ ] Integration tests passing
- [ ] Coverage > 80%
- [ ] HTML coverage generated

---

# 🛠️ Troubleshooting Guide

---

## ❌ Import Errors

Ensure:

```bash
pwd
```

Shows project root.

Activate environment:

```bash
source venv/bin/activate
```

---

## ❌ Decimal Precision Problems

Use:

```python
from decimal import Decimal
```

Avoid:

```python
float
```

For monetary calculations.

---

## ❌ Fixture Not Found

Verify:

- Fixture names match
- Fixture scope is correct
- Fixtures exist in class or conftest.py

---

## ❌ Coverage Missing

Verify:

```bash
--cov=src/order_system
```

Matches source path.

---

## ❌ Low Coverage

Check:

- Edge cases
- Validation paths
- Error handling
- Failed order processing

---

# 🎓 DevOps Testing Best Practices

### ✅ Unit Tests

Fast, isolated, deterministic.

### ✅ Integration Tests

Validate component interaction.

### ✅ Coverage Analysis

Identify untested code.

### ✅ Clear Assertions

Provide meaningful failure messages.

### ✅ Automated Execution

Run tests in CI/CD pipelines.

---

# 🚀 Conclusion

Congratulations! 🎉

You have successfully upgraded your testing strategy using a professional multi-layered approach.

### Skills Acquired

🔹 Unit Testing

🔹 Integration Testing

🔹 Coverage Analysis

🔹 Assertion Design

🔹 Test Organization

🔹 DevOps Quality Practices

### Business Benefits

✅ Increased Deployment Confidence

✅ Faster Debugging

✅ Reduced Production Bugs

✅ Safer Refactoring

✅ Better System Reliability

✅ Higher Software Quality

This testing strategy mirrors modern DevOps workflows where automated validation is a critical part of continuous integration and deployment pipelines.

---

# 🏆 Lab Completed Successfully

### Test Strategy Upgrade Lab ✔️

🧪 Build Quality Through Testing • Deploy With Confidence 🚀
````
