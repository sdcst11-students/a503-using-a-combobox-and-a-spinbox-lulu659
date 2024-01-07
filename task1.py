"""
##### Task 1 Select birthdate.
Create an application that allows the user to select the month, day and year of their birthdate. You will need 3 separate entries: month,day, year.

You are responsible for designing your GUI.  You may use the pack, grid or place methods for doing so, but your GUI layout should be organized and visually appealing.

Display the results of their selection in an entry box in the widget.

Extra: Can you create some of the lists of values dynamically instead of explicitly listing them all?
"""
import tkinter
from tkinter import ttk
from tkinter import *

def button(event):
    print(event)
    output = f"{c1.get()}.{c2.get()}.{c3.get()}"
    a1.delete(0,tkinter.END)
    a1.insert(0, output)

win = tkinter.Tk()
win.attributes('-topmost',True)

l1 = tkinter.Label(win,text="Select  your birthday")
c1 = ttk.Combobox(win,values=list(range(1, 32)))
c1.set('Date')
c2 = ttk.Combobox(win,values=list(range(1, 13)))
c2.set('Month')
c3 = ttk.Combobox(win,values=list(range(2024, 1899, -1)))
c3.set('Year')

b1 = Button(win, text="Display")
a1 = Entry(win, width=20)

l1.pack()
c1.pack()
c2.pack()
c3.pack()
b1.pack()
a1.pack()


b1.bind("<Button>", button)

win.mainloop()