import turtle
import random
t = turtle.Pen()
tr = turtle.Pen()
def circle(x,y):
    colors = ["blue","red", "yellow","orange","purple", "brown"]
    color = random.choice(colors)
    t.up()
    t.goto(x, y)
    t.down()
    t.begin_fill()
    t.fillcolor(color)
    t.circle(random.randint(10,50))
    t.end_fill()
turtle.onscreenclick(circle)
speed = 5
second_speed = 5


def go():
    global speed
    x, y = t.xcor(), t.ycor()
    t.goto(x, y + speed)


def go_back():
    global speed
    x, y = t.xcor(), t.ycor()
    t.goto(x, y - speed)


def go_right():
    global speed
    x,y = t.xcor(), t.ycor()
    t.goto(x+speed,y)

def go_left():
    global speed
    x,y = t.xcor(), t.ycor()
    t.goto(x-speed,y)

def go2():
    global speed
    x,y = tr.xcor(), tr.ycor()
    tr.goto(x, y + speed)

def go_back2():
    global speed
    x,y = tr.xcor(), tr.ycor()
    tr.goto(x, y - speed)


def go_right2():
    global speed
    x,y = tr.xcor(), tr.ycor()
    tr.goto(x + speed,y)

def go_left2():
    global speed
    x, y = tr.xcor(), tr.ycor()
    tr.goto(x - speed,y)


turtle.onkeypress(go, "Up")
turtle.onkeypress(go_back, "Down")
turtle.onkeypress(go_right, "Right")
turtle.onkeypress(go_left, "Left")

turtle.onkeypress(go2, "w")
turtle.onkeypress(go_back2, "s")
turtle.onkeypress(go_right2, "d")
turtle.onkeypress(go_left2, "a")

turtle.listen()
