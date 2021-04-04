s = str(input())

list1=list(s)
print('List =   ',list1)

for x in list1:
    if not x.isalpha():
        list1.remove(x)
        
str = ''.join(list1)
print('Our words =   ', str)

