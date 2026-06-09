def get_health_advice(aqi):

    if aqi <= 50:
        return [
            "Air quality is excellent.",
            "Outdoor activities are safe.",
            "Children can play outside."
        ]

    elif aqi <= 100:
        return [
            "Air quality is acceptable.",
            "Outdoor activities are generally safe."
        ]

    elif aqi <= 200:
        return [
            "Sensitive groups should reduce outdoor exposure.",
            "Children should avoid prolonged outdoor play.",
            "Asthma patients should carry inhalers."
        ]

    elif aqi <= 300:
        return [
            "Wear an N95 mask outdoors.",
            "Reduce outdoor exercise.",
            "Keep windows closed during peak pollution."
        ]

    elif aqi <= 400:
        return [
            "Avoid outdoor activities.",
            "Use air purifiers if available.",
            "Keep children and elderly indoors."
        ]

    else:
        return [
            "Stay indoors.",
            "Avoid all outdoor activities.",
            "Use masks and air purifiers.",
            "Follow emergency health precautions."
        ]

aqi = float(input("Enter AQI: "))

advice = get_health_advice(aqi)

print("\n===== HEALTH ADVISORY =====")

for item in advice:
    print("•", item)