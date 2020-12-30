import requests

user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, \
like Gecko) Chrome/87.0.4280.88 Safari/537.36'

header = {'user-agent': user_agent}

myurl = 'https://movie.douban.com/top250'

response = requests.get(myurl, headers=header)

print(response.text)
print(f'返回码是： {response.status_code}')
