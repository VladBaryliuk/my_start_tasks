list1 = [int(j) for j in input().split()]
n = int(input())
for i in list1:
    if i < n:
        if i+1 == n :
            print(i)
