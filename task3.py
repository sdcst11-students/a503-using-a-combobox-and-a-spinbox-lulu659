#!python3

"""
##### Task 3 tKinter Compound Interest 
Create an application to calculate the final value of a compount interest value problem.  Recall that the final value can be calculated with:

A = P(1+r/n)^(n*t) where:
P = Principal (amount of the initial investment)
r = Interest rate as a decimal (4% has r = 0.04)
n = Number of compounding periods in a year (monthly n = 12, daily n=365)
t = number of years

You should decide which values should have regular entry widgets, comboboxes or spinboxes.  You will need a label or entry box to show your result.
"""
import tkinter
from tkinter import ttk
from tkinter import *

def rate(event):  
    print(event)  
    pr = float(p.get())
    rr = float(r.get())/100
    nr = float(n.get())
    tr = float(t.get())
    A = pr*(1+rr/nr)**(nr*tr)
    a.delete(0,tkinter.END)
    a.insert(0,f"The amount is {A}")
    
win = tkinter.Tk()
win.attributes('-topmost',True)

l1 = tkinter.Label(win,text="COMPOUND INTEREST")
l2 = tkinter.Label(win, text="principle")
p = tkinter.Entry(win, width=15)
l3 = tkinter.Label(win, text="interest rate")
r = tkinter.Entry(win, width=15)
n = ttk.Combobox(win, values=[12, 365])
n.set('compounding periods annually')
t = ttk.Combobox(win, values=list(range(1, 101)))
t.set("years")

b = Button(win, text = "result")
a = Entry(win, width=50)

l1.grid(row=1, column=1, columnspan=2, pady=5)
l2.grid(row=2, column=1, pady=5, sticky='e')
p.grid(row=2, column=2, pady=5, sticky='w')
l3.grid(row=3, column=1, pady=5, sticky='e')
r.grid(row=3, column=2, pady=5, sticky='w')
n.grid(row=4, column=1, columnspan=2, pady=5)
t.grid(row=5, column=1, columnspan=2, pady=5)
b.grid(row=6, column=1, columnspan=2, pady=5)
a.grid(row=7, column=1, columnspan=2, pady=5, padx=5)

b.bind("<Button>", rate)

win.mainloop()