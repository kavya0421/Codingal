# Random Password Generator in Python

import random
import string

# Function to generate password
def generate_password():

    print("Welcome to the Random Password Generator!")

    # Ask user for password length
    length = int(input("Enter the password length: "))

    # Characters to be used in password
    lower_case = string.ascii_lowercase
    upper_case = string.ascii_uppercase
    numbers = string.digits

    all_characters = lower_case + upper_case + numbers

    password = ""

    # Generate password
    for i in range(length):
        password += random.choice(all_characters)

    # Shuffle the password
    password_list = list(password)
    random.shuffle(password_list)

    password = "".join(password_list)

    print("\nGenerated Password:", password)

    # Ask user if they want another password
    restart = input("\nGenerate another password? (y/n): ")

    if restart == "y" or restart == "Y":
        generate_password()
    else:
        print("Thank you for using the Password Generator!")

# Main Program
if __name__ == "__main__":
    generate_password()