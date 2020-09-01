# -*- coding: utf-8 -*-
# coding=utf-8
import  re, urllib.request

url = 'http://www.nmc.cn'
html = urllib.request.urlopen(url).read()
html = html.decode('utf-8')     #python3版本中需要加入
links = re.findall('<a target="_blank" href="(.+?)" title',html)
titles = re.findall('<a target="_blank" .+? title="(.+?)">',html)
tags = re.findall('<a target="_blank" .+? title=.+?>(.+?)</a>',html)

for link,title,tag in zip(links,titles,tags):
    print(tag,url+link,title)

print("capture finished")