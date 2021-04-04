from tkinter import *
root = Tk()
root.geometry('400x300')
root.title('cinemalover')
text = Label(root, text="Укажите Ваши любимые жанры кино:")
text.grid()
flags_comedy = StringVar()
flags_drama = StringVar()
flags_love = StringVar()
flags_detective = StringVar()
flags_action_films = StringVar()
flags_adventure_films = StringVar()
ch_comedy = Checkbutton(root, text="Комедии", var=flags_comedy, onvalue="Комедии",offvalue="-")

ch_drama = Checkbutton(root, text="Драма", var=flags_drama, onvalue="Драма",offvalue="-")

ch_love = Checkbutton(root, text="Фильмы о любви", var=flags_love, onvalue="Фильмы о любви",offvalue="-")

ch_detective = Checkbutton(root, text="детектив", var=flags_detective, onvalue="детектив",offvalue="-")

ch_action_films = Checkbutton(root, text="боевики", var=flags_action_films, onvalue="боевики",offvalue="-")

ch_adventure_films = Checkbutton(root, text="приключеньческие фильмы", var=flags_adventure_films, onvalue="приключеньческие фильмы",offvalue="-")

lis = Listbox(root, height=6)
ch_comedy.deselect()
ch_drama.deselect()
ch_love.deselect()
ch_detective.deselect()
ch_action_films.deselect()
ch_adventure_films.deselect()
def result(event):
    var1 = flags_comedy.get()
    var2 = flags_drama.get()
    var3 = flags_love.get()
    var4 = flags_detective.get()
    var5 = flags_action_films.get()
    var6 = flags_adventure_films.get()
    vars = [var1, var2, var3,var4,var5,var6]
    lis.delete(0, 5)
    for v in vars:
        lis.insert(END, v)
btn = Button(root, text="Узнать результат!")
btn.bind('<Button-1>', result)
ch_comedy.grid()
ch_drama.grid()
ch_love.grid(columnspan=2)
ch_detective.grid()
ch_action_films.grid()
ch_adventure_films.grid(columnspan=2)
btn.grid()
lis.grid()
