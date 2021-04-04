import time 
import random
from tkinter import *
root = Tk()
root.geometry("500x500")
canvas = Canvas(root,width=500,height=500)
canvas.pack()
y = 20
text =""
count = 0
time_list = []
def main():
    global ball
    ball = canvas.create_oval(225,225,275,275,fill="black")
    root.after(random.randint(3000,10000),set_time)
def set_time():
    canvas.itemconfig(ball,fill="green")
    global start_time
    start_time = time.time()
def timer(want):
    global ball
    global count
    global text
    if count >= 5:
        canvas.delete(ball)
        canvas.delete(text)
        total=round(float(sum(time_list)) / len(time_list), 3)
        return
    sec = round(time.time()-start_time,3)
    if sec < 1:
        time_list.append(sec)
        count+=1
        global y
        canvas.create_text(40,y,font="Arial 14",text=sec)
        y+=20
    else:
        canvas.create_text(40,y,font="Arial 14",text="1")
        canvas.delete(ball)
        y+=20
        count+=1
    root.after(500,main)
canvas.bind_all('<Button-1>',timer)
main()
root.mainloop()
