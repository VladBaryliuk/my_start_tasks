# list1 = [i for i in range(5, 16)]
# print(list1)
# list1 = [i for i in range(0, 11)]
# for i in range(11):
#     if i > 0:
#          print(list1[i-1] * list1[i])
# list1 = [i * j for i in range(1, 10) for j in range(1, 10)]
# print(list1)

str1 = str(input())
strArray = list(str1)
newList = []
for i in strArray:
    if i > "e":
        del i
    else:
        newList.append(i)

print(*newList)