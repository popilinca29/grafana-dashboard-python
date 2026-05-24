# Test Strategy – Grafana Synthetic Monitoring Dashboard

## 1. Objective

The objective of this testing effort is to validate the functionality, reliability, and usability of the Grafana Synthetic Monitoring dashboard UI.

The focus is on:
- Interactive dashboard behavior
- Dynamic data visualization
- Search and filtering functionality
- UI responsiveness under changing data conditions


## 2. Scope

### In Scope
- Dashboard page load and rendering
- Search functionality validation
- Filtering and dynamic UI updates
- Table/data visualization updates
- Basic UI consistency checks

### Out of Scope
- Backend/API validation (no direct API access assumed)
- Performance/load testing
- Authentication flows
- Cross-browser exhaustive testing

## 3. Test Approach

A **UI-based black-box testing approach** will be used.

Automation is implemented using:
- Playwright (Python)
- Pytest framework
- Page Object Model (POM) design pattern

Key principles:
- Validate UI behavior, not internal implementation
- Use stable locators and auto-waiting mechanisms
- Focus on dynamic content handling instead of static assertions

---

## 4. Test Scenarios

### 4.1 Dashboard Load Validation
- Verify dashboard page loads successfully
- Validate key UI components are visible (search bar, table/widgets)
- Ensure no critical UI errors or blank states

### 4.2 Search Functionality
- Enter valid search input in dashboard search field
- Validate that the application navigates to the Observability page/view
- Verify URL change reflects navigation (if applicable)
- Confirm Observability page elements are loaded (headers, widgets, panels)
- Ensure no broken state or partial rendering after redirect
- Validate back navigation returns to dashboard correctly

### 4.4 Filtering Functionality
- Apply filters to dashboard data
- Validate filtered results reflect selected criteria
- Remove filters and confirm data resets correctly

## 5. Test Data Strategy

- Use live dashboard data from Grafana demo environment
- No static test dataset required
- Validate using:
  - presence/visibility of elements
  - row counts (relative validation)
  - UI state changes after interactions

## 6. Test Environment

- Application: Grafana Synthetic Monitoring Demo
- URL: https://play.grafana.org/a/grafana-synthetic-monitoring-app/home
- Browser: Chromium (Playwright)
- Execution: Local machine (headless or headed mode) + Github Actions

## 7. Risks
### Risks
- Dynamic UI may lead to flaky tests
- Changing data may affect consistency of assertions
- Limited control over backend data

### Mitigation
- Use resilient locators
- Avoid hard-coded values
- Retry mechanisms for unstable UI elements

## 8. Tools & Frameworks

- Python 3.12
- Playwright
- Pytest
- Page Object Model (POM)
- Allure reporting

## 9.CI/CD Execution (GitHub Actions)

Tests are executed via GitHub Actions on every push and pull request.

### Workflow:
- Runs on main branch updates and PRs
- Uses Python 3.12
- Installs dependencies + Playwright browsers
- Runs tests in headless mode
- Injects environment variables (BASE_URL, HEADLESS) via GitHub Repository Variables

## 10. Test Artifacts & Reporting

GitHub Actions stores execution artifacts for debugging and traceability. Artifacts can be downloaded from each workflow run.

Includes:
- HTML test report (pytest-html)
- Screenshots (on failure, if enabled)
- Logs and execution outputs

## 11. Conclusion

This test strategy focuses on validating the Grafana dashboard from an end-user perspective, ensuring that key UI interactions (search, filtering, and dynamic updates) work reliably under changing data conditions.

The approach prioritizes stability, maintainability, and realistic UI validation over rigid data assertions.