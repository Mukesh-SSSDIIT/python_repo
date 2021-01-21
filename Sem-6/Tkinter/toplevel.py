from tkinter import *

mainwin = Tk()
mainwin.geometry("500x500")

def btn1_click():
    topwin2 = Toplevel(topwin1)
    topwin2.geometry("100x100")
    Label(topwin2,"This is top window-2").pack()
    Button(topwin2,text="Exit",command=topwin2.destroy).pack()
    topwin2.grab_set()

def btn_click():
    topwin1 = Toplevel()
    topwin1.geometry("300x300")
    lbl1 = Label(topwin1,text = "This is top window-1")
    lbl1.pack()
    btn1 = Button(topwin1,text="Click Me",command=btn1_click)
    btn1.pack()
    # topwin1.grab_set()

lbl = Label(mainwin,text="This is main window")
lbl.pack()

btn = Button(mainwin,text="Show window",command=btn_click)
btn.pack()
mainwin.mainloop()