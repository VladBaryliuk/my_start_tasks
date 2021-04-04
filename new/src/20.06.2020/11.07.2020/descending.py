list_of_input = list(input())
list_of_input_test = sorted(list_of_input, reverse=True)
if list_of_input == list_of_input_test:
    print("yes")
else:
    print("no")