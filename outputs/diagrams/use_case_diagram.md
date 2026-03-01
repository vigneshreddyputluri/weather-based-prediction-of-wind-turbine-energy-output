# Use Case Diagram

```mermaid
flowchart LR
    OP[Wind Farm Operator] --> UC1[Predict Energy Output]
    OP --> UC2[Fetch Weather Data]
    OP --> UC3[Manual Input]
    OP --> UC4[View Prediction Result]

    GO[Grid Operator] --> UC1
    GO --> UC4
    GO --> UC5[View Historical Data]

    EM[Energy Manager] --> UC1
    EM --> UC3
    EM --> UC4

    SA[System Admin] --> UC6[Train Model]
```

## Use Case Scenarios

### 1. **Wind Farm Operator**
- Predict daily energy output for turbine maintenance planning
- Fetch real-time weather data automatically
- Manually input weather parameters for offline predictions
- View prediction results for scheduling purposes

### 2. **Grid Operator**
- Predict aggregate wind energy production
- Balance renewable and conventional energy sources
- Monitor historical production patterns
- Plan grid load distribution

### 3. **Energy Manager**
- Forecast energy availability for pricing decisions
- Input specific weather scenarios
- Compare predictions with actual output
- Optimize energy distribution strategy

### 4. **System Administrator**
- Train and retrain ML models with new data
- Maintain API integration
- Monitor system performance
- Manage database and backups
