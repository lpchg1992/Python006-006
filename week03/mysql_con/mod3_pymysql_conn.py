# pip install pymysql
import pymysql

# 打开数据库连接
# mysql> create database testdb;
# %匹配所有远程IP地址
# mysql> GRANT ALL PRIVILEGES ON testdb.* TO 'testuser'@'%' IDENTIFIED BY
#      '!Geektime8848';

db = pymysql.connect(host="47.244.201.185", port=3306, user="testuser", 
                     password="!Geektime8848", db="testdb")

try:

    # 使用cursor()方法创建一个游标对象
    with db.cursor() as cursor:
        sql = '''SELECT VERSION()'''
        # 使用 execute()方法执行sql语句
        cursor.execute(sql)
        result = cursor.fetchone()
    db.commit()

except Exception as e:
    print(f"fetch_error: {e}")

finally:
    # 关闭数据库连接
    db.close()

print(f"database version: {result}")
