import requests
import os.path
import time
from bs4 import BeautifulSoup
from multiprocessing import Process

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

    @staticmethod
    def write_file(text, title):
        """将正文写到文件中"""
        with open('store/' + title + '.txt', 'w') as f:
            f.write(text)

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

    def read_links(self):
        length = len(self.links)
        if not os.path.exists('store/'):                    # 检测是否有store目录
            os.makedirs('store')
        for i in range(length):
            if i > 20:
                break
            print('正在爬取第 ' + str(i+1) + ' 章...')
            #Process(target=self.crawl, args=(i,)).start()
            self.crawl(i)

        print('下载完毕！')

    def crawl(self, x):
        """爬取第x章内容"""
        html = self.get_HTML(self.links[x])
        text = self.get_text(html)
        self.write_file(text, self.titles[x])

    def get_text(self, html):
        """获取正文"""
        dom = BeautifulSoup(html, 'lxml')
        clr = dom.find(style='clear:both')
        text = ''
        for tag in clr.next_siblings:
            if tag == clr:
                break
            text += tag.string
        return text.replace('\xa0\xa0\xa0\xa0', '\n  ')



if __name__ == '__main__':
    url = 'http://www.qingyunian.net/'
    sc = StoryCrawler(url)
    sc.get_chapter_links()
    sc.read_links()