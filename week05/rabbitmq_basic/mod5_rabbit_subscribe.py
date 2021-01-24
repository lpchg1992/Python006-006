# 生产者代码
import pika


# 可以分配不同的用户管理不同的功能。
credentials = pika.PlainCredentials('geektime', 'geektime')


# 虚拟队列参数
parameters = pika.ConnectionParameters(
    host='localhost',
    port=5672,
    virtual_host='/',  # 虚拟队列一般不用填写。
    credentials=credentials
)

# 阻塞方法
# 消费者连接到mq，默认阻塞，当有新的消息才处理，默认阻塞。
connection = pika.BlockingConnection(parameters)

# 建立信道

channel = connection.channel()

# 声明消息队列，也就是消息的载体，既可以publish声明，也可以消费者声明。声明发现不存在，就创建，发现存在就直接使用。
# 一般订阅发布两边都声明一遍，因为订阅发布两端都是客户端，只是角色不同而已。有可能生产者先启动或者消费者先启动。
# 如果不存在自动创建
# durable=True 队列持久化。保存在硬盘上面。

# 此处“重复声明一个”queue
channel.queue_declare(queue='direct_demo', durable=True)

# 消费方式：
# basic_consume 需要制定对应队列，定义接收方式：回调方式：on_message_callback
# 通过start_consumming消费，默认阻塞方式。避免死锁。可以通知消费者被阻塞，等待有资源再分配。

# 此处定义一个处理队列信息的函数

def callback(ch, method, properties, body):
    '''
    body: 消息
    ch: channel
    '''
    
    # 手动发送确认消息，对消息进行确认，防止消息丢失，告诉mq消息已经接收，正在处理中。和轮询方式有关。
    # 后面需要确认再加上。如果没有确认，即便接收到了，消息队列也不会清除消息。
    # ch.basic_ack(delivery_tag=method.delivery_tag)
    # 实现消息处理
    print(body.decode()) 

# 消费者使用队列和哪个回调函数处理消息
channel.basic_consume('direct_demo', on_message_callback=callback)

# 开始消费，默认阻塞方式，避免死锁，当资源不足，mq告诉客户端被阻塞，先暂停处理，待有资源再行分配。
channel.start_consuming()

