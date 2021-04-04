from tkinter import *
from tkinter import messagebox as mb
root = Tk()
root.title('TK')
root.geometry('300x400')
ent = Entry(root,width = 12)

def answer():
    data = 0
    answer = mb.askyesno(title="Question",message="Check the data?")
    if answer == True:
        if ent.get().isdigit():
            data = ent.get()
            print(data)
        else:
            mb.showerror(title="ERROR",message="This is not a number")
        print(data)       
btn = Button(root,text='Copy',command = answer)
ent.pack()
btn.pack() 
