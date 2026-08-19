import math

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

if a == 0 or b == 0:
    lcm = 0
else:
    lcm = abs(a * b) // math.gcd(a, b)

print("LCM =", lcm)