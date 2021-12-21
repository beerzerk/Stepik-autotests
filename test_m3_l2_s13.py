from selenium import webdriver
import time
import unittest

class TestRegistration(unittest.TestCase):
    def registration(self, link):
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("div.first_block input.first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector("div.first_block input.second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector("div.first_block input.third")
        input3.send_keys("ivan.petrov@test.org")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Registration Error")

        time.sleep(5)
        browser.quit()

    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.registration(link)
    def test_registration2(self):   
        link = "http://suninjuly.github.io/registration2.html" 
        self.registration(link)


if __name__ == "__main__":
    unittest.main()