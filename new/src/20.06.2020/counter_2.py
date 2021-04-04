from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root = Tk()
root.title("counter")
calc_entry = Entry(root, width = 10)

#counter's logics
def calc(key):
    global memory
    if key == "=":
#exclude spelling
        strl = "+0123456789-*/"
        if calc_entry.get()[0] not in strl:
            calc_entry.insert(END,"first simbol is not number!")
            messagebox. showerror("error!","you write not number!")

#count
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str (result))
        except:
                calc_entry.insert(END, "ERROR")
                messagebox.showerror("ERROR","check the correctness of the data")
#clear field
    elif key == "c":
        calc_entry.delete(0, END)
#change +-
    elif key == "-/+":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END,key)
#create all buttons
button_list = ["7","8","9","+","-",
               "4","5","6","*","/",
               "1","2","3","-/+","=",
               "0","c"]


r = 1
c = 0
for i in button_list:
    rel = ""
    cmd= lambda x = i:calc(x)
    ttk.Button(root,text=i, command = cmd).grid(row = r, column=c)
    c += 1
    if c>4:
        c=0
        r+=1

calc_entry.grid(row = 0,column = 0 ,columnspan = 5 )
root.mainloop()