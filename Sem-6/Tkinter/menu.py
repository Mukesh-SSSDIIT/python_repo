from tkinter import *

win = Tk();
win.title("Menu Example")
win.geometry("400x400")

def somemethod():
    Label(text="Menu clicked").pack()

def shortcutmethod(self):
    Label(text="Menu clicked").pack()

menubar = Menu(win)

filemenu = Menu(menubar)
menubar.add_cascade(label ='File', menu = filemenu) 
filemenu.add_command(label="New File",command=somemethod,accelerator="Ctrl+N")
filemenu.add_command(label="New Window",command=somemethod,accelerator="Ctrl+W")
filemenu.add_separator()
filemenu.add_command(label="Open File",command=somemethod,accelerator="Ctrl+f")
filemenu.add_command(label="Exit",command=win.destroy,accelerator="Ctrl+E")

editmenu = Menu(menubar)
menubar.add_cascade(label="Edit", menu= editmenu)
editmenu.add_command(label="Cut",command=somemethod)
editmenu.add_command(label="Copy",command=somemethod)
editmenu.add_command(label="Paste",command=somemethod)
editmenu.add_separator()
editmenu.add_command(label="Find...",command=somemethod)

win.bind_all("<Control-e>", shortcutmethod)
win.bind_all("<Control-q>", shortcutmethod)

win.config(menu=menubar)
win.mainloop()