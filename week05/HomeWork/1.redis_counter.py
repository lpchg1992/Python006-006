import redis
from random import randint
from concurrent import futures
from time import sleep


def video_id_generator():
    '''
    generate 10 ID number string.
    '''
    return (str(1000 + i) for i in range(10))


def connector():
    '''
    a simple connector.
    '''
    return redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')


def initial_redis_data():
    '''
    initial the redis datas, set all 10 video ID with value '0'.
    '''
    vig = video_id_generator()
    redis_conn = connector()
    try:
        for i in vig:
            redis_conn.set(i, '0')
            print(f'ID {i} set succesfully!')
        return True
    except Exception:
        return False

def counter(video_id):
    '''
    Use the redis native method to increate the number.
    '''
    sleep(generate_random_int('i'))
    redis_conn = connector()
    redis_conn.incr(video_id)
    count = redis_conn.get(video_id).decode()
    print(f'{video_id}:{count}')

def generate_random_int(type_):
    '''
    Generate random int between 0-9. Use as mock data here.
    '''
    if type_ == 's':
        return str(1000 + randint(0, 9))
    if type_ == 'i':
        return randint(1, 10)

def main():
    '''
    Use random int as mock data to test counter with several threadings.
    '''
    if initial_redis_data():
        sleep(2)
        print('ready to exec counters!')
        all_videos_watched = (generate_random_int('s') for i in range(10000))
        with futures.ThreadPoolExecutor(max_workers=1000) as executor:
            executor.map(counter, all_videos_watched)

if __name__ == "__main__":
    main()