# ORM方式连接mysql数据库
# pip install sqlalchemy

from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData,\
ForeignKey, desc, func, and_, or_, not_

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
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


dburl = "mysql+pymysql://testuser:!Geektime8848@47.244.201.185:3306/testdb"
engine = create_engine(dburl, echo=True, encoding="utf-8")

# 创建session
# 维护了一个事物
SessionClass = sessionmaker(bind=engine)
session = SessionClass()

# 更新
# update()
# query = session.query(Book_table)
# query = query.filter(Book_table.book_id == 2)
# query.update({Book_table.book_name: 'newbook'})
# new_book = query.first()
# print(new_book.book_name)

# 删除
# delete() 用 where控制好删除的范围
# query = session.query(Book_table)
# query = query.filter(Book_table.book_id == 2)
# session.delete(query.one())

# 就地删除，删除后返回none
query = session.query(Book_table)
query = query.filter(Book_table.book_id == 1)
query.delete()
print(query.first())

session.commit()
