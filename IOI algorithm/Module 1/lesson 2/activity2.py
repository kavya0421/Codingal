print("==============================")
print("PYTHON OPERATORS DEMO")
print("==============================")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("\nArithmetic Operators")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
if num2 != 0:
	print("Division:", num1 / num2)
	print("Floor Division:", num1 // num2)
	print("Modulus:", num1 % num2)
else:
	print("Division:", "Not possible when the second number is 0")
	print("Floor Division:", "Not possible when the second number is 0")
	print("Modulus:", "Not possible when the second number is 0")
print("Exponent:", num1 ** num2)

print("\nComparison Operators")
print("num1 == num2:", num1 == num2)
print("num1 != num2:", num1 != num2)
print("num1 > num2:", num1 > num2)
print("num1 < num2:", num1 < num2)
print("num1 >= num2:", num1 >= num2)
print("num1 <= num2:", num1 <= num2)

print("\nAssignment Operators")
value = num1
print("Original value:", value)
value += num2
print("After +=", value)
value -= num2
print("After -=", value)
value *= num2
print("After *=", value)
