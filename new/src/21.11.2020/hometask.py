from selenium import webdriver
from selenium.webdriver.common.by import By
import time

my_file = open("just_file.txt", "w")
videos =[]
browser = webdriver.Chrome(r'd:\Программирование\Влада программирование\chromedriver_win32\chromedriver.exe')
browser.get('https://www.youtube.com/user/MasterskayaNastroeny/videos')
time.sleep(2)

for g in range(12):
    browser.execute_script("window.scrollTo(0,10000000);")
    videos.append(browser.find_elements(By.CLASS_NAME, 'yt-simple-endpoint'))
    time.sleep(1)
for i in videos:
    for y in set (i):
        if len(y.text) < 20:
            del y
        else:
            print(y.text)
            my_file.write(y.text + '\n')
my_file.close()