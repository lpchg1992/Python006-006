import pika, time


credentials = pika.PlainCredentials('geektime', 'geektime')
parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',
    credentials=credentials
)

connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)

# 回调函数
def callback(ch, method, properties, body):

    time.sleep(1)
    print(body.decode())
    ch.basic_ack(delivery_tag=method.delivery_tag)

# 如果该消费者的channel上未确认的消息数达到了prefetch_count数量，则不向该消费者发送消息。
# 一般也就是消费者出现问题，这个时候需要记录日志中，等待分析。
channel.basic_qos(prefetch_count=1)

# 消费者使用哪个队列和哪个回调函数处理消息，自动采用轮询机制round robine，注意：同一个消息只被处理一次！！！！！
channel.basic_consume('task_queue', callback)

# 开始接收消息，进入阻塞状态
channel.start_consuming()