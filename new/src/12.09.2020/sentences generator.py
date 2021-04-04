import random
global sentence
sentence = []
def function(words):
    for i in range(len(words)):
        sentence.append(random.choice(words))
        if i >= len(words):
            break
    return sentence
print(*function(input().split()))