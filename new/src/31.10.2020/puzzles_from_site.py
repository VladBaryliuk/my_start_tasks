import requests
from bs4 import BeautifulSoup
import random

link = 'https://www.riddles.com/riddle-of-the-day'
r = requests.get(link)
soup = BeautifulSoup(r.text, 'html.parser')
riddles = soup.find_all('blockquote', {'class': 'orange_dk_blockquote hidden-print'})
answers = soup.find_all('blockquote', {'class': 'dark_purple_blockquote'})

new_riddles = []
new_answers = []


def slice(title):
    start = title.find('>') + 1
    end = title[2:].find('<') + 1
    return title[start:end]


def create_new_list(list_first):
    list_smth = [i1.find_all('p') for i1 in list_first]
    new_list = [slice(str(i2)) for i2 in list_smth]

    return new_list


riddles = create_new_list(riddles)
answers = create_new_list(answers)

game = True
while game:
    riddle_index = random.randint(1, len(riddles) - 1)
    print(riddles[riddle_index])
    for i in range(3):
        players_answer = str(input())
        if players_answer == answers[riddle_index]:
            print("you are right")
            break
        elif players_answer != answers[riddle_index] and i < 2:
            print("alas, the answer is not correct")
        elif i == 2:
            print("alas, the answer is not correct right answer was ", answers[riddle_index])
            game = False
