from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Ask yes No example")
win.geometry("200x200")

def btn_click():
    r = messagebox.askretrycancel("Confirmation","Are you sure? Exit ?")
    if r == True:
        messagebox.showinfo("Info","Pressed Retry button")
    else:
        messagebox.showinfo("Info","Pressed Cancel button")

Button(win,text="Click Me",command=btn_click).pack()

win.mainloop()