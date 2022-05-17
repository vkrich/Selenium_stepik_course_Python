from selenium import webdriver
from math import log, sin

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)

x = int(browser.find_element_by_id("input_value").text)
x = log(abs(12*sin(x)))
browser.find_element_by_id("answer").send_keys(x)

browser.find_element_by_id("robotCheckbox").click()

rule = browser.find_element_by_id("robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", rule)
rule.click()

button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()
