from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element1 = browser.find_element(by='id', value='num1')
    x_element2 = browser.find_element(by='id', value='num2')
    x1 = x_element1.text
    x2 = x_element2.text
    y = int(x1) + int(x2)
    
    select = Select(browser.find_element(by='id', value='dropdown'))
    select.select_by_value(str(y))

    button = browser.find_element(by='css selector', value="button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
