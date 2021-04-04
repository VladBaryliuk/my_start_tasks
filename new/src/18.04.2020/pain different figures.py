from tkinter import *
window = Tk()
drawing = Canvas(window,width=500,height=500)
drawing.pack()
rect1 = drawing.create_rectangle(100,100,300,200)
squarel = drawing.create_rectangle(30,30,80,80)
oval1 = drawing.create_oval(100,100,300,200)
circle = drawing.create_oval(30,30,80,80,outline='red',fill='blue')
