import redis

client = redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')


#  当需要排序时。如果存储越大，添加时间越长，这是区别于队列和哈希的。查询也是同样。
#  主要利用其不重复性，而且可以排序。
# 
client.zadd('有序集合的名字', {'a': 4, 'b': 3, 'd':1})
client.zadd('rank', {'a': 4, 'b': 3, 'd':1, 'c':2, 'e':5})
client.zincrby('rank', -2, 'e')

# 从小到大
rank = client.zrangebyscore('rank', min=1, max=5)
# 从大到小
# zrevrank

# 基card，也就是后面的分数的个数
rank = client.zcard('rank')
# 同时显示评分和排序【分数】
print(client.zrange('rank', 0, -1, withscores=True))
# 反向
print(client.zrevrange('rank', 0, -1, withscores=True))
print(rank)
# 一般用于评分和排序，例如用户排名等。使用无需考虑重复。