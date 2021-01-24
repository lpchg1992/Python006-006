import pika


credentials = pika.PlainCredentials('geektime', 'geektime')
parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()

# 定义了交换机，交换模式fanout【此处一对多】（如果没有指定默认一对一）
# channel这一步只管到交换机，不管下一步的操作。交换机决定哪一个队列绑定到交换机。
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

message = 'send message to fanout!'

# 与之前不同的是，这里将消息发送给"自定义的一对多交换机"，由交换机决定后续发布。
# routing_key现在为空，交给交换机判断。
channel.basic_publish(
    exchange='logs',
    routing_key='',
    body=message
)

connection.close()