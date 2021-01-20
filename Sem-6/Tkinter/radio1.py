from tkinter import *

win = Tk()
win.title("Message Widget Example")
win.geometry("200x200")

r_radio = StringVar()

def radio_click():
    txt = r_radio.get()
    lbl = Label(win,text=txt)
    lbl.pack()

radio1 = Radiobutton(win,text="C Language",value=1,variable=r_radio,
                                                command=radio_click)
radio2 = Radiobutton(win,text="C++",value=2,variable=r_radio,
                                                command=radio_click)
radio3 = Radiobutton(win,text="Python",value=3,variable=r_radio,
                                                command=radio_click)

radio1.pack()
radio2.pack()
radio3.pack()
win.mainloop()