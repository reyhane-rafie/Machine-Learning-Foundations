# 20. Drought Warning Tool
# Input:
# Rainfall
# Temperature

# Output:
# Low Risk
# Medium Risk
# High Risk
# =====================

def drought_warning(rainfall, temperature):
    if rainfall < 50 and temperature > 35:
        return "High Risk"
    
    elif rainfall < 100 or temperature > 30:
        return "Medium Risk"
    
    else:
        return "Low Risk"
while True:     
    rainfall = input("Enter rainfall (mm) or type exit: ")

    if rainfall == "exit":
        break

    rainfall = float(rainfall)    
    
    temperature = float(input("Enter temperature (°C): "))

    print("Drought Status:", drought_warning(rainfall, temperature))