from tkinter import *
import random
root = Tk()
row = 0
column = 0
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
buttons = []
random.shuffle(numbers)
index = 0
wins = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
def is_empty(structure):
    if structure:
        return False
    else:
        return True

def binding(i, n,):
    if n == wins[0]:
        del wins[0]
        string = "you have to write",wins[0]
        lb1 = Label(root,text =string )
        lb1.grid(columnspan = 3)
    else:
        print("error")
    if is_empty(wins):
        root.destroy()
        print("you are winner")
for index, numbs in enumerate(numbers):
    btn = Button(root,text=str(numbs),font="20", width=3, height=5,bg="#C1C4C7"
    ,command = lambda idx=index, num = numbs: binding(idx, num))
    btn.grid(row=row, column=column)
    column += 1
    index+=1
    if column == 3:
        column = 0
        row += 1
    buttons.append(btn)
root.mainloop()