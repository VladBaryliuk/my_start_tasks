from tkinter import *
w = Tk()
w.geometry ('400x400')
Button(text='Test',font='Verdana 15',fg='white',relief=RIDGE,
              bd=5,justify=CENTER,width=5,
              bg='gray50',
              activebackground='green',
              activeforeground='black',
              state=NORMAL).place(x=200, y=300)
Label(text='Too much knowledge makes the \nhead bald.'
                'Too much knowledge \nmakes the head bald.'
                'Too much knowledge makes the head bald.',
                justify=CENTER,
                relief=SUNKEN,
                font='Arial 9',
                fg='red',
                width=50,
                height=5).place(x=25, y=150)
E1 = Entry(bg='white',fg='black',font='Helvetica 12',justify=CENTER,
           relief=RAISED,width=20,
           state=NORMAL)
E1.insert(0, 'Hello, world!')
E1.delete(5,END)
E1.place(x=150, y=50)
x = E1.get()

w.mainloop
