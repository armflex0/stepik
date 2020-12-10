from selenium import webdriver
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_first(self):
        link = "http://suninjuly.github.io/registration1.html"
        # link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('input.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input.second[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input.third[required]')
        input3.send_keys("I.p@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(3)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You do not register")
        time.sleep(3)
        browser.quit()

    def test_second(self):
        # link = "http://suninjuly.github.io/registration1.html"
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_css_selector('input.first[required]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector('input.second[required]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('input.third[required]')
        input3.send_keys("I.p@mail.ru")

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(3)

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "You do not register")
        time.sleep(3)
        browser.quit()

if __name__ == "__main__":
    unittest.main()

