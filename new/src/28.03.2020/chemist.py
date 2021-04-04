from tkinter import *
root = Tk()
root.title("chemist")
root.geometry('220x500')
root.resizable(False,False)
im = PhotoImage(file='flask1.gif')
elements = ['O','H','C','S','Ci','Na']
sub1 = ['OH','OC','OHS','HCi','CiNa','OHNa','HS','OS','OSNa','HC','CNa','OCi']
sub2 = ['H2O','CO2','H2SO4','HCi','NaCi','NaOH','H2S','SO2','Na2S04','CH4',
        'Na3C','Ci207']
sub3 = ["вода","углукислый газ","серная кислота","соляная кислота","поваренная соль","едкий натр","сероводород","оксид серы","сульфат натрия","метан","карбид натрия","оксид хлора"]
def substance():
    subst=''
    elem_check=[elem1.get(),elem2.get(),elem3.get(),elem4.get(),elem5.get(),elem6.get()]
    for i in range(len(elem_check)):
        if elem_check[i]==1:
            subst=subst+elements[i]
        if sub1.count(subst)!=0:
            a=sub1.index(subst)
            lb_2.config(text=sub2[a])
            lb_3.config(text=sub3[a])
        else:
            lb_2.config(text="")
            lb_3.config(text="no connection found")
elem1= IntVar()
elem1.set(0)
elem2= IntVar()
elem2.set(0)
elem3= IntVar()
elem3.set(0)
elem4= IntVar()
elem4.set(0)
elem5= IntVar()
elem5.set(0)
elem6= IntVar()
elem6.set(0)
el1 = Checkbutton(text="O",variable=elem1,onvalue=1,offvalue=0,indicatoron=0,font='Arial20',width=7,height=3)
el2 = Checkbutton(text="H",variable=elem2,onvalue=1,offvalue=0,indicatoron=0,font='Arial20',width=7,height=3)
el3 = Checkbutton(text="C",variable=elem3,onvalue=1,offvalue=0,indicatoron=0,font='Arial20',width=7,height=3)
el4 = Checkbutton(text="S",variable=elem4,onvalue=1,offvalue=0,indicatoron=0,font='Arial20',width=7,height=3)
el5 = Checkbutton(text="Ci",variable=elem5,onvalue=1,offvalue=0,indicatoron=0,font='Arial20',width=7,height=3)
el6 = Checkbutton(text="Na",variable=elem6,onvalue=1,offvalue=0,indicatoron=0,font='Arial20',width=7,height=3)
lb_1=Label(text='chemical elements',font='Arial,14',fg='blue',bg='#ffffff',width=20,height=2)
lb_2=Label(text="",font='Arial,20',fg='blue',bg='#ffffff',width=220,height=220,image=im,compound=CENTER)
lb_3=Label(text='',font='Arial,14',fg='blue',bg='#ffffff',width=20,height=2)
lb_1.grid(row=0,column=0,columnspan=3)
el1.grid(row=1,column=0)
el2.grid(row=1,column=1)
el3.grid(row=1,column=2)
el4.grid(row=2,column=0)
el5.grid(row=2,column=1)
el6.grid(row=2,column=2)
btn=Button(text="Соединить элементы", bg='#87CEEB', width=20, height=2, font='Arial, 10', command=substance)
btn.grid(row=3,column=0,columnspan=3)
lb_2.grid(row=5,column=0,columnspan=3)
lb_3.grid(row=4,column=0,columnspan=3)
root.mainloop()

