import turtle
t = turtle.Pen()
n = int (input())
for i in range (n):
    t.forward (50)
    t.left (360 / n)
