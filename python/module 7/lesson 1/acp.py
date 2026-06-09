# Import necessary libraries
from tkinter import *

# Create Window
window = Tk()

# Set the window Title and Geometry
window.title('Product Details')
window.geometry('400x300')

# Create Labels
label1 = Label(window, text="Here is the Product")
label1.pack(pady=20)

label2 = Label(window, text="Product Name: Laptop")
label2.pack()

label3 = Label(window, text="Price: $500")
label3.pack()

# Start the GUI event loop
window.mainloop()