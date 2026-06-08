import pandas as pd

# Load dataset
df = pd.read_csv("C:\\Users\\hp\Downloads\\Raw_data_1Day_2025_site_1421_Dr._Karni_Singh_Shooting_Range_Delhi_DPCC_1Day.csv")

print(df.head())
print(df.info())
selected_columns = [
    'PM2.5 (µg/m³)',
    'PM10 (µg/m³)',
    'NO2 (µg/m³)',
    'SO2 (µg/m³)',
    'CO (mg/m³)',
    'Ozone (µg/m³)',
    'AT (°C)',
    'RH (%)',
    'WS (m/s)'
]
df = df[selected_columns]
print(df.head())
df = df.fillna(df.mean(numeric_only=True))
print(df.isnull().sum())
X = df[
[
    'PM10 (µg/m³)',
    'NO2 (µg/m³)',
    'SO2 (µg/m³)',
    'CO (mg/m³)',
    'Ozone (µg/m³)',
    'AT (°C)',
    'RH (%)',
    'WS (m/s)'
]
]
y = df['PM2.5 (µg/m³)']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
print("Training Records:", len(X_train))
print("Testing Records:", len(X_test))
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
model.fit(X_train, y_train)
print("Model Trained Successfully")
from sklearn.metrics import mean_absolute_error, r2_score

predictions = model.predict(X_test)

mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("Mean Absolute Error:", mae)

print("R2 Score:", r2)
import joblib

joblib.dump(model, "aqi_model.pkl")

print("Model Saved")