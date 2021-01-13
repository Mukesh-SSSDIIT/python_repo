from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Ask yes No example")
win.geometry("200x200")

def btn_click():
    r = messagebox.askquestion("Confirmation","Are you sure? Exit ?",icon="warning")
    if r == "yes":
        messagebox.showinfo("Info",r)
    elif r == "no":
        messagebox.showinfo("Info","Pressed No button")

Button(win,text="Click Me",command=btn_click).pack()

win.mainloop()


# Error
# Info
# Warning
# Question