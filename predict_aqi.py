import joblib
import pandas as pd

model = joblib.load("aqi_model.pkl")

pm25 = float(input("Enter PM2.5: "))
pm10 = float(input("Enter PM10: "))
no2 = float(input("Enter NO2: "))
o3 = float(input("Enter O3: "))
co = float(input("Enter CO: "))
so2 = float(input("Enter SO2: "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))
wind_speed = float(input("Enter Wind Speed: "))
pressure = float(input("Enter Pressure: "))

new_data = pd.DataFrame({
    "pm25": [pm25],
    "pm10": [pm10],
    "no2": [no2],
    "o3": [o3],
    "co": [co],
    "so2": [so2],
    "temperature": [temperature],
    "humidity": [humidity],
    "wind_speed": [wind_speed],
    "pressure": [pressure]
})

aqi = model.predict(new_data)

print("\nPredicted AQI:", round(aqi[0], 2))