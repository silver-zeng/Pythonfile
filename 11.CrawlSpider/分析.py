"""
一级页面--列表页
https://book.zongheng.com/store/c0/c0/b0/u0/p1/v9/s1/t0/u0/i1/ALL.html

二级页面--小说详情页
https://book.zongheng.com/book/1173086.html

三级页面--小说目录页
https://book.zongheng.com/showchapter/1173086.html

四级页面--小说内容页
https://book.zongheng.com/chapter/1173086/67367501.html

"""

"""
https://book.zongheng.com/book/1066246.html
https://book.zongheng.com/book/1232810.html
https://book.zongheng.com/book/1270327.html

https://book.zongheng.com/book/\d+.html
"""

import pymysql

db_config = {
    'host':'127.0.0.1',
    'port':3306,
    'password':'qwe123',
    'user':'tongyao',
    'db':'class21',
    'charset':"utf8",
}

conn = pymysql.connect(**db_config)
print(conn)