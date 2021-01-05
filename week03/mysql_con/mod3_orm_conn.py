import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, \
    MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

# 打开数据库连接

Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)


# 对比：

# book_table = Table('book', metadata,
#                    Column('id', Integer, primary_key=True),
#                    Column('name', String(20))
#                    )

# 定义一个更多的列属性的类
# import规范写法要写在最开始
from datetime import datetime
from sqlalchemy import DateTime


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, 
                        onupdate=datetime.now)


# 实例化一个引擎
dburl = "mysql+pymysql://testuser:!Geektime8848@47.244.201.185\
:3306/testdb"
engine = create_engine(dburl, echo=True, encoding='utf-8')

Base.metadata.create_all(engine)
