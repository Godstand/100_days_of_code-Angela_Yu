from tkinter import *


def miles_km():
    distance_miles = float(miles_entry.get())
    distance_km =   round(distance_miles * 1.60934)
    km_label_result.config(text=f"{distance_km}")
    # my_label.grid(column=1, row=2)


window = Tk()
window.title("Miles to KIlometers Converter Project")
window.minsize(width=300, height=200)
window.config(padx=50, pady=25)

miles_entry = Entry(width=5)
miles_entry.insert(END, string="0")
miles_entry.grid(column=1, row=1)

miles_label = Label(text="miles")
miles_label.grid(column=2, row=1)

is_equal_label = Label(text="equal to  ")
is_equal_label.grid(column=0, row=2)

km_label = Label(text="km")
km_label.grid(column=2, row=2)

km_label_result = Label(text="0")
km_label_result.grid(column=1, row=2)

calculate_button = Button(text="Calculate", command=miles_km)
calculate_button.grid(column=1, row=4)

window.mainloop()
