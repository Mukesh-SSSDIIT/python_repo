from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Ask yes No example")
win.geometry("200x200")

def btn_click():
    r = messagebox.askyesnocancel("Confirmation","Are you sure? Exit ?")
    if r == True:
        messagebox.showinfo("Info","Pressed Yes Button")
    elif r == False:
        messagebox.showinfo("Info","Pressed No Button")
    elif r == None:
        messagebox.showinfo("Info","Pressed Cancel button")

Button(win,text="Click Me",command=btn_click).pack()

win.mainloop()