from tkinter import *
root = Tk()
root.title('rainbow')
root.geometry('205x380')
root.bg= "white"
root.resizable(False,False)

def change_label(index):
        lb_color.config(text=colors[index])
        lb_code.config(text=code[index])

lb_color=Label(text ='', font ='Arial,14', bg='#ffffff', width=20, height=2)

lb_color.pack()
lb_code=Label(text ='', font ='Arial,14', bg='#ffffff', width=20, height=2)

lb_code.pack()

code=['#FF0000','#FFA500','#FFFF00','#008000','#000080',
      '#0000FF','#4B0082']
for index in range (len(code)):
    btn=Button(bg=code[index],width=25,height=2,command=lambda index1=index:change_label(index1))
    btn.pack()
colors=["красный", "оранжевый", "желтый", "зеленый", "синий","голубой", "фиолетовый"] 

root.mainloop()  
