from tkinter import *
root = Tk()
root.title ("thirt")
root.geometry("300x250")
btn1 = Button(text='назад',bg="black",fg="white",padx="25",pady="6",font="15")
btn1.place(relheight=0.15,relwidth=0.20,relx=0.10,rely=0.80)
btn2 = Button(text='далее',bg="black",fg="white",padx="25",pady="6",font="15")
btn2.place(relheight=0.15,relwidth=0.20,relx=0.65,rely=0.80)

root.mainloop()
