from tkinter import *
from tkinter import messagebox

window = Tk();
window.title("Entry Widget Example")
window.geometry("500x500")

tv1 = StringVar();
tv2 = StringVar();

def btn_click():
     msg = messagebox.showinfo( "Entry Widget Example", "Hello " + tv1.get() + " " + tv2.get())

lbl1 = Label(window,text="First Name")
txt1 = Entry(window,textvariable=tv1)
lbl2 = Label(window,text="Last Name")
txt2 = Entry(window,textvariable=tv2)
btn = Button(window,command=btn_click, text="Click Me")

lbl1.grid(row=0,column=0)
txt1.grid(row=0,column=1)
lbl2.grid(row=1,column=0)
txt2.grid(row=1,column=1)
btn.grid(row=2,column=1)

window.mainloop()