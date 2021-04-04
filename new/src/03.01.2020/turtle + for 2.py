import turtle
t = turtle.Pen()
a = int (input())
b = int (input())
for i in range (a):
    for g in range (b):
        t.forward(20)
        t.left(360 / b)
    t.up()
    t.forward(70)
    t.down()
