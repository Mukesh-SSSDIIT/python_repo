import tkinter as tk
from tkinter import messagebox
from tkinter import Button

def btn_click():
    msg = messagebox.showinfo( "Hello Python", "Welcome to python")

top = tk.Tk()
btn = Button(top,text="Click Me !!",command=btn_click)
btn.place(x= 100,y=100)
top.mainloop()