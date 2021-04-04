a = 0
b = 0
c = 0
while True:
    d = float (input())
    if d < -300:
        c = a / b
        break
    a += d
    b += 1
print (c)
