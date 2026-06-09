# Import necessary packages
from tkinter import *

# Create Window
window = Tk()

window.title("Interest Calculator")
window.geometry("400x300")

# Function to calculate simple interest
def calculate_interest():

    principal = float(entry_principal.get())
    rate = float(entry_rate.get())
    time = float(entry_time.get())

    interest = (principal * rate * time) / 100

    result_label.config(
        text="Simple Interest = " + str(interest)
    )

# Heading
heading = Label(window, text="Interest Calculator")
heading.pack(pady=10)

# Principal Amount
label_principal = Label(window, text="Enter Principal Amount")
label_principal.pack()

entry_principal = Entry(window)
entry_principal.pack()

# Rate of Interest
label_rate = Label(window, text="Enter Rate (%)")
label_rate.pack()

entry_rate = Entry(window)
entry_rate.pack()

# Time
label_time = Label(window, text="Enter Time (Years)")
label_time.pack()

entry_time = Entry(window)
entry_time.pack()

# Calculate Button
btn_calculate = Button(
    window,
    text="Calculate Interest",
    command=calculate_interest
)

btn_calculate.pack(pady=10)

# Result Label
result_label = Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()