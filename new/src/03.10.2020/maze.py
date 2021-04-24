from tkinter import *
root = Tk()
root.title('maze')

WIDTH = 480
HEIGHT = 304
c = Canvas(root, width=WIDTH, height=HEIGHT)

current_level = 0
level1 = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WP                          WW',
         'WWWW WWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWW          W             WW',
         'WWWWWWWWWWWW  WWWWWWWWW  WWWWW',
         'WWWWWWWWWWWW  SS  WWWWW  WWWWW',
         'W  WWWWWWWWW  WW  WWWWW  WWWWW',
         'W  WW         WW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W  WW  WWWWWWWWW  WWWWW  WWWWW',
         'W                KD          E',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
         ]
level2 = ['WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
          'WP      WWWWWWWWWWWWWWWWWWWWWW',
          'WW WWWWWWWWWWWWWWWWWWWWWWWWWWW',
          'WW        WWWWWWWWWWWWWWWWWWWW',
          'WW WWWWWWSWWWWWWWWWWWWWWEEEWWW',
          'WW WWWWWWKWWWWWWWWWWWWWW   WWW',
          'WW    WWWWWWWWWWWWWWWWWW  WWWW',
          'WWKWW WWWWWWWWWWWWWWWWWW  WWWW',
          'WWWWW WWWWWWWWWWWWWWWWWWW WWWW',
          'WWWWW             SSSSKWW    W',
          'WWWWWWWWW WWWWWWW WWWWWWWWWW W',
          'WWWWWWWWW        kWWWWWWWWWW W',
          'WWWWWWWWW WWWWWWWWWWWWWWWWWWDW',
          'WWWWWWWWW                  SSW',
          'WWWWWWWWWWWWWWWWWW WWWWWWWWWWW',
          'WWWWWWWWWWK         WWWWWWWWWW',
          'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
          ]
levels = [level1, level2]
secrets = []
exits = []
walls = []
keys = []
doors = []
players = []
def create_level(level_number):
    exits.clear()
    walls.clear()
    keys.clear()
    doors.clear()
    players.clear()
    x = 0
    y = 0
    for i in levels[level_number]:
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
                player = c.create_rectangle(17, 17, 31, 31, fill='green', outline='green')
                players.append(player)
            elif g == 'S':
                secret = c.create_rectangle(x, y, x+16, y+16, fill='black')
                secrets.append(secret)
            x += 16
        y += 16
        x = 0

create_level(current_level)
def player_move(event):
    global current_level
    player = players[0]
    x = y = 0
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
                c.itemconfig(doors[0], fill='blue', outline='green')
    for door in doors:
        x1,y1,x2,y2 = c.coords(door)
        if player in c.find_overlapping(x1, y1, x2, y2) and len(keys) != 0:
            c.move(player, -x, -y)
    for exit in exits:
        x1,y1,x2,y2 = c.coords(exit)
        if player in c.find_overlapping(x1, y1, x2, y2):
            c.delete("all")
            current_level += 1
            if current_level < len(levels):
                create_level(current_level)
                c.bind_all('<Key>', player_move )
            if current_level == len(levels):
                c.create_text(50, 50, text = 'You won')
                c.unbind_all('<Key>')
                return


c.bind_all('<Key>', player_move )
c.pack()

root.mainloop()