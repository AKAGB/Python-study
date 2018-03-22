import requests
from bs4 import BeautifulSoup

class StoryCrawler:

    def __init__(self, url):
        """初始化各种变量"""
        self.url = url             # 目的url
        self.links = []                                     # 存放链接列表
        self.titles = []                                    # 存放每一章节的标题

    @staticmethod
    def get_HTML(url):
        """爬取网页代码"""
        try:    
            rsp = requests.get(url)                         # 爬取首页html
            html = str(rsp.content, rsp.apparent_encoding)  # 获取正确编码的网页
        except Exception:
            html = None                                     # 若爬取失败则返回None
        return html

    def get_chapter_links(self):
        """获取章节链接"""
        html = self.get_HTML(self.url)
        if html:
            soup = BeautifulSoup(html, 'lxml')
            tables = soup.find_all('table')
            for eachTable in tables:
                links = eachTable.find_all('a')
                for eachChapter in links[1:]:
                    self.links.append(eachChapter['href'])
                    self.titles.append(eachChapter.string)
        else:
            print('获取失败！请检查输入网址。')


if __name__ == '__main__':
    url = 'http://www.qingyunian.net/'
    sc = StoryCrawler(url)
    sc.get_chapter_links()
    length = len(sc.titles)
    for i in range(length):
        print(sc.titles[i] + ' -> ' + sc.links[i])