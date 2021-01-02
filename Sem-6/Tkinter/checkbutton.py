import tkinter as tk
from tkinter import *
from tkinter import Checkbutton
from tkinter import Button
from tkinter import messagebox
from tkinter import Label

tw = tk.Tk()

def cb_bca_click():
    msg = messagebox.showinfo("Welcome to python", "BCA Check Button status changed")

def cb_bscit_click():
    msg = messagebox.showinfo("Welcome to python", "B.Sc.IT Check Button status changed")

def cb_pgdca_click():
    msg = messagebox.showinfo("Welcome to python", "PGDCA Check Button status changed")

def btn_click():
    m = ""
    if var1.get() == 1:
        m += "BCA is checked"
    else:
        m += "BCA is unchecked"
    if var2.get() == 1:
        m += "\nBscit is checked"
    else:
        m += "\nBscit is unchecked"
    if var3.get() == 1:
        m += "\nPGDCA is checked"
    else:
        m += "\nPGDCA is unchecked"
    msg = messagebox.showinfo("Welcome to python", m)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

cb_bca = Checkbutton(tw,text="BCA",command=cb_bca_click,variable=var1, onvalue = 1, offvalue = 0)
cb_bscit = Checkbutton(tw,text="B.Sc.IT",command=cb_bscit_click,variable=var2, onvalue = 1, offvalue = 0)
cb_pgdca = Checkbutton(tw,text="PGDCA",command=cb_pgdca_click,variable=var3, onvalue = 1, offvalue = 0 )

btn1 = Button(tw,text="Click Me",command=btn_click)

lbl1 = Label(tw,text="Checkbox for BCA")
lbl2 = Label(tw,text="Checkbox for B.Sc.IT")
lbl3 = Label(tw,text="Checkbox for PGDCA")
lbl4 = Label(tw,text="Show")


# cb_bca.place(x=50,y=50)
# cb_bscit.place(x=50,y=75)
# cb_pgdca.place(x=50,y=100)
# btn1.place(x=50,y=150)

# cb_bca.pack()
# cb_bscit.pack()
# cb_pgdca.pack()
# btn1.pack()

lbl1.grid(row=0,column=0)
lbl2.grid(row=0,column=1)
lbl3.grid(row=0,column=2)
lbl4.grid(row=0,column=3)


cb_bca.grid(row=1,column=0)
cb_bscit.grid(row=1,column=1)
cb_pgdca.grid(row=1,column=2)
btn1.grid(row=1,column=3)

tw.mainloop()


# x = StringVar() # Holds a string; default value ""
# x = IntVar() # Holds an integer; default value 0
# x = DoubleVar() # Holds a float; default value 0.0
# x = BooleanVar() # Holds a boolean, returns 0 for False and 1 for True

