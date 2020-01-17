from selenium import webdriver
from selenium.webdriver.support.ui import Select

browser = webdriver.Chrome()
#link = ('http://suninjuly.github.io/selects1.html')
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element_by_tag_name("button")
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()


#num1 = int(browser.find_element_by_id("num1").text)
#num2 = int(browser.find_element_by_id("num2").text)
#x = num1
#y = num2
#result = str(int(x) + int(y))
#select = Select(browser.find_element_by_css_selector('#dropdown'))
#select.select_by_value(result)
#submit = browser.find_element_by_css_selector('body > div > form > button')
#submit.click()