from tkinter import *
root = Tk()
root.title("знаки зодиака")
root.geometry("300x500")
def define():
    day = int(ent1.get())
    month = int(ent2.get())
    images = [im,im1,im2,im3,im4,im5,im6,im7,im8,im9,im10,im11,im12,im1]
    gor = ["козерог","водолей","рыбы","овен","телец","близнецы","рак","лев","дева","весы","скорпион","стрелец","козерог"]
    if day>0 and day<32 and month>0 and month<13:
        if day>21:
            month += 1
        lb4.config(text=gor[month - 1])
        lb5.config(image=images[month])
    else:
        lb4.config(text="error!!!")
        lb5.config(image=images[0])
lb1 = Label(root,text="enter your birthday date",font="Impact 18")
lb2=Label(root,text="day",font="Impact 16")
ent1=Entry()
lb3=Label(root,text="month",font="Impact 16")
ent2=Entry()
btn = Button(root,text="определить знак",command = define)
lb4=Label(root,text=" ",font="Impact 20")
lb1.pack()
lb2.pack()
ent1.pack()
lb3.pack()
ent2.pack()
btn.pack()
lb4.pack()
im = PhotoImage(file='start.gif')
im1 = PhotoImage(file='козерог.gif')
im2 = PhotoImage(file='водолей.gif')
im3 = PhotoImage(file='рыбы.gif')
im4 = PhotoImage(file='овен.gif')
im5 = PhotoImage(file='телец.gif')
im6 = PhotoImage(file='близнецы.gif')
im7 = PhotoImage(file='рак.gif')
im8 = PhotoImage(file='лев.gif')
im9 = PhotoImage(file='дева.gif')
im10 = PhotoImage(file='весы.gif')
im11 = PhotoImage(file='скорпион.gif')
im12 = PhotoImage(file='телец.gif')
lb5 = Label(root,image=im,width=250,height=250)
lb5.pack()

root.mainloop()
