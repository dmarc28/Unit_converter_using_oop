
from tkinter import *
from tkinter import IntVar
from tkinter.ttk import Combobox
from convert_class import Convert
from lenght_dict import len_units
from volume_dict import vol_units

window = Tk()
window.title("Miles to Kms Converter")
window.minsize(600, 225)
window.config(padx=15, pady=25)

# Entry

user_entry = Entry(width=10)
user_entry.insert(END, string=f'{0}')
user_entry.grid(row=0, column=1)
user_entry.get()
user_entry.focus()

# Text
label_to = Label(text="Unit", font=("Arial", "12", "bold"))
label_to.grid(row=1, column=3)
label_to.config(padx=25)

label_conversion = Label(text="is equal to", font=("Arial", "12", "bold"))
label_conversion.grid(row=1, column=0)
label_conversion.config(padx=15, pady=10)

label_converted = Label(text="0", width=15, font=("Arial", "12", "bold"))
label_converted.grid(row=1, column=1)
label_converted.config(padx=40, pady=10)

# Button Calculate

volume_list = (vol_units[0].keys())
lenght_list = (len_units[0].keys())
temperature_list = ["celsius", "fahrenheit", "kelvin"]

convert_units = Convert()


def function_1_list():
    radio_value = radio_state.get()
    if radio_value == 1:
        return lenght_list
    elif radio_value == 2:
        return volume_list
    else:
        return temperature_list


def get_result():
    result_1 = function_1_list()
    input_value = user_entry.get()
    unit_from = from_unit.get()
    unit_to = to_unit.get()

    if radio_state.get() == 1:
        return convert_units.convert_length(unit_from, unit_to, input_value)
    elif radio_state.get() == 2:
        return convert_units.convert_volume(unit_from, unit_to, input_value)
    else:
        return convert_units.convert_temperature(unit_from, unit_to, input_value)



radio_state = IntVar()
button_length = Radiobutton(text="length", variable=radio_state, value=1, command=get_result)
button_volume = Radiobutton(text="Volume", variable=radio_state, value=2, command=get_result)
button_temp = Radiobutton(text="Temperature", variable=radio_state, value=3, command=get_result)
button_volume.grid(row=0, column=3)
button_temp.grid(row=1, column=3)
button_length.grid(row=2, column=3)


from_unit = Combobox(values=function_1_list(), width=15)
# from_unit.bind("<<ComboboxSelected>>", change_from_label)
from_unit.current(0)
from_unit.grid(row=6, column=0)
unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
unit_label_hide.grid(row=4, column=0)
unit_label_from = Label(text="From", font=("Arial", "12", "bold"))
unit_label_from.grid(row=5, column=0)
unit_label_from.config(padx=1, pady=1)

# To

to_unit = Combobox(values=function_1_list(), width=15)
to_unit.current(0)
to_unit.grid(row=6, column=3)
# from_unit.bind("<<ComboboxSelected>>", change_to_label)
to_unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
to_unit_label_hide.grid(row=4, column=3)
to_unit_label = Label(text="To", font=("Arial", "12", "bold"))
to_unit_label.grid(row=5, column=3)
to_unit_label.config(padx=1, pady=1)

input_value = user_entry.get()
unit_from = from_unit.get()
unit_to = to_unit.get()


from_unit = Combobox(values=function_1_list(), width=15)
# from_unit.bind("<<ComboboxSelected>>", change_from_label)
from_unit.current(0)
from_unit.grid(row=6, column=0)
unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
unit_label_hide.grid(row=4, column=0)
unit_label_from = Label(text="From", font=("Arial", "12", "bold"))
unit_label_from.grid(row=5, column=0)
unit_label_from.config(padx=1, pady=1)

# To

to_unit = Combobox(values=function_1_list(), width=15)
to_unit.current(0)
to_unit.grid(row=6, column=3)
# from_unit.bind("<<ComboboxSelected>>", change_to_label)
to_unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
to_unit_label_hide.grid(row=4, column=3)
to_unit_label = Label(text="To", font=("Arial", "12", "bold"))
to_unit_label.grid(row=5, column=3)
to_unit_label.config(padx=1, pady=1)

button = Button(text="Calculate", command=get_result)
button.grid(row=2, column=1)
button_hide = Button(text="Calculate")
button_hide.grid(row=2, column=1)

# radio_state.set(1)


# from_unit.bind("<<ComboboxSelected>>", change_from_label)
#
unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
unit_label_hide.grid(row=4, column=0)
unit_label_hide.config(padx=35, pady=1)

to_unit_label_hide = Label(text="", font=("Arial", "12", "bold"))
to_unit_label_hide.grid(row=4, column=3)
to_unit_label_hide.config(padx=35, pady=1)

button = Button(text="Calculate", command=get_result)
button.grid(row=2, column=1)

window.mainloop()
