import requests
import hashlib
import random
import time

class Translator():
    def __init__(self):
        # 参数设置
        self.url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        self.headers = {
            'Cookie' : 'OUTFOX_SEARCH_USER_ID=-1443294221@10.168.8.61; JSESSIONID=aaa6JQvAXx8sCfSpKgjiw; OUTFOX_SEARCH_USER_ID_NCOO=572982542.7036237; ___rl__test__cookies=1520572536948',
            'Referer' : 'http://fanyi.youdao.com/',
            'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            'X-Requested-With' : 'XMLHttpRequest',
        }
        self.postData = {
            'i' : '你好',
            'from' : 'AUTO',
            'to' : 'AUTO',
            'smartresult' : 'dict',
            'client' : 'fanyideskweb',
            'salt' : '1520572536951',
            'sign' : '5b3ca2d1b69c12bcb82aa1b710d2a648',
            'doctype' : 'json',
            'version' : '2.1',
            'keyfrom' : 'fanyi.web',
            'action' : 'FY_BY_REALTIME',
            'typoResult' : 'false',
        }
        self.S = 'fanyideskweb'
        self.D = 'ebSeFb%=XZ%T[KZ)c(sy!'

    def translate(self, str_input):
        self.postData['i'] = str_input

        # 处理salt和sign
        self.postData['salt'] = str(int(time.time()*1000) + int(random.random()*10))
        self.postData['sign'] = hashlib.md5((self.S + str_input + self.postData['salt'] + self.D)
                            .encode('utf-8')).hexdigest()

        rsp = requests.post(self.url, headers=self.headers, data=self.postData)
        result = rsp.json()
        return result['translateResult'][0][0]['tgt']

def main():
    t = Translator()
    while True:
        str_input = input(r'Please input the context("q! to exit"): ')
        if str_input == 'q!':
            break
        result = t.translate(str_input)
        print('Result:', result)
    print('Exit...')

if __name__ == '__main__':
    main()
