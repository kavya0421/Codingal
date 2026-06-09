# Import necessary libraries
from tkinter import *

# Create window
window = Tk()
window.title("Length Converter")
window.geometry("300x200")

# Function to convert length
def convert_length(event):
    cm = float(entry.get())

    meter = cm / 100

    result_label.config(
        text=str(cm) + " cm = " + str(meter) + " m"
    )

# Heading
heading = Label(window, text="Length Converter")
heading.pack(pady=10)

# Input Label
label = Label(window, text="Enter Length in cm")
label.pack()

# Entry Box
entry = Entry(window)
entry.pack(pady=5)

# Convert Button
button = Button(window, text="Convert")
button.pack(pady=10)

# Bind button click event
button.bind("<Button-1>", convert_length)

# Result Label
result_label = Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()