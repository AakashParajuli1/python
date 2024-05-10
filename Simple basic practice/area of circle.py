#  Area of circle
import math
radius = float(input("Enter radius of the circle : "))
Area = math.pi * pow(radius, 2)
print(f"Area of circle is : {round(Area, 2)} cm^2")

# If statements in python:

age = int(input("Enter your age : "))
if age < 0:
    print("You haven't been born yet! ")
elif age > 120:
    print("You are already dead!")
elif age >= 18:
    print("You are eligible! ")
else:
    print("You are not eligible!")