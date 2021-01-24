# 操作list
import redis

client = redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')

# 0 - -1 队列的左侧右侧

client.lpush('列表名称', '内容')
client.rpush('列表名称', '内容')

# 一般会存储大量数据， 基于软件能力，可以达到100万条。
# 一般先查长度

client.llen('列表名称')

# 同样有pop方法，弹出数据
data1 = client.lpop('列表名称')
data2 = client.rpop('列表名称')

print(data1, data2)

data3 = client.lpop('列表名称')
# 此时返回none
print(data3)

# 查看一定范围的数据
client.lpush('列表名称', '内容1')
client.rpush('列表名称', '内容2')
client.lpush('列表名称', '内容3')
client.rpush('列表名称', '内容4')

data = client.lrange('列表名称', 0, -1)
print(data)

# 大多数当成队列使用。相同角色做相同事情。比如双11 发放优惠券，做数据发送时，短信网关有并发限制
# 所有用户存入redis，依次取出10个用户，发送成功再取，不成功的放入新的队列。
# 右侧rpop，发送成功则弹出，发送失败则lpush。

while True:
    phone = client.rpop('队列名称')
    if not phone:
        print('发送完毕')
        break
    # 封装的发送函数。
    # sendsms(phone)
    # 发送失败返回次数
    # result_times = retry_once(phone)
    # if result_times >= 5:
    #     client.lpush('队列名称', phone)
    