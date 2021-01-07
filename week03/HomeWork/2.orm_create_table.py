import pymysql
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from user_table_enums import GenderEnum, DegreeEnum


Base = declarative_base()


class UserInfo(Base):
    __tablename__ = 'userinfo'
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(30), nullable=False, unique=True)
    user_age = Column(Integer(), default=18)
    user_birthday = Column(DateTime(), default=datetime(2020, 1, 1))
    user_gender = Column(Enum(GenderEnum), default=GenderEnum.male)
    user_degree = Column(Enum(DegreeEnum), default=DegreeEnum.bachelor)
    # default值的设定是在orm层做的，没有在数据库层实现
    created_on = Column(DateTime(), default=datetime.now)
    updated_on = Column(DateTime(), default=datetime.now,
                        onupdate=datetime.now)


dburl = "mysql+pymysql://testuser:!Geektime8848@47.244.201.185\
:3306/testdb"
engine = create_engine(dburl, echo=True, encoding='utf-8')

Base.metadata.create_all(engine)
