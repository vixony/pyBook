#!/usr/bin/python
# -*- coding: UTF-8 -*-

import MySQLdb

# 打开数据库连接
db = MySQLdb.connect("localhost", "root", "qwer1234", "test", charset='utf8' )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()

# 如果数据表已经存在使用 execute() 方法删除表。
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE `employee` (
  `Id` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT COMMENT 'Id',
  `LoginName` varchar(255) NOT NULL COMMENT '登录账号名',
  `LoginPsw` varchar(255) DEFAULT NULL COMMENT '登录密码',
  `NickName` varchar(255) DEFAULT NULL COMMENT '昵称',
  `WeiXin` varchar(255) DEFAULT NULL COMMENT '微信',
  `TelePhone` varchar(15) DEFAULT NULL COMMENT '电话',
  `Mail` varchar(255) DEFAULT NULL COMMENT '邮件',
  `IDCode` char(20) DEFAULT NULL COMMENT '身份证号',
  `KeyFlag` varchar(255) DEFAULT NULL COMMENT '关键标签',
  `infoContent` varchar(255) DEFAULT NULL COMMENT '介绍信息',
  `GroupInfo` varchar(255) DEFAULT NULL COMMENT '组织信息',
  `CompanyInfo` varchar(255) DEFAULT NULL COMMENT '公司信息',
  `LatestLoginTime` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT '最新登录时间',
  `CreateTime` timestamp NULL DEFAULT current_timestamp() COMMENT '创建时间',
  `RegistTime` timestamp NULL DEFAULT current_timestamp() COMMENT '注册时间',
  `updateTime` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT '更新时间',
  PRIMARY KEY (`Id`,`LoginName`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8"""

cursor.execute(sql)
print("数据库emplyee创建成功")
# 关闭数据库连接
db.close()