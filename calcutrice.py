from tkinter import *
import tkinter as tk
from tkinter import StringVar
import tkinter.messagebox
from tkinter.constants import SUNKEN
from math import sqrt


def calculate():
    try:
        expression = entry_input.get()
        result = eval(expression)
        entry_input.set(result)
    except Exception as e:
        tk.messagebox.showinfo("Error", str(e))


def clear_input():
    entry_input.set('')


# Create the main window
window = tk.Tk()
window.config( background="#161b22")
window.title('calculator')

# StringVar for the entry widget
entry_input = StringVar()

# Entry widget for input and output
entry = tk.Entry(window, relief=SUNKEN, borderwidth=3, textvariable=entry_input, width=26,
                 justify='left', border=2, font=('Comic Sans', 13, 'bold'), )

# Buttons for digits and operators
buttons = [
    'C', '^', 'sqrt', '%',
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]


# Function to handle button clicks
def button_click(value):
    if value == '=':
        if entry_input.get() =='':
            entry_input.set("the input is emty")
        calculate()
    elif value == 'C':
        clear_input()
    elif value == '^':
        if entry_input.get() =='':
            entry_input.set("the input is emty")
        current_input = entry_input.get()
        entry_input.set(current_input + '^')
    elif value == 'sqrt':
        if entry_input.get() =='':
            entry_input.set("the input is emty")
        current_input = float(entry_input.get())
        sqrt_val = sqrt(current_input)
        entry_input.set(value= sqrt_val)
    elif value == '%':
        if entry_input.get() =='':
            entry_input.set("the input is emty")
        current_input = entry_input.get()
        entry_input.set(current_input + '%')
    else:
        current_input = entry_input.get()
        entry_input.set(current_input + value)



# Create buttons and add them to the grid
row_val = 1
col_val = 0
for button in buttons:
    tk.Button(window, foreground="white", border=0, bg="#0d1117", text=button, bd=0, cursor="hand2", command=lambda b=button: button_click(b),
              padx=15, pady=5, width=3).grid(row=row_val, column=col_val, padx=5, pady=5)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1


# Layout for the entry widget
entry.grid(row=0, column=0, columnspan=8, padx=10, ipady=4, pady=20, sticky="e")

# Run the Tkinter event loop
window.mainloop()