import turtle
import random

t = turtle.Pen()

colors = ["blue", "red", "orange", "yellow", "green"]


def square():
    a=random.randint(50, 200)
    pen=random.choice(colors)
    fill=random.choice(colors)
    t.color(pen, fill)
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.lt(90)
        t.end_fill()
for i in range (10):
    square()
    t.up()
    t.goto(random.randint(-100,100),random.randint(-100, 100))
    t.down()
