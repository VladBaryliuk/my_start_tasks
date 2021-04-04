a = 0
c = 0
d = 0
while True:
    b = int(input())
    d += b
    if b > 1000:
        c = b % 20
        a += c
    elif b < 0:
        break
d -= a
print (d)
