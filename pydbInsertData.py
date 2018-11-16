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

firstName =[
('Smith','史密斯'),('Johnson', '约翰逊'),('Williams','威廉姆斯'),('Jones','约翰'),('Brown','布朗'),('Davis','戴维斯'),('Miller','米勒'),('Wilson','威尔逊'),('Moore','摩尔'),('Taylor','泰勒'),('Anderson','安德森'),('Thomas','托马斯'),('Jackson','杰克逊'),('White','怀特'),('Harris','哈里斯'),
('Martin','马丁'),('Thompson','汤姆逊'),('Garcia','加西亚'),('Martinez','玛丁尼'),('Robinson','罗宾森'),('Clark','克拉克'),('Rodriguez','罗德里格斯'),('Lewis','路易斯'),('Lee','李'),('Walker','沃克'),('Hall','郝'),('Allen','艾伦'),('Young','杨'),('Hernandez','埃尔南德斯'),('King','金'),
('Wright','怀特'),('Lopez','洛佩兹'),('Hill','希尔'),('Scott','斯科特'),('Green','格林'),('Adams','亚当'),('Baker','贝克'),('Gonzalez','冈萨雷斯'),('Nelson','纳尔逊'),('Carter','卡特'),('Mitchell','米切尔'),('Perez','佩雷斯'),('Roberts','罗伯特'),('Turner','特纳'),('Phillips','菲利普'),
('Campbell','坎贝尔'),('Parker','帕克'),('Evans','埃文斯'),('Edwards','爱德华'),('Collins','柯林斯'),('Stewart','斯图尔特'),('Sanchez','桑切斯'),('Morris','莫里斯'),('Rogers','罗杰斯'),('Reed','里德'),('Cook','库克'),('Morgan','摩根'),('Bell','贝尔'),('Murphy','墨菲'),('Bailey','贝利'),
('Rivera','里韦拉'),('Cooper','库珀'),('Richardson','理查德森'),('Cox','考克斯'),('Howard','霍华德'),('Ward','瓦尔德'),('Torres','托雷斯'),('Peterson','彼得森'),('Gray','格雷'),('Ramirez','拉米雷兹'),('James','詹姆斯'),('Watson','沃森'),('Brooks','布鲁克斯'),('Kelly','凯莉'),('Sanders','桑德斯'),
('Price','普里塞'),('Bennett','班尼特'),('Wood','伍德'),('Barnes','巴尔内斯'),('Ross','罗丝'),('Henderson','亨德森'),('Coleman','科尔曼'),('Jenkins','詹金斯'),('Perry','佩里'),('Powell','鲍威尔'),('Long','朗'),('Patterson','帕特森'),('Hughes','休斯'),('Flores','弗洛里斯'),('Washington','华盛顿'),
('Butler','布特勒'),('Simmons','西蒙'),('Foster','福斯特'),('Gonzales','冈萨雷斯'),('Bryant','布赖恩特'),('Alexander','亚历克斯'),('Russell','拉塞尔'),('Griffin','格里芬'),('Diaz','迪亚兹'),('Hayes','海耶斯'),('Emily','艾米丽'),('Madison','麦迪逊'),('Ava','阿娃'),('Olivia','奥利维亚'),('Sophia','索菲亚'),
('Abigail','艾比盖尔'),('Elizabeth','伊丽莎白'),('Chloe','克洛伊'),('Samantha','沙曼萨'),('Addison','艾迪生'),('Natalie','娜塔莉'),('Mia','米厄'),('Alexis','亚历克西丝'),('Alyssa','艾丽萨'),('Hannah','汉娜'),('Ashley','阿什丽'),('Ella','艾拉'),('Sarah','萨拉'),('Grace','格丽丝'),('Taylor','泰勒'),
('Brianna','布丽安娜'),('Lily','莉莉'),('Hailey','海丽'),('Anna','安娜'),('Victoria','维多丽娅'),('Kayla','凯拉'),('Lillian','丽莲'),('Lauren','劳伦'),('Kaylee','凯丽'),('Allison','艾丽森'),('Savannah','萨瓦娜'),('Nevaeh','内维娅'),('Gabriella','加布丽艾拉'),('Sofia','索菲亚'),('Makayla','马凯拉'),
('Avery','艾佛芮'),('Riley','莱丽'),('Julia','朱丽娅'),('Leah','丽娅'),('Audrey','奥德丽'),('Jasmine','佳丝敏'),('Audrey','奥布里'),('Katherine','凯瑟琳'),('Morgan','摩根'),('Brooklyn','布鲁克林'),('Destiny','戴斯蒂尼'),('Sydney','悉尼'),('Alexa','亚历克萨'),('Kylie','凯丽'),('Brooke','布鲁克'),
('Kaitlyn','凯特琳'),('Evelyn','伊芙琳'),('Madeline','麦德林'),('Kimberly','金伯莉'),('Zoe','佐伊'),('Jessica','杰西卡'),('Peyton','佩顿'),('Alexandra','亚历山德拉'),('Madelyn','麦德琳'),('Maria','玛丽娅'),('Mackenzie','麦肯西'),('Arianna','艾丽阿娜'),('Jocelyn','乔丝琳'),('Amelia','阿米莉亚'),
('Angelina','安吉丽娜'),('Trinity','安德丽'),('Sophie','索菲亚'),('Rachel','蕾切尔'),('Vanessa','瓦内萨'),('Aaliyah','艾丽雅'),('Mariah','艾丽娅'),('Gabrielle','加布里艾拉'),('Katelyn','凯特琳'),('Ariana','艾丽阿娜'),('Bailey','贝丽'),('Camila','卡米拉'),('Jennifer','詹妮芙'),('Melanie','梅兰妮'),
('Gianna','吉阿娜'),('Charlotte','夏洛特'),('Paige','佩奇'),('Autumn','奥特姆'),('Payton','佩顿'),('Faith','菲丝'),('Sara','萨拉'),('Isabelle','伊莎贝尔'),('Caroline','卡罗琳'),('Genesis','詹妮西丝'),('Isabel','伊莎贝尔'),('Mary','玛丽'),('Zoey','佐伊'),('Gracie','格雷西'),('Megan','梅根')]


