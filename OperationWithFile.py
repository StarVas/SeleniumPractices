from selenium import webdriver

import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/alert_accept.html"
browser.get(link)

browser.find_element_by_css_selector('button.btn.btn-primary ') .click()
confirm = browser.switch_to.alert
confirm.accept()
x = browser.find_element_by_css_selector('span#input_value.nowrap').text
y = calc(x)
browser.find_element_by_css_selector('#answer').send_keys(y)
button = browser.find_element_by_tag_name('button') .click()

