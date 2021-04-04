b = 0
a = int (input())
for i in range (1, a+1):
    if a % i == 0:
        print(i)
        b += 1
if b == 2:
     print ("simple")
else:
     print("no")
        
    
