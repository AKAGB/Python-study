from selenium import webdriver

chromeOptions = webdriver.ChromeOptions()
chromeOptions.set_headless()
driver = webdriver.Chrome(chrome_options=chromeOptions)
driver.get('http://music.163.com/')
driver.find_element_by_xpath('//a/em[text()="排行榜"]').click()
print(driver.page_source)
driver.close()