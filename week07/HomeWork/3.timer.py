from functools import wraps
from time import sleep, time


def timer(func):
    @wraps(func)
    def decorator(*args, **kwargs):
        print(f'decorated function: {func.__name__}')
        start_time = time()
        func(*args, **kwargs)
        print(time()-start_time)
    return decorator


@timer
def func(x):
    sleep(x)

func(1.6)