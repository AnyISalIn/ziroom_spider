# ziroom_spider

> 仅支持 `Python 3`

## usage

```python
In [1]: from spider import ZiroomSpider

In [2]: z = ZiroomSpider('http://sh.ziroom.com/z/nl/z3-o1.html')

# 默认抓取第一页房子信息
In [3]: z.crawl_houses()
2017-02-28 21:48:49,879 INFO  - ====== 开始抓取地铁数据 ========
2017-02-28 21:48:49,910 INFO  - 地铁站 [闵行吴泾]  存在
2017-02-28 21:48:49,911 INFO  - 地铁站 [上海周边昆山] 11号线光明路 存在
2017-02-28 21:48:49,912 INFO  - 地铁站 [嘉定菊园新区] 11号线嘉定西 存在
2017-02-28 21:48:49,913 INFO  - 地铁站 [嘉定嘉定新城] 11号线白银路 存在
2017-02-28 21:48:49,914 INFO  - 地铁站 [嘉定嘉定老城]  存在
2017-02-28 21:48:49,915 INFO  - 地铁站 [嘉定菊园新区] 11号线嘉定北 存在
2017-02-28 21:48:49,916 INFO  - 地铁站 [嘉定嘉定老城]  存在
2017-02-28 21:48:49,916 INFO  - 地铁站 [嘉定嘉定老城]  存在
2017-02-28 21:48:49,917 INFO  - 地铁站 [嘉定嘉定新城] 11号线白银路 存在
2017-02-28 21:48:49,920 INFO  - 地铁站 [浦东航头] 16号线鹤沙航城 存在
2017-02-28 21:48:49,921 INFO  - 地铁站 [嘉定嘉定老城]  存在
2017-02-28 21:48:49,922 INFO  - 地铁站 [嘉定嘉定新城] 11号线白银路 存在
2017-02-28 21:48:49,922 INFO  - 地铁站 [嘉定菊园新区] 11号线嘉定西 存在
2017-02-28 21:48:49,923 INFO  - 地铁站 [浦东航头] 16号线鹤沙航城 存在
2017-02-28 21:48:49,924 INFO  - 地铁站 [嘉定嘉定老城]  存在
2017-02-28 21:48:49,925 INFO  - 地铁站 [嘉定菊园新区] 11号线嘉定北 存在
2017-02-28 21:48:49,925 INFO  - 地铁站 [嘉定嘉定老城]  存在
2017-02-28 21:48:49,926 INFO  - 地铁站 [宝山罗店] 7号线罗南新村 存在
2017-02-28 21:48:49,926 INFO  - ====== 开始抓取房子数据 ========
2017-02-28 21:48:50,598 INFO  - 光明捷座4居室-北卧 没有变化
2017-02-28 21:48:50,655 INFO  - 南北周4居室-北卧 没有变化
2017-02-28 21:48:50,714 INFO  - 盘古嘉德4居室-西卧 没有变化
2017-02-28 21:48:50,769 INFO  - 日月光伯爵天地4居室-西卧 没有变化
2017-02-28 21:48:50,829 INFO  - 新城香溢都荟5居室-北卧 没有变化
2017-02-28 21:48:50,890 INFO  - 获取 新城香溢都荟5居室-北卧 价格 960
2017-02-28 21:48:50,952 INFO  - 南北周4居室-南卧 没有变化
2017-02-28 21:48:51,009 INFO  - 现代苑3居室-北卧 没有变化
2017-02-28 21:48:51,065 INFO  - 万科金色领域4居室-北卧 没有变化
2017-02-28 21:48:51,164 INFO  - 新城香溢璟庭二期5居室-北卧 没有变化
2017-02-28 21:48:51,223 INFO  - 美罗家园润苑3居室-南卧 没有变化
2017-02-28 21:48:51,280 INFO  - 获取 万科金色领域4居室-北卧 价格 1030
2017-02-28 21:48:51,339 INFO  - 鹤沙航城顺和苑3居室-北卧 没有变化
2017-02-28 21:48:51,395 INFO  - 获取 新城香溢都荟5居室-北卧 价格 1060
2017-02-28 21:48:51,455 INFO  - 日月光伯爵天地4居室-北卧 没有变化
2017-02-28 21:48:51,509 INFO  - 南苑新世纪公寓4居室-北卧 没有变化
2017-02-28 21:48:51,571 INFO  - 获取 新城香溢璟庭二期5居室-北卧 价格 990
2017-02-28 21:48:51,625 INFO  - 获取 鹤沙航城顺和苑3居室-北卧 价格 990
2017-02-28 21:48:51,628 INFO  - ====== 抓取进程结束 ========

# 不抓取地铁信息
In [4]: z.crawl_houses(subway=False)
2017-02-28 21:49:18,334 INFO  - ====== 开始抓取房子数据 ========
2017-02-28 21:49:18,830 INFO  - 现代苑3居室-北卧 没有变化
2017-02-28 21:49:18,892 INFO  - 美罗家园润苑3居室-南卧 没有变化
2017-02-28 21:49:18,971 INFO  - 新城香溢都荟5居室-北卧 没有变化
2017-02-28 21:49:19,034 INFO  - 新城香溢璟庭二期5居室-北卧 没有变化
2017-02-28 21:49:19,086 INFO  - 鹤沙航城顺和苑3居室-北卧 没有变化
2017-02-28 21:49:19,146 INFO  - 南北周4居室-北卧 没有变化
2017-02-28 21:49:19,251 INFO  - 盘古嘉德4居室-西卧 没有变化
2017-02-28 21:49:19,301 INFO  - 获取 鹤沙航城顺和苑3居室-北卧 价格 990
2017-02-28 21:49:19,364 INFO  - 光明捷座4居室-北卧 没有变化
2017-02-28 21:49:19,865 INFO  - 日月光伯爵天地4居室-西卧 没有变化
2017-02-28 21:49:19,920 INFO  - 获取 新城香溢璟庭二期5居室-北卧 价格 1030
2017-02-28 21:49:19,981 INFO  - 南苑新世纪公寓4居室-北卧 没有变化
2017-02-28 21:49:20,035 INFO  - 万科金色领域4居室-北卧 没有变化
2017-02-28 21:49:20,091 INFO  - 日月光伯爵天地4居室-北卧 没有变化
2017-02-28 21:49:20,142 INFO  - 获取 万科金色领域4居室-北卧 价格 930
2017-02-28 21:49:20,203 INFO  - 获取 新城香溢都荟5居室-北卧 价格 960
2017-02-28 21:49:20,270 INFO  - 获取 新城香溢都荟5居室-北卧 价格 960
2017-02-28 21:49:20,332 INFO  - 南北周4居室-南卧 没有变化
2017-02-28 21:49:20,334 INFO  - ====== 抓取进程结束 ========

# 抓取所有房子信息
In [5]: z.crawl_houses(all=True)
2017-02-28 21:49:36,501 INFO  - ====== 开始抓取地铁数据 ========
2017-02-28 21:49:44,201 INFO  - 地铁站 [闵行吴泾]  存在
2017-02-28 21:49:44,202 INFO  - 地铁站 [上海周边昆山] 11号线光明路 存在
2017-02-28 21:49:44,203 INFO  - 地铁站 [嘉定菊园新区] 11号线嘉定西 存在
2017-02-28 21:49:44,204 INFO  - 地铁站 [嘉定嘉定新城] 11号线白银路 存在
2017-02-28 21:49:44,205 INFO  - 地铁站 [嘉定嘉定老城]  存在
2017-02-28 21:49:44,205 INFO  - 地铁站 [嘉定菊园新区] 11号线嘉定北 存在
2017-02-28 21:49:44,206 INFO  - 地铁站 [嘉定嘉定老城]  存在
....
2017-02-28 21:50:42,774 INFO  - 获取 新城香溢都荟5居室-南卧 价格 1430
2017-02-28 21:50:42,843 INFO  - 泰翔嘉苑4居室-南卧 没有变化
2017-02-28 21:50:42,913 INFO  - 繁荣华庭3居室-南卧 没有变化
2017-02-28 21:50:42,978 INFO  - 获取 菱翔苑3居室-北卧 价格 1430
2017-02-28 21:50:43,052 INFO  - 金榜雅苑4居室-北卧 没有变化
2017-02-28 21:50:43,128 INFO  - 金地自在城（二期）7居室-北卧 没有变化
2017-02-28 21:50:43,197 INFO  - 获取 金地自在城（二期）7居室-北卧 价格 1430
2017-02-28 21:50:43,260 INFO  - 获取 日月光伯爵天地4居室-南卧 价格 1430
2017-02-28 21:50:43,332 INFO  - 获取 招商海德名门（公寓）4居室-北卧 价格 1430
2017-02-28 21:50:43,405 INFO  - 获取 百鸟苑3居室-北卧 价格 1460
2017-02-28 21:50:43,482 INFO  - 获取 华川家园3居室-南卧 价格 1430
...

# 查询
In [15]: from models import House, Subway

In [16]: z.query_subway().count()
Out[16]: 252

In [17]: z.query_subway().first()
Out[17]: <Subway [普陀桃浦] 11号线桃浦新村>

In [18]: z.query_subway().first().houses
Out[18]:
[<House 中金海棠湾（公寓）4居室-南卧 1490 10.1>,
 <House 桃浦五村迎春苑3居室-南卧 2460 16.7>,
 <House 桃浦一村瑞香苑2居室-东 4590 55.03>,
 <House 桃浦六村绿春苑2居室-南卧 2160 15.4>,
 <House 桃浦一村瑞香苑2居室-东 4590 55.03>,
 <House 桃浦二村永汇新苑3居室-南卧 2330 12.3>,
 <House 桃浦五村迎春苑3居室-南卧 2460 16.7>,
 <House 桃浦一村瑞香苑2居室-东 4590 55.03>,
 <House 桃浦二村永汇新苑3居室-南卧 2330 12.3>,
 <House 桃浦五村迎春苑3居室-南卧 2460 16.7>,
 <House 桃浦二村永汇新苑3居室-南卧 2330 12.3>,
 <House 桃浦一村瑞香苑2居室-东 4590 55.03>,
 <House 桃浦一村瑞香苑2居室-东 4590 55.03>,
 <House 桃浦二村永汇新苑3居室-南卧 2330 12.3>,
 <House 桃浦一村瑞香苑2居室-东 4590 49.76>,
 <House 桃浦五村迎春苑3居室-北卧 1590 7.8>,
 <House 桃浦九村4居室-北卧 1630 10.7>]

In [38]: z.query_houses().filter(House.name.like("润江花苑%")).all()
Out[38]:
[<House 润江花苑3居室-北卧 1530 9.4>,
  <House 润江花苑3居室-北卧 1530 9.4>,
  <House 润江花苑3居室-北卧 1530 9.4>,
  <House 润江花苑3居室-北卧 1530 9.4>,
  <House 润江花苑3居室-北卧 1530 9.4>,
  <House 润江花苑4居室-南卧 1530 10.9>]
```

