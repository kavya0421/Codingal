print("==============================")
print("NUMBER SWAP PROGRAM")
print("==============================")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print("\nBefore Swapping:")
print("First Number:", first_number)
print("Second Number:", second_number)

first_number, second_number = second_number, first_number

print("\nAfter Swapping:")
print("First Number:", first_number)
print("Second Number:", second_number)
