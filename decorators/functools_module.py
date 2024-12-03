# reduce 用于对序列中的元素执行累积操作
# reduce(function, iterable[, initial])
from functools import reduce

print(reduce(lambda x, y: x + y, range(5)))  # function必须是两参函数
# 计算流程
# 1 将序列中的前两个元素传递给function的两个参数
# 2 将步骤1的返回值和序列的下一个元素再次传递给function，以此类推，直到元素被处理完

print(reduce(lambda x, y: x + y, range(5), 100))  # 从100开始累积
print(reduce(lambda x, y: x + y + 100, range(5)))
print(reduce(lambda x, y: x * y, range(1, 6)))  # 阶乘

# partial 偏函数 把旧函数的某些参数值固定下来，只需要提供剩余的参数，形成一个新函数，并返回这个新函数
from functools import partial


def add1(x, y):
    return x + y


newadd1 = partial(add1, y=5)  # 固定y的值，只需要提供x的值
print(newadd1(1))
print(newadd1(4, y=15))


def add2(x, y, *args):
    return x + y + sum(args)


newadd2 = partial(add2, 1, 2, 3, 4, 5)  # x=1,y=2,*args=(3,4,5)
print(newadd2())
print(newadd2(1))  # 1被*arg拿走

# lru_cache 缓存 最近最少使用
from functools import lru_cache


@lru_cache()
def fib(n):
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)
