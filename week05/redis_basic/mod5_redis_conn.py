# 连接redis
import redis


client = redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')

print(client.keys())

for key in client.keys():
    print(key.decode())