from tkinter import *
root = Tk()
root.geometry('300x400')
btn2 = Button(text = 'save')
btn2.pack()
text = Entry()
text.pack()
list = Text()
list.pack()
def add ():
    todo = text.get() + '\n'
    list.insert (END, todo)
btn = Button(text = 'enter',command=add)
btn.pack()

root.mainloop()
