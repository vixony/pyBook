1.python环境
    python:win32 3.6.3版本

    运行环境介绍：在python读取txt文档的时候在首行会出现诡异的\ufeff，对比字符串就会对比失败

2.调试代码
    不多说上代码，要兑取的txt文档内容如下：    

测试ufeff问题
    python测试代码如下：
#coding=utf-8
 
filePath = r'C:\Users\xzp\Desktop\python\userConfig.txt'
s='测试ufeff问题'
with open(filePath,'r',encoding='utf-8') as dic:
##    dic.read()
    for item in dic:
        if item.strip() == s:
            print('ok')
        print(item)
print(s)
    上面程序的输出结果如下：
测试ufeff问题
测试ufeff问题
    上面的输入没有ok。于是我进入了debugger看看那个变量的情况

    调试过后发现如下结果：



这个问题出现了！！！！！

3.解决方案：

#coding=utf-8
 
filePath = r'C:\Users\xzp\Desktop\python\userConfig.txt'
s='测试ufeff问题'
with open(filePath,'r',encoding='utf-8') as dic:
##    dic.read()
    for item in dic:
        if item.encode('utf-8').decode('utf-8-sig').strip() == s:
            print('ok')
        print(item)
print(s)
程序的输出结果：

ok
﻿测试ufeff问题
测试ufeff问题
--------------------- 
作者：浅颜半夏 
来源：CSDN 
原文：https://blog.csdn.net/xiazhipeng1000/article/details/79720391 
版权声明：本文为博主原创文章，转载请附上博文链接！
