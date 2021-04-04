from tkinter import *
import random
window = Tk()
window.title('Greetings')
window.geometry('400x300')
def phrase_generator():
    phrases = ["hello ","what's up ",
               "aloha ","hallo ","привет "]
    name = e1.get()
    greeting = phrases[random.randint(0,4)] + name
    t1.delete(0.0,END)
    t1.insert(END,greeting)
l1 = Label(text='Welcome to my app',font = ('Times New Roman',20))
l1.place(x=69,y=0)
l2 = Label(text='What is your name?')
l2.place(x=69,y=30)
btn = Button(text='click me',bg = 'red',command = phrase_generator)
btn.place(x=100,y=45)
e1 = Entry(width=20)
e1.place(x=230,y=30)
t1 = Text(height=10,width=25)
t1.place(x=0,y=69)

window.mainloop()
