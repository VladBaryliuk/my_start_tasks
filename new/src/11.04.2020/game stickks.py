from  tkinter import *
from  random import randint
root = Tk()
root.geometry('400x250')
root.title('game sticks')
root.configure(bg='green')
quantity = 20
def computer_function():
    global quantity
    comp = randint(1,3)
    if  comp == 1 or comp == 2 or comp == 3 and comp < quantity:
        quantity -= comp
        l2.config(text=quantity * '|')
        l3.config(text = str(quantity))
    if quantity > 1:
        l1.config(text='your turn')
        root.after(2000,lambda:btn)
    if quantity == 1 or quantity < 1 :
        l3.config(text = 'computer is winner')
        
ent = Entry(width=15)
l1 = Label (root,text = 'your turn',font = 'arial5')
l2 = Label (root,text = quantity *'|',bg = 'green',width = 15,height = 1,font = 'Arial 23')
l3 = Label (root,text = quantity,bg = 'green',width = 15,height = 2,font = 'Arial 11')
def player_function():
    global quantity
    player = int (ent.get())
    if player ==  1 or player == 2 or player == 3 and player < quantity:
        quantity -= player
        l2.config(text = quantity * '|')
        l3.config(text = str(quantity))
    else:
        l3.config(text = 'error')
    if quantity > 1:
        l1.config(text='comp_turn')
        root.after(2000,lambda:computer_function())  
    if quantity == 1:
        l3.config(text = 'you are winner')
    if quantity < 1:
        l3.config(text = 'you are winner')
btn = Button (root,text = 'take sticks',command=player_function)
l1.pack()
ent.pack()
l2.pack()
l3.pack()
btn.pack()

        
 
