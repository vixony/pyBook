# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 13:55:22 2018
@author: wangxi
"""
import os
import random
import datetime
import time
import string

BASE_DIR =  os.path.dirname(__file__)
DC_PATH = BASE_DIR  + "/districtcode.txt"

# print(random.random())#随机浮点数，默认取0-1，不能指定范围
# print(random.randint(1,20))#随机整数
# print(random.randrange(1,20))#随机产生一个range
# print(random.choice('x23serw4'))#随机取一个元素
# print(random.sample('hello',2))#从序列中随机取几个元素
# print(random.uniform(1,9))#随机取浮点数，可以指定范围
# x = [1,2,3,4,6,7]
# random.shuffle(x)#洗牌,打乱顺序，会改变原list的值
# print(x)
# print(string.digits)#所有的数字
# print(string.ascii_letters)#所有的字母
# print(string.punctuation)#所有的特殊字符
# 随机生成手机号码


def createPhone():
      prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
      return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))

# 随机生成身份证号


def getdistrictcode():
    with open(DC_PATH, 'r', encoding='UTF-8') as file:
        data = file.read()
        districtlist = data.split('\n')
    for node in districtlist:
    # print node
        node = node.encode('utf-8').decode('utf-8-sig').strip()
    # 省
        if node[10:11] != ' ':
            state = node[10:].strip()
    # 城市
        if node[10:11] == ' ' and node[12:13] != ' ':
            city = node[12:].strip()

        if node[10:11] == ' ' and node[12:13] == ' ':
            district = node[14:].strip()
            code = node[0:6]
            codelist.append({"state":state,"city":city,"district":district,"code":code, "idc":0})

# 构建随机身份证号
def generatorIDC():
    global codelist
    codelist = []
    idcobj = {}
    if not codelist:
        getdistrictcode()

    ranCode = random.randint(0,len(codelist)-1)
    idcobj = codelist[ranCode]

    id = idcobj['code'] #地区项
    id = id + str(random.randint(1930,2017)) #年份项
    da = datetime.date.today()+datetime.timedelta(days=random.randint(1,366)) #月份和日期项
    id = id + da.strftime('%m%d')
    id = id+ str(random.randint(100,300))#，顺序号简单处理

    print(id)

    i = 0
    count = 0
    weight = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2] #权重项
    checkcode ={'0':'1','1':'0','2':'X','3':'9','4':'8','5':'7','6':'6','7':'5','8':'5','9':'3','10':'2'} #校验码映射
    for i in range(0,len(id)):
        count = count +int(id[i])*weight[i]
        id = id + checkcode[str(count%11)] #算出校验
        idcobj['idc'] = id
        return idcobj





# 随机生成邮箱
def createEmail( emailType=None, rang=None):
    __emailtype = ["@qq.com", "@163.com", "@126.com", "@189.com"]

    # 如果没有指定邮箱类型，默认在 __emailtype中随机一个
    if emailType == None:
        __randomEmail = random.choice(__emailtype)
    else:
        __randomEmail = emailType

    # 如果没有指定邮箱长度，默认在4-10之间随机
    if rang == None:
        __rang = random.randint(4, 10)
    else:
        __rang = int(rang)
    __Number = "0123456789qbcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPWRSTUVWXYZ"
    __randomNumber = "".join(random.choice(__Number) for i in range(__rang))
    _email = __randomNumber + __randomEmail
    return _email

# 生成随时字符组合（包括特殊字符）
def randomChars(lenth=8):
    seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
    sa = []
    for i in range(lenth):
      sa.append(random.choice(seed))
    salt = ''.join(sa)
    return salt

#生成一定长度的字符串
def newStr(length=8):
#    nameList = "1234567890abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    randomStr = ''.join(random.sample(string.ascii_letters + string.digits, length))
    return randomStr

if __name__ == '__main__':
    idobj = generatorIDC()

    print("createEmail: " + createEmail())
    print("createEmail: " + createEmail(emailType='@emoney.cn',rang=12))
    print("createPhone: " + createPhone())
    print("generatorIDC: " + idobj['state'])
    print("generatorIDC: " + idobj['city'])
    print("generatorIDC: " + idobj['district'])
    print("generatorIDC: " + idobj['idc'])
    print("newStr: " + newStr(8))
    print("randomChars: " + randomChars(8))

#createEmail: Ontf@126.com
#createEmail: IREIhiX96OS7@emoney.cn
#createPhone: 13543185057
#generatorIDC: 440403197012311206
#newStr: 3K4fIrc6Jj
#randomChars: p1zHs$Z-lzG5
