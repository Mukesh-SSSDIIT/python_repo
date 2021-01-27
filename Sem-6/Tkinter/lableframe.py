from tkinter import *

win = Tk()
win.title("Lable Frame Widget Example")
win.geometry("500x500")

lbl_frame = LabelFrame(win,
                        text="Personal Information",
                        padx=10,
                        pady=10)
lbl_frame.pack(padx=20,pady=20,fill=BOTH)

btn = Button(lbl_frame,text="Do not click me")
btn.pack()

win.mainloop()