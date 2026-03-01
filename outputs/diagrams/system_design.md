# System Design Diagram

```mermaid
flowchart TB
    subgraph CLIENT[Client Layer]
        BROWSER[Web Browser]
        PAGES[HTML Pages]
    end
    subgraph APP[Application Layer]
        FLASK[Flask App]
        ROUTES[Routes]
        TPL[Template Engine]
    end
    subgraph LOGIC[Business Logic]
        VALID[Input Validation]
        PREP[Preprocessing]
        ENGINE[Prediction Engine]
    end
    subgraph DATA[Data and Model]
        MODEL[Random Forest Model]
        STORE[Model and CSV Storage]
    end
    subgraph EXT[External]
        WEATHER[OpenWeatherMap API]
    end

    BROWSER --> FLASK
    PAGES --> BROWSER
    FLASK --> ROUTES
    FLASK --> TPL
    ROUTES --> VALID
    VALID --> PREP
    PREP --> ENGINE
    ENGINE --> MODEL
    STORE --> MODEL
    VALID --> WEATHER
```

## System Components Architecture

### Client Layer
| Component | Role |
|-----------|------|
| **Web Browser** | User interface rendering |
| **HTML Templates** | UI structure and forms |
| **CSS Stylesheets** | Visual styling and responsiveness |
| **JavaScript** | Dynamic interactions and validations |

### Application Layer
| Component | Role |
|-----------|------|
| **Flask App** | Request handling and routing |
| **Route Handlers** | URL routing logic |
| **Jinja2 Engine** | Dynamic template rendering |

### Business Logic Layer
| Component | Role |
|-----------|------|
| **Validation** | Input verification and sanitization |
| **Preprocessing** | Feature normalization and scaling |
| **Prediction Engine** | ML model inference |

### Data & Model Layer
| Component | Role |
|-----------|------|
| **ML Model** | Random Forest Regression engine |
| **Feature Scaler** | StandardScaler for normalization |
| **Joblib** | Model serialization/deserialization |

### Storage Layer
| Component | Role |
|-----------|------|
| **CSV Database** | Historical training data |
| **Model Store** | Serialized model files |
