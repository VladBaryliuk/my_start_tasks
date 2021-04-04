list_of_input = list(input())
list_of_input2 = list(input())
test_list = list()
count = len(list_of_input)
count2 = len(list_of_input2)


def count_for(temp_list, temp_list2):

    for i in range(len(temp_list)):
        count_test = 0
        for j in range(len(temp_list2)):
            if temp_list[i] == temp_list2[j]:
                for g in range(len(test_list)):
                    if temp_list[i] == test_list[g]:
                        count_test += 1
        if count_test == 0:
            test_list.append(temp_list[i])


if count == count2 or count < count2:
    count_for(list_of_input, list_of_input2)

else:
    count_for(list_of_input2, list_of_input)

print(*test_list)
