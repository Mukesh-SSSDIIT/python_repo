import tkinter as tk
from tkinter import *
from tkinter import Checkbutton
from tkinter import Button
from tkinter import messagebox

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
    if var2.get() == 1:
        m += "\nBscit is checked"
    if var3.get() == 1:
        m += "\nPGDCA is checked"
    msg = messagebox.showinfo("Welcome to python", m)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

cb_bca = Checkbutton(tw,text="BCA",command=cb_bca_click,variable=var1, onvalue = 1, offvalue = 0)
cb_bscit = Checkbutton(tw,text="B.Sc.IT",command=cb_bscit_click,variable=var2, onvalue = 1, offvalue = 0)
cb_pgdca = Checkbutton(tw,text="PGDCA",command=cb_pgdca_click,variable=var3, onvalue = 1, offvalue = 0 )

btn1 = Button(tw,text="Click Me",command=btn_click)

cb_bca.place(x=50,y=50)
cb_bscit.place(x=50,y=75)
cb_pgdca.place(x=50,y=100)
btn1.place(x=50,y=150)

tw.mainloop()

