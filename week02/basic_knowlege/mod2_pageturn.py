# 翻页的处理
import requests
# 网页内容匹配的功能，XPath依赖的包
from lxml import etree
# pip install lxml
from time import sleep
# 控制请求频率，引入time模块，避免被反爬虫


# 使用def定义函数，myurl是函数的参数
def get_url_name(myurl):
    ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {'user-agent': ua}
    response = requests.get(myurl, headers=header)

    selector = etree.HTML(response.text)
    # 电影名称列表
    film_name = selector.xpath('//div[@class="hd"]/a/span[1]/text()')

    # 电影链接列表
    film_link = selector.xpath('//div[@class="hd"]/a/@href')

    # 遍历对应关系字典
    film_info = dict(zip(film_name, film_link))
    for i in film_info:
        print(f'电影名称： {i} \t\t 电影链接： {film_info[i]}')


if __name__ == "__main__":
    # 生成包含所有页面的元组（生成器==》元组）
    # 此处利用翻页url规律
    urls = tuple(f'https://movie.douban.com/top250?start={ page*25 }&filter='
                 for page in range(10))

    for page in urls:
        get_url_name(page)
        sleep(5)
