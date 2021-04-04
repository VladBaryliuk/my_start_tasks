str1 = str(input())
str_list = list(str1)
list1 = list(input())

breakFlag = -1
index = -1
newInt = 0
for i in range(len(list1)):
    count = 0
    if breakFlag == 1:
        break
    for j in range(len(str_list)):

        if count == len(str_list)-1:
            newInt = 1
        if list1[i] != str_list[j] or str_list[j] == ' ' and list1[i] != ' ':
            count += 1
        if list1[i] != ' ' and str_list[j] != ' ' and list1[i] == str_list[j]:
            count = 100
            if j > index:

                index = j
                breakFlag = 0
            else:
                breakFlag = 1
                break
if breakFlag == -1:
    print("No matches")

elif breakFlag == 0 and newInt != 1:
    print("Yes")

elif breakFlag == 1 or newInt == 1 :
    print("No")

