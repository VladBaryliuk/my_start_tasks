import random
def oddrandom(a,b):
    global result
    result = random.randint(a,b)
    if result % 2 != 0:
        return result
    else:
        return result-1
oddrandom(int(input()),int(input()))
def check(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
    if counter == 2:
        return True
    elif counter != 2:
        return False

print(check(result))