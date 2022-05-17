from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# Выбор страницы регистрации
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link1)

try:

    # Ваш код, который заполняет обязательные поля

    # Изначально сделал поиск всех required:
    # elems = browser.find_elements(By.TAG_NAME, "input[required]")
    # for elem in elems:
    # elem.send_keys("val")

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
