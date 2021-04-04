a = int (input())
b = int (input())
for i in range (a,b+1):
    if a > b:
        print ("error")
    elif i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print (i)
