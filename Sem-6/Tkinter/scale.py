from tkinter import *
from tkinter import messagebox
win = Tk()
win.geometry("500x500")
win.title("Spin Box Example")

scalevar = DoubleVar()

def btn_click():
    messagebox.showinfo("Result",scalevar.get())

s = Scale(win,variable=scalevar,from_=-100,to=100,
            showvalue=1,
            resolution=0.2)
s.pack()

btn = Button(win,text="Click Me",command=btn_click)
btn.pack()

win.mainloop()