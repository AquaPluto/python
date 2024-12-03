# 需求：测试一个函数执行的时间有多长
# 以此需求使用无参装饰器
import datetime
import time


def logger(fn):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('Function {} took {}s.'.format(fn.__name__, delta))
        return ret
    return wrapper


@logger  # add = logger(add) <=> add = wrapper
def add(x, y):
    time.sleep(5)
    return x + y


print(add(1, 2))
