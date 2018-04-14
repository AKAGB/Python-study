import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get('https://www.baidu.com/')
time.sleep(1)
driver.find_element_by_xpath('/html/body').send_keys(Keys.CONTROL + 't')
time.sleep(1)