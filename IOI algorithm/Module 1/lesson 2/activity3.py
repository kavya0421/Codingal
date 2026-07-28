print("==============================")
print("PYTHON STRING OPERATIONS")
print("==============================")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")

full_name = first_name + " " + last_name
message = full_name + " lives in " + city + "."

print("\nOriginal Strings")
print("First Name:", first_name)
print("Last Name:", last_name)
print("City:", city)

print("\nString Operations")
print("Full Name:", full_name)
print("Message:", message)
print("Uppercase Name:", full_name.upper())
print("Lowercase City:", city.lower())
print("Title Case Name:", full_name.title())
print("Length of Full Name:", len(full_name))
print("First Letter of First Name:", first_name[0])
print("Last 3 Letters of City:", city[-3:])
print("Name with 'a' replaced by '@':", full_name.replace("a", "@"))
print("Does the city contain 'a'?", "a" in city.lower())
