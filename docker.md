# 关键字：

```
镜像 images
镜像名 image_name
镜像id image_id
容器 container
容器名 con_name
容器id con_id
```

* **从公网拉取一个镜像**

```
docker pull images_name
```

* **查看已有的docker镜像**

```
[root@docker ~]# docker images
```

* **查看帮助**

```
docker command --help
```

* **查看镜像列表**

```
docker search nginx
```

* **启动一个容器**

\#基于hello-world镜像启动一个容器，如果本地没有镜像会从公网拉取过来，这次做为测试用

```
docker run hello-world
```

* **导出镜像**

```
docker save -o image_name.tar image_name
```

* **删除镜像**

```
docker rmi image_name
```

* **启动一个容器**

```
docker run --name=con_name images
--name  #设置容器名
```

**基于创建好的容器自定义docker镜像**

```
docker commit -m "con_name" con_id image_name
```

**创建一个容器的同时进入这个容器**

```
docker run -it --name=con_name images
it     #在启动之后进入这个容器
```

**创建一个容器，放入后台运行，把物理机80端口映射到容器的80端口**

```
docker run -d -p 81:80 image_name
#-p 参数说明
-p hostPort:containerPort
-p ip:hostPort:containerPort
-p ip::containerPort
-p hostPort:containerPort:udp
```

**看容器的端口映射情况**

```
docker port con_id
```

**查看正在运行的容器**

```
docker ps
```

**查看所有的容器**

```
docker ps -a
```

**动态查看容器日志**

```
docker logs -f con_name
```

**进入容器**

```
docker attach con_name
```

**退出容器**

\# 方法一

```
exit
```

\# 方法二

```
ctrl+p && ctrl+q (一起按，注意顺序，退出后容器依然保持启动状态)
```

**删除容器**

```
docker rm  con_name
#强制删除需要加-f，不加-f不能删除正在运行中的容器，非常危险，最好不用
```

**查看docker网络**

```
[root@docker ~]# docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
3f91f2097286        bridge              bridge              local
d7675dbd247c        docker_gwbridge     bridge              local
5b36c7e947fd        host                host                local
ims6qkpikafu        ingress             overlay             swarm
85ba10e7ef79        none                null                local
```

**创建一个docker网络my-docker**

```
docker network create -d bridge \
--subnet=192.168.0.0/24 \
--gateway=192.168.0.100 \
--ip-range=192.168.0.0/24 \
```

my-docker

**利用刚才创建的网络启动一个容器**

```
#docker run --network=my-docker --ip=192.168.0.5 -itd --name=con_name -h lb01 image_name
--network   #指定容器网络
--ip        #设定容器ip地址
-h          #给容器设置主机名
```

**查看容器pid**

```
#方法一：docker top con_name
#方法二：docker inspect --format "{{.State.Pid}}" con_name
```

**运行dockerfile并给dockerfile创建的镜像建立名字**

    docker build -t mysql:3.6.34 `pwd`

**mariadb容器启动前需先设置密码方法**

```
docker run -d -P -e MYSQL_ROOT_PASSWORD=password  img_id
```

**docker修改镜像名**

```
docker tag imageid name:tag
```

**进入docker容器脚本**

    [root@docker ~]# cat nsenter.sh 
    PID=`docker inspect --format "{{.State.Pid}}" $1`
    nsenter -t $PID -u --mount -i -n -p

**创建一个网络**

```
docker network create --driver bridge --subnet 172.22.16.0/24 --gateway 172.22.16.1 my_net2
```

**将容器添加到my\_net2网络 connect**

```
docker network connect my_net2 oldboy1
```

**docker日志模块**

**使用filebeat收集日志**

```
{
  "registry-mirrors": ["https://56px195b.mirror.aliyuncs.com"],
  "cluster-store":"consul://192.168.56.13:8500",
  "cluster-advertise": "192.168.56.11:2375",
  "log-driver": "fluentd",
  "log-opts": {
        "fluentd-address":"192.168.56.13:24224",
        "tag":"linux-node1.example.com"
  }
}
```



