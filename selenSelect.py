from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/selects1.html")

a = int(browser.find_element(By.ID, "num1").text)
b = int(browser.find_element(By.ID, "num2").text)

select = Select(browser.find_element(By.TAG_NAME, "select"))
select.select_by_value(str(a+b))

btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
btn.click()
