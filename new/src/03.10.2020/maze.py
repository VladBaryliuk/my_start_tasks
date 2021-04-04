from tkinter import *
root = Tk()
root.title('maze')

WIDTH = 480
HEIGHT = 304
c = Canvas(root, width=WIDTH, height=HEIGHT)

player = c.create_rectangle(17,17,31,31,fill = 'green')

level = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'W                           WW',
         'WWWW WWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWW          W             W',
         'WWWWWWWWWWWW  WWWWWWWWW  WWWW',
         'WWWWWWWWWWWW  WW  WWWWW  WWWWW',
         'W  WWWWWWWWW  WW  WWWWW  WWWWW',
         'W  WW         WW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W                            E',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         ]
exits = []
walls = []
x = 0
y = 0
for i in level:
    for g in i:
        if g == 'W':
            c.create_rectangle(x,y,x+16,y+16,fill = 'black')
            walls.append((x, y, x + 16, y + 16))
        elif g == 'E':
            c.create_rectangle(x,y,x+16,y+16,fill = 'white')
            exits.append((x, y, x + 16, y + 16))
        x += 16
    y += 16
    x = 0
def player_move(event):
    dx = dy =0
    key = event.keysym
    if key == "Up":
        dy = -4
    if key == "Down":
        dy = 4
    if key == "Left":
        dx = -4
    if key == "Right":
        dx = 4
    c.move(player, dx, dy)
    for wall in walls:
        if player in c.find_overlapping(wall[0], wall[1], wall[2], wall[3]):
            c.move(player, -dx, -dy)
    for e in exits:
        if player in c.find_overlapping(e[0], e[1], e[2], e[3]):
            c.create_text(300,200,text = 'you are winner')
c.bind_all('<Key>', player_move )
c.pack()
