# 操作hash
import redis

client = redis.Redis(host='127.0.0.1', password='iuTG^*)OJFWQ@$%TFVH_)oiuygtb')

# 记录用户是否vip，多个用户存入。同时还可以记录vip等级积分等等。
# 可以将多条记录yongjson格式记录在一个redis记录，也可以将一个用户对应的多个属性记录在多个记录中。

client.hset('redis_hash_demo', 'key', 'value')

client.hset('vip_user', '1001', 1)

client.hset('vip_user', '1002', 2)

client.hdel('vip_user', '1002')
# 是否存在
client.hexists('vip_user', '1002')

# 存储哈希表，可以大幅度降低内存消耗。

# 批量添加大量
client.hmset('vip_user', {'1003': 1, '1004':1})
# 这个功能会被慢慢取代。用hset。

#  hkeys[获取所有字段名称，也就是一个哈希对应的所有字段] 
# hget【获取字段对应的值】 
# hmget 
# hgetall【取出所有键值对】
# 注意事项：获取值可能取得出，取不出，执行hget的返回值永远都是none，只能通过结果判断是否有值存在。
# 返回的都是bytes，需要decode。

