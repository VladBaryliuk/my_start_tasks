import random
import time

global variable
variable = "yes"

def display_Intro():
    print("You are in a land full of dragons..")
    print("In front of you, you see two caves")
    print(" In one cave, the dragon is friendly and will share his treasure with you.")
    print("The other dragon is greedy and hungry and wants to eat you.")
    print("")


def choose_Cave():
    number = int(input("enter cave number"))
    return number


def check_Cave(choosencave):
    print("You are comming to the cave")
    time.sleep(2)
    print("It is dark and scary")
    time.sleep(2)
    print("A big dragon jump to you")
    print("He opens his jaws and...")
    print("")
    time.sleep(2)
    dragon = random.randint(1, 2)
    if dragon == choosencave:
        print("and give you his treasure")
    else:
        print("and eat you from one bite")

while variable == "yes" or variable == "y":
    cave_number = choose_Cave()
    display_Intro()
    check_Cave(cave_number)
    variable = str(input("do you want to play again,print yes or no"))
