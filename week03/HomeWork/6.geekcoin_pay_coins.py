# 基础不好，先做一个勉强能用的
import pymysql
import sys
from sqlalchemy import create_engine, and_, desc
from sqlalchemy.orm import sessionmaker
from geekcoin_db_orm import DBURL, GeekTimeCoin, GeekTimeRecords, GeekTimeUser
from dbini_parser import read_db_config
from datetime import datetime


# to get coin number
def get_the_number_to_transform():
    # initial the class with out __init__
    user_coins = PaymentHandler.__new__(PaymentHandler)
    print(user_coins)
    coins = input('input the number of the coins to pay: ')
    try:
        coins = float(coins)
    except Exception:
        pass
    if isinstance(coins, float):
        if coins == -1:
            sys.exit(0)
        return coins
    else:
        print('please input a number, -1 + enter to exit.')
        get_the_number_to_transform()


# to get the id gives money
def get_the_id_from():
    id_from = input('input the id to giveout money: ')
    try:
        id_from = int(id_from)
    except Exception:
        pass
    if isinstance(id_from, int):
        if id_from == -1:
            sys.exit(0)
        return id_from
    else:
        print('please input a number, -1 + enter to exit.')
        get_the_id_from()


# to get the id receives money
def get_the_id_to():
    id_to = input('input the id to receive money: ')
    try:
        id_to = int(id_to)
    except Exception:
        pass
    if isinstance(id_to, int):
        if id_to == -1:
            sys.exit(0)
        return id_to
    else:
        print('please input a number, -1 + enter to exit.')
        get_the_id_to()


# add some data to the db
def initial_db():
    db = pymysql.connect(**read_db_config())
    try:
        with db.cursor() as cursor:
            sql = [
                # '''INSERT INTO geektimeuser (user_name) VALUES (%s)''',
                '''INSERT INTO geektimecoin (coin_user_id, total_coin) VALUES (%s, %s)'''
            ]
            value = (
                # (
                #     ('hanmeimei'),
                #     ('lilei'),
                #     ('yhs')
                # ),
                # 要保证外键的一致性。
                (
                    (4, 1000),
                    (5, 10000000),
                    (6, 10)
                ),
            )
            print([{i: j} for i, j in zip(sql, value)])
            for i, j in zip(sql, value):
                cursor.executemany(i, j)
        db.commit()

    except Exception as e:
        print(f"fetch_error: {e}")

    finally:
        db.close()


# execute the payment
class PaymentHandler:
    def __init__(self):
        self.coin_number = get_the_number_to_transform()
        self.from_id = get_the_id_from()
        self.to_id = get_the_id_to()

    # a class method to get session
    @classmethod
    def payment_session(self):
        engine = create_engine(DBURL, encoding="utf-8")
        Session = sessionmaker(bind=engine)
        session = Session()
        return session

    # make a payment using a session to control the context
    def make_a_payment(self):
        session = self.payment_session()
        try:
            query = session.query(GeekTimeCoin.total_coin)
            query = query.filter(
                and_(
                    GeekTimeCoin.coin_user_id == self.from_id,
                    GeekTimeCoin.total_coin >= self.coin_number
                )
            )
            query.update(
                {GeekTimeCoin.total_coin: query.one()[0]-self.coin_number})

            query = session.query(GeekTimeUser.user_name)
            query = query.filter(GeekTimeUser.user_id == self.from_id)
            from_name = query.one()[0]

            query = session.query(GeekTimeUser.user_name)
            query = query.filter(GeekTimeUser.user_id == self.to_id)
            to_name = query.one()[0]

            query = session.query(GeekTimeCoin.total_coin)
            query = query.filter(GeekTimeCoin.coin_user_id == self.to_id)
            query.update(
                {GeekTimeCoin.total_coin: query.one()[0]+self.coin_number}
            )

            new_record = GeekTimeRecords(from_id=self.from_id,
                                         to_id=self.to_id,
                                         trans_amount=self.coin_number)

            session.add(new_record)

            session.commit()

            print(
                f'{from_name} make a {self.coin_number} coins payment to {to_name} at {datetime.now()}.')

        except Exception as e:
            print(e)
            session.rollback()
        finally:
            session.close()

    def show_records(self):
        session = self.payment_session()
        query = session.query(GeekTimeRecords.from_id, GeekTimeRecords.to_id,
                              GeekTimeRecords.trans_amount,
                              GeekTimeRecords.trans_time).order_by(
                                  desc(GeekTimeRecords.trans_time)).limit(3)
        for i in query:
            print(f'user {i[0]} paid to {i[1]} : {i[2]} coins . At {i[3]}')

    # return the recent coins status
    def __str__(self):
        session = self.payment_session()
        query = session.query(GeekTimeCoin.coin_user_id,
                              GeekTimeCoin.total_coin)
        user_coins = ''
        for i in query:
            user_coins += f' user: {i[0]}, coins: {i[1]} ||'
        return "initial coins are:" + user_coins


if __name__ == "__main__":
    print('Waiting for database...')
    PaymentHandler().make_a_payment()
    print('Waiting for database for records...')
    PaymentHandler.__new__(PaymentHandler).show_records()


# 示例：该示例由于6只有10个coin，所以查询出错，无法完成支付。
# initial coins are: user: 4, coins: 1000.0 || user: 5, coins: 10000000.0 || user: 6, coins: 10.0 ||
# input the number of coins to pay: 100
# input the id to give out money: 6
# 提示：No row was found for one()

# 示例：会成功支付，并在记录表中进行记录
# initial coins are: user: 4, coins: 1000.0 || user: 5, coins: 10000000.0 || user: 6, coins: 10.0 ||
# input the number of the coins to pay: 1000
# input the id to giveout money: 5
# input the id to receive money: 4
# 提示：lilei make a 1000.0 coins payment to hanmeimei at 2021-01-07 21:10:12.577521.
