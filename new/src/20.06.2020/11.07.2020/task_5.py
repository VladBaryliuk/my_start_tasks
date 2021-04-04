list_of_input = list(input())

sum = 0
if len(list_of_input) == 0:
    print(0)
else:
    for i in range(len(list_of_input)):
        if i % 2 == 0:
           sum += int(list_of_input[i])

    result = sum * int(list_of_input[0])
    print(result)
