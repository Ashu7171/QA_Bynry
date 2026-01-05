```markdown
# Test Automation Framework Design

## 📁 Proposed Folder Structure

```
test-automation-framework/
├── tests/
│   ├── web/              # Web UI tests (Playwright)
│   ├── mobile/           # Mobile tests (BrowserStack)
│   └── api/              # REST API tests
├── pages/                # Page Object Model classes
├── utils/
│   ├── auth.py           # Login and token handling
│   ├── tenant_manager.py # Manage tenant contexts
│   └── browserstack.py   # BrowserStack capability setup
├── config/
│   ├── environments.yaml # Tenant-specific URLs
│   └── browsers.yaml     # Browser and device configs
├── data/
│   └── users/            # Test users by tenant and role
├── conftest.py           # Pytest fixtures
├── requirements.txt
└── reports/              # Test reports
```

## ⚙️ Configuration Management

### Environments
Defined in `config/environments.yaml`:
```yaml
company1:
  web_url: "https://company1.workflowpro.com"
  api_base: "https://api.workflowpro.com/v1"
  tenant_id: "company1"
company2:
  web_prot: "https://company2.workflowpro.com"
  api_base: "https://api.workflowpro.com/v1"
  tenant_id: "company2"
```

### Browsers & Devices
Stored in `config/browsers.yaml`:
```yaml
web:
  - browser: Chrome, version: latest
  - browser: Firefox, version: latest
mobile:
  - device: iPhone 15, os: iOS 17
  - device: Samsung Galaxy S23, os: Android 13
```

### Test Data
- User credentials organized by tenant and role in `data/users/`
- Loaded dynamically (e.g., `get_test_user(tenant="company1", role="admin")`)
- Secrets (e.g., BrowserStack credentials) passed via environment variables

## 🧩 Key Design Principles

- **Page Object Model**: Reusable, maintainable UI abstractions
- **Pytest Fixtures**: Isolated, reusable test setups (e.g., `logged_in_page`)
- **Shared Auth Logic**: Reuse login/token logic across API and UI tests
- **BrowserStack Integration**: Conditional remote execution in CI
- **Tenant-Aware Tests**: Every test runs in a single tenant context by default

## ❓ Missing Requirements – Key Questions

1. How is **test data cleaned up** after execution?  
2. Is **2FA disabled** for test accounts in staging?  
3. What is the **BrowserStack session limit**? Should mobile tests be limited?  
4. Do we need **parallel test execution**? What’s the CI concurrency limit?  
5. What **reporting format** is preferred (Allure, HTML, etc.)?  
6. How are **secrets managed** in CI (e.g., BrowserStack credentials)?  
7. Which **CI/CD platform** is used (GitHub Actions, Jenkins, etc.)?
```