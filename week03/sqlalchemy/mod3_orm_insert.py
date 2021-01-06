# ORM方式连接mysql数据库
# pip install sqlalchemy

from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy import DateTime

# 打开数据库连接
Base = declarative_base()


class Book_table(Base):
    __tablename__ = 'bookorm'
    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(50), index=True)

    def __repr__(self):
        return "Book_table(bookid='{self.book_id}', "\
            "book_name={self.book_name})".format(self=self)


class Author_table(Base):
    __tablename__ = 'authororm'
    user_id = Column(Integer(), primary_key=True)
    username = Column(String(15), nullable=False, unique=True)
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)

# Float
# Decimal
# Boolean
# Text

# primary_key
# default
# unique
# nullable
# autoincrement

# 最顶层：业务逻辑，开发时可以只关注逻辑层，其余由中间层和底层进行处理。
# 中间：持久层，实现对数据库的更高效访问。将逻辑层语句转为sql执行
# 数据库层

# orm劣势：损失性能，复杂查询无法orm；sql调优

# 实例化一个引擎


dburl = "mysql+pymysql://testuser:!Geektime8848@47.244.201.185:3306/testdb"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
# 维护了一个事物
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 增加数据
# 实际上是一种实例化
book_demo = Book_table(book_name='小深刻的救赎')
# repr魔术方法在打印时被调用
# print(book_demo)
# add 会被自动转换成INSERT INTO 语句
session.add(book_demo)
session.commit()
