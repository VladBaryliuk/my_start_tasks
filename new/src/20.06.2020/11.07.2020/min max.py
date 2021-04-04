list1 = list(input())
min1 = min(list1)
print(min1)
max1 = max(list1)
print(max1)
if min1.isdigit() and max1.isdigit():
    maxmin =int(max1)-int(min1)

print(maxmin)
print("список случайных чисел:",list1,
      "максимальное число из списка:",max1,
      "минимальное число из списка:",min1,
      "разница между максимальным и минимальным:",maxmin)