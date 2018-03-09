import requests
import hashlib
import random
import time

# 参数设置
url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
headers = {
    'Cookie' : 'OUTFOX_SEARCH_USER_ID=-1443294221@10.168.8.61; JSESSIONID=aaa6JQvAXx8sCfSpKgjiw; OUTFOX_SEARCH_USER_ID_NCOO=572982542.7036237; ___rl__test__cookies=1520572536948',
    'Referer' : 'http://fanyi.youdao.com/',
    'User-Agent' : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With' : 'XMLHttpRequest',
}
postData = {
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
S = 'fanyideskweb'
D = 'ebSeFb%=XZ%T[KZ)c(sy!'

def translator(str_input):
    postData['i'] = str_input

    # 处理salt和sign
    postData['salt'] = str(int(time.time()*1000) + int(random.random()*10))
    postData['sign'] = hashlib.md5((S + str_input + postData['salt'] + D)
                        .encode('utf-8')).hexdigest()

    rsp = requests.post(url, headers=headers, data=postData)
    result = rsp.json();
    return result['translateResult'][0][0]['tgt']

def main():
    while True:
        str_input = input(r'Please input the context("q! to exit"): ')
        if str_input == 'q!':
            break
        result = translator(str_input)
        print('Result:', result)
    print('Exit...')

if __name__ == '__main__':
    main()
