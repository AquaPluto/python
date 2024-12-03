# global
x = 1


def foo():
    global x  # 说明x是全局变量
    x += 1  # 没有global语句，x是局部变量，但是局部没有定义的话就会报错
    print(x)


foo()


# 闭包
def outer_function(x):
    def inner_function(y):
        return x + y

    return inner_function


add_five = outer_function(5)  # add_five是一个闭包，记住了x，x是自由变量，会一直在函数作用域中保存，即使引用计数为0
print(add_five(10), add_five(20))  # 相对于在调用inner_function()，输出：15 25


# nonlocal
def counter():
    count = 0

    def inc():
        nonlocal count  # 声明变量count不是本地变量，使得count是闭包的一部分
        count += 1
        return count

    return inc


foo = counter()  # 返回inc函数，foo是一个闭包
print(foo(), foo())  # 相当于在调用inc(), 输出：1 2
