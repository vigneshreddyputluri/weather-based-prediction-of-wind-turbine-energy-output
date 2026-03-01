import pandas as pd
import joblib
import matplotlib.pyplot as plt
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error

# Load dataset
df = pd.read_csv("data/T1.csv")

# Clean column names (VERY IMPORTANT)
df.columns = df.columns.str.strip()

# Features and target
X = df[['WindSpeed(m/s)', 'Theoretical_Power_Curve (KWh)']]
y = df['LV ActivePower (kW)']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("R2 Score:", r2)
print("RMSE:", rmse)

# Save model
joblib.dump(model, "power_prediction.sav")

# Accuracy graph
plt.figure()
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Power (kW)")
plt.ylabel("Predicted Power (kW)")
plt.title("Actual vs Predicted Power")
plt.savefig("static/accuracy_graph.png")
plt.close()

print("✅ Model trained & accuracy graph saved")
