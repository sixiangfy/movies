# @Time : 2020/12/8 16:34
# @Author : siaingfy
# @File : baidumoviesrop50.py
# @Software : PyCharm

import re, requests, time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'
}


def main():

    url = 'http://top.baidu.com/buzz?b=26'          # 电影
    # url = 'http://top.baidu.com/buzz?b=19'          # 综艺
    # url = 'http://top.baidu.com/buzz?b=23'          # 动漫
    # url = 'http://top.baidu.com/buzz?b=1677'        # 少儿
    # url = 'http://top.baidu.com/buzz?b=4'           # 电视剧
    # url = 'http://top.baidu.com/buzz?b=7'           # 小说
    get_info(url)

def get_info(url):
    req = requests.get(url, headers=headers)
    req.encoding='gbk'                              # charset=gb2312
    html = req.text

    names =re.findall('title".*?>(.*?)</a>',html)               # 名字
    jianjie = re.findall('<td class="tc".*?href="(.*?)">简介</a>', html,re.S)     # 简介

    # get_intro(jianjie)

    zhishus = re.findall('<span class="icon-.*?">(.*?)</span>', html, re.S)      # 指数



    print(names,len(names))
    # print(jianjie,len(jianjie))
    print(zhishus,len(zhishus))

def get_intro(jianjie_list):            # 简介
    pass
if __name__ == '__main__':
    startTime = time.time()            # 开始时间
    main()
    endTime = time.time()
    a = endTime - startTime
    print('开始时间',startTime)
    print('结束时间',endTime)
    print(a)