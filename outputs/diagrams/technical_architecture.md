# Technical Architecture Diagram

```mermaid
flowchart TB
    subgraph UI_LAYER[User Interface Layer]
        UI[Web UI]
    end
    subgraph BACKEND[Flask Backend]
        ROUTE[Route Handler]
        API[Weather API Integration]
        PROCESS[Data Processing]
    end
    subgraph ML_LAYER[Machine Learning]
        MODEL[Random Forest Model]
        FEAT[Feature Engineering]
    end
    subgraph DATA_LAYER[Data Layer]
        CSV[T1.csv]
        MODEL_FILE[power_prediction.sav]
    end

    UI --> ROUTE
    ROUTE --> API
    API --> PROCESS
    PROCESS --> MODEL
    CSV --> FEAT
    FEAT --> MODEL
    MODEL_FILE --> ROUTE
    MODEL --> ROUTE
    ROUTE --> UI
```

## Architecture Components

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Frontend** | HTML5, CSS3, JavaScript | User interface for data input & result display |
| **Backend** | Flask, Python | Route handling, API integration, data processing |
| **ML Engine** | Scikit-learn, Joblib | Model training, prediction, serialization |
| **Data Processing** | NumPy, Pandas, SciPy | Feature engineering, normalization |
| **External APIs** | OpenWeatherMap | Real-time weather data retrieval |
| **Data Storage** | CSV, Joblib | Historical data & trained model persistence |
