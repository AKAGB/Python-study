import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)

driver.get('http://dreamgqk.cn')
target_elem = driver.find_element_by_link_text('Python-Chapter8')
driver.execute_script('return arguments[0].scrollIntoView();', target_elem)