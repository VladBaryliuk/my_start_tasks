import time 
import random
messages = [
"Из всех деревьев мы врезались в то, которое смогло дать нам сдачи.",
"Если не прекратить его попытки спасти вам жизнь, он вас убьет.",
"Нашу сущность намного лучше демонстрируют действия, а не возможности.",
"Я маг, а не размахивающий палкой бабуин.",
"Величие порождает зависть, зависть — злобу, злоба — ложь.",
"В мечтах мы попадаем в наш и только наш мир.",
"Я убежден, что истина, как правило, предпочтительнее лжи.",
"Казалось, что рассвет следует за полночью с неприличной поспешностью." 
]
print("Проверка скорости набора. Введите следующую фразу. Я засеку время…")

time.sleep(2)

print("приготовиться")

time.sleep(1)

print("сосредоточиться...")

time.sleep(1)

print("начали")

message = random.choice(messages)
print(message)

start_time = time.time()
answer = input(str())
end_time = time.time()
delta = end_time-start_time
speed = len(answer) / delta
print("You introduced" ,len(answer),"characters from",delta,"seconds" )
print("You introduced",speed,"characters in 1 second")
print ("You shoulded to introduc string",message,".And you introduced",answer)
