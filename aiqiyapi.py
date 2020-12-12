# -*- coding=utf-8 -*-
# @Time : 2020/12/11 16:14
# @Author : siaingfy
# @File : aiqiyapi.py
# @Software : PyCharm

import requests,re

def main():
    url = 'https://pcw-api.iqiyi.com/album/album/fytoplist?cid=1&dim=hour&type=realTime&size=50'
    req = requests.get(url)

    print(req.text)

if __name__ == '__main__':

    main()