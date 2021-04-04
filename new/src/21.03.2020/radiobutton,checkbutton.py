from tkinter import *
root = Tk()
root.geometry('600x400')
root.resizable(False,False)
L1 = Label(text = 'jyde')
def colour():
    if radiovar2 == 0:
        L1 = Label(text = 'dd',bg = 'red')
        L1.place(x=0,y=140)
    elif radiovar2 == 1:
        L1 = Label(text = 'dd',bg = 'green')
        L1.place(x=0,y=140)
    elif radiovar2 == 2:
        L1 = Label(text = 'dd',bg = 'blue')
        L1.place(x=0,y=140)
radiovar = BooleanVar()
radio1 = Radiobutton(text='Radiobutton1',variable = radiovar,value = True,indicatoron = 0)
radio2 = Radiobutton(text='Radiobutton2',variable = radiovar,value = False,indicatoron = 0)
radio1.place(x = 30,y = 30)
radio2.place(x = 130,y = 30)
radiovar2 = IntVar()
radio3 = Radiobutton(text='Red',variable = radiovar2,value = 0,indicatoron = 0,command = colour)
radio4 = Radiobutton(text='Green',variable = radiovar2,value = 1,indicatoron = 0,command = colour)
radio5 = Radiobutton(text='Blue',variable = radiovar2,value = 2,indicatoron = 0,command = colour)
radio3.place(x = 130,y = 70)
radio4.place(x = 130,y = 92)
radio5.place(x = 130,y = 114)
L1 = Label(text = 'dd',bg = 'white')
