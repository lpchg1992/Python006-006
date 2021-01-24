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
channel.queue_declare(queue='task_queue', durable=True)

message = 'send msg tok tskq'

channel.basic_publish(
    exchange='',
    routing_key='task_queue',
    body=message,
    properties=pika.BasicProperties(
        delivery_mode=2 # 消息持久化
    )
)


connection.close()
