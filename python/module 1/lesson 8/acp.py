print("Enter First Number: ")
num1 = int(input())

print("Enter Second Number: ")
num2 = int(input())

print("\nBefore Swapping")
print("First Number =", num1)
print("Second Number =", num2)

# Swapping the numbers
temp = num1
num1 = num2
num2 = temp

print("\nAfter Swapping")
print("First Number =", num1)
print("Second Number =", num2)