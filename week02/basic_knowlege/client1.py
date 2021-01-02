import requests

# get模拟浏览器
r = requests.get('http://www.httpbin.org')
print(r.status_code)
print(r.headers)
# print(r.text)
