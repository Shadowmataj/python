from tkinter import *

window = Tk()
window.title("Mile to kilometer converter")
window.config(padx=20, pady=20)

def button_clicked():

    miles = float(tk_input.get())
    km = miles * 1.609
    km_label.config(text=f"{round(km,2)}")

#Label

#ENTRY
tk_input = Entry(width=7, justify="center")
tk_input.grid(column = 1, row = 0)

km_label = Label(text= "0")
km_label.grid(column = 1, row = 1)

km_txt_label = Label(text="Km")
km_txt_label.grid(column = 2, row = 1)

txt_label = Label(text= "Is equal to:")
txt_label.grid(column = 0, row = 1)

miles_label = Label(text= "Miles")
miles_label.grid(column = 2, row = 0)

#BUTTON
button = Button(text="Calculate", command=button_clicked)
button.grid(column = 1, row = 2)



window.mainloop()

