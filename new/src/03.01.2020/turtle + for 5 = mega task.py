import random 
import turtle
t = turtle.Pen()
for s in range (4):
    for y in range (5):
        for i in range (5):
            for g in range (3):
                t.pencolor(random.random(),random.random(),random.random())
                t.forward (10)
                t.left(360 / 3)
            t.left(72)
        t.up()
        t.forward(20)
        t.down()
    t.left(90)
    
