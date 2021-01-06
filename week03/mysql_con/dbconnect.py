import pymysql
from dbconfig import read_db_config

# 可以直接将字典读取为键值参数
db = pymysql.connect(**read_db_config())

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
