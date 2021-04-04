from tkinter import *

root = Tk()
root.title("bomb")
root.geometry("500x500")

wick = 100
day = 0

no_photo = PhotoImage(file = "bomb_no.gif")
normal_photo = PhotoImage(file = "bomb_normal.gif")
bang_photo = PhotoImage(file = "bang.gif")
start_Label = Label(root, text = "put Enter to start game", font = ("Helvetica", 12))
bomb_Label = Label(root, text = "wick" + str(wick), font = ("Helvetica", 12))
day_Label = Label(root, text = "day" + str(day), font = ("Helvetica", 12))
bomb_normal = Label(root, image = normal_photo)


Ok_to_pressReturn = True


def start(event):
    global Ok_to_pressReturn
    if Ok_to_pressReturn == False:
        pass
    else:
        start_Label.config(text="")
        update_bomb()
        update_day()
        update_display()

        Ok_to_pressReturn = False

def update_display():
    global wick, day
    if wick <= 50:
        bomb_normal.config(image = no_photo)
    else:
        bomb_normal.config(image = normal_photo)
    bomb_Label.config(text = "wick" + str(wick))
    day_Label.config(text = "day" + str(day))
    bomb_normal.after(100, update_display)

def update_bomb():
    global wick
    wick -= 1
    if isAlive():
        bomb_Label.after(500, update_bomb)

def update_day():
    global day
    day += 1
    if isAlive():
        bomb_Label.after(5000, update_day)

def  stop():
    global wick
    if isAlive():
        if wick<=55:
            wick += 3
        else:
            wick -= 30

def isAlive():
    global wick
    if wick <= 0:
        start_Label.cofig(text = "booooooooooooooom!!!")
        no_photo.config(image = bang_photo)
        return False
    else:
        return True

btn_no_bomb = Button(root, text = "put me", command=stop)

start_Label.pack()
bomb_Label.pack()
day_Label.pack()
bomb_normal.pack()
btn_no_bomb.pack()

root.bind("<Return>", start)



root.mainloop()