# using a try and except
try:
    age = int(input("Enter your age: "))
    print("Your age is", age)

# using value error
except ValueError as ex:
    print("Exception:", ex)