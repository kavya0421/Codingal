import math  # importing module

# Take input from user
angle = int(input("Enter an angle in degrees: "))

# Calculate trigonometric values
sine = math.sin(math.radians(angle))
cosine = math.cos(math.radians(angle))
tangent = math.tan(math.radians(angle))

# Display the result
print("Sin value =", sine)
print("Cos value =", cosine)
print("Tan value =", tangent)