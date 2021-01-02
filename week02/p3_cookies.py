import requests

# 在同一个 Session 实例发出所有请求之间保持 cookie
# 指定一个会话，几次连接由同一个会话发起
s = requests.Session()

# 该会话进行第一次请求
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
# 该会话进行第二次请求
r = s.get('http://httpbin.org/cookies')

print(r.text)
# '{"cookies": {"sessioncookie": "123456789"}}'

# 会话可以使用上下文管理器
with requests.Session() as s:
    s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')

# 可借助浏览器理解
