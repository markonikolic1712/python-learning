from tkinter import *

from main import button

window = Tk()
window.title("Mile to Kilometer Converter")
window.minsize(width=220, height=100)
window.config(padx=20, pady=20)

def convert_mile_to_km():
    print(input.get())
    try:
        miles = float(input.get())
        result.config(text=str(round(miles * 1.60934, 2)))
    except ValueError:
        print("Invalid input")

input = Entry(width=7)
input.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.grid(column=2, row=0)

is_equal_to_label = Label(text="is equal to", font=("Arial", 12))
is_equal_to_label.grid(column=0, row=1)

result = Label(text="0", font=("Arial", 12))
result.grid(column=1, row=1)

km = Label(text="Km", font=("Arial", 12))
km.grid(column=2, row=1)

button = Button(text="Calculate", command=convert_mile_to_km)
button.grid(column=1, row=2)








window.mainloop()