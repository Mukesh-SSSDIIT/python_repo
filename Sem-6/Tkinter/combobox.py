from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import mysql.connector as con

mydb = con.connect(
    host = "localhost",
    user = 'root',
    password = '',
    database = 'pythonexample'
)

mycursor = mydb.cursor()
mycursor.execute("select * from coursedetails")
courses = mycursor.fetchall()

courselist = []

for course in courses:
    courselist.append(course[1])

win = Tk()
win.title("Combobox Example")
win.geometry("400x400")

lbldata = StringVar()

Label(win,textvariable=lbldata).pack()

mycombo = Combobox(win, textvariable=lbldata,width=30)
mycombo['values'] = courselist
mycombo.current(2)

mycombo.pack()
win.mainloop()

