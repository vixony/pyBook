# -*- coding: utf-8 -*-

from urllib import request
import socket

from  lxml.html import etree
import json

def get_url(url):
    headers = {
               'User-Agent': r'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             r'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
#              'Referer': r'http://www.lagou.com/zhaopin/Python/?labelWords=label',
               'Referer': r'https://finance.sina.com.cn/',
               'Connection': 'keep-alive'
              }
    
    socket.setdefaulttimeout(5)   
    req = request.Request(url, headers=headers)
    try:
        page = request.urlopen(req).read()
    except :        
        page = ''
    return page


if __name__ == '__main__': 
    #分析网页获取数据
    url='https://finance.sina.com.cn/money/forex/hq/USDCNY.shtml'
    page = get_url(url) 
    print(page)
    tree=etree.HTML(page) 
    
    #使用xpath来解析十大流通股东
    stocktitle= tree.xpath(u"/*[@id='hotHorex']")
    print(stocktitle)
    #title =stocktitle[].text
    #getdate=title[title.find('(')+1:title.find(')')] 
    #param=[]
    #nodes=tree.xpath(u"/html/body/div[9]/div[32]/table") 
     
 
     
    #for node in nodes:
    #    for data in node:
    #        stockhold=[]  
    #        for listdata in data: 
    #            stockhold.append(listdata.text)
    #        param.append(stockhold)
    #print(param)
    
    #使用JS接口来获取数据
    #url='http://zhishu.analysys.cn/public/qianfan/topRank/listTopRank?page=1&pageSize=200&cateId=101&tradeId='
    url='http://m.qianfan.analysys.cn/qianfan/topRank/ranksIndexData?rankType=3&_=1524218489900'
    page=get_url(url)
    pagedata = json.loads(page)  
    print(pagedata['datas'])