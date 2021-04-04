string = str (input())
anumber = string.find("a")
bnumber = string.find("b")
if anumber<bnumber:
    print("a")
if bnumber<anumber:
    print("b")
else:
    print("error")
