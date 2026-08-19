
binary = input("Enter a binary number: ")

if all(digit in "01" for digit in binary):
    decimal = int(binary, 2)
    print("Decimal value:", decimal)
else:
    print("Invalid binary number")
