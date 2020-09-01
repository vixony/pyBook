@(tigerfive)[学习笔记][flask][python][环境搭建]
### 1.环境的准备
```shell
yum -y install gcc gcc-c++ zlib zlib-devel openssl openssl-devel pcre pcre-devel GeoIP gd libXpm libxslt sqlite-devel nginx
systemctl restart nginx
```
检测nginx
```shell
ps -ef | grep nginx 或 直接浏览器访问
wget https://dev.mysql.com/get/mysql57-community-release-el7-11.noarch.rpm 
yum -y install mysql-community-server 安装的是5.7
systemctl start mysqld systemctl enable mysqld
grep password /var/log/mysqld.log
mysqladmin -u root -p'原密码' password '新密码'
mysql -u root -p'新密码'
```
检测mysql
```shell
ps -ef | grep mysql 或者
wget https://www.python.org/ftp/python/3.6.0/Python-3.6.0.tgz
```
### 2.安装python3.6
```
tar xvf Python-3.6.0.tgz
cd  Python-3.6.0
./configure --prefix=/usr/local/python3.6 && make && make install
```
3.删除2.7的命令链接,并新建链接
```
rm -rf /usr/bin/python
ln -s /usr/local/python3.6/bin/python3.6 /usr/bin/python
```
4.修改环境变量
```
vim ~/.bash_profile
PATH=$PATH:$HOME/bin:.usr/local/python3.6/bin
```
5.解决yum失效问题
```
vim /usr/bin/yum 修改解释器为python2.7
```
6.测试python是否安装成功
```
python -V
```

7.使用pip安装python模块
```
rm -rf /usr/bin/pip
ln -s /usr/local/python3.6/bin/pip3.6 /usr/bin/pip
```
8.安装flask
```
pip install flask
```

9.创建项目目录
```shell 
mkdir  /root/flask_pro
vim /root/flask_pro/flask_app.py
#vim /root/flask_pro/flask_app.py
from flask import Flask, request
app = Flask(name)@app.route('/helloworld/')<br/" rel="nofollow">br/>@app.route('/helloworld/')<br <="" a="">def helloword():
return 'hello world'
if name == 'main' :
app.run(host='0.0.0.0', port=5005)
```

测试：
```python
python flask_app.py  http://+ip/域名:5005/*/
```
10.安装uwsgi   是python的web容器
```
pip install uwsig
```

11.配置uwsgi
```shell
vim /root/flask_pro/uwsgi.ini
[uwsgi]
socket=127.0.0.1:5005
chdir=/root/flask_pro/
wsgi-file=flask_app.py
callable=app
processes=2
threads=2
buffer-size=65536
```
12.nginx配置文件：
```
#vim /usr/local/nginx/conf/nginx.conf   添加一个虚拟主机，添加到default server前面
server {
listen       80;
server_name  xiangmu.buy360.xyz;
    location / {        include  uwsgi_params;        uwsgi_pass  127.0.0.1:5005;    }}
```
注意：添加内容后要把nginx.conf中原先的 server{ listen 80;……} 配置删除或注释掉。

13.
```
uwsgi --ini /root/flask_pro/uwsgi.ini &
```
实际使用要把上面的命令写到开机启动文件内：rc.local

14.systemctl restart nginx

15.测试：http://192.168.100.10/helloworld/

项目测试

1 拷贝乐居项目 到ls /root/flask_pro/
[root@localhost flask_pro]# ls
app  flask_app.py  manage.py  migrations  requirements.txt  tests  uwsgi.ini  venv

而后安装依赖包。
```
#pip install -r requirements.txt
```
查看flask项目使用的哪个端口：
```
#cat manage.py    修改如下内容
if name == 'main':
manager.run(host='0.0.0.0',port=5000)
```
2 修改初始化文件，指向乐居
```
vim uwsgi.ini
[uwsgi]
socket=127.0.0.1:5000
chdir=/root/flask_pro/
wsgi-file=manage.py
callable=app
processes=2
threads=2
buffer-size=65536
```

3 修改nginx端口转发
```
server {
listen       80;
server_name  xiangmu.buy360.xyz;

    location / {        include  uwsgi_params;        uwsgi_pass  127.0.0.1:5000;    }}
```
4 python 加载uwsgi.ini 
```
#uwsgi -d --ini /root/flask_pro/uwsgi.ini
```

做开机启动：
```
#vim /etc/rc.local  追加如下内容
uwsgi -d  --ini /root/flask_pro/uwsgi.ini
#chmod  +x  /etc/rc.d/rc.local
#systemctl enable rc-local
```
5 重启nginx，并访问。
```
#systemctl restart nginx
http://xiangmu.buy360.xyz
```
看到
“RESTFul API 开发测试”
即可。
