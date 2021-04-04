import random
draws = 0
comp_wins = 0
player_wins = 0
rounds = int(input("how many rounds do you want to play:"))
defeated_by = {"stone": "scissors" "lizard", "scissors": "paper" "lizard", "paper": "stone" "spok", "lizard": "spok" "paper", "spok": "scissors" "stone"}
elem_list = (list(defeated_by.keys()))
i = 1
while i < rounds + 1:
    print("Round: ", i)
    players_element = str(input("choose the element(stone, scissors or paper):"))
    computer_element = random.choice(elem_list)
    print("computer chose:", computer_element)
    if computer_element in defeated_by.get(players_element):
        print("player won")
        player_wins += 1
    elif computer_element == players_element:
        print("draw")
        draws += 1
        i -= 1
    else:
        print("computer won")
        comp_wins += 1
    i += 1
print("there are", draws, "draws")
print("there are", player_wins, "player's wins")
print("there are", comp_wins, "computer's wins")

