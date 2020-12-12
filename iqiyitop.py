# -*- coding=utf-8 -*-
# @Time : 2020/12/11 10:07
# @Author : siaingfy
# @File : iqiyitop.py
# @Software : PyCharm

import requests,re

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.57'
}

def get_info(url):
    req = requests.get(url,headers=headers)
    html = req.text
    fi = '\d+><\S+ src="(.*?)".*?href="(.*?)".*?class="title.*?>(.*?)</a>.*?66>(.*?)</p>'
    content2 =re.findall(fi,html,re.S)
    print(content2,len(content2))
def main():

    url = 'https://top.iqiyi.com/dianying.html'
    get_info(url)
    # api  'https://pcw-api.iqiyi.com/album/album/fytoplist?cid=1&dim=hour&type=realTime&size=50'
if __name__ == '__main__':
    main()