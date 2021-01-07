import pymysql
from datetime import datetime
from dbini_parser import read_db_config
from user_table_enums import GenderEnum, DegreeEnum


db = pymysql.connect(**read_db_config())

try:
    with db.cursor() as cursor:
        sql = '''INSERT INTO userinfo (user_name, user_age,\
            user_birthday, user_gender, user_degree, created_on)\
                VALUES (%s, %s, %s, %s, %s, %s)'''
        value = (
            ('hanmeimei', 16, datetime(2004, 1, 1),
             GenderEnum.female.name, DegreeEnum.bachelor.name, datetime.now()),
            ('lilei', 17, datetime(2003, 1, 1),
             GenderEnum.male.name, DegreeEnum.bachelor.name, datetime.now()),
            ('yhs', 20, datetime(2000, 1, 1),
             GenderEnum.male.name, DegreeEnum.phd.name, datetime.now())
        )
        cursor.executemany(sql, value)
    db.commit()

except Exception as e:
    print(f"fetch_error: {e}")

finally:
    # 关闭数据库连接
    db.close()
