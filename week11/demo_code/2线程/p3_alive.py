import threading
import time
def start():
    time.sleep(5)


thread1 = threading.Thread(target=start)
# 判断当前线程是否活动
print(thread1.is_alive())
# 启动
thread1.start()
# 获取名字和存活状态
print(thread1.getName())
print(thread1.is_alive())

# 执行完成后，线程已经结束。
thread1.join()

print(thread1.is_alive())