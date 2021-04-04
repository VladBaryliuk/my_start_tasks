s = str (input())
arr = s.split()
letters = 0
word = ""
for i in arr:
    if len(i)>letters:
        word = i
        letters = len(i)
print(word)