## command line

```shellscript
$ python command.py -h
usage: spider [-h] [-l LIMIT] [-s SORT] [-b] [-a] [-d] {update} ...

positional arguments:
  {update}
    update              update house

optional arguments:
  -h, --help            show this help message and exit
  -l LIMIT, --limit LIMIT
                        limit output
  -s SORT, --sort SORT  sort by column
  -b, --subway          show subway
  -a, --all             show all houses
  -d, --desc            desc


$ python command.py
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 名称                     | 编号               |   价格 |   面积 | 链接                                    |
+==========================+====================+========+========+=========================================+
| 盘古嘉德4居室-西卧       | SHZRGY081757070_03 |    930 |   6    | http://sh.ziroom.com/z/vr/60407547.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 盘古嘉德3居室-北卧       | SHZRGY031604161_02 |    990 |   6    | http://sh.ziroom.com/z/vr/60215174.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 兰馨苑（泗泾）3居室-南卧 | SHZR72471992_02    |   1330 |   6    | http://sh.ziroom.com/z/vr/60077149.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 新凯城丹桂苑3居室-南卧   | SHZR82273387_02    |   1490 |   6    | http://sh.ziroom.com/z/vr/60061036.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 兰馨苑（泗泾）3居室-南卧 | SHZR72471992_02    |   1330 |   6    | http://sh.ziroom.com/z/vr/60077149.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 兰馨苑（泗泾）3居室-南卧 | SHZR72471992_02    |   1330 |   6    | http://sh.ziroom.com/z/vr/60077149.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 兰馨苑（泗泾）3居室-南卧 | SHZR72471992_02    |   1330 |   6    | http://sh.ziroom.com/z/vr/60077149.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 兰馨苑（泗泾）3居室-南卧 | SHZR72471992_02    |   1330 |   6    | http://sh.ziroom.com/z/vr/60077149.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 盘古嘉德4居室-西卧       | SHZRGY081757070_03 |    930 |   6    | http://sh.ziroom.com/z/vr/60407547.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+
| 胜悦嘉苑4居室-北卧       | SHZRGY081756394_03 |   1090 |   6.01 | http://sh.ziroom.com/z/vr/60405440.html |
+--------------------------+--------------------+--------+--------+-----------------------------------------+

$ python command.py -l 10 --sort=area  --desc --subway
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 名称                         | 编号          |   价格 |   面积 | 链接                                    | 地铁                          |
+==============================+===============+========+========+=========================================+===============================+
| 中凯城市之光（静安）4居室-南 | SHJA95117797  |  25280 | 203.89 | http://sh.ziroom.com/z/vr/20041755.html | [静安南京西路] 2号线南京西路  |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 太阳都市花园2居室-南         | SHZR50742607  |  12320 | 145.56 | http://sh.ziroom.com/z/vr/60042295.html | [黄浦豫园] 10号线豫园         |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 美岸栖庭（公寓）3居室-南     | SHBS28503866  |   7170 | 142.48 | http://sh.ziroom.com/z/vr/20034076.html | [宝山高境] 3号线长江南路      |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 尊园3居室-南                 | SHZR80106625  |  12720 | 139.14 | http://sh.ziroom.com/z/vr/60048574.html | [徐汇徐家汇] 9号线徐家汇      |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 新城海上名园3居室-南北       | SHPDX25071822 |  11080 | 123.44 | http://sh.ziroom.com/z/vr/20020823.html | [浦东洋泾] 9号线杨高中路      |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 财富公寓3居室-南             | SHYP40113733  |   8010 | 118.47 | http://sh.ziroom.com/z/vr/20032461.html | [杨浦五角场] 10号线江湾体育场 |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 新家坡园景苑3居室-南         | SHHP11242894  |   9750 | 109.57 | http://sh.ziroom.com/z/vr/20013271.html | [黄浦五里桥] 9号线马当路      |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 九歌上郡2居室-南             | SHMH52848971  |   8190 | 106.01 | http://sh.ziroom.com/z/vr/20019800.html | [闵行静安新城] 9号线合川路    |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 东航公寓3居室-南             | SHXH09981389  |  10010 | 104.35 | http://sh.ziroom.com/z/vr/20012919.html | [徐汇徐家汇] 4号线宜山路      |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
| 九城湖滨国际3居室-南         | SHZR33000919  |   6120 | 100.15 | http://sh.ziroom.com/z/vr/60000922.html | [松江九亭] 9号线九亭          |
+------------------------------+---------------+--------+--------+-----------------------------------------+-------------------------------+
```
