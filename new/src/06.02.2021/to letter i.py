alfabet ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
human_string = str(input("enter your string in the russian language"))
def before_letter_i():
    global human_string
    for i in human_string:
        if i < "и":
            human_string = human_string.replace(i, "")
    return human_string
print(before_letter_i())