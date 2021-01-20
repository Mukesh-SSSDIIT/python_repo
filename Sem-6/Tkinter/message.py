from tkinter import *



win = Tk()
win.title("Message Widget Example")
win.geometry("200x200")

msg = Message(win,text="This is message widget",width=300,bg="blue",
                                                        fg="yellow")
msg.pack()

win.mainloop()