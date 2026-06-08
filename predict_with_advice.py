import joblib

def get_health_advice(pm25):

    if pm25 <= 50:
        return "Good Air Quality"

    elif pm25 <= 100:
        return "Moderate Air Quality"

    elif pm25 <= 150:
        return "Wear a Mask Outdoors"

    elif pm25 <= 250:
        return "Avoid Outdoor Exercise"

    else:
        return "Stay Indoors"

# Load Model
model = joblib.load("aqi_model.pkl")

sample_data = [[
    150,
    40,
    15,
    1.2,
    50,
    32,
    65,
    2.5
]]

prediction = model.predict(sample_data)

predicted_pm25 = prediction[0]

print("\nPredicted PM2.5:", round(predicted_pm25, 2))

print("Health Advice:", get_health_advice(predicted_pm25))