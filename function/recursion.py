# 简单例子
def my_recursion(n):
    print("start:" + str(n))
    if n == 1:
        print("recursion over!")
    else:
        my_recursion(n - 1)
    print("end:" + str(n))


my_recursion(3)


# 斐波那契数列递归
def fib_v1(n):  # 当 n = 35 开始往后，执行速度慢
    return 1 if n < 3 else fib_v1(n - 1) + fib_v1(n - 2)


def fib_v2(n, a=1, b=1):  # 使用迭代的方法
    return b if n < 3 else fib_v2(n - 1, a, b)


# 阶乘
def factorial_v1(n):
    return 1 if n == 1 else n * factorial_v1(n - 1)


def factorial_v2(n, p=1):  # 使用迭代的方法
    return p if n == 1 else factorial_v2(n - 1, p * n)
