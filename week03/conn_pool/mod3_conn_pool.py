import pymysql
# pip install DBUtils
# 注意新版中需要小写
# 在连接层面解决连接池问题，应用层无感知
# 还可能解决线程安全的问题
# 两种用法：每个线程一个连接或者共享连接，此处第二种
# 关于封装的做法是一个很好的学习资源
from dbutils.pooled_db import PooledDB
db_config = {
    "host": '47.244.201.185',
    "port": 3306,
    "user": 'testuser',
    "passwd": '!Geektime8848',
    "db": 'testdb',
    "charset": 'utf8mb4',
    "maxconnections": 0,  # 连接池允许的最大连接数
    "mincached": 4,       # 初始化时连接池中至少创建的空闲连接，0不创建
    "maxcached": 0,       # 连接池中最多闲置的连接，0不限制
    "maxusage": 5,        # 每个连接最多被重复使用的次数，None表示无限制
    "blocking": True      # 连接池中如果没有可用连接是否阻塞等待，True等待，False，不等待，报错，根据不同业务特点处理
}

spool = PooledDB(pymysql, **db_config)

conn = spool.connection()
cur = conn.cursor()
SQL = "select * from bookorm;"
cur.execute(SQL)
f = cur.fetchall()
print(f)
cur.close()
conn.close()
