import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_items(browser):
    browser.get(link)
    time.sleep(30)
    button = browser.find_element_by_css_selector("button[value='Add to basket']")
    assert button , "No button"
    
