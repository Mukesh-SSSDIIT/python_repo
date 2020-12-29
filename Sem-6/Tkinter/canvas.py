from tkinter import *
master = Tk() 
w = Canvas(master, width=500, height=500,bg="red") 
w.pack() 
# canvas_height=20
# canvas_width=200
# y = int(canvas_height / 2) 
w.create_line(10, 10, 100, 10 ) 
coord = 10, 50, 240, 210
arc = w.create_arc(coord, start=0, extent=150, fill="blue")
mainloop() 
