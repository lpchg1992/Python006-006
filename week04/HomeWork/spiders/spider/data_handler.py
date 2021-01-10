import re
import os
import django
import sys
from lxml import etree
pathname = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, pathname)
sys.path.insert(0, os.path.abspath(os.path.join(pathname, '../..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HomeWork.settings')
django.setup()
from showcmt.models import Comments


def star_parser(classnames):
    star_numbers = []
    for starclass in classnames:
        try:
            star_numbers.append(int(int(re.findall(r'\d{2}', starclass)[0])/10))
        except IndexError:
            star_numbers.append(0)

    return star_numbers


def data_parser_cleaner(htmltext):
    selector = etree.HTML(htmltext)
    contents = selector.xpath('//li[@class="comment-item"]/div[@class="comment"]/p[@class="comment-content"]/span/text()')
    star_class = selector.xpath('//li[@class="comment-item"]/div[@class="comment"]/h3/span[@class="comment-info"]/span[1]/@class')
    stars = star_parser(star_class)
    contents = [string.strip() for string in contents]
    return stars, contents


def data_insert(stars, contents):
    datas = zip(stars, contents)
    for cmt in datas:
        try:
            Comments.objects.create(stars=cmt[0], content=cmt[1])
        except Exception as e:
            raise e
