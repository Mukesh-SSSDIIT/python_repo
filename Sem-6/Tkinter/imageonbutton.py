import tkinter as tk
from tkinter import PhotoImage, messagebox
from tkinter import Button

def btn_click():
    msg = messagebox.showinfo( "Hello Python", "Welcome to python")

topwindow = tk.Tk(screenName='Test', className='My First Program')

btnimage = PhotoImage(file = "C:\\Users\\Mukesh\\Pictures\\forloop.png")
#btnimage = btnimage.zoom(2,2)

btn = Button(topwindow, text ="I am button",image=btnimage,height=100,width=100)
btn.place(x= 50,y=50)
topwindow.mainloop();