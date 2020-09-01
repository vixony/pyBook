# -*- coding: utf-8 -*-

EmployeeRecord = namedtuple('EmployeeRecord', 'name, age, title, department, paygrade')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv", "rb"))):
    print(emp.name, emp.title)

# sqlite数据库
import sqlite3
conn = sqlite3.connect('/companydata')
cursor = conn.cursor()
cursor.execute('SELECT name, age, title, department, paygrade FROM employees')
for emp in map(EmployeeRecord._make, cursor.fetchall()):
    print(emp.name, emp.title)
    
# MySQL 数据库
import mysql
from mysql import connector
from collections import namedtuple
user = 'herbert'
pwd = '######'
host = '127.0.0.1'
db = 'world'
cnx = mysql.connector.connect(user=user, password=pwd, host=host,database=db)
cur.execute("SELECT Name, CountryCode, District, Population FROM CITY where CountryCode = 'CHN' AND Population > 500000")
CityRecord = namedtuple('City', 'Name, Country, Dsitrict, Population')
for city in map(CityRecord._make, cur.fetchall()):
    print(city.Name, city.Population)