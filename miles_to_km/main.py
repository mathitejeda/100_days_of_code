from tkinter import *

window = Tk()
window.title("Miles to km converter")
window.minsize()
window.config(padx=20, pady=20)

def convert_units():
    result = float(entry_box.get()) * 1.609
    result_label.config(text = result)

# Labels

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="Equal to: ")
equal_label.grid(column=0, row=1)

result_label = Label()
result_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)

# button

convert_button = Button(text="calculate",command = convert_units)
convert_button.grid(column=1, row=2)

# entry

entry_box = Entry(width = 5)
entry_box.focus()
entry_box.grid(column=1, row=0)

window.mainloop()
