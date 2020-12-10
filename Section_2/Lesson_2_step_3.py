from selenium import webdriver
import time


link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a = int(browser.find_element_by_id("num1").text)
    b = int(browser.find_element_by_id("num2").text)
    x = a + b
    text = "[value='"+str(x)+"']"

    browser.find_element_by_tag_name("select").click()
    browser.find_element_by_css_selector(text).click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(20)
    browser.quit()

