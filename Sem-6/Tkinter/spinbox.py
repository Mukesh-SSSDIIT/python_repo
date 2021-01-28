from tkinter import *

win = Tk()
win.geometry("500x500")
win.title("Spin Box Example")

s_box = Spinbox(win,from_=11,to=20)
s_box.pack()

Entry(win).pack()
win.mainloop()