from tkinter import *
b = Tk()
b.geometry('400x200')
b.title('GUI на Python')
btn1 = Button (text='button1')
btn1.grid(row=0,column=0,padx=2,pady=1,ipadx=25,ipady=7,columnspan=1)
btn2 = Button (text='button2')
btn2.grid(row=0,column=1,padx=2,pady=1,ipadx=25,ipady=7,columnspan=1)
btn3 = Button (text='button3')
btn3.grid(row=1,column=0,padx=2,pady=1,ipadx=25,ipady=7,columnspan=1)
btn4 = Button (text='button4')
btn4.grid(row=1,column=1,padx=2,pady=1,ipadx=25,ipady=7,columnspan=1)
btn5 = Button (text='button5')
btn5.grid(row=0,column=2,padx=2,pady=1,ipadx=25,ipady=35,columnspan=1,rowspan=2)
btn6 = Button (text='button6')
btn6.grid(row=2,column=0,padx=2,pady=1,ipadx=130,ipady=7,columnspan=3)

b.mainloop
