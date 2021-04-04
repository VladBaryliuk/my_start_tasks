from tkinter import *
import random
root = Tk()
root.geometry("225x230")
root.resizable = False
root.title = ("learning English")
words = {"FIRE": "ОГОНЬ", "KEY": "КЛЮЧ", "CASTLE": "ЗАМОК", "SCHOOL": "ШКОЛА", "TEACHER": "УЧИТЕЛЬ"}
cnt = 0
rus_words = words
eng_words = dict([[v, k]for k,v in words.items()])
def show_menu():
    menu1.pack()
    menu2.pack()
def hide_menu():
    menu1.pack_forget()
    menu2.pack_forget()
def choose_word(languege):
    if languege == "rus":
        word = random.choice([i for i in rus_words])
    else:
        word = random.choice([i for i in eng_words])
    return word
def start_level(languege):
    hide_menu()
    word = choose_word(languege)
    def choose_letter(button):
        global cnt

        if button.cget("text") == word[cnt] and button.cget("bg") != "green":
            button.config(bg = "green")
            label_2.config(text = label_2.cget("text") + word[cnt])
            cnt += 1
        elif button.cget("bg") != "green":
            for i in buttons:
                i.config(bg = "SystemButtonFace")
            label_2.config(text = "")
            cnt = 0
        if cnt > len(word) - 1:
            cnt = 0
            delete()
            show_menu()
    def delete():
        del letters[:]
        for i in buttons:
            i.destroy()
        del buttons[:]
        label_1.destroy()
        label_2.destroy()

    if languege == "rus":
        random_letters = [random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")for i in range (25-len(word))]
        label_1 = Label(root, text = rus_words.get(word), font = "Arial 20")
        label_1.grid(columnspan=5, sticky="ew")
        label_2 = Label(root, text="", font="Arial 20")
        label_2.grid(columnspan=5, sticky="ewsn")
    elif languege == "eng":
        random_letters = [random.choice("АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ")for i in range(33-len(word))]
        label_1 = Label(root, text = eng_words.get(word), font = "Arial 20")
        label_1.grid(columnspan=5, sticky="ew")
        label_2 = Label(root, text="", font="Arial 20")
        label_2.grid(columnspan=5, sticky="ewsn")
    letters = [i for i in word]
    letters += random_letters
    random.shuffle(letters)
    buttons = []
    column = 0
    row = 3
    for i in range(0, len(letters) - 1):
        buttons.append(Button(root, text=letters[i], width=5))
        buttons[i].config(command=lambda button=buttons[i]: choose_letter(button))
        buttons[i].grid(column=column, row=row, sticky="ew")
        column += 1
        if column > 4:
            column = 0
            row += 1


menu1 = Button(root, text = "can you translate?\nENG -> RUS", height = 7, width = 32, command = lambda lang = "eng": start_level(lang))
menu2 = Button(root, text = "can you translate?\nRUS -> ENG", height = 7, width = 32, command = lambda lang = "rus": start_level(lang))


show_menu()


root.mainloop()
