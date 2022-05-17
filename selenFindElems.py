from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

elems = browser.find_elements(By.TAG_NAME, "input")
for elem in elems:
    elem.send_keys("Мой ответ")

button = browser.find_element(By.CSS_SELECTOR, "button.btn")
button.click()
# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
browser.quit()
