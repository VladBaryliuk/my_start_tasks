password = input()
alpha = False
upalpha = False
digit = False
for i in password:
    if i.isspace():
        print("NOPE")
        break
    if i.isdigit():
        digit = True
    if i.isalpha():
        if i.isupper():
            upalpha = True
        if i.islower():
            alpha = True
else:
    if alpha and upalpha and digit:
        print("OK")
    else:
        print("NOPE")
