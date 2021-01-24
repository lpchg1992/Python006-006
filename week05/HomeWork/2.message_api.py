import redis
from time import sleep
from random import randint, choices
from datetime import datetime

def connector():
    '''
    a simple connector.
    '''
    return redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')


def initial_user_infos():
    '''
    initial user infos in redis.
    '''
    phone_number = randint(1880000000, 1889999999)
    time_circle = 0
    count_circle = 0
    return phone_number, time_circle, count_circle

def get_content():
    content_list = ['happy!', 'OH!', 'Yummy', 'YOYO', 'QWERT', 'APIOPP']
    return ''.join(choices(content_list, k=10))

def sendsms(phone_number, content):
    print('waitting for send...')
    sleep(2)
    conn = connector()
    first_time = conn.hget(phone_number, 'time_circle').decode()
    now_count = int(conn.hget(phone_number, 'count_circle').decode())
    success = True
    if first_time ==  '0':
        conn.hmset(phone_number, {'time_circle': str(datetime.now()), 'count_circle': 1})
    else:
        time_delta = datetime.now() - datetime.fromisoformat(first_time)
        if time_delta.seconds <= 60 and now_count >= 5:
            success = False
        elif time_delta.seconds > 60:
            conn.hmset(phone_number, {'time_circle': str(datetime.now()), 'count_circle': 1})
        else:
            conn.hincrby(phone_number, 'count_circle')
    if success:
        print(f"发送成功给{phone_number}！内容：{content}")
    else:
        print("每分钟只能发送5条，请稍后再试！")

def main():
    conn = connector()
    numbers = []
    for i in range(3):
        phone_number, time_circle, count_circle = initial_user_infos()
        conn.hmset(phone_number, {'time_circle': time_circle, 'count_circle': count_circle})
        numbers.append(phone_number)
    
    print(numbers)
    contents = (get_content() for i in range(100))

    for i in contents:
        print(f'start sending {i}...')
        for n in numbers:
            sendsms(n, i)

if __name__ == "__main__":
    main()