from tkinter import *

def button_clicked():
    # my_label.config(text="Button Got Clicked")
    my_label.config(text=input.get())

# kreira se window tako sto se inicijalizuje objekat klase Tk i dobijamo prozor
# Tk klasa je predefinisana u tkinter modulu
window = Tk()
window.title("Mt Firsy GUI program")
# korisnik moze da povecava i smanjuje prozor ali je potrebno da setujemo minimalnu velicinu
window.minsize(width=500, height=300)
# dodavanje paddinga u prozoru
window.config(padx=20, pady=20)

# Label - za kreiranje label-a koristi se klasa Label iz tkinter modula
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
# sa pack() dodaje label u prozor - pakuje ga u prozor
# promena teksta sa config()
my_label.config(text="New Text")
my_label.grid(column=0, row=0)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)

button = Button(text="New Button", command=button_clicked)
button.grid(column=2, row=0)

# Entry komponenta je input polje
input = Entry(width=20)
input.grid(column=3, row=2)

# kada se inicijalizuje objekat Tk on prolazi dalje kroz kod i proverava da li ima nekih instrukcija. Ako nema prozor ce se sam zatvoriti. Da se to ne bi dogodilo poziva se metoda mainloop().
# u mainloop() je while petlja koja se stalno vrti i u kojoj s epoziva listener metoda koja prati da li ima nekih promena u prozoru. Ova petlja bi bila: while True: listening()
# window.mainloop() se poziva na kraju koda
window.mainloop()
