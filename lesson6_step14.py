from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math


def calc(x, y):
  return str(x+y)

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.execute_script("alert('Robots at work');")
##    x_element = browser.find_element_by_id("num1")
##    x = x_element.text
##    x = int(x)
##    y_element = browser.find_element_by_id("num2")
##    y = y_element.text
##    y = int(y)
##
##    s = calc(x, y)
##
##    select_number = Select(browser.find_element_by_id("dropdown"))
##    select_number.select_by_value(s)
##    
##    button = browser.find_element_by_xpath("//button[@type='submit']")
##    button.click()
##
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
