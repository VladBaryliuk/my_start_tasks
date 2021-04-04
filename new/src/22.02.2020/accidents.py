import random
a = ''
random.choice ("abcdefghimnopqrstuvwxyz")
for i in range(5):
    a+=random.choice ("abcdefghimnopqrstuvwxyz")
    a+=random.choice ("1234567890")
print(a)
