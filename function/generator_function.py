# 包含yield语句的函数是生成器函数
def inc():
    for i in range(5):
        yield i


g = inc()
print(next(g))  # 使用next迭代
for x in g:
    print(x)  # 使用for迭代


# 应用1：计数器
def inc():
    def counter():
        count = 0
        while True:
            count += 1
            yield count

    c = counter()

    def inner():
        return next(c)

    return inner


foo = inc()  # 闭包
print(foo())  # 输出1
print(foo())  # 输出2
print(foo())  # 输出3


# 应用2：斐波那契数列
def fib():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b


f = fib()
for i in range(1, 102):
    print(i, next(f))


# yield from
def foo():
    yield from range(10)


for x in foo():
    print(x)


def inc():
    yield from map(lambda x: x + 100, range(1000))


for x in inc():
    print(x)
