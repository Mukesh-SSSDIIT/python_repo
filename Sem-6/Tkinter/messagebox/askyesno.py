from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Ask yes No example")
win.geometry("200x200")

def btn_click():
    r = messagebox.askyesno("Confirmation","Are you sure? Exit ?")
    if r == True:
        win.destroy()
    else:
        messagebox.showinfo("Info","You chhose not to exit")

Button(win,text="Click Me",command=btn_click).pack()

win.mainloop()