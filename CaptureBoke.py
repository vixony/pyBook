#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 抓取csdn博客页面的所有文章

from urllib import request
from bs4 import BeautifulSoup
import json
from selenium import webdriver
import time


def write2file(filename, content):
    try:
        f = open(filename, mode='w', encoding='utf-8')
        f.write(content)

    finally:
        if f:
            f.close()


# 将['\n', <span class="article-type type-1">
#             原        </span>, '\n        安卓微信浏览器location.reload()无效      ']
# 这种结构提取为: 安卓微信浏览器location.reload()无效
def list2str(sequence):
    s = ''
    for i in sequence:
        if i and isinstance(i, str) and len(i.strip()):
            s = s + i.strip()

    return s


def getPage(url):
    try:
        return request.urlopen(url).read().decode('utf-8')
    except Exception as e:
        return ''


def page2blogList(page):
    soup = BeautifulSoup(page, 'html.parser')
    blogList = []

    for blogTitle in soup.find_all('h4', class_="text-truncate"):
        linkNode = blogTitle.find_all('a')[0]
        link = linkNode.get('href')
        text = linkNode.contents
        text = list2str(text)
        blogList.append({'link': link, 'text': text})

    return blogList


# 页码是动态渲染出来的, 不能用soup抓
def getTotalPage(url):
    # soup = BeautifulSoup(html, 'html.parser')
    # oPageContainer = soup.find_all(attrs={'id': 'pageBox'})
    # print(oPageContainer)
    #return
    browser = webdriver.PhantomJS()
    browser.get(url)
    time.sleep(2)
    oTotalPageContainer = browser.find_element_by_id('pageBox')
    pageText = oTotalPageContainer.text

    # 上一页123...7下一页
    return int(pageText[-4:-3], 10)

def getUrlByPageNum(pageNum = 1):
    url = 'https://blog.csdn.net/butterfly5211314/article/list/%s'
    # print(url % (pageNum))
    return url % (pageNum)


url = getUrlByPageNum(1)
page = getPage(url)
blogList = page2blogList(page)
# print(blogList)

totalPage = getTotalPage(url)
# print('totalPage:', totalPage)
# write2file('blog.json', json.dumps(blogList, indent=4, ensure_ascii=False))


def getAllBlogs():
    url = getUrlByPageNum(1)
    totalList = [];
    totalPage = getTotalPage(url)

    for i in range(1, totalPage + 1):
        url = getUrlByPageNum(i)
        print(url)
        page = getPage(url)
        totalList.extend(page2blogList(page))

    return  totalList

#print(getAllBlogs())
write2file('blog.json', json.dumps(getAllBlogs(), indent=4, ensure_ascii=False))
