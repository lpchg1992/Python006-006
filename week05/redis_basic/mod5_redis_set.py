import redis

client = redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')

# 添加值
client.sadd('redis_set_demo', 'new_data')

# 弹出 真随机数
client.spop('redis_set_demo')

# 查看所有值
client.smembers('redis_set_demo')

# 交集，例如即买了啤酒又买了尿布的人
client.sinter('set_a', 'set_b')

# 并集
client.sunion()

# 差集
client.sdiff()

# 一般去重使用，方便进行逻辑与或非的运算

