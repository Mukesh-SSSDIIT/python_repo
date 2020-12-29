import tkinter as tk
from tkinter import messagebox
from tkinter import Button
from tkinter import font as tkFont

def btn_click():
    msg = messagebox.showinfo( "Hello Python", "Welcome to python")

topwindow = tk.Tk(screenName='Test', className='My First Program')
btn1 = Button(topwindow,text="Click Me 1",command=btn_click,
            width=20,height=2,activebackground="red",activeforeground="white",bg="yellow")
btn2 = Button(topwindow,text="Click Me 2",command=btn_click,width=20,height=2,
            activebackground="green",activeforeground="#ff8fa8458",bg="green")
btn3 = Button(topwindow,text="Click Me 3",command=btn_click,
            width=20,height=2,activebackground="blue")
btn1.place(x= 50,y=50)
btn2.place(x= 200,y=50)
btn3.place(x= 350,y=50)

fnt = tkFont.Font(family='Times new roman', size=10, weight='bold')
btn1['font'] = fnt
btn2['font'] = fnt
btn3['font'] = fnt

# #4 bits per color
# tkinter.Button(window_main, activebackground='#rgb') #f00, #8af
# #8 bits per color
# tkinter.Button(window_main, activebackground='#rrggbb') #ff853a
# #12 bits per color
# tkinter.Button(window_main, activebackground='#rrrgggbbb') #ff8aba53a
# #standard color names
# tkinter.Button(window_main, activebackground='red') #red, green, yellow, blue

topwindow.mainloop()