from tkinter import *
import math
import datetime
root = Tk()
root.title('clocks')
radius = 150
width = 400
height = 400
canvas = Canvas(root, width = width, height = height)

def chanche_hand(lenght, time, clock_hand, degree):
    alpha = 90 - time * degree
    x1 = x_coordinate(0, alpha)
    y1 = x_coordinate(0, alpha)
    x2 = x_coordinate(lenght, alpha)

    y2 = y_coordinate(lenght, alpha)
    canvas.coords(clock_hand, x1, y1, x2, y2)
    
canvas.pack()
canvas.create_oval(width/2-radius,height/2-radius,width/2+radius,height/2+radius,)
seconds = canvas.create_line(0,0,0,0,fill = 'red')
minutes = canvas.create_line(0,0,0,0)
hours = canvas.create_line(0,0,0,0)

def update():

    time = str (datetime.datetime.now())
    
    sec = int(time [17:19])
    min = int(time [14:16])
    hour = int(time [11:13])
    
    chanche_hand(radius-20,sec,seconds,6)
    chanche_hand(radius-40,min,minutes,6)
    chanche_hand(radius/2,hour,hours,30)
    root.after(1000,update)

    
def x_coordinate(length,angle):
    return width/2+length*math.cos(angle*math.pi/180)

def y_coordinate(lenght,angle):
    return height/2-lenght*math.sin(angle*math.pi/180)
alpha = 60

for i in range (1,13):
    canvas.create_text(x_coordinate(radius + 20,alpha),y_coordinate(radius + 20,alpha),text=i,fill = 'darkblue',font='times 10 italic bold')
    alpha-=30
    
for i in range(60):
    x1 = x_coordinate(radius, alpha)
    y1 = y_coordinate(radius, alpha)
    
    if alpha%30 == 0:
        x2 =x_coordinate(radius-20, alpha)
        y2 =y_coordinate(radius-20, alpha)
    else:
        x2 =x_coordinate(radius-10,alpha)
        y2 =y_coordinate(radius-10,alpha)
    canvas.create_line(x1, y1, x2, y2)
    alpha+=6

update()
root.mainloop()
