from tkinter import *

root = Tk()
root.title('paint')

width = 700
height = 500
brush_size = 3
color = 'black'
c = Canvas(width=width, height=height, bg='white')


def paint(event):
    global brush_size
    global color
    x1 = event.x - brush_size
    x2 = event.x + brush_size
    y1 = event.y - brush_size
    y2 = event.y + brush_size
    c.create_oval(x1, y1, x2, y2,
                  fill=color, outline=color)


def change_brush_size(new_size):
    global brush_size
    brush_size = new_size


def change_color(new_color):
    global color
    color = new_color


c.bind("<B1-Motion>", paint)

red_btn = Button(text="red", width=10,
                 command=lambda: change_color("red"))
yellow_btn = Button(text="yellow", width=10,
                    command=lambda: change_color("yellow"))
white_btn = Button(text="rubber", width=10,
                   command=lambda: change_color("white"))
blue_btn = Button(text="blue", width=10,
                  command=lambda: change_color("blue"))
black_btn = Button(text="black", width=10,
                   command=lambda: change_color("black"))
clear_btn = Button(text="delete all", width=10,
                   command=lambda: c.delete("all"))
change_size_5_btn = Button(text="change_size5", width=10,
                           command=lambda: change_brush_size(5))
change_size_7_btn = Button(text="change_size7", width=10,
                           command=lambda: change_brush_size(7))
change_size_10_btn = Button(text="change_size10", width=10,
                            command=lambda: change_brush_size(10))
change_size_12_btn = Button(text="change_size12", width=10,
                            command=lambda: change_brush_size(12))
change_size_3_btn = Button(text="change_size3", width=10,
                           command=lambda: change_brush_size(3))
c.grid(row=2, column=0,
       columnspan=7, padx=5,
       pady=5, sticky="E" + "W" + "S" + "N")
c.columnconfigure(6, weight=1)
c.rowconfigure(2, weight=1)

red_btn.grid(row=0, column=2)
yellow_btn.grid(row=1, column=2)
white_btn.grid(row=0, column=1)
blue_btn.grid(row=1, column=1)
black_btn.grid(row=0, column=3)
clear_btn.grid(row=1, column=3)

change_size_5_btn.grid(row=0, column=4)
change_size_7_btn.grid(row=1, column=4)
change_size_10_btn.grid(row=0, column=5)
change_size_12_btn.grid(row=1, column=5)
change_size_3_btn.grid(row=0, column=6)
root.mainloop()
