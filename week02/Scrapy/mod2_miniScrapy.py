import requests
from lxml import etree
from queue import Queue
import threading
import json


class CrawlThread(threading.Thread):
    '''
    爬虫类
    '''

    def __init__(self, thread_id, queue):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/87.0.4280.88 Safari/537.36'
        }

    def run(self):
        # 重写run方法
        print(f'线程启动：{self.thread_id}')
        self.scheduler()
        print(f'结束线程：{self.thread_id}')

    # 模拟任务调度
    def scheduler(self):
        while not self.queue.empty():
            # 队列空则不处理
            page = self.queue.get()
            print('现在线程： {self.thread_id}, 下载页面：{page}')
            url = f'https://book.douban.com/top250?start={page*250}'

            try:
                # downloader 下载器
                response = requests.get(url, headers=self.headers)
                # 这里dataqueue是全局变量，稍有不妥。
                dataQueue.put(response.text)
            except Exception as e:
                print('下载出现异常', e)


class ParserThread(threading.Thread):
    '''
    页面内容分析
    '''

    def __init__(self, thread_id, queue, file_):
        super().__init__()
        self.thread_id = thread_id
        self.queue = queue
        self.file = file_

    def run(self):
        print(f'启动线程: {self.thread_id}')
        while flag:
            try:
                # 参数为false时队列为空，抛出异常，不为空则说明网页已经被取回
                item = self.queue.get(False)
                if not item:
                    continue
                self.parse_data(item)
                # get之后检测是否会阻塞
                self.queue.task_done()
            except Exception:
                pass
        print(f'结束线程：{self.thread_id}')

    def parse_data(self, item):
        '''
        解析网页内容的函数
        :param item:
        :return:
        '''
        try:
            html = etree.HTML(item)
            books = html.xpath('//div[@class="pl2"]')
            for book in books:
                try:
                    title = book.xpath('./a/text()')
                    link = book.xpath('./a/@href')
                    response = {
                        'title': title,
                        'link': link
                    }
                    # 解析方法和scrapy相同，再构造一个json
                    json.dump(response, fp=self.file, ensure_ascii=False)
                except Exception as e:
                    print('book error', e)

        except Exception:
            pass


if __name__ == "__main__":

    #  定义存放网页的队列，将需要处理的页面存放到队列
    pageQueue = Queue(20)
    for page in range(0, 11):
        pageQueue.put(page)

    # 定义存放解析数据的任务队列，用于存放处理后的数据
    dataQueue = Queue()

    # 爬虫线程
    # 定义三个爬虫处理待处理的页面
    crawl_threads = []
    crawl_name_list = ['crawl_1', 'crawl_2', 'crawl_3']
    for thread_id in crawl_name_list:
        thread = CrawlThread(thread_id, pageQueue)
        thread.start()
        crawl_threads.append(thread)

    # 将队列中的结果保存到json文件
    with open('book.json', 'a', encoding='utf-8') as pipline_f:

        # 解析线程，也就是对下载数据的处理管道
        parse_thread = []
        parser_name_list = ['parse_1', 'parse_2', 'parse_3']
        flag = True
        for thread_id in parser_name_list:
            thread = ParserThread(thread_id, dataQueue, pipline_f)
            thread.start()
            parse_thread.append(thread)

        # 结束crawl线程
        for t in crawl_threads:
            t.join()

        # 结束parse线程
        flag = False
        for t in parse_thread:
            t.join()

    print('退出主线程')
