from tkinter import *
window = Tk()
window.title('Alien')
c = Canvas(window,height=400,width=600)
c.pack()
body = c.create_oval(100,150,300,250,fill='green')
eye = c.create_oval(170,70,230,130,fill='white')
eyeball = c.create_oval(190,90,210,110,fill='black')
mouth = c.create_oval(150,220,250,240,fill='red')
neck = c.create_line(200,150,200,130)
hat = c.create_polygon(180,75,220,75,200,20,fill='blue')
def mouth_open():
    c.itemconfig(mouth,fill='black')
def mouth_close():
    c.itemconfig(mouth,fill='red')
def blink():
    c.itemconfig(eye,fill='green')
    c.itemconfig(eyeball,state=HIDDEN)
def unblink():
    c.itemconfig(eye,fill='white')
    c.itemconfig(eyeball,state=NORMAL)
def blink2(event):
    c.itemconfig(eye,fill='green')
    c.itemconfig(eyeball,state=HIDDEN)
def unblink2(event):
    c.itemconfig(eye,fill='white')
    c.itemconfig(eyeball,state=NORMAL)
c.bind_all('<KeyPress-a>',blink2)
c.bind_all('<KeyPress-z>',unblink2)
def eye_control(event):
    key = event.keysym
    if key == "Up":
        c.move(eyeball,0,-1)
    elif key == "Down":
        c.move(eyeball,0,1)
    elif key == "Left":
        c.move(eyeball,-1,0)
    elif key == "Right":
        c.move(eyeball,1,0)
c.bind_all('<Key>',eye_control)
words = c.create_text(200,280,text='I am an alien!')
def steal_hat():
    c.itemconfig(hat,state = HIDDEN)
    c.itemconfig(words,text='Give my hat back!')
window.attributes('-topmost',1)
def burp(event):
    mouth_open()
    c.itemconfig(words,text='Burp!')
c.bind_all('<Button-1>',burp)
def give_hat():
    c.itemconfig(hat,state = NORMAL)
    c.itemconfig(words,text='thank you!')
def brother():
    global body
    global eye
    global eyeball
    global mouth
    global neck
    global hat
    body = c.create_oval(300,150,500,250,fill='blue')
    eye = c.create_oval(370,70,430,130,fill='white')
    eyeball = c.create_oval(390,90,410,110,fill='black')
    mouth = c.create_oval(350,220,450,240,fill='red')
    neck = c.create_line(400,150,400,130)
