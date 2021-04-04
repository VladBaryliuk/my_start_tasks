from tkinter import *
import random
window = Tk()
window.geometry('300x300')
window.title('my app')
button_height = 5
button_width = 10
def buttonbigger():
    global button_height, button_width
    button_height += 2
    button_width += 10
    rainbow.config(height=button_height,width=button_width)
def buttonless():
    global button_height, button_width
    button_height -= 2
    button_width -= 10
    rainbow.config(height=button_height,width=button_width)
rainbow = Button(text='rainbow',height = 5,width = 10)
rainbow.place(x=110,y=0)
btn1= Button(text='bigger',height = 5,width = 7,bg = 'green',command = buttonbigger)
btn1.place(x=0,y=0)
btn2= Button(text='less',height = 5,width = 7,bg = 'red',command = buttonless)
btn2.place(x=230,y=0)

window.mainloop()
