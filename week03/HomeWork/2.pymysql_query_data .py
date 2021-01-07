import pymysql
from dbini_parser import read_db_config


db = pymysql.connect(**read_db_config())

try:
    with db.cursor() as cursor:
        sql = '''SELECT * FROM userinfo'''
        cursor.execute(sql)
        users = cursor.fetchall()
        for user in users:
            print(user)
    db.commit()

except Exception as e:
    print(f"fetch_error: {e}")

finally:
    # 关闭数据库连接
    db.close()
