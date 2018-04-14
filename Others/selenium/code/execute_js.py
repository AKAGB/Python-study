import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(6)
driver.get('https://www.baidu.com')

driver.execute_script('window.alert("Hello, world");')
time.sleep(2)
driver.quit()
