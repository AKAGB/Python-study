from selenium import webdriver
import re

chromeOptions = webdriver.ChromeOptions()
chromeOptions.set_headless()
driver = webdriver.Chrome(chrome_options=chromeOptions)
# driver.maximize_window()
driver.implicitly_wait(6)

driver.get('http://home.baidu.com/contact.html')

doc = driver.page_source
emails = re.findall(r'[\w]+@[\w\.-]+', doc)
driver.quit()
for email in emails:
    print(email)