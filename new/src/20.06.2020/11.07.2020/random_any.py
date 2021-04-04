import random

list_of_random = []

n = int(input())
for i in range(n):
    list_of_random.append(random.randint(1, 100))

print(*list_of_random)