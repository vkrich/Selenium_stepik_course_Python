from selenium import webdriver
from selenium.webdriver.common.by import By
import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'result.txt')           # добавляем к этому пути имя файла


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/file_input.html")

for elem in browser.find_elements(By.XPATH, "//input[@type=\"text\" and @required]"):
    elem.send_keys("val")

browser.find_element(By.ID, "file").send_keys(file_path)

browser.find_element(By.CSS_SELECTOR, "button.btn").click()

