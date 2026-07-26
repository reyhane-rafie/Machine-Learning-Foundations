# 17. Weather Station
# Input:
# Temperature
# Humidity
# Wind speed

# Output"
# Hot day?
# Comfortable?
# Windy?
# =================
def hot_day(temperature):
    return temperature > 30


def comfortable(temperature, humidity):
    return 20 <= temperature <= 25 and humidity < 60


def windy(wind_speed):
    return wind_speed > 20


temperature = float(input("Enter temperature (°C): "))
humidity = float(input("Enter humidity (%): "))
wind_speed = float(input("Enter wind speed (km/h): "))

print("Hot Day:", hot_day(temperature))
print("Comfortable:", comfortable(temperature, humidity))
print("Windy:", windy(wind_speed))

# ======================
# Bonus Improvement   
# print("\nWeather Report")

# if hot_day(temperature):
#     print("✓ Hot Day")
# else:
#     print("✗ Not a Hot Day")

# if comfortable(temperature, humidity):
#     print("✓ Comfortable Weather")
# else:
#     print("✗ Not Comfortable")

# if windy(wind_speed):
#     print("✓ Windy")
# else:
#     print("✗ Not Windy")
# =======================