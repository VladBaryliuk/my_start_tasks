import random
NUMDIGITS = 3
MAXGUESS = 10

print('Я задумал %s-значное число. Попробуйте угадать его.' % (NUMDIGITS))
print(' вот некоторые подсказки:')
print(' когда я говорю: это означает:')
print('  Быки - одна цифра правильная и в правильном положении.')
print('  Коровы - одна цифра является правильным, но в неправильном положении.')
print('  Не угадал – нет правильных цифр.')

def getSecretNum(numDigits):
    numbers=list(range(10))
    random.shuffle(numbers)
    list(range(10))
    secretNum=''
    for i in range(numDigits):
        secretNum += str(numbers[i])
    return secretNum
def getClues(guess, secretNum):
    if guess == secretNum:
        return'you guessed'
    clue =  []
    for i in range (len(secretNum)):
        if guess[i] == secretNum[i]:
            clue.append('bulls')
        elif guess[i] in secretNum:
            clue.append('cows')
    if len(clue) == 0:
        return"there aren't correct numbers"
    clue.sort()
    return ' '.join(clue)
def isOnlyDigits (num):
     if num =="":
        return False
     for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False
     return True
def playAgain():
     print("do you want to play again (yes or no)")
     return input(). lower(). startswith('yes')
getSecretNum(NUMDIGITS)
while True:
    secretNum = getSecretNum(NUMDIGITS)
    print('Я задумал %s-значное число. Попробуйте угадать его.' % (NUMDIGITS))
    numGuesses = 1
    while numGuesses <= MAXGUESS:
        guess = ""
        while len(guess) != NUMDIGITS or not isOnlyDigits(guess):
            print('У тебя  %s попытка ' % (numGuesses))
            guess = input()
        clue = getClues(guess, secretNum)
        print(clue)
        numGuesses += 1
    if guess == secretNum:
        break
    if numGuesses > MAXGUESS:
        print(' У вас закончились попытки. Ответ был %s.' % (secretNum))
    if not playAgain():
        break

