from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("500x500")

def btn_click():
    messagebox.showinfo("Messagebox Example","Hello Friends")

btn = Button(win,text="Click Me",command=btn_click).pack()

win.mainloop()