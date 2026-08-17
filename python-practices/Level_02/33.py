# 33. Image Brightness Simulator
# Represent a grayscale image as a NumPy array.

# Allow
# - Increase brightness
# - Decrease brightness
# - Threshold

# Practice
# - array indexing
# - clipping values
# -------------------------------------------------
                              
import numpy as np


def increase_brightness(image, amount):
    bright_image = image + amount
                      
    bright_image = np.clip(bright_image, 0, 255)

    return bright_image

def decrease_brightness(image, amount):                              
    dark_image = image - amount

    dark_image = np.clip(dark_image, 0, 255)

    return dark_image
                             
def threshold_image(image, value):
    result = np.where(image >= value, 255, 0) 

    return result
                             
image = np.array([
    [50, 100, 150],
    [200, 180, 120],
    [30, 90, 255]
])

while True:

    print("\n--- Image Brightness Simulator ---")
    print("1. Show Image")
    print("2. Increase Brightness")
    print("3. Decrease Brightness")
    print("4. Apply Threshold")
    print("5. Exit")

    choice = int(input("Choose: ")) 

    if choice == 1:
        print(image)

    elif choice == 2:
        amount = int(input("Increase brightness by: "))
        print(increase_brightness(image, amount))

    elif choice == 3:
        amount = int(input("Decrease brightness by: "))
        print(decrease_brightness(image, amount))

    elif choice == 4:
        value = int(input("Threshold value: "))
        print(threshold_image(image, value))

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")    

