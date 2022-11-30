﻿from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(by='name',value='firstname')
    print(input1)
    input1.send_keys("Ivan")
    input2 = browser.find_element(by='name', value='lastname')
    print(input2)
    input2.send_keys("Petrov")
    input3 = browser.find_element(by='name', value='email')
    print(input3)
    input3.send_keys("petrov@mail.ru")

    element = browser.find_element(by='name',value='file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "bio_form.txt"
    file_path = os.path.join(current_dir, file_name)
    element.send_keys(file_path)

    
    button = browser.find_element(by='css selector', value="button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

