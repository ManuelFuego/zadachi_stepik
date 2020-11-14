from selenium import webdriver
import math

link = 'http://suninjuly.github.io/get_attribute.html'

browser = webdriver.Firefox()
#browser = webdriver.Chrome()  снять коммент если необхолимо протестировать на Chrome
browser.get(link)
def calc(m):
    return str(math.log(abs(12*math.sin(int(m)))))


findchest = browser.find_element_by_id("treasure")
x = findchest.get_attribute("valuex")
y = calc(x)    
answer_field = browser.find_element_by_id('answer')
answer_field.send_keys(y)
find_checkbox = browser.find_element_by_id('robotCheckbox')
find_checkbox.click()
find_robotsrule = browser.find_element_by_id('robotsRule')
find_robotsrule.click()
find_submit= browser.find_element_by_xpath('//button[@type="submit"]')
find_submit.click()

