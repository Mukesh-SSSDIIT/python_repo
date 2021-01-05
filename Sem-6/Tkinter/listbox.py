from tkinter import *
from tkinter import messagebox
w = Tk();

def btn_click():
    curindex = lb.curselection()
    for i in curindex:
        msg = messagebox.showinfo( "Entry Widget Example", lb.get(i))
    
lb = Listbox(w,selectmode=MULTIPLE)
lb.insert(1,'BCA')
lb.insert(2,'B.Sc.IT')
lb.insert(3,"PGDCA")
lb.pack()

btn = Button(w, text="click me", command=btn_click)
btn.pack()

w.mainloop()