# simpleProxy

多线程获取IP代理池及User-Agent代理池 无需安装数据库，使用方便

This project is used to provide IP agent pool and user-agent pool for reptiles.

---

## 使用步骤
#### 一、安装Python3
* 进入Python官网安装Python3 https://www.python.org/downloads/

#### 二、安装requests
    pip install requests

#### 三、安装bs4
    pip install bs4

#### 四、运行脚本
    python pool_ua.py # 获取代理头（可不运行，文件一寸照）
    python pool_ip.py # 获取代理ip
    python proxy_test.py http://www.baidu.com # 测试代理ip（参数未所要请求的地址，可根据自己的业务逻辑重构）

* 代理ip来自于西刺代理：http://www.xicidaili.com/nn/
* 代理user-agent来自于fake-useragent：https://fake-useragent.herokuapp.com/browsers/0.1.8/
* 默认获取10页西刺代理，线程不能调过大，可能会玩脱
