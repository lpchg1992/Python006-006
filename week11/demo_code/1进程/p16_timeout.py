from multiprocessing import Pool
import time

def f(x):
    return x*x

if __name__ == '__main__':
    # 使用关键字参数增加代码可读性。
    with Pool(processes=4) as pool:         # 进程池包含4个进程
        result = pool.apply_async(f, (10,)) # 执行一个子进程，result接收执行结果。
        # 直接显示result是不行的，所以：
        print(result.get(timeout=1))        # 显示执行结果
        # 既可以取得结果，又解决超时的问题。

        # 休眠10秒
        result = pool.apply_async(time.sleep, (10,))
        # 会超时，所以抛出异常。
        print(result.get(timeout=1))        # raises multiprocessing.TimeoutError
