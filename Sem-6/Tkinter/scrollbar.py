from tkinter import *

win = Tk()
win.title("Scrollbar Example")
win.geometry("500x500")

s_bar = Scrollbar(win)
s_bar.pack(side=RIGHT,fill=Y)

l_box = Listbox(win, yscrollcommand = s_bar.set)
for i in range(100):
    l_box.insert(END,"List item No. : " + str(i+1))
l_box.pack(side=RIGHT,fill=BOTH)

s_bar.config(command=l_box.yview)

win.mainloop()