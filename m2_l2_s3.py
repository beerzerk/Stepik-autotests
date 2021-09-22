from selenium import webdriver
import time

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    
    browser.find_element_by_id("dropdown").send_keys(str(int(num1.text)+int(num2.text)))
    
    button = browser.find_element_by_css_selector("[type='submit']")
    button.click()
    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()

