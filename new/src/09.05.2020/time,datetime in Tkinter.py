import time 
import random
from tkinter import *
root = Tk()
root.geometry("400x300")
messages = [
"Из всех деревьев мы врезались в то, которое смогло дать нам сдачи.",
"Если не прекратить его попытки спасти вам жизнь, он вас убьет.",
"Нашу сущность намного лучше демонстрируют действия, а не возможности.",
"Я маг, а не размахивающий палкой бабуин.",
"Величие порождает зависть, зависть — злобу, злоба — ложь.",
"В мечтах мы попадаем в наш и только наш мир.",
"Я убежден, что истина, как правило, предпочтительнее лжи.",
"Казалось, что рассвет следует за полночью с неприличной поспешностью." 
]
message = random.choice(messages)
def entt():
    ent = Entry(root)
    ent.grid()
    start_time = time.time()
    def time_of_writing():
        end_time = time.time()
        delta = end_time-start_time
        speed = len(ent.get()) / delta
        lbl_of_speed = Label(root,text="You introduced" +str(len(ent.get()))+"characters from"+str(delta)+"seconds" )
        lbl_of_speed2 = Label(root,text="You introduced"+str(speed)+"characters in 1 second")
        lbl_of_speed3 = Label(root,text="You shoulded to introduc string"+message+".And you introduced "+ent.get() )
        lbl_of_speed.grid()
        lbl_of_speed2.grid()
        lbl_of_speed3.grid()

    btn = Button(root,text="enter",command=time_of_writing)
    btn.grid()
def lbl1():
    lb1 = Label(root,text="Проверка скорости набора. Введите следующую фразу. Я засеку время…")
    lb1.grid()
    root.after(2000,lbl2)
def lbl2():
    lb2 = Label(root,text="приготовиться")
    lb2.grid()
    root.after(1000,lbl3)
def lbl3():
    lb3 = Label(root,text="сосредоточиться...")
    lb3.grid()
    root.after(1000,lbl4)
def lbl4():
    lb4 = Label(root,text="начали")
    lb4.grid()
    root.after(50,lbl5)    
def lbl5():
    lb5 = Label(root,text=message)
    lb5.grid()
    root.after(50,entt)
    
lbl1()

