from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
way = r'd:\Программирование\Влада программирование\chromedriver_win32\chromedriver.exe'
browser = webdriver.Chrome(r'd:\Программирование\Влада программирование\chromedriver_win32\chromedriver.exe')
browser.get('https://portal.itgen.io/')
WebDriverWait(browser, 20). until(EC.element_to_be_clickable((By.TAG_NAME, "button")))
username_field = browser. find_element(By.NAME, 'username')
username_field.send_keys('14480747')
password_field = browser. find_element(By.NAME, 'password')
password_field.send_keys(' q1ti5ruq')
accept_button = browser. find_element(By.TAG_NAME, "button")
accept_button.click()
WebDriverWait(browser, 20). until(EC. element_to_be_clickable((By.TAG_NAME, "button")))
chat_button = browser. find_element(By.CLASS_NAME, "chat-button")
chat_button.click()
WebDriverWait(browser, 20). until(EC. element_to_be_clickable((By.CSS_SELECTOR, "div[class='room-item']")))
chats = browser. find_elements(By.CSS_SELECTOR, ".room-item")
chats[1].click()
WebDriverWait(browser, 20). until(EC. element_to_be_clickable((By.TAG_NAME, "text_area")))
message_field = browser. find_element(By.TAG_NAME, "text_area")
message_field.send_keys("я выполнил задание")
buttons = browser. find_elements(By.TAG_NAME, "swg")
send_button = buttons[1]
send_button.click()