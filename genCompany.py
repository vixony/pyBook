import os
import string
import random

KEY_PATH = "i:\\pythonProject\\companyname.txt"
DC_PATH = "i:\\pythonProject\\area.txt"
COM_PATH = "i:\\pythonProject\\com.txt"

comArea = ""
comName = ""
comCom = "" 

# 随机抽取文本行内容
ki = []
def get_list_item(pathstr = KEY_PATH): 
    with open(pathstr, 'r', encoding='UTF-8') as file: 
        data = file.read() 
        districtlist = data.split('\n')       
    #   strs = "{'state':" + state + ",'city':" + city + ",'district':" + district + ", 'code': " + code +"}"
    return districtlist

def randomCompany():
    """
    随机生成公司名称
    """
    global comArea
    comArea = random.choice(get_list_item(DC_PATH))
    global comName
    comName = random.choice(get_list_item(KEY_PATH))
    global comCom
    comCom = random.choice(get_list_item(COM_PATH))

    result = ""
    result += comArea
    result += comName
    result += comCom
    
    return result
  
#randomCompany()

# getdistrictcode()
# print( ) 