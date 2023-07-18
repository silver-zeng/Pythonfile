import pymysql
import redis
class Mysql_con():
    def __init__(self,host='127.0.0.1',port=3306,user="zengfanyu",password="zengfanyu1314",database="testdb",charset='utf8'):
        self.host=host
        self.port=port
        self.user=user
        self.password=password
        self.database=database
        self.charset=charset
    def mysql_connection(self):

            # "host": "localhost",
            # "port": 3306,
            # "user": "zengfanyu",
            # "password": "zengfanyu1314",
            # "database": "testdb",

        config = {
            "host": self.host,
            "port": self.port,
            "user": self.user,
            "password": self.password,
            "database": self.database,
            "charset": self.charset,
        }
        # 连接数据库
        con = pymysql.connect(**config)
        # 获取游标，所有sql都是游标去操作
        cur = con.cursor()
        self.con=con
        self.cur=cur


    def mysql_todo(self,sql):  # 创建表

        #sql="create table `test`(`id` int(5) not null AUTO_INCREMENT,`name` varchar(20),`age` int(3), `hobby` varchar(50),PRIMARY KEY(`id`))"
        try:
            self.cur.execute(sql)
        except Exception as e:
            print("sql语句有错误！" + sql)
            self.con.rollback()  # 事务回滚
        else:
            print("sql执行成功！")
            all=self.cur.fetchall()  # 获取所有结果
            self.con.commit()  # 提交事务
            print(all)
        self.cur.close()
        self.con.close()

class Redis_con():
    def __init__(self,host='127.0.0.1', port=6379,db=0,decode_responses=True):
        self.host=host
        self.port=port
        self.db=db
        self.decode_responses=decode_responses # redis 取出的结果默认是字节，设定 decode_responses=True 改成字符串
    def redis_connection(self): # 连接Redis
        redis_conn = redis.StrictRedis(host=self.host, port=self.port, db=self.db,decode_responses=self.decode_responses)
        self.redis_conn = redis_conn
    def redis_str_set(self,name,value): # 覆盖增加值
        self.redis_conn.set(name,value)
        print("插入成功=====>"+f"{name}:{value}")
    def redis_str_fing(self,name):  # 查询健值
        valu=self.redis_conn.get(name)
        print(valu)
    def redis_str_rename(self,name,newname): # 改健名字
        self.redis_conn.rename(name,newname)
        print(f"{name}，改名为{newname}")

if __name__ == '__main__':
    # Mysqlcon=Mysql_con("localhost",3306,"zengfanyu","zengfanyu1314","testdb")
    # Mysqlcon.mysql_connection()
    # # sql="create table `test`(`id` int(5) not null AUTO_INCREMENT,`name` varchar(20),`age` int(3), `hobby` varchar(50),PRIMARY KEY(`id`))"
    # # sql="insert into test values ('5','哈哈哈','22','羽毛球')"
    # sql="select * from test"
    # Mysqlcon.mysql_todo(sql)
    Redis=Redis_con()
    Redis.redis_connection()
    Redis.redis_str_set('zeng','asfasfasfasfasfasf')
    Redis.redis_str_fing("zeng")



