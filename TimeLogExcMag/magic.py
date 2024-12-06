# 可视化
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return "{}-{}".format(self.a, self.b)

    __repr__ = __str__


print(A(1, 2))  # print使用__str__，如果没有定义，就去找__repr__
print([A(1, 2)])  # 间接引用，会使用__repr__，如果没有__repr__，返回内存地址
print([A(1, 2), str(A(1, 2)), '{}'.format(A(1, 2))])  # str，format使用__str__


# bool
class A:
    def __bool__(self):
        return False
        # return True


print(bool(A))
print(bool(A()))  # self控制的是实例，如果没有定义，就去找__len__


# 运算符重载
# 1 比较运算符
class A:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.name == other.name

    def __gt__(self, other):
        return self.age > other.age

    def __ge__(self, other):
        return self.age >= other.age


tom = A('Tom')
jerry = A('jerry', 18)
print(tom == jerry, tom != jerry)  # 本质：tom.__eq__(jerry)
print(tom > jerry, tom < jerry)
print(tom >= jerry, tom <= jerry)


# 2 算术运算符
class A:
    def __init__(self, name, score=80):
        self.name = name
        self.score = score

    def __sub__(self, other):
        return self.score - other.score

    def __isub__(self, other):
        self.score -= other.score
        return self

    def __repr__(self):
        return "{}-{}".format(self.name, self.score)


tom = A('Tom')
jerry = A('jerry', 90)
print(jerry.score - tom.score)
print(jerry - tom)
# jerry = jerry - tom
# print(tom)
# print(jerry)  # jerry的类型改变了
jerry -= tom
print(tom)
print(jerry)


# 容器方法
# 需求：设计一个购物车，可以添加商品，返回长度；可视化看到里面的元素；可以迭代元素，遍历元素；可以索引操作
class Cart:
    def __init__(self):
        self.__items = []

    def additem(self, *items):
        for item in items:
            self.__items.append(item)
        return self

    def __len__(self):  # 返回长度
        return len(self.__items)

    def __repr__(self):  # 可视化
        return "{}".format(self.__items)

    def __iter__(self):  # 迭代，遍历
        return iter(self.__items)

    def __getitem__(self, index):  # 索引访问
        return self.__items[index]

    def __setitem__(self, index, value):  # 索引赋值
        self.__items[index] = value


cart = Cart()
cart.additem(1, 2, 3)
print(cart)

for item in cart:  # 迭代
    print(item)

print(3 in cart)  # 遍历

print(cart[1])
cart[1] = "123"
print(cart[1])


# 可调用对象
# 1 累加
class Add:
    def __call__(self, *args, **kwargs):
        self.result = sum(args)
        return self.result


add = Add()
print(add(*range(5)))


# 2 斐波那契数列
# 需求：方便调用计算第n项；增加迭代数列的方法；返回数列长度；支持索引查找数列项的方法。
class Fib:
    def __init__(self):
        self.items = [0, 1, 1]

    def __len__(self):
        return len(self.items)

    def __call__(self, index):
        if index < 0:  # 不支持负索引
            raise IndexError("wrong index")

        if index < len(self.items):  # 思考边界，用作缓存
            return self.items[index]

        for item in range(len(self.items), index + 1):
            self.items.append(self.items[item - 1] + self.items[item - 2])
        return self.items[index]

    def __iter__(self):
        return iter(self.items)

    __getitem__ = __call__  # 因为它们参数一致，直接可以相等，如果参数不一致，各自定义


fib = Fib()
print(fib(5), len(fib))  # 全部计算
print(fib(10), len(fib))  # 部分计算，因为有缓存
for i in enumerate(fib):
    print(i)
print(fib[5], fib[6])


# 上下文管理
# 1 从下例执行顺序来看，先进行实例化，再执行with语句，即执行__enter__方法，然后再执行with语句块内的，最后执行__exit__方法
class Point:
    def __init__(self):
        print("1 init start")
        print("2 init finished")

    def __enter__(self):
        print("3 enter start")
        print("4 enter finished")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # exc_type：异常类型；exc_val：异常说明
        print("5 exit")
        return 1  # 返回值为True，就会压制异常


with Point() as point:
    print(point)  # 是__enter__方法的返回值
    print("6 in with")
    1 / 0
    print("7 with finished")  # 有异常不会再继续执行

# 2 应用：对一个函数计算它的执行时间
import datetime, time


def add(x, y):
    time.sleep(2)
    return x + y


class Timeit:
    def __init__(self, fn):
        self.fn = fn

    def __enter__(self):  # 执行函数前做
        self.start = datetime.datetime.now()
        print("开始计时")
        return self
        # return self.fn

    def __exit__(self, exc_type, exc_val, exc_tb):  # 执行完函数做
        delta = (datetime.datetime.now() - self.start).total_seconds()
        print('{} took {}s'.format(self.fn.__name__, delta))


with Timeit(add) as t:
    add(1, 2)
    # t(1, 2)


# 反射
# 1 __getattr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        print(item)  # z
        return 1  # 默认返回None


p = Point(1, 2)
print(p.x, p.y, p.z)


# 2 __setattr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattr__(self, item):
        print(item)  # z
        return 1  # 默认返回None

    def __setattr__(self, key, value):
        print("setattr {}:{}".format(key, value))
        # super().__setattr__(key, value)


p = Point(1, 2)  # 调用了__setattr__
print(p.x, p.y)  # 赋值是通过__getattr__赋值的，因为__setattr__会拦截初始化时的操作，转而去调用__setattr__，为了正确赋值，调用父类的方法


# 3 __delattr__
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __delattr__(self, item):  # 覆盖父类的方法，拦截删除操作
        print('Not delattr, {}'.format(item))


p = Point(1, 2)
del p.x
print(p.__dict__)
del p.__dict__['x']  # 拦截不了通过字典来删除
print(p.__dict__)


# 4 __getattribute__
class Point:
    z = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __getattribute__(self, item):  # 跟__setattr__不一样的是，虽然初始化赋值已经完成了，但是却访问不到，因为会先调用该方法，简称属性访问第一站
        print("getattribute {}".format(item))
        # return 100
        # return super().__getattribute__(item)


p1 = Point(4, 5)  # 调用__getattribute__
print(p1.x, p1.y)  # 是__getattribute__的返回值
print(Point.z, p1.z)
print(p1.__dict__)


# 哈希
# 1 例子
class A:
    def __init__(self, name):
        self.name = name

    def __hash__(self):  # hash值只是为了判断有无hash冲突，去重还是要去看双方是否相等
        return hash(self.name)

    def __eq__(self, other):  # 这个方法是为了判断双方是否相等，相等就会在集合中去重，没有这个方法，就不能去重
        return self.name == other.name

    def __repr__(self):
        return self.name


a1 = A("tom")
a2 = A("tom")
print(a1 == a2, a1 is a2)
print([a1, a2])
print((a1, a2))
print({a1, a2})


# 2 练习：设计二维坐标类Point，使其成为可hash类型，并比较2个坐标的实例是否相等
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __hash__(self):
        return 1  # 必须是int类型

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "({}, {})".format(self.x, self.y)


p1 = Point(1, 2)
p2 = Point(1, 2)
print(hash(p1), hash(p2))
print(p1 == p2, p1 is p2)
print({p1, p2})
