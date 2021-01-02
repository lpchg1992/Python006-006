import time
import requests
from fake_useragent import UserAgent


ua = UserAgent(verify_ssl=False)
headers = {
    'User_Agent': ua.random,
    'Refere': 'https://accounts.douban.com/passport/login_popup?login_source=anony'
}

s = requests.Session()
# 会话对象： 在同一个 Session 实例发出的所有请求之间保持cookie，
# 期间使用 urllib3 的 connection pooling 功能，做一个连接池，发起时，选一个空闲连接。
# 向同一主机发送多个请求，底层的TCP连接将会被重用，从而带来显著的性能提升。
login_url = 'https://accounts.douban.com/j/mobile/login/basic'
form_data = {
    'ck': '',
    'name': '15055495@qq.com',
    'password': 'test123test456',
    'remember': 'false'
}

response = s.post(login_url, data=form_data, headers=headers)


# 登陆后可以进行后续请求
# url2 = 'https://accounts.douban.com/passport/setting'

# response2 = s.get(url2, headers = headers)
# response3 = newsession.get(url3, headers=headers, cookies=s.cookies)

# with open('profile.html', 'w+') as f:
#   f.write(response2.text)
