# QA Automation Case Study – Bynry Internship

## Overview
- **Part 1**: Fix flaky login tests  
- **Part 2**: Design a scalable test framework (documentation only)  
- **Part 3**: End-to-end API + UI + mobile + security test

## Tech Stack
- Python 3.9+
- Playwright (for UI)
- `requests` (for API)
- pytest (test runner)

## How to Run

### Part 1: Flaky Test Fix
```bash
pip install -r requirements.txt
playwright install chromium
pytest part1_flaky_test/test_login_fixed.py -v
```

### Part 3: Integration Test (conceptual)
```bash
pytest part3_integration_test/test_project_creation_flow.py -v
```

## Structure
- `part1_flaky_test/` – Fixed login test  
- `part2_framework_design/` – Framework design document  
- `part3_integration_test/` – API + UI integration test  
- `docs/` – Test plan and sample report