#"""
#INSERT TABLE EMPLOYEE(`LoginName`,
#  `LoginPsw` ,
#  `NickName` ,
#  `WeiXin` ,
#  `TelePhone` ,
#  `Mail` ,
#  `KeyFlag` ,
#  `infoContent` ,
#  `GroupInfo` ,
#  `CompanyInfo` 
#)
#VALUES(
#
#)
#"""
# SQL 插入语句
sql = "INSERT INTO EMPLOYEE(LoginName, LoginPsw, NickName, WeiXin, TelePhone, Mail, IDCode, KeyFlag, infoContent, GroupInfo, CompanyInfo) VALUES('{ln}', '{lpw}', '{nik}', '{WeiXin}' , '{TelePhone}' ,  '{Mail}' ,'{IDCode}', '{KeyFlag}' ,'infoContent' ,'GroupInfo' , '{CompanyInfo}')"
SQLS = [sql.format(ln = en,
                   lpw = randomIDtel.newStr(8),
                   nik = zh, 
                   TelePhone = randomIDtel.createPhone(), 
                   IDCode = randomIDtel.generatorIDC(), 
                   Mail = randomIDtel.createEmail(),
                   WeiXin = randomName.genOneWordDigit(lowercase=False),
                   CompanyInfo = genCompany.randomCompany(),
                   KeyFlag = genCompany.comArea + "、"+ genCompany.comName + "、" + genCompany.comCom + "" 
                   ) for en, zh in firstName]


def fillDatable(SQLSi):
    "输出sql0"
    
    try:
       # 执行sql语句
       cursor.execute(SQLSi)
       # 提交到数据库执行
       db.commit()
       
       print('写入完成')
    except:
       # Rollback in case there is any error
       print('出错了')
       db.rollback()

for sqlItem in SQLS:
    
    fillDatable(sqlItem)

# 关闭数据库连接
db.close()

