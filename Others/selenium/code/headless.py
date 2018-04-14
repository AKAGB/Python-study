from selenium import webdriver

fireFoxOptions = webdriver.FirefoxOptions()
fireFoxOptions.set_headless()
browser = webdriver.Firefox(firefox_options=fireFoxOptions)

browser.get('https://www.baidu.com')
print(browser.page_source)
browser.close()