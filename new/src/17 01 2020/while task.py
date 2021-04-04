#дом с приведениями
import random
print ("дом с приведениями")
score = 0
while True:
    ghost_door = random. randint (1,3)
    print("ты в страшном и большом доме...")
    print("перед тобой 3 двери...")
    print("за одной приведение")
    print("в какую из дверей ты решишься зайти")
    door_num = int(input("1,2 ,или 3"))
    if door_num ==ghost_door:
        print("ааа это приведение")
        print("у тебя получилось убежать")
    else:
        score +=1
        print ("пронесло тут нет приведения")
    fatigue = input ("ты устал?")
    if fatigue == "да":
        print ("жалко я так хотел с тобой поиграть ладно уходи")
        break
    else:
        print ("хорошо, играем дальше")
print ("ты открыл",score,"дверь(ей)")
    
