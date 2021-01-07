import pymysql
from sqlalchemy import create_engine
from geekcoin_db_orm import DBORM, DBURL


engine = create_engine(DBURL, echo=True, encoding='utf-8')
DBORM.metadata.create_all(engine)
