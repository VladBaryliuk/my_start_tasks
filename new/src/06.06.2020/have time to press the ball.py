from tkinter import *
import random
import time
root = Tk()
c = Canvas(root,width=900, height=300, background="orange")
c.pack()
c.delete(ALL)
points = 0
def new_ball():
    global x, y, r
    x = random.randint(1, 830)
    y = random. randint(140, 230)
    r = random. randint(20, 70)
    ball = c.create_oval(x, y,x+r,y+r,fill = 'blue')
def click(event):
    global points, x
    
    if (event.y - y)**2 + (event.x - x)**2 <= r**2:
        points += 1
        x = -1000
        c.delete(ALL)
        c.create_text(5,15,text=points,fill='black')
        new_ball()
    if points == 50:
        c.delete(ALL)
        c.create_text(125,30,text='you are winner',fill='black',font='Arial 22')    
c.bind_all('<Button-1>',click) 
new_ball()
