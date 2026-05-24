# Data Validation Approach – Grafana Synthetic Monitoring Dashboard

## 1. Objective

The objective of this approach is to ensure that data displayed on the Grafana Synthetic Monitoring dashboard is consistent, accurate, and reflects expected UI behavior, even in the absence of direct backend or API access.


## 2. Validation Strategy Overview

Since direct access to backend APIs or databases is not available, validation is performed using a UI based validation approach 

The focus is on:
- UI consistency
- Data presence and structure
- Relative correctness of displayed values
- Behavioral validation after user interactions

## 3. UI-Based Validation Methods

### 3.1 Element Presence Validation
- Ensure key dashboard components are visible
- Validate that tables, charts, and widgets are rendered correctly
- Confirm no missing or broken UI elements

### 3.2 Structural Data Validation
- Validate presence of rows in tables or entries in lists
- Ensure data is formatted correctly (e.g., timestamps, status labels)
- Verify expected columns or labels exist in UI components

### 3.3 Relative Data Validation
- Validate changes in data after user actions (e.g., search/filter)
- Ensure that applying filters changes visible results
- Confirm that result count decreases/increases logically after interactions

### 3.4 Consistency Validation Across UI Components
- Compare related UI elements (e.g., summary vs detailed table view)
- Ensure no contradiction between widgets displaying similar metrics
- Validate that dashboard updates are reflected across all relevant components

## 4. Handling Dynamic Data

Since the application contains real-time and dynamic data:

- Strict value assertions are avoided (for example exact numbers) - flexible assertions instead
- Playwright auto-waiting instead of fixed sleeps
- Stable locators (role-based or attribute-based)


## 5. Validation Without API Access

In absence of backend/API validation:

- Treat UI as the source of truth
- Validation of correctness through:
  - user interactions (search/filter behavior)
  - visible state transitions
  - consistency across UI components
- Use heuristic checks (format, range, and structure validation)

## 6. Limitations

- Cannot validate raw backend data accuracy
- Limited visibility into data generation logic
- UI changes may introduce minor inconsistencies in real-time values

## 7. Conclusion

This approach ensures reliable validation of dashboard data by focusing on UI behavior, structural correctness, and relative consistency. It is suitable for dynamic, real-time systems where backend access is not available, and emphasizes stability over strict value matching.