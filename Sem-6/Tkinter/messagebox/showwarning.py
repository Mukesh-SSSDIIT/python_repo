from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("200x200")
win.title("Show warning example")

messagebox.showwarning("warning","This is warning")

win.mainloop()