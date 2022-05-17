from selenium import webdriver
import time

try: # ВНИМАНИЕ!!!ЗДЕСЬ ЛИНК НА ВТОРУЮ ФОРМУ. ЧТОБЫ ПРОВЕРИТЬ НА ПЕРВОЙ ФОРМЕ, НУЖНО ИЗМЕНИТЬ ЛИНК
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_xpath('//input[@class="form-control first" and @required]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[@class="form-control second" and @required]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[@class="form-control third" and @required]')
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(5)

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

