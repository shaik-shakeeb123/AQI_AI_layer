import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# ===============================
# LOAD DATASET
# ===============================

df = pd.read_csv("C:\\Users\\hp\\Downloads\\data-1781009634141.csv")
print("Dataset Loaded Successfully")
print(df.head())
for col in ['pm25', 'pm10', 'no2', 'so2', 'co', 'o3', 'temperature', 'humidity', 'wind_speed', 'pressure']:
    df[col] = df[col].fillna(df[col].median())
def normalize_co(value):
    if value > 50:
        return value / 1000
    return value

df['co'] = df['co'].apply(normalize_co)
df.drop_duplicates(inplace=True)


# ===============================
# SELECT FEATURES
# ===============================

features = [
    "pm25",
    "pm10",
    "no2",
    "o3",
    "co",
    "so2",
    "temperature",
    "humidity",
    "wind_speed",
    "pressure"
]

target = "aqi"

# ===============================
# HANDLE MISSING VALUES
# ===============================

df = df[features + [target]]

df = df.fillna(df.mean(numeric_only=True))

# ===============================
# INPUTS AND OUTPUT
# ===============================

X = df[features]

y = df[target]

# ===============================
# SPLIT DATASET
# ===============================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# ===============================
# TRAIN MODEL
# ===============================

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

print("\nModel Trained Successfully")

# ===============================
# PREDICT
# ===============================

predictions = model.predict(X_test)
print("\nActual AQI vs Predicted AQI\n")

for actual, predicted in zip(y_test[:10], predictions[:10]):
    print(f"Actual AQI: {actual:.2f} | Predicted AQI: {predicted:.2f}")

# ===============================
# EVALUATION
# ===============================

mae = mean_absolute_error(y_test, predictions)

r2 = r2_score(y_test, predictions)

print("\nMean Absolute Error:", round(mae, 2))
print("R2 Score:", round(r2, 2))

# ===============================
# SAVE MODEL
# ===============================

joblib.dump(model, "aqi_model.pkl")

print("\nModel Saved Successfully")