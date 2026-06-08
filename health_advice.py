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

if __name__ == "__main__":

    pm25 = float(input("Enter PM2.5 Value: "))

    print(get_health_advice(pm25))