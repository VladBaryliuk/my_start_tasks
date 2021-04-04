from tkinter import *
from tkinter import messagebox
from random import shuffle
import time
root = Tk()
root.geometry('1150x700+210+90')
x = 950
y = 45
number_questions = 0
your_money = 0
money = 0
moneyplus = 10000
questions = [['Which Disney character famously leaves a glass slipper behind at a royal ball?' , 'Pocahontas', 'Sleeping Beauty', 'Cinderella', 'Elsa','Cinderella'],
             ['Which of these is a country in Africa?', 'Botswana', 'England','Saudi Arabia','China', 'Botswana'],
             ['What is the last name of the family depicted in the movie The Sound of Music?', 'Von Furstenburg', 'Von Plummer', 'Von Trapp', 'Von Vanderberg', 'Von Trapp'],
             ['The game of Mah-Jong originated in what country?', 'England', 'China','Japan', 'Russia', 'China'],
             ['What nationality is celebrated on St. Patricks Day?', 'Mexican', 'Welsh', 'American Indian', 'Irish', 'Irish'],
             ['What chemical is added to the water in swimming pools?', 'Chlorine', 'Sulfur', 'Vinegar', 'Ammonia', 'Chlorine'],
             ['Who wrote the novels that introduced the characters Hercule Poirot and Miss Jane Marple?', 'Ellery Queen', 'Ruth Rendell', 'H. G. Wells', 'Agatha Christie', 'Agatha Christie'],
             ['What is the Italian word for a square or marketplace?', 'Presto', 'Pisa', 'Piazza', 'Plaza', 'Piazza'],
             ['Which team won the first two Super Bowls?', 'Kansas City Chiefs', 'Minnesota Vikings', 'Chicago Bears', 'Green Bay Packers', 'Green Bay Packers'],
             ['How many different combinations of dots are possible in Braille?', '49', '63', '75', '87', '63']]
money_label = Label(root, text = f'if you answer right you \n will win  {money} Dolars', width = 30)
now_money_label = Label(root, text = f'your money is  \n {your_money} Dolars', width = 30)
money_label.place(x = x, y = y)
now_money_label.place(x = 950, y = 16)
def check(otv):
    global your_money
    global moneyplus
    global money
    global questions
    global number_questions
    if otv == questions[number_questions][5]:
        messagebox.showinfo('Right!', 'Well done!')
        number_questions +=1
        money += moneyplus
        moneyplus += 5000
        your_money += money
        btns = questions[number_questions][1:5]
        shuffle(btns)
        money_label.config(text = f'if you answer right you \n will win  {money} Dolars', width = 30)
        money_label.place(x=x, y=y)
        now_money_label.config(text = f'your money is  \n {your_money} Dolars', width = 30)
        now_money_label.place(x = 950, y = 16)
        questionsLabel.config(text=questions[number_questions][0])
        btn1.config(text=btns[0], command=lambda: check(btns[0]))
        btn2.config(text=btns[1], command=lambda: check(btns[1]))
        btn3.config(text=btns[2], command=lambda: check(btns[2]))
        btn4.config(text=btns[3], command=lambda: check(btns[3]))
        money_label.place(x, y)
    elif number_questions == 10:
        messagebox.showinfo('You won !!!')
        time.sleep(5)
    else:
        messagebox.showerror('Wrong!', 'Sorry, but now your game is  over :( ')
        number_questions = 0
        root.destroy()
    if number_questions == 8:
        money = 900000
        money_label.place(x=x, y=y)

btns = questions[number_questions][1:5]
shuffle(btns)
pic = PhotoImage(file='logo.gif')
picL = Label(root, image=pic)
questionsLabel = Label(root, text=questions[number_questions][0], font='Verdana 22')
btn1 =Button(root, text=btns[0], font='Verdana 22', width=20,
             command=lambda: check(btns[0]))
btn2 =Button(root, text=btns[1], font='Verdana 22', width=20,
             command=lambda: check(btns[1]))
btn3 =Button(root, text=btns[2], font='Verdana 22', width=20,
             command=lambda: check(btns[2]))
btn4 =Button(root, text=btns[3], font='Verdana 22', width=20,
             command=lambda: check(btns[3]))
picL.grid(row=0, column=0, columnspan=2)
btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)
btn3.grid(row=3, column=0)
btn4.grid(row=3, column=1)
questionsLabel.grid(row=1, column=0, columnspan=2)

root.mainloop()
