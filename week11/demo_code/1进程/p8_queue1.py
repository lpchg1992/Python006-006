# multiprocessing 支持进程之间的两种通信通道
# 队列
# 来自官方文档的一个简单demo
# Queue 类是一个近似 queue.Queue 的克隆
# 现在有这样一个需求：我们有两个进程，一个进程负责写(write)一个进程负责读(read)。
# 当写的进程写完某部分以后要把数据交给读的进程进行使用
# write()将写完的数据交给队列，再由队列交给read()

from multiprocessing import Process, Queue

def f(q):
    # 当设置了队列大小，可以根据blocked的情况以及timeout处理put行为。
    # 当无法写入，可以抛出full错误。
    q.put([42, None, 'hello'])

if __name__ == '__main__':
    # put get是两个主要的方法。实际操作需要对队列的最大存储值进行设置，打个比方，就是设置最大排队数量。
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    # 通过参数控制get行为。
    # 如果blocked值是true，直到timeout都是true，则没有数据，可以抛出empty等。
    print(q.get())    # prints "[42, None, 'hello']"
    p.join()

# 队列是线程和进程安全的
