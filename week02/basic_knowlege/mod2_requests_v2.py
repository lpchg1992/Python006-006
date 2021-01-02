import requests
from pathlib import *
import sys

ua = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/87.0.4280.88 Safari/537.36'
header = {'user-agent': ua}

myurl = "https://movie.douban.com/top250"

try:
    response = requests.get(myurl, headers=header)
except requests.exceptions.ConnectTimeout as e :
    print(f"requests库超时{e}")
    # 当捕获系统内置的异常，程序会自动停止，但是当非系统异常，则程序不会主动退出，需要手动退出。
    # 返回一个1，说明是非正常退出的状态。
    sys.exit(1)

# 将网页内容改为存入文件
# print(response.text)

# 获得python脚本的绝对路径
p = Path(__file__)
# 提取该文件所在的目录
pyfile_path = p.resolve().parent
# 建立新的目录html
html_path = pyfile_path.joinpath('html')

if not html_path.is_dir():
    Path.mkdir(html_path)
page = html_path.joinpath('douban.html')

# 上下文管理器
try:
    with open(page, 'w', encoding="utf-8") as f:
        f.write(response.text)
    # 文件找不到，可能是一些权限的问题，或者路径处理有问题
except FileNotFoundError as e:
    print(f'文件无法打开：{e}')
    # 磁盘被写满，或者硬件的问题
except IOError as e:
    print(f'读写文件错误：{e}')
except Exception as e:
    print(e)
    

