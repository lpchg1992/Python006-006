# pip install sqlalchemy
# 为了方便理解映射关系，这里先看底层实现

import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, \
    MetaData, ForeignKey

# 打开数据库连接
# echo=True开启调试，执行时终端会显示执行日志
engine = create_engine("mysql+pymysql://testuser:!Geektime8848@47.244.201.185\
:3306/testdb", echo=True)

# 创建元数据，也就是描述数据的数据，例如：图书的书号，页数，厚度，出版单位等就是元数据。
# 对元数据进行初始化，也就是连接到数据库
metadata = MetaData(engine)

# 在元数据中创建book
book_table = Table('book', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(20)),
                   )
author_table = Table('author', metadata,
                     Column('id', Integer, primary_key=True),
                     Column('book_id', None, ForeignKey('book.id')),
                     Column('author_name', String(128), nullable=False)
                     )

try:
    metadata.create_all()
except Exception as e:
    print(f'create_all error: {e}')
