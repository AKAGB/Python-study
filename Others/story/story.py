import requests
import chardet

# 爬取首页html
url = 'http://www.qingyunian.net/'
rsp = requests.get(url)

# 获取正确编码的网页
html = str(rsp.content, rsp.apparent_encoding)

# 输出测试效果
print(html)