# Python之MySQLdb

> MySQLdb是用于Python链接Mysql数据库的接口，它实现了Python数据库API规范V2.0，基于MySql C API上建立的。

#### 1. MySQLdb安装

1. 安装Mysql，参考上篇博客数据库之MySql。
2. 使用pip安装MySQLdb：

* ```
  pip install MySQL-python
  ```

> 但是安装的时候会报错：error: command 'C:\Program Files\Microsoft Visual Studio 14.0\VC\BIN\cl.exe' failed with exit status 2
>
> 下面推荐两种方法进行解决：

1. 下载Python-3.5及上版本扩展的mysql驱动：[https://pypi.python.org/pypi/mysqlclient/1.3.10](https://pypi.python.org/pypi/mysqlclient/1.3.10)

> 之后将下载后的\*.whl文件跟pip.exe放在同个目录（一般是在 ..\Python36\Scripts 里）
>
> 然后用cmd命令进入到这个目录执行PIP命令安装：

```
pip install mysqlclient-1.3.10-cp36-cp36m-win32.whl
```

1. 安装pymysql代替：

```
pip install pymysql
```

> 注：以上安装方法内容来自原文[https://www.cnblogs.com/bu1tcat/p/8283742.html](https://www.cnblogs.com/bu1tcat/p/8283742.html)



