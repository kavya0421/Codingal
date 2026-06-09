# Import necessary libraries
from tkinter import *

# Setting up Main Window
root = Tk()
root.geometry("400x300")
root.title("Password Strength Checker")

# Function to check password strength
def check_password():

    password = entry.get()

    # Setting up Top Window
    top = Toplevel()
    top.geometry("250x150")
    top.title("Result")

    if len(password) < 6:
        result = "Weak Password"

    elif len(password) < 10:
        result = "Medium Password"

    else:
        result = "Strong Password"

    # Display result
    label = Label(top, text=result)
    label.pack(pady=20)

# Heading
heading = Label(root, text="Password Strength Checker")
heading.pack(pady=10)

# Password Entry
label1 = Label(root, text="Enter Password")
label1.pack()

entry = Entry(root, show="*")
entry.pack(pady=5)

# Button
btn = Button(root,
             text="Check Strength",
             command=check_password)

btn.pack(pady=10)

# Start GUI
root.mainloop()