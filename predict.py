import joblib

model = joblib.load("aqi_model.pkl")

sample_data = [[
    150,     # PM10
    50,      # NO2
    15,      # SO2
    1.5,     # CO
    40,      # Ozone
    32,      # Temperature
    65,      # Humidity
    2.0      # Wind Speed
]]

prediction = model.predict(sample_data)

print("Predicted PM2.5:", prediction[0])