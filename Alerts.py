#from selenium import webdriver

#import time
#import math

#def calc(x):
  #return str(math.log(abs(12*math.sin(int(x)))))

#browser = webdriver.Chrome()
#link = "http://suninjuly.github.io/redirect_accept.html"
#browser.get(link)

#browser.find_element_by_css_selector('button') .click()
#new_window = browser.window_handles[1]
#browser.switch_to.window(new_window)
#x = browser.find_element_by_css_selector('span#input_value.nowrap').text
#y = calc(x)
#browser.find_element_by_css_selector('#answer').send_keys(y)
#button = browser.find_element_by_tag_name('button') .click()

#time.sleep(5)
#browser.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
button = browser.find_element_by_css_selector("button#book.btn.btn-primary ") .click()

x = browser.find_element_by_css_selector('span#input_value.nowrap').text
y = calc(x)
browser.find_element_by_css_selector('#answer').send_keys(y)
browser.find_element_by_css_selector('button#solve.btn.btn-primary') .click()

