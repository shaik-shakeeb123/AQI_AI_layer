def safe_window(aqi, temperature, humidity):

    if aqi <= 50 and temperature <= 35 and humidity <= 70:

        return {
            "status": "SAFE",
            "children":
                "Children can play outdoors from 6 AM - 9 AM and 5 PM - 7 PM",

            "senior_citizens":
                "Safe for morning and evening walks",

            "general_public":
                "All outdoor activities are safe"
        }

    elif aqi <= 100:

        return {
            "status": "MODERATE",
            "children":
                "Outdoor play allowed between 6 AM - 8 AM",

            "senior_citizens":
                "Short walks only",

            "general_public":
                "Normal activities with caution"
        }

    elif aqi <= 200:

        return {
            "status": "UNHEALTHY FOR SENSITIVE GROUPS",
            "children":
                "Avoid prolonged outdoor play",

            "senior_citizens":
                "Stay indoors if possible",

            "general_public":
                "Wear masks outdoors"
        }

    elif aqi <= 300:

        return {
            "status": "VERY POOR",
            "children":
                "No outdoor play",

            "senior_citizens":
                "Avoid going outside",

            "general_public":
                "Avoid outdoor exercise"
        }

    else:

        return {
            "status": "SEVERE",
            "children":
                "Keep children indoors",

            "senior_citizens":
                "Remain indoors and use air purification",

            "general_public":
                "Avoid all outdoor activities"
        }


aqi = float(input("Enter AQI: "))
temperature = float(input("Enter Temperature: "))
humidity = float(input("Enter Humidity: "))

result = safe_window(aqi, temperature, humidity)

print("\n===== SAFE WINDOW REPORT =====")

print("Status:", result["status"])

print("\n👶 Children:")
print(result["children"])

print("\n👴 Senior Citizens:")
print(result["senior_citizens"])

print("\n🏃 General Public:")
print(result["general_public"])