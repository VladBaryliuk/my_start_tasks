from tkinter import *
root = Tk()
root.title ("second")
root.geometry("300x250")
btn1 = Button(text='button1',bg="black",fg="white",padx="25",pady="6",font="15")
btn1.pack(fill=Y,side=LEFT)
btn2 = Button(text='button2',bg="black",fg="white",padx="25",pady="6",font="15")
btn2.pack(fill=Y,side=RIGHT)
btn3 = Button(text='button3',bg="black",fg="white",padx="15",pady="6",font="15")
btn3.pack(side=TOP)
btn4 = Button(text='button4',bg="black",fg="white",padx="15",pady="6",font="15")
btn4.pack(side=BOTTOM)

root.mainloop()
