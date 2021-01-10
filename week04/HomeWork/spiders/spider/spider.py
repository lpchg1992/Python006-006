import requests
import sys
from time import sleep
from fake_useragent import UserAgent
from data_handler import data_parser_cleaner, data_insert


def get_rough_data(url, header):
    try:
        response = requests.get(url, headers=header)
    except ConnectionError:
        get_rough_data(url, header)
    return response.text


def main():
    ua = UserAgent(verify_ssl=False)
    header = {
        'user-agent': ua.random,
        'Refere': 'https://book.douban.com/subject/25862578/'
    }
    urls = (f'https://book.douban.com/subject/25862578/comments/?start={i}&limit=20&status=P&sort=new_score'
            for i in range(0, 200, 20))
    count = 0
    for url in urls:
        stars, content = data_parser_cleaner(get_rough_data(url, header))
        try:
            data_insert(stars, content)
            print('20 comments inserted.')
        except Exception as e:
            print(e)
        finally:
            header['Refere'] = url
            print('wait for 5 sec.')
            sleep(5)
        count += 20
    print(f"About {count} comments inserted.")


if __name__ == "__main__":
    main()
