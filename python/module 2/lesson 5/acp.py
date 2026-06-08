# Take input from user
rows = int(input("Please Enter the total Number of Rows : "))

print("Mirrored Triangle")

# Outer loop for number of rows
for i in range(1, rows + 1):

    # Inner loop for spaces
    for j in range(rows - i):
        print(" ", end=" ")

    # Inner loop for stars
    for k in range(i):
        print("*", end=" ")

    print()