# driver.get(url) 用设定好的浏览器打开url
# driver.find_element_by_*()用来查找网页元素
# driver.page_source获取网页渲染后的源代码


from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get('http://www.python.org/')

assert "Python" in driver.title

elem = driver.find_element_by_name('q')
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)
print(driver.page_source)