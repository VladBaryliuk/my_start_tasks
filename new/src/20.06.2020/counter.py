from tkinter import *

root =Tk()
root.title("progect")

lb = Label(text = "Enter a mathematical expression of numbers and signs +, -, *, /, //,%, **")
lb.grid()
ent = Entry()
ent.focus()
ent.grid()
result = Label(text = "")
result.grid()
def function(event):
    try:
        result ["text"] = eval(entry.get())
        
    except:
        result["text"] = "The expression was entered with an error!"


ent.bind('<Return>',function)
        
