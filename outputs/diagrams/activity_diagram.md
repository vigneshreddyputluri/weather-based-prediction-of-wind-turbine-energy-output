# Activity Diagram - Wind Energy Prediction Flow

```mermaid
flowchart TD
    START([Start]) --> A[Open Prediction Page]
    A --> B{Input Method}
    B -->|API| C[Enter City]
    B -->|Manual| D[Enter Parameters]
    C --> E[Fetch Weather Data]
    E --> F{Request Successful}
    F -->|No| A
    F -->|Yes| G[Extract Weather Values]
    D --> G
    G --> H[Validate Data]
    H --> I{Valid}
    I -->|No| A
    I -->|Yes| J[Preprocess Features]
    J --> K[Load Model]
    K --> L[Predict Output]
    L --> M[Show Result]
    M --> N{Predict Again}
    N -->|Yes| A
    N -->|No| FINISH([End])
```

## Prediction Flow Stages

| Stage | Activity | Status |
|-------|----------|--------|
| **Input** | User selects prediction method and provides data | 🔵 Initial |
| **Validation** | System validates input parameters and format | 🟡 Processing |
| **Preparation** | Features are normalized and scaled for ML model | 🟡 Processing |
| **Prediction** | Random Forest model generates energy output | 🔵 Critical |
| **Output** | Results formatted and displayed to user | 🟢 Final |
