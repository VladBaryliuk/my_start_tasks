a = 0
sstr = 0
while True:
    c = float (input())
    sstr += 1
    if c > 22.0:
        break
    elif sstr == 7:
        a = sstr // 7
print (a)
