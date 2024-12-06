# 产生异常
# def foo():
#     print("before")
#     I / 0
#     raise Exception("my exception")  # raise后面必须是BaseException类的子类或者实例
#     print("after")  # 异常就会中断执行
#
#
# foo()


# 捕获异常
def foo():
    try:
        print("before")
        I / o
        print("after")  # 异常生成位置之后的语句将不再执行
    except:  # 捕获异常后就会正常执行，不会中断
        print("error")
    print("finished")


foo()


# 捕获指定类型的异常
def foo():
    try:
        print("before")
        I / O  # 这里的错误是NameError
        print("after")
    except NameError:  # 指定捕获的类型，也可以改为Exception
        print('error')
    print("finished")


foo()

# 异常类及继承层次，详细的可去官网中找
# BaseException
#   +-- SystemExit
#   +-- KeyboardInterrupt
#   +-- Exception
#         +-- NameError
#         +-- SyntaxError
#         +-- ValueError
#         +-- TypeError
#         +-- FileNotFoundError
#         +-- IOError
#         +-- ArithmeticError
#         +-- LookupError
#               +-- IndexError
#               +-- KeyError

# 异常类型的捕获
# 1 SystemExit：sys.exit() 函数引发的异常
import sys

try:
    print("before")
    sys.exit(10)  # 指定异常状态码，默认为1
    print("after")
except SystemExit:  # 换成Exception不能捕获，因为SystemExit不是Exception的子类，如果换成Exception，退出状态码为10
    print("Sysexit")
print("outer")

# 2 KeyboardInterrupt：用户的中断行为造成的异常
import time

try:
    while True:
        time.sleep(1)
        print('running')
except KeyboardInterrupt:
    print("Ctrl + c")


# 3 SyntaxError：语法错误，不能捕获
# def a():
#     try:
#         0a = 5
#     except:
#         pass

# 自定义异常类
class MyException(Exception):  # 继承Exception类
    pass


try:
    raise MyException()
except MyException:  # 捕获自定义异常
    print("catch u")

# 多种捕获
try:
    a = 1 / 0  # ZeroDivisionError
    raise MyException()
    open('t')  # exception
    sys.exit(1)
except ZeroDivisionError:
    print('zero')
except ArithmeticError:
    print('arith')
except MyException:  # 捕获自定义异常
    print('catch u')
except Exception:  # 如果在这之前已经有其他异常捕获了，就不会再次捕获了
    print('exception')
except:  # 写在最后，缺省捕获
    print('error')

# 其他子句
# 1 as子句
try:
    open("t.txt")
except FileNotFoundError as e:  # 获取异常类的实例对象
    print(e)

# 2 finally子句
# f = None  # 如果finally有捕获异常语句，可以没有这个定义。因为没有这个定义，由于open("t.txt")会错误，所以f没有被赋值成功，那么f.close()就会抛异常
try:
    f = open("t.txt")
except FileNotFoundError as e:  # 获取异常类的实例对象
    print(e)
finally:  # 不管是否发生异常，都会执行，一般放置资源释放的语句
    try:  # 也可以嵌套
        f.close()
    except Exception as e:
        print(e)

# 3 else子句
try:
    ret = 1 * 0
except ArithmeticError as e:
    print(e)
else:  # 没有任何异常就执行
    print('OK')
finally:
    print('fin')


# 语句嵌套捕获
try:
    try:
        1 / 0
    except KeyError as e:
        print(1, e)
    finally:
        print(2, 'inner fin')
except FileNotFoundError as e:
    print(3, e)
finally:
    print(4, 'outer fin')


# 异常捕获装饰器
# 1 基本异常捕获装饰器
def exception(fn):
    def wrapper(*args, **kwargs):
        try:
            ret = fn(*args, **kwargs)
            return ret
        except Exception as e:
            print(e)

    return wrapper


@exception  # divide = exception(divide) <=> divide = wrapper
def divide(a, b):
    return a / b


print(divide(2, 0))  # 触发除零异常


# 2 捕获指定类型的异常
def exception(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except ZeroDivisionError as e:
            print(f"捕获到除零异常:{e}")
        except ValueError as e:
            print(f"捕获到数值错误:{e}")
        except Exception as e:
            print(f"捕获到其他异常:{e}")

    return wrapper


@exception
def divide(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("参数类型错误")
    return a / b


print(divide(10, 0))  # 捕获除零异常
print(divide("10", 2))  # 捕获数值错误
