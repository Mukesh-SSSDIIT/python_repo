import tkinter as tk
from tkinter import messagebox
from tkinter import Button

def btn_click():
    msg = messagebox.showinfo( "Hello Python", "Welcome to python")

topwindow = tk.Tk(screenName='Test', className='My First Program')
btn1 = Button(topwindow,text="Click Me !! - I am button 1",command=btn_click)
btn2 = Button(topwindow,text="Click Me !! - I am button 2",command=btn_click)
btn3 = Button(topwindow,text="Click Me !! - I am button 3",command=btn_click)
btn1.place(x= 100,y=50)
btn2.place(x= 100,y=100)
btn3.place(x= 100,y=150)
topwindow.mainloop()