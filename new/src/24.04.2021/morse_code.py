from tkinter import *
from winsound import *
root = Tk()
root.geometry('500x300')

mc = {'a': ['•—', 'A.waw'], 'b': ['—•••', 'B.waw'], 'c': ['—•—•', 'C.waw'], 'd': ['—••', 'D.waw'], 'e': ['•', 'E.waw'], 'f': ['••—•', 'F.waw'], 'g': ['——•', 'G.waw'], 'h': ['••••'], 'i': ['••', 'I.waw'],
      'j': ['•———', 'J.waw'], 'k': ['—•—', 'K.waw'], 'l': ['•—••', 'L.waw'], 'm': ['——', 'M.waw'], 'n': ['—•', 'N.waw'], 'o': ['———', 'O.waw'], 'p': ['•——•', 'P.waw'], 'q': ['——•—'], 'r': ['•—•', 'R.waw'],
      's': ['•••', 'S.waw'], 't': ['—', 'T.waw'], 'u': ['••—', 'U.waw'], 'v': ['•••—', 'V.waw'], 'w': ['•——', 'W.waw'], 'x': ['—••—', 'X.waw'], 'y': ['—•——', 'Y.waw'], 'z': ['——••', 'Z.waw']}


def code():
    new_string = ''
    for i in en1.get().upper():
        i = i.lower()
        new_string += mc[i][0] + ' '
        l1.config(text=new_string)
        root.update()
        PlaySound('sounds/%s' % mc[i][1], SND_FILENAME)


l1 = Label(root, text='Enter the word:', font='Verdana 28')
en1 = Entry(root, font='Verdana 28')
btn01 = Button(root, text='translate', font='Verdana 18',
               command=code)
l1.pack()
en1.pack()
btn01.pack()

root.mainloop()
