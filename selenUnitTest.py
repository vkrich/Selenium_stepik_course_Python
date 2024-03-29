from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAssert(unittest.TestCase):
    link1 = "http://suninjuly.github.io/registration1.html"
    link2 = "http://suninjuly.github.io/registration2.html"

    def func(self, link):
        browser = webdriver.Chrome()

        # Выбор страницы регистрации
        browser.get(link)
        # Затем переделал под поиск отдельных элементов (div.first_block - все обязательные поля):
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
        input1.send_keys("val")
        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
        input2.send_keys("val")
        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
        input3.send_keys("val")

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

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        return "Congratulations! You have successfully registered!" == welcome_text

    def test_page1(self):
        self.assertTrue(self.func(self.link1))

    def test_page2(self):
        self.assertTrue(self.func(self.link2))


if __name__ == "__main__":
    unittest.main()
