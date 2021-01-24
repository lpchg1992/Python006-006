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
channel.queue_declare(queue='direct_demo', durable=True)

# 往队列发布信息
# 指定交换机
# 指定交换机为空，此处直接生产者写队列。
# routing_key使用哪一个队列
# body是消息，但是一般为json或者xml格式的字符串。
channel.basic_publish(exchange='', routing_key='direct_demo',
                      body='send message to rabbitmq'
                      )

# 关闭连接
connection.close()

# 执行没有返回值。一般认为已经建立连接并发送。
# 观察网页变化


