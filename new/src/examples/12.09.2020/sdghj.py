import turtle
t = turtle.Pen()
def square(a, pen="red", fill = 'blue'):
    t.color(pen, fill)
    t.begin_fill()
    for i in range(4):
        t.fd(a)
        t.lt(90)
        t.end_fill()
square(100,pen ='blue', fill = 'red')
t.up()
t.fd(150)
t.down()
square(50)
