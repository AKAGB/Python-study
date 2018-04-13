from selenium import webdriver

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://music.163.com/')
driver.close()