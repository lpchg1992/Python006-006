# 显示所涉及的各个进程ID，这是一个扩展示例

from multiprocessing import Process
import os
import multiprocessing

def debug_info(title):
    print('-'*20)
    print(title)
    # 打印更加详细的信息
    print('模块名称:', __name__)
    print('父进程:', os.getppid())
    # 负责执行代码的父进程，其父进程是上述父进程。
    print('当前进程:', os.getpid())
    print('-'*20)

def f(name):
    debug_info('function f')
    print('hello', name)

if __name__ == '__main__':
    debug_info('main')
    p = Process(target=f, args=('bob',))
    p.start()

    # 父进程（主）进程中输出一些子进程的信息。可用于检测存活的子进程等。
    # 只有当子进程结束得比这个代码晚，才能够被下列代码获取。
    for p in multiprocessing.active_children():
        print(f'子进程名称: {p.name}  id: { str(p.pid) }' )
    print('进程结束')
    # 每个进程占用1个核心，一般进程数量等同于cpu核心数量。
    print(f'CPU核心数量: { str(multiprocessing.cpu_count()) }')
    
    p.join()


