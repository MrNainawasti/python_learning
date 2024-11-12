from tkinter import *


def miles_to_km():
    km = float(entry.get()) * 1.609344
    answer = round(km, 4)
    label1.config(text= answer)



window = Tk()
window.title("Miles to Km converter")
window.config(padx=20, pady=20)

# label
label1 = Label(text= "0")
label1.config(padx= 20)
label1.place(x=80, y= 25)


label2 = Label(text="is equal to")
label2.grid(column=0, row=1)

label3 = Label(text="Miles")
label3.config(padx= 20)
label3.grid(column=3, row=0)

label4 = Label(text="Km")
label4.grid(column=3, row=1)


# button
button = Button(text="Calculate", command= miles_to_km)
button.grid(column=2, row=3)


# entry
entry = Entry(width= 10)
entry.grid(column=2, row= 0)


window.mainloop()