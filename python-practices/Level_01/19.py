# 19. NDVI Interpreter
# Input NDVI

# Example:
# 0.75
# Output:
# Dense vegetation

# Rules:
# <0 Water
# 0-0.2 Bare soil
# 0.2-0.5 Grass
# >0.5 Forest
# ===================

def classify_ndvi(ndvi):
    if ndvi < 0:
        return "Water"
    
    elif 0 <= ndvi <= 0.2:
        return "Bare soil"
    
    elif 0.2 < ndvi <= 0.5:
        return "Grass"
    
    else:
        return "Forest"
    
ndvi = float(input("Enter NDVI value: "))    

print("Land Cover:", classify_ndvi(ndvi))