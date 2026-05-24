# grafana-dashboard-python
grafana-dashboard-python

# Grafana UI Automation Framework (Playwright + Python)
Python - 3.12.x
Playwright - latest

A lightweight UI automation framework built using Playwright + Python + Pytest to test the Grafana Synthetic Monitoring dashboard, focusing on dynamic content handling, filtering, and search functionality.

# Application Under Test

[Grafana Synthetic Monitoring Demo](https://play.grafana.org/a/grafana-synthetic-monitoring-app/home)

# Key Features
Page Object Model (POM) design
Playwright auto-waiting for dynamic UI
Handling of dynamic dashboard data
Search and filtering validation
Stable locator strategy

# Project Structure
ggrafana-dashboard-python/
│
├── github/workflows
│   ├── 
├── test_data/
│   └── constants.py
├── pages/
│   ├── __init__.py
│   └── dashboard_page.py
│
├── tests/
│   ├── __init__.py
│   ├── test_dashboard_load.py
│   ├── test_search.py
│   └── test_dynamic_behavior.py
│
├── utils/
│   ├── __init__.py
│   └── helpers.py
│
├── conftest.py
├── requirements.txt
├── pytest.ini
├── .gitignore
├── .env
├── README.md
├── test_strategy.md
└── data_validation_report.md

# Prerequisites
VS Code
Python (`brew install python@3.12`)

# Setup & Installation
# Clone repo
git clone <repo-url>
cd grafana-dashboard-python

# Create virtual environment
python3.12 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install browsers
playwright install
# Running Tests
Run all tests: pytest -v

# Run with browser visible
To run all tests: `pytest --headed`
To run a specific test: e.g `pytest tests/test_dashboard_load.py`

# Test Coverage
1. Dashboard Load Validation
Verify dashboard loads successfully
Validate key UI elements are visible
2. Search Functionality
Validate search input works
Verify results update dynamically
3. Filter Behavior
Apply filters on monitoring data
Validate UI updates accordingly

# Approach to Dynamic UI
Used Playwright auto-waiting for async rendering
Avoided hard-coded waits where possible
Validated presence/structure instead of exact values
Handled dynamic data using stable assertions (visibility, count, format)


# Data Validation Strategy
UI-based validation (DOM checks, row counts, widget visibility)
Cross-widget consistency checks (summary vs table data)
Heuristic validation for dynamic metrics (format/range checks)
Designed to work even without direct API access

# Tools Used
Python
Playwright
Pytest
Page Object Model

# Notes
Tests are designed for dynamic dashboards with changing data
Focus is on stability and resilience rather than exact data matching
Framework is structured for easy extension and CI integration

# CI/CD
- Project uses Github Actions - script is automatically triggered on push and PR events, as well as manual trigger (`workflow_dispatch`) where you can choose the branch you want to run it on