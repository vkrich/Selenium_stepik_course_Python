import math
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/get_attribute.html")
check = browser.find_element(By.ID, "robotCheckbox")
check.click()
check2 = browser.find_element(By.ID, "robotsRule")
check2.click()
input1 = browser.find_element(By.ID, "answer")
value = browser.find_element(By.ID, "treasure")
input1.send_keys(calc(value.get_attribute("valuex")))
btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()
