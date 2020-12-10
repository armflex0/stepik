from selenium import webdriver
import time
import math
import pytest

@pytest.mark.parametrize('numbers', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(numbers):
    link = f"https://stepik.org/lesson/{numbers}/step/1"
    browser = webdriver.Chrome()
    browser.get(link)

    time.sleep(5)

    input1 = browser.find_element_by_css_selector('textarea.textarea')
    answer = math.log(int(time.time() - 0.8))
    input1.send_keys(str(answer))

    button = browser.find_element_by_css_selector("button.submit-submission")
    button.click()

    time.sleep(1)

    corect = browser.find_element_by_css_selector('pre.smart-hints__hint').text

    if "Correct!" != corect:
        print(corect)

    time.sleep(10)
    browser.quit()