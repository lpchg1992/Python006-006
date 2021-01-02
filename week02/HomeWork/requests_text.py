# 改为爬取solidot首页新闻内容
import requests
import json
# 网页内容匹配的功能，XPath依赖的包
from lxml import etree


# 使用def定义函数，solidoturl是对应站点名称
def get_news_info(solidoturl):
    ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/87.0.4280.88 Safari/537.36'
    header = {'user-agent': ua}
    response = requests.get(solidoturl, headers=header)

    selector = etree.HTML(response.text)
    # 新闻标题列表
    news_title = selector.xpath('//div[@class="block_m"]/div[@class="ct_tittle"]/div[@class="bg_htit"]/h2/a/text()')

    # 新闻简介列表
    news_abstract = selector.xpath('//div[@class="block_m"]/div[@class="p_content"]/div[@class="p_mainnew"]/text()')

    # 生成新闻标题：新闻简介字典
    news_info = dict(zip(news_title, news_abstract))
    with open('./week02/HomeWork/requests_text/solidot.txt',
              'w', encoding='utf-8') as f:
        f.write(str(news_info))


if __name__ == "__main__":
    get_news_info('https://www.solidot.org/')
