"""
    This is a miles to kilometres converter GUI Application
"""
from tkinter import *

# Creating the window
window = Tk()
# Specifying the window title
window.title("Mile to Km Converter")
#Specify the window size
window.minsize(width=250, height=150)
# Add some padding to the sides
window.config(padx=20, pady=20)


# Now Create an Entry
my_entry = Entry(width=10)
my_entry.grid(column=2, row=1)


# Add a label to the end of the Entry
miles_label = Label(text="miles")
miles_label.grid(column=3, row=1)

# The labels for the km
km_label_1 = Label(text="is equal to")
km_label_1.grid(column=1, row=2)


km_label_2 = Label()
km_label_2.grid(column=2, row=2)

km_label_3 = Label(text="km")
km_label_3.grid(column=3, row=2)


# Creating a Button consuming a function
def miles_to_km_converter():
    km_equivalent = 1.60934 * float(my_entry.get())
    km_rounded = round(km_equivalent, 2)
    km_label_2["text"] = str(km_rounded)

# Add an event-listener to the button
calculate_button = Button(text="Convert", command=miles_to_km_converter)
calculate_button.grid(column=2, row=3)


# Sustain the window
window.mainloop()

