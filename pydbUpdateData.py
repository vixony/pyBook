#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb
import math
import string
import random
import randomIDtel
import randomName
import genCompany

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "qwer1234", "test", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

seed = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-"
sa = []
for i in range(8):
  sa.append(random.choice(seed))
salt = ''.join(sa)

print(salt)

toUpdateIDlist = []
# SQL 查询语句 

sql = "SELECT Id, KeyFlag FROM EMPLOYEE WHERE Id > 0"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
       Id = row[0]
       toUpdateIDlist.append(Id)
except:
   print("Error: 未能拉取数据")
#
def gen_SQL_seg(thisId):
    SQLS = "UPDATE EMPLOYEE SET  CompanyInfo ='"+ genCompany.randomCompany() +"', KeyFlag ='" + genCompany.comArea + "、" + genCompany.comName + "、" + genCompany.comCom +"' WHERE Id = " + str(thisId)
    return SQLS

def gen_nameSQL_seg(thisId):
    SQLS = "UPDATE EMPLOYEE SET  ChinaName ='"+ randomName.gen_china_name()+"' WHERE Id =" + str(thisId)
    return SQLS

def updateDBlist():
    
    for item in toUpdateIDlist:
        sql_str = gen_nameSQL_seg(item)
        
        try:
           # 执行sql语句
           cursor.execute(sql_str)
           # 提交到数据库执行
           db.commit()
           
           print(sql_str)
        except (IOError, ZeroDivisionError) as e:
           # Rollback in case there is any error
           print(e)
           print('出错了')
           
           db.rollback()

    print("完成更新")
    
updateDBlist()
# 关闭数据库连接
db.close()

