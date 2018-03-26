import urllib.request
import urllib.error
import itertools
import re

def download(url, user_agent='wswp', num_retries=2):
    print('Downloading:', url)    
    headers = {'User-agent': user_agent}
    request = urllib.request.Request(url, headers=headers)
    try:
        html = urllib.request.urlopen(request).read()
    except urllib.error.URLError as e:
        print('Download Error:', e.reason)
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code < 600:
                # recursively retry 5xx HTTP errors
                return download(url, num_retries-1)
    return html

def crawl_sitemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('<a href="(.*?)">', str(sitemap))
    # download each link
    for link in links:
        print(link)
        # scrape html here

def link_crawler(seed_url, link_regex):
    """Crwal from the given seed URL following links matched by link_regex
    """
    crawl_queue = [seed_url]
    while crawl_queue:
        url = crawl_queue.pop()
        html = download(url)
        for link in get_links(html.deocde()):
            # 筛选link
            if re.match(link_regex, link):
                crawl_queue.append(link)

def get_links(html):
    """返回这个页面中的所有链接
    """
    webpage_regex = re.compile('<a[^>]+href=["\'](.*?)["\']', 
        re.IGNORECASE)
    return webpage_regex.findall(html)
    
    

if __name__ == '__main__':
    # 允许发生错误的最大次数
    max_error = 5
    # 记录连续发生的错误次数
    num_errors = 0
    for page in itertools.count(45):
        url = 'http://example.webscraping.com/places/default/view/%d' % page
        html = download(url)
        if html:
            num_errors += 1
            if num_errors == max_error:
                break
        else:
            # 重置错误计数器
            num_errors = 0