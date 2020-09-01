# -*- coding: utf-8 -*-
from multiprocessing import Pool
from urllib.parse import urlencode
import requests
import json
from requests import RequestException
from bs4 import BeautifulSoup
import re
# import pymongo


#client = pymongo.MongoClient('localhost',connect=False)
#db = client['toutiaowenzhang']

def get_index(offset):
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': '美文',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from':'search_tab'
    }
    url = 'https://www.toutiao.com/search_content/?'+urlencode(data)
    
    print(url)
    
    response = requests.get(url)
    
    try:
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

def get_urls(html):
    data = json.loads(html)
    if data and 'data' in data.keys():
        for item in data.get('data'):
            yield item.get('article_url')

def get_index_detail(url):
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

def parse_detail(html):
    try:
        soup = BeautifulSoup(html,'lxml')
        title = soup.select('title')[0].get_text()
        compile_allarticle= re.compile('content.*?&lt;div&gt(.*?)&lt;/div&gt;',re.S)
        allarticle = re.findall(compile_allarticle,html)
        # article =re.sub('(&lt;.*?&lt;span&gt;)','',allarticle[0])#正则匹配上不需要的那部分
        article =re.sub('[a-zA-Z0-9/#;&\._]','',str(allarticle)).strip()#直接把字母数字全部替换
        data = {
            'title':title,
            'article':article
        }
        return data
    except TypeError:#解决出现了404界面
        pass
    
#def save_to_mongodb(result):
#    if db['toutiaowenzhang'].insert(result):
#        print('successful')
#    else:
#        print('fail')

def save_to_mysqldb(result):
     print(result)

def main(offset):
    html = get_index(offset)
    items = get_urls(html)
    for item in items:
        if item:
            ab = get_index_detail(item)
            result = parse_detail(ab)
#            save_to_mongodb(result)
            save_to_mysqldb(result)
            
            
if __name__=='__main__':
    groups = [x*20 for x in range(3)]
    pool = Pool()
    pool.map(main,groups)
