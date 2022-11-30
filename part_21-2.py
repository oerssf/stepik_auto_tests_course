from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element(by='id', value='treasure')
    x_element1 = x_element.get_attribute("valuex")
    x = x_element1
    y = calc(x)
    
    input1 = browser.find_element(by='id', value='answer')
    input1.send_keys(y)

    option1 = browser.find_element(by='id', value='robotCheckbox')
    option1.click()
    option2 = browser.find_element(by='id', value='robotsRule')
    option2.click()

    button = browser.find_element(by='css selector', value="button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
