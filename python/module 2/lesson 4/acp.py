# Take input of a number
number = int(input("Please enter a number : "))

# Convert the number to binary
binary = bin(number)[2:]

# Display the result
print("The Binary Value of", number, "=", binary)