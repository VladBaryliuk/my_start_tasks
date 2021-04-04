string = str (input())
string_copy = string
new_string = string.replace(string[0],string[-1])
new_string = string_copy.replace(string_copy[-1],string_copy[0])
print(new_string)
