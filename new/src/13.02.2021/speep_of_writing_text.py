import time
import random
messages = ["Don't be dashing while it is quiet.",
"Friend is known in trouble.",
"Still waters run deep.",
"Being a guest is good, but being at home is better."]
print("Checking the speed of typing. I will mark the time ... ")
time.sleep(2)
print("On your marks…")
time.sleep(1)
print("Attention…")
time.sleep(1)
print("start ...")
phrase = random.choice(messages)
print(phrase)
start_time = time.time()
answer = str(input())
end_time = time.time()
user_time = end_time - start_time
rounded_user_time = round(user_time, 6)
print("You wrote ", len(phrase), "symbols for ", rounded_user_time, "seconds")
if answer == phrase:
    print("You have no mistakes")
elif answer != phrase:
    mistake_count = 0
    for i in range(len(answer)):
        if answer[i] != phrase[i]:
            mistake_count += 1
            print("You have written ", answer[i], "instead of", phrase[i])
    print("you have", mistake_count, "mistakes")

