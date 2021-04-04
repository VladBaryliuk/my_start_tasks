from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
window = Tk()
window.title('text editor')  
def loadfile():
    filename = filedialog.Open(window,filetypes = [('*.txt files', '.txt')]).show()
    if filename == '':
        return
    textbox.delete('1.0', 'end')
    textbox.insert('1.0',open(filename,'rt').read())
def savefile(): 
    filename = filedialog.SaveAs(window,filetypes = [('*.txt files', '.txt')]).show()
    if filename == '':
        return
    if not filename.endswith(".txt"):
        filename+=".txt"
    open (filename,'wt').write(textbox.get('1.0', 'end'))
def Quit():
        global window
        window.destroy()
panel = Frame(window,height = 60,bg = 'gray')
panel.pack(side = 'top',fill = 'x')
textframe = Frame(window,height = 340,width = 600)
textframe.pack(side = 'bottom',fill = 'both')
textbox = Text(textframe,wrap = 'word',font = 'Verdana')
textbox.pack(side = 'left',fill = 'both')
scroll = Scrollbar(textframe)
scroll.pack(side = 'right',fill = 'y')
scroll['command'] = textbox.yview
textbox['yscrollcommand'] = scroll.set
load = Button(panel,text = 'load',bg = 'blue',command = loadfile)
load.place(x = 25,y = 10,width = 60,height = 40)
save = Button(panel,text = 'save',bg = 'green',command = savefile)
save.place(x = 125,y = 10,width = 60,height = 40)
quitt = Button(panel,text = 'quit',bg = 'red',command = Quit)
quitt.place(x = 225,y = 10,width = 60,height = 40)
