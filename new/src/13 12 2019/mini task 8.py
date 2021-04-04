a = float (input())
b = float (input())
c = str (input())
if c == "+":
    print (a + b)
elif c == "-":
    print (a - b)
elif c == "*":
    print (a * b)
elif c == "/":
    print (a / b)
else:
    print("error")
if b == 0 and c == "/":
    print ("error")
