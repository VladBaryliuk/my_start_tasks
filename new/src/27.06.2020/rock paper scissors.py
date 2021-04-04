import random
wins = 0
draw = 0
defeat = 0
startraundes = 0
list_1 = ["rock","paper","scissors"]
def raundes():
    global raundes
    while True:
        try:
            raundes = int(input())
            if int (raundes):
                break
        except:
            print("you did  a mistake")
raundes()
while startraundes < raundes:
    def computer():
        global comp_answer
        comp_answer = random.choice(list_1)
    answer = str(input("rock,paper or scissors "))
    if answer not in list_1:
        answer = str(input("rock,paper or scissors "))
    else:
        computer()
        print(comp_answer)
    startraundes += 1
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
print(wins,draw,defeat)
