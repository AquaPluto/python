# 以文档字符串介绍带参装饰器

import datetime
import time
from functools import wraps


# 三引号引起来就是文档字符串，用来介绍函数的功能，使用 __doc__ 这个属性来访问
# def logger(fn):
#     def wrapper(*args, **kwargs):
#         """wrapper's doc"""
#         start = datetime.datetime.now()
#         ret = fn(*args, **kwargs)
#         delta = (datetime.datetime.now() - start).total_seconds()
#         print('Function {} took {}s.'.format(fn.__name__, delta))
#         return ret
#
#     return wrapper
#
#
# @logger  # add = logger(add) <=> add = wrapper
# def add(x, y):
#     """add's doc"""
#     time.sleep(5)
#     return x + y
#
#
# print("name={}, doc={}".format(add.__name__, add.__doc__))  # name=wrapper, doc=wrapper's doc

# 因为 add 被 wrapper 装饰了，所以属性被它覆盖了，解决这个问题，使用 @wraps ，是一个带参装饰器
def logger(fn):
    @wraps(fn)  # wrapper = wraps(fn)(wrapper)
    def wrapper(*args, **kwargs):
        """wrapper's doc"""
        start = datetime.datetime.now()
        ret = fn(*args, **kwargs)
        delta = (datetime.datetime.now() - start).total_seconds()
        print('Function {} took {}s.'.format(fn.__name__, delta))
        return ret

    return wrapper


@logger  # add = logger(add) <=> add = wrapper
def add(x, y):
    """add's doc"""
    time.sleep(5)
    return x + y


print("name={}, doc={}".format(add.__name__, add.__doc__))
