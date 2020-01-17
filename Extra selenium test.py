from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"
browser.get(link)
x = browser.find_element_by_css_selector('span#input_value.nowrap').text
y = calc(x)
browser.find_element_by_css_selector('#answer').send_keys(y)
button = browser.find_element_by_tag_name('button')
browser.execute_script("return arguments[0].scrollIntoView(true);",button)
checkbox = browser.find_element_by_css_selector('input#robotCheckbox').click()
radio = browser.find_element_by_css_selector('input#robotsRule.form-check-input ').click()
button.click()

time.sleep(10)
browser.quit()