from tkinter import *
from tkinter import messagebox

win = Tk()
win.title("Lable Frame Widget Example")
win.geometry("500x500")

def btn_cleartext():
    txt.delete(2.5,3.7)
    # txt.delete(1.0,END)
    # txt.delete(2.5,END)

def btn_gettext():
    t = txt.get(1.0,END);
    messagebox.showinfo("Title",t)

txt = Text(win,height=10,width=50)
txt.pack()

btnclear =  Button(win,text="Clear Text",command=btn_cleartext)
btnclear.pack()

btngettext = Button(win,text="Get Text",command=btn_gettext)
btngettext.pack()

win.mainloop()