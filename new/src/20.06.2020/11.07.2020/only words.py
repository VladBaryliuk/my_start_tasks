list_of_input = input().split()
print(list_of_input)

count = 0
  # 3 параметр в range(1, 4, 2) 2 это насколько будет увеличеваться
for i in range(len(list_of_input)):
    if i > 0:
        if list_of_input[i].isalpha() and list_of_input[i-1].isalpha():
            print(list_of_input[i-1], list_of_input[i])
            count += 1
if count == 0:
    print("few words")
