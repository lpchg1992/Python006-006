import pymysql

db = pymysql.connect(host="47.244.201.185", port=3306, user="testuser",
                     password="!Geektime8848", db="testdb")

try:

    # sql语句中%是占位符
    with db.cursor() as cursor:
        sql = '''UPDATE book SET name = %s WHERE id = %s'''
        value = ("改变", 1002)
        cursor.execute(sql, value)
    db.commit()

except Exception as e:
    print(f"update error {e}")

finally:
    # 关闭数据库连接
    db.close()
    # 游标作用的行数，并不是表中行数
    print(cursor.rowcount)
