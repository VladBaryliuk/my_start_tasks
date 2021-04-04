string = str (input())
arr = string.split()
print (arr)
print (arr[0])
print("Вывожу количество вхождений буквы а: ", arr[0].count("a"))
if arr[1].count("a")== 0:
    print("error")
print(arr[1].replace("a","A"))
print(len(arr[2]))
