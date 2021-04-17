from tkinter import *
root = Tk()
root.title('maze')

WIDTH = 480
HEIGHT = 304
c = Canvas(root, width=WIDTH, height=HEIGHT)


level1 = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WP                         KWW',
         'WWWW WWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWW          W             WW',
         'WWWWWWWWWWWW  WWWWWWWWW  WWWWW',
         'WWWWWWWWWWWW  WWK WWWWW  WWWWW',
         'WK WWWWWWWWW  WW  WWWWW  WWWWW',
         'W  WW         WW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W                 D          E',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         ]

exits = []
walls = []
keys = []
doors = []
players = []
def create_level():
    x = 0
    y = 0
    for i in level1:
        for g in i:
            if g == 'W':
                wall = c.create_rectangle(x,y,x+16,y+16,fill = 'black')
                walls.append(wall)
            elif g == 'E':
                exit = c.create_rectangle(x,y,x+16,y+16,fill = 'orange')
                exits.append(exit)
            elif g == 'K':
                key = c.create_rectangle(x,y,x+16,y+16,fill = 'yellow')
                keys.append(key)
            elif g == 'D':
                door = c.create_rectangle(x,y,x+16,y+16,fill = 'red')
                doors.append(door)
            elif g == 'P':
                player = c.create_rectangle(17,17,31,31,fill = 'green', outline = 'green')
                players.append(player)
            x += 16
        y += 16
        x = 0
create_level()
def player_move(event):
    player = players[0]
    x = y =0
    key = event.keysym
    if key == "Up":
        y = -4
    if key == "Down":
        y = 4
    if key == "Left":
        x = -4
    if key == "Right":
        x = 4
    c.move(player, x, y)

    for wall in walls:
        x1,y1,x2,y2 = c.coords(wall)
        if player in c.find_overlapping(x1, y1, x2, y2):
            c.move(player, -x, -y)
    for key in keys:
        x1,y1,x2,y2 = c.coords(key)
        if player in c.find_overlapping(x1, y1, x2, y2):
            c.delete(key)
            keys.remove(key)
            if len(keys) == 0:
                doors[0].itemconfig(fill = 'blue')
    for door in doors:
        x1,y1,x2,y2 = c.coords(door)
        if player in c.find_overlapping(x1, y1, x2, y2) and len(keys) != 0:
            c.move(player, -x, -y)
    for wall in walls:
        x1,y1,x2,y2 = c.coords(wall)
        if player in c.find_overlapping(x1, y1, x2, y2):
            c.create_text(300,200,"you win")

c.bind_all('<Key>', player_move )
c.pack()

root.mainloop()