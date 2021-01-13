from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Messagebox Example")
win.geometry("200x200")

def btn_click():
    messagebox.showerror("Error messge","This is error message")

btn = Button(win,text="Click me",command=btn_click).pack()

win.mainloop()