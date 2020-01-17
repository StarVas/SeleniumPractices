from selenium import webdriver
import time
import math

from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
browser = webdriver.Chrome()


#from selenium import webdriver
#import time
#import math

try:

link = "http://suninjuly.github.io/get_attribute.html"
browser.get(link)
x_element = browser.find_element_by_id('[id="input_value"]').get_attribute('valuex')
x = x_element.text
y = calc(x)
input1 = browser.find_elements_by_class_name('[class="form-control"]')[0]
input1.send_keys(y)
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
checkbox = browser.find_element_by_id ('[id="robotCheckbox"]').click()
radio = browser.find_element_by_id ('[id="robotsRule"]').click()
button = browser.find_element_by_class('[class="btn btn-primary"]').click()
button.click()

finally:
    time.sleep(10)
    browser.quit()



#sel1 = browser.find_element_by_id("num1")


#x = sel1.text
#sel2 = browser.find_element_by_id("num2")
#y = sel2.text
#z = str(int(x) + int(y))

#catch = browser.find_element_by_tag_name("dropdown").click()
#look_for = browser.find_element_by_css_selector("[value='" + z + "']").click()

#button = browser.find_element_by_css_selector("button.btn")
#button.click()

#time.sleep(1)


#
# try:
#    link = "http://suninjuly.github.io/selects1.html"
#    driver = webdriver.Chrome()
#     driver.get(link)
#     x_element = driver.find_element_by_xpath('//*[@id="num1"] ')
#    y_element = driver.find_element_by_xpath('[//*[@id="num2"] ')
#     x = x_element.text
#    y = y_element.text
#         option1 = browser.find_element_by_id('[id="num1"]')
#     option2 = browser.find_element_by_id('[id="num2"]')
#    result = str(int(x) + int(y))
#    select = Select(driver.find_element_by_css_selector('[for="dropdown"]'))
#    select.select_by_value(result)
#
#     img = browser.find_element_by_xpath('//img[@valuex]')
#     img_treasure=img.get_attribute("valuex")
#    x_element = browser.find_element_by_id('treasure').get_attribute('valuex')
#    #y = calc(x_element)
#    input1.send_keys(y)
#    option1.click()
#    option2.click()
#
#     input1 = browser.find_elements_by_css_selector('.form-control.first')[0]
#     input1.send_keys("Vas")
#     input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
#     input2.send_keys("Star")
    # input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
    # input3.send_keys("s@awe.com")
    # input4 = browser.find_element_by_css_selector('[placeholder="Input your phone:"]')
    # input4.send_keys("1234567")
    # input5 = browser.find_element_by_css_selector('[placeholder="Input your address:"]')
    # input5.send_keys("Street 123")
    #button = driver.find_element_by_css_selector("button.btn")
    #button = driver.find_element_by_css_selector('[type="submit"]')
    #button.click()

    # welcome_text_elt = browser.find_element_by_tag_name("h1")

    # welcome_text = welcome_text_elt.text

    # assert "Congratulations! You have successfully registered!" == welcome_text

#finally:
    #time.sleep(10)

#browser.quit()

#try:
 #   link = "http://suninjuly.github.io/selects1.html"
  #  browser = webdriver.Chrome()
   ## browser.get(link)

  #  num1 = int(browser.find_element_by_id("num1").text)
 #   num2 = int(browser.find_element_by_id("num2").text)
 #   sum1 = str(num1 + num2)

#    Select(browser.find_element_by_tag_name("select")).select_by_value(sum1)

    # Отправляем заполненную форму
   # button = browser.find_element_by_css_selector("button.btn-default")
   # button.click()

   # print("Тест успешно завершен. 20 сек на закрытие браузера...")

#finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
   # time.sleep(20)
    # закрываем браузер после всех манипуляций
    #browser.quit()