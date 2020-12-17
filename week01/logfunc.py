import logging
import os
from datetime import datetime


def called_time_log():
    today_is = f'{datetime.now()}'.split(' ')[0]
    file_dir = f'/home/luopingcheng/prgtemp/log/python-{today_is}'
    if not os.path.exists(file_dir):
        os.makedirs(file_dir)
    logging.basicConfig(filename=file_dir + '/called_time_log.log',
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(message)s'
                        )
    logging.info('function called.')


if __name__ == '__main__':
    called_time_log()
