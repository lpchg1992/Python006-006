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

# 消费者这里也要和订阅者一样声明
channel.exchange_declare(
    exchange='logs',
    exchange_type='fanout'
)

# 声明消息队列
# exclusive当与消费者断开连接，队列被立即删除!!!!!!!!!!!!!!!!!!!!!。
result = channel.queue_declare(
    queue='', # 随即产生队列
    exclusive=True
)
queue_name = result.method.queue

# 与之前的差别是，这里需要通过交换机处理数据。
channel.queue_bind(
    exchange='logs',
    queue = queue_name
)

# 定义一个回调函数来处理消息队列中的消息
def callback(ch, method, properties, body):
    print(body.decode())

    # 本例中使用自动确定
    # ch.basic_ack=(delivery_tag=method.delivery_tag)


channel.basic_qos(prefetch_count=1)
# 消费者使用队列和哪个回调函数处理消息
channel.basic_consume(
    queue=queue_name,
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()