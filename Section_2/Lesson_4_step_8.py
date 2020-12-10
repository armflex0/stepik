from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price_p = browser.find_element_by_id("price")
    price = price_p.text

    print(price+'a')

    while price != '$100':
        print(price)
        price = price_p.text
        time.sleep(0.3)

    button = browser.find_element_by_css_selector("button#book")
    button.click()

    button = browser.find_element_by_css_selector("button#solve")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys(y)

    # browser.execute_script("window.scrollBy(0, 100);")

    button.click()

finally:
    time.sleep(10)
    browser.quit()

