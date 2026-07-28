# 18. Water Quality Classifier
# Input:
# pH
# Turbidity

# Output
# Good
# Moderate
# Poor

# Use simple rules.
# ===============

def classify_water(ph, turbidity):
    if 6.5 <= ph <= 8.5 and turbidity < 5:
        return "Good"

    elif 6 <= ph <= 9 and turbidity < 10:
        return "Moderate"
    
    else:
        return "Poor"
    
ph = float(input("Enter pH: "))
turbidity = float(input("Enter Turbidity (NTU): "))

print("Water Quality:", classify_water(ph, turbidity))