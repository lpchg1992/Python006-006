from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


DBURL = "mysql+pymysql://testuser:!Geektime8848@47.244.201.185\
:3306/testdb"

DBORM = declarative_base()


class GeekTimeUser(DBORM):
    __tablename__ = 'geektimeuser'
    user_id = Column(Integer(), primary_key=True, autoincrement=True)
    user_name = Column(String(30), nullable=False)


class GeekTimeCoin(DBORM):
    __tablename__ = 'geektimecoin'
    coin_id = Column(Integer(), primary_key=True, autoincrement=True)
    coin_user_id = Column(Integer(), ForeignKey('geektimeuser.user_id'))
    total_coin = Column(Float(), default=0)


class GeekTimeRecords(DBORM):
    __tablename__ = 'geektimerecords'
    record_id = Column(Integer(), primary_key=True, autoincrement=True)
    trans_time = Column(DateTime(), default=datetime.now)
    from_id = Column(Integer(), nullable=False)
    to_id = Column(Integer(), nullable=False)
    trans_amount = Column(Float(), nullable=False)
