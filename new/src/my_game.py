from tkinter import *
import random
root = Tk()
root.geometry("200x200")
enemy_health = 30
health = 100
money = 0
money_have = 25
wave = 1
super_attack = 0

enemy_hp_lbl = Label(root, text="HP of enemy is " + str(enemy_health))
hp_lbl = Label(root, text="Your HP is " + str(health))
energy_drink_lbl = Label(root, text="Your super attack energy is " + str(super_attack))


def punch():
    global enemy_health, super_attack
    enemy_health -= 5
    enemy_hp_lbl.config(text="HP of enemy is " + str(enemy_health))
    super_attack += random.randint(1, 5)
    energy_drink_lbl.config(text="Your super attack energy is " + str(super_attack))


def first_aid_kit():
    global health
    health += 100
    hp_lbl.config(text="Your HP is " + str(health))


def bandages():
    global health
    health += 20
    hp_lbl.config(text="Your HP is " + str(health))


def energy_drink():
    global super_attack
    super_attack += 15
    energy_drink_lbl.config(text="Your super attack energy is " + str(super_attack))


def start():
    root.geometry("550x250")
    name_lbl.place_forget()
    start_btn.place_forget()
    first_aid_kit_btn.place(x=0, y=180)
    bandages_btn.place(x=70, y=180)
    energy_drink_btn.place(x=140, y=180)
    punch_btn.place(x=225, y=180)
    enemy_hp_lbl.place(x=50, y=30)
    hp_lbl.place(x=0, y=215)
    money_lbl.place(x=90, y=215)
    energy_drink_lbl.place(x=195, y=215)


name_lbl = Label(root, text="shooter")
start_btn = Button(root, text="start game", command=start)
name_lbl.place(x=70, y=0)
start_btn.place(x=70, y=150)
first_aid_kit_btn = Button(root, text="first aid kit", width=7, command=first_aid_kit)
bandages_btn = Button(root, text="bandages", width=7, command=bandages)
energy_drink_btn = Button(root, text="energy drink", width=9, command=energy_drink)
punch_btn = Button(root, text="punch", width=7, command=punch)
money_lbl = Label(root, text="your money is " + str(money))


root.mainloop()
