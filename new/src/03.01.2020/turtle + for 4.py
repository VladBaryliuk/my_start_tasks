import random
import turtle
t = turtle.Pen()
for i in range (15):
    for g in range (3):
        t.pencolor(random.random(),random.random(),random.random())
        t.forward(50)
        t.left(360 / 3)
    t.left(24)
t.up()
t.left(90)
t.forward(75)
t.down()
for i in range (15):
    for g in range (3):
        t.pencolor(random.random(),random.random(),random.random())
        t.forward(50)
        t.left(360 / 3)
    t.left(24)
