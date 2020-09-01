# Redis命令操作详解

### 一、key pattern 查询相应的key

　　（1）redis允许模糊查询key　　有3个通配符  \*、?、\[\]



　　（3）type key：返回key存储的类型



　　（5）del key：删除key

　　（6）rename key newkey：改名

　　（7）renamenx key newkey：如果newkey不存在则修改成功

　　（8）move key 1：将key移动到1数据库

　　（9）ttl key：查询key的生命周期（秒）

　　（10）expire key 整数值：设置key的生命周期以秒为单位

　　（11）pexpire key 整数值：设置key的生命周期以毫秒为单位

　　（12）pttl key：查询key 的生命周期（毫秒）

　　（13）perisist key：把指定key设置为永久有效

### 二、字符串类型的操作







xx：如果key存在则修改其值















对于字符串的下标，左数从0开始，右数从-1开始

注意：当start&gt;length，则返回空字符串

当stop&gt;=length，则截取至字符串尾

如果start所处位置在stop右边，则返回空字符串





（10）incrby key 2：跳2自增






                   offset最大到多少

2^32-1，即可推出最大的字符串为512M









### 







































### 

　　Redis hash 是一个string类型的field和value的映射表，它的添加、删除操作都是O\(1\)（平均）。hash特别适用于存储对象，将一个对象存储在hash类型中会占用更少的内存，并且可以方便的存取整个对象。



　　　　　 hash\_max\_zipmap\_value 512 \#配置value最大为512字节

　　（1）hset myhash field value：设置myhash的field为value

　　（2）hsetnx myhash field value：不存在的情况下设置myhash的field为value

　　（3）hmset myhash field1 value1 field2 value2：同时设置多个field

　　（4）hget myhash field：获取指定的hash field

　　（5）hmget myhash field1 field2：一次获取多个field

　　（6）hincrby myhash field 5：指定的hash field加上给定的值

　　（7）hexists myhash field：测试指定的field是否存在

　　（8）hlen myhash：返回hash的field数量

　　（9）hdel myhash field：删除指定的field

　　（10）hkeys myhash：返回hash所有的field

　　（11）hvals myhash：返回hash所有的value

　　（12）hgetall myhash：获取某个hash中全部的field及value　

### 五、集合结构操作



　　（1）sadd key value1 value2：往集合里面添加元素

　　（2）smembers key：获取集合所有的元素

　　（3）srem key value：删除集合某个元素

　　（4）spop key：返回并删除集合中1个随机元素（可以坐抽奖，不会重复抽到某人）　　　

　　（5）srandmember key：随机取一个元素

　　（6）sismember key value：判断集合是否有某个值

　　（7）scard key：返回集合元素的个数

　　（8）smove source dest value：把source的value移动到dest集合中

　　（9）sinter key1 key2 key3：求key1 key2 key3的交集

　　（10）sunion key1 key2：求key1 key2 的并集

　　（11）sdiff key1 key2：求key1 key2的差集

　　（12）sinterstore res key1 key2：求key1 key2的交集并存在res里　

### 六、有序集合





　　当元素被添加到集合中时，一个元素到score的映射被添加到hash table中，所以给定一个元素获取score的开销是O\(1\)。另一个score到元素的映射被添加的skip list，并按照score排序，所以就可以有序地获取集合中的元素。添加、删除操作开销都是O\(logN\)和skip list的开销一致，redis的skip list 实现是双向链表，这样就可以逆序从尾部去元素。sorted set最经常使用方式应该就是作为索引来使用，我们可以把要排序的字段作为score存储，对象的ID当元素存储。

　　（1）zadd key score1 value1：添加元素

　　（2）zrange key start stop \[withscore\]：把集合排序后,返回名次\[start,stop\]的元素  默认是升续排列  withscores 是把score也打印出来

　　（3）zrank key member：查询member的排名（升序0名开始）

　　（4）zrangebyscore key min max \[withscores\] limit offset N：集合（升序）排序后取score在\[min, max\]内的元素，并跳过offset个，取出N个 





　　（7）zrem key value1 value2：删除集合中的元素

　　（8）zremrangebyrank key start end：按排名删除元素，删除名次在\[start, end\]之间的

　　（9）zcard key：返回集合元素的个数

　　（10）zcount key min max：返回\[min, max\]区间内元素数量

　　（11）zinterstore dest numkeys key1\[key2..\] \[WEIGHTS weight1 \[weight2...\]\] \[AGGREGATE SUM\|MIN\|MAX\]

求key1，key2的交集，key1，key2的权值分别是weight1，weight2





### 七、服务器相关命令

　　（1）ping：测定连接是否存活



　　（3）select：选择数据库

　　（4）quit：退出连接

　　（5）dbsize：返回当前数据库中key的数目

　　（6）info：获取服务器的信息和统计

　　（7）monitor：实时转储收到的请求

　　（8）config get 配置项：获取服务器配置的信息

　　　　 config set 配置项  值：设置配置项信息

　　（9）flushdb：删除当前选择数据库中所有的key

　　（10）flushall：删除所有数据库中的所有的key



　　（12）bgrewriteaof：后台保存rdb快照









　　注意：如果不小心运行了flushall，立即shutdown nosave，关闭服务器，然后手工编辑aof文件，去掉文件中的flushall相关行，然后开启服务器，就可以倒回原来是数据。如果flushall之后，系统恰好bgwriteaof了，那么aof就清空了，数据丢失。



　　问：多慢才叫慢？

　　答：由slowlog-log-slower-than 10000，来指定（单位为微秒）

　　问：服务器存储多少条慢查询记录

　　答：由slowlog-max-len 128，来做限制　　
