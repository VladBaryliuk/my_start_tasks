s = input().lower()
string = ""
for i in s:
    if i.isalpha() or i.isspace():
        string+=i

string = string.split()
words = input().split()
a = []

for i in string:
    if i in words and i not in a:
        a.append(i)

if a == words:
    print("Yes")
else:
    print("No")