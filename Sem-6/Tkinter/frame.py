from tkinter import *

win = Tk()
win.geometry("500x500")

topframe = Frame(win,bg="green",bd=2,height=50,width=500,cursor="plus")
bottomframe = Frame(win,bg="red",bd=2,height=50,width=500,cursor="circle")
leftframe = Frame(win,bg="blue",bd=2,height=500,width=100)
rightframe = Frame(win,bg="yellow",bd=2,height=500,width=400)
topframe.pack(side=TOP)
bottomframe.pack(side=BOTTOM)
leftframe.pack(side=LEFT)
rightframe.pack(side=RIGHT)

Label(topframe,text="This is my frame example",font="Arial").pack()
Label(bottomframe,text="About us : Program created by BCA Students").pack()
Label(leftframe,text = "Home").pack();
Label(leftframe,text="Inventory").pack(side=TOP);
Label(leftframe,text="Stock").pack(side=TOP);

win.mainloop()