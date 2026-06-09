# Import necessary libraries
from tkinter import *

# Function to calculate age
def calculate_age():
    birth_year = int(entry.get())
    current_year = 2026

    age = current_year - birth_year

    result_label.config(text="Your Age is: " + str(age))

# Create Window
root = Tk()

root.title('Age Calculator')
root.geometry('300x200')

# Heading
heading = Label(root, text="Age Calculator")
heading.pack(pady=10)

# Input Label
label = Label(root, text="Enter Birth Year")
label.pack()

# Input Box
entry = Entry(root)
entry.pack(pady=5)

# Button
button = Button(root,
                text="Calculate Age",
                command=calculate_age)

button.pack(pady=10)

# Result Label
result_label = Label(root, text="")
result_label.pack()

# Start the GUI event loop
root.mainloop()