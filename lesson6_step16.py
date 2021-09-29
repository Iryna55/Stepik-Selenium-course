from selenium import webdriver
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    button = browser.find_element_by_class("btn.btn-primary")
    button.click()

    confirm = browser.switch_to.confirm
    confirm.accept()
    
    
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
