from tkinter import *

window = Tk()

window.title("Miles to Km Converter")
window.minsize(width=400, height=300)
window.config(padx = 20, pady = 20)

entry = Entry()
entry.grid(row = 0, column = 1)

label1 = Label(text = "Miles")
label1.grid(row = 0, column = 2)

label2 = Label(text = "is equal to")
label2.grid(row = 1, column = 0)

label3 = Label(text = "")
label3.grid(row = 1, column = 1)

label4 = Label(text = "Km")
label4.grid(row = 1, column = 2)

def button_clicked():
    miles = float(entry.get())
    km = miles * 1.609
    km = int(km)
    label3.config(text = km)

button = Button(text = "Calculate", command = button_clicked)
button.grid(row = 2, column = 1)

window.mainloop()