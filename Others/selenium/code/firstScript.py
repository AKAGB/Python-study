# coding=utf-8
import time
from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(8)

driver.get('https://www.baidu.com')
driver.find_element_by_xpath('//*[@id="kw"]').send_keys('selenium')
driver.find_element_by_xpath('//*[@id="su"]').click()

time.sleep(2)

driver.find_element_by_xpath('//div/h3/a[text()="官网"]/../a/em[text()="Selenium"]') \
        .is_displayed()
driver.quit()