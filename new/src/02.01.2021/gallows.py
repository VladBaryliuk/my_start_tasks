from tkinter import *
import random

root = Tk()
root.title("gallows")

c = Canvas(root, width = 800, height = 600)
c.pack()

words = ['ability', 'absence', 'academy', 'account', 'accused', 'achieve', 'acquire', 'address', 'advance', 'advised',
         'adviser', 'against', 'airline', 'aiport', 'already', 'ancient', 'another', 'anxiety', 'anxious', 'anybody', 'applied',
         'arrange', 'arrival', 'article', 'assault']
def bg():
    y = 0

    while y < 600:
        x = 0
        while x < 800:
            c. create_rectangle(x, y, x + 33, y + 27, fill="white", outline="blue")
            x = x + 33
        y = y + 27
    c.create_line(16, 405, 16, 16, width = 4)
    c.create_line(16, 16, 102, 16, width = 4)
    c.create_line(16, 54, 66, 16, width = 4)
    c.create_line(99, 16, 99, 58, width = 4)
faq = '''Hi player lets play!
 the rules are as follows: the computer thinks out a word and
  writes the first and last letter, as well as the gallows, 
  you must name the letters that, in your opinion, can be included in this word
   if the letter is really included in the word, then the computer writes it to the place of the pass,
   and if there are no such letters, then the computer draws 
   the human element on the gallows 
   if the person is fully assembled, then you will lose and if you hit the word, then you win'''

def change_let():
    bg()
    word = random.choice(words)
    help1 = word[1:-1]
    help2 = []
    for i in help1:
        help2.append(i)
    l0 = c.create_text(282, 40, text = word[0], fill = "purple", font = ("Helvetica", "18"))
    l1 = c.create_text(315, 40, text = "_", fill = "purple", font = ("Helvetica", "18"))
    l2 = c.create_text(347, 40, text = "_", fill = "purple", font = ("Helvetica", "18"))
    l3 = c.create_text(380, 40, text = "_", fill = "purple", font = ("Helvetica", "18"))
    l4 = c.create_text(412, 40, text = "_", fill = "purple", font = ("Helvetica", "18"))
    l5 = c.create_text(444, 40, text = "_", fill = "purple", font = ("Helvetica", "18"))
    l6 = c.create_text(477, 40, text = word[-1], fill = "purple", font = ("Helvetica", "18"))
    unknow = [1, 2, 3, 4, 5]
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    er = []
    win = []

    def add(let):
        ind_alf = alfabet.index(let)
        key = alfabet[ind_alf]

        if let in help2:
            temp = 0
            for i in help2:
                if i == let:
                    temp += 1
            while temp > 0:
                ind = help2.index(let)
                b2 = ind
                help2[ind] = '1'
                def kord():
                    x1, y1 = 0, 0
                    if b2 == 0:
                        x1, y1 = 315, 40
                    if b2 == 1:
                        x1, y1 = 347, 40
                    if b2 == 2:
                        x1, y1 = 380, 40
                    if b2 == 3:
                        x1, y1 = 412, 40
                    if b2 == 4:
                        x1, y1 = 444, 40
                    return x1, y1

                x1, y1 = kord()
                win. append(let)
                a2 = c.create_text(x1, y1, text = help1[ind],  fill = "purple", font = ("Helvetica", "18"))
                temp -= 1
            btn[key]["bg"] = "green"

            if not let  in help2:
                btn[key] ["state"] = "disabled"
            if let in help2:
                win.append(let)
                ind2 = help2.index (let)
                b2 = unknow[ind2]
                x1, y1 = kord()
                c.create_text(x1,y1, text = help1[ind2],  fill = "purple", font = ("Helvetica", "18"))
            if len(win) == 5:
                c.create_text(150, 150, text = "you won", fill = "purple", font = ("Helvetica", "18"))
                for i in alfabet:
                    btn[i]["state"] = ["disabled"]
        else:
            er.append(let)
            btn[key]["bg"] = "red"
            btn[key]["state"] = "disabled"
            if len(er) == 1:
                head()
            elif len(er) == 2:
                body()
            elif len(er) == 3:
                left_hand()
            elif len(er) == 4:
                right_hand()
            elif len(er) == 5:
                legs()
                end()
                root. update()
    btn = {}

    def gen (count,x, y):
        btn[count] = Button(root, text = count, width = 3, height = 1, command = lambda: add(count))
        btn[count].place(x = str(x), y=str(y))
    x = 265
    y = 110
    for i in alfabet[0:7]:
        gen(i, x, y)
        x += 33
    x = 265
    y = 137
    for i in alfabet[7:14]:
        gen(i, x, y)
        x += 33
    x = 265
    y = 164
    for i in alfabet[14:20]:
        gen(i, x, y)
        x += 33
    x = 265
    y = 191
    for i in alfabet[20:26]:
        gen(i, x, y)
        x += 33

    def head():
        c.create_oval(79,59, 120, 80, width = 4, fill = 'white')
        root.update()
    def body():
        c.create_line(100, 80, 100, 200, width = 4)
        root.update
    def body():
        c.create_line(100, 80, 100, 200, width = 4)
        root.update
    def left_hand():
        c.create_line(100, 80, 45, 100, width = 4)
        root.update
    def right_hand():
        c.create_line(100, 80, 145, 100, width = 4)
        root.update
    def legs():
        c.create_line(100,200, 45, 300, width = 4)
        c.create_line(100,200, 145, 300, width = 4)
        root.update
    def end():
        c.create_text(150, 150, text = "you lose", fill = "purple", font = ("Helvetica", "18"))
        for i in alfabet:
            btn[i]["state"] = "disabled"
c.create_text(400, 270, text = faq, fill = "purple", font = ("helvetica", "14"))
btn1 = Button(root, text ="start game", width = 10, height = 2, bg = "red", command = lambda: change_let())
btn1.place(x = 355, y = 538)


root.mainloop()