# 操作string
import redis


client = redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')

# 该函数还有其他参数，例如ex，px等可以设置过期参数等。
client.set('key', 'value')

result = client.get('key')

# 通常需要解码处理。
print(result.decode())

# 其他问题：
# nx参数：可以设置如果值存在，不覆盖。默认覆盖。增加nx=true不覆盖。
# 一般存放用户ID，用户名的关系。

# 修改数据
# 原有字符串+
client.append('key', 'value4')

# 如果数据是数字：
# 字符串是数字也可以
client.set('key2', 100)

client.incr('key2')  # +1
client.decr('key2')  # -1


result = client.get('key2')
print(result.decode())
