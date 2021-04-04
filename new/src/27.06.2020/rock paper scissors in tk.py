import random
from tkinter import *
root = Tk()
root.title("rock,paper,scissors")
root.geometry('220x220')
wins = 0
draw = 0
defeat = 0
start_raundes = 0
list_1 = ["rock","paper","scissors"]
ent = Entry(root)
def raundes():
    global raundes
    while True:
        try:
            raundes = ent.get()
            if raundes.isdigit():
                int(raundes)
                # ent.grid_forget()
                break
        except:
            lb1 = Label(root,text = "you did a mistake")
            lb1.grid()
raundes()
def rock():
    global answer
    answer = "rock"
def paper():
    global answer
    answer = "paper"
def scissors():
    global answer
    answer = "scissors"
rock = Button(root,text = "rock",command = rock())
rock.grid()
paper = Button(root,text = "paper",command = paper())
paper.grid()
scissors = Button(root,text = "scissors",command = scissors())
scissors.grid()
while start_raundes < raundes:
    def computer():
        global comp_answer
        comp_answer = random.choice(list_1)
    lb2 = Label(root, text = "rock,paper or scissors ")
    lb2.grid()
    computer()
    lb3 = Label(root, text = comp_answer)
    lb3.grid()
    start_raundes += 1
    if answer == "rock" and comp_answer == "paper":
        defeat += 1
    elif answer == "paper" and comp_answer == "scissors":
        defeat += 1
    elif answer == "scissors" and comp_answer == "rock":
        defeat += 1
    elif answer == "paper" and comp_answer == "rock":
        wins += 1
    elif answer == "scissors" and comp_answer == "paper":
        wins += 1
    elif answer == "rock" and comp_answer == "scissors":
        wins += 1
    elif answer == comp_answer:
        draw += 1
lb4 = Label(root,text = wins + draw + defeat)
lb4.grid()
root.mainloop()