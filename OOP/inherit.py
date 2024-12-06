# 简单的继承
class Animal:  # 它的基类就是object
    def __init__(self, name):
        self.name = name

    def shout(self):
        print("{} shout".format(self.name))


class Cat(Animal):
    pass


c = Cat("cat")
c.shout()

print(Animal.__base__)  # 基类元组第一项
print(Animal.__bases__)  # 基类元组
print(Animal.__mro__)  # 方法查找顺序列表
print(Animal.__subclasses__())  # 类的子类列表
print(Cat.__base__)
print(Cat.__bases__)
print(Cat.mro())


# 继承中的访问控制
class Animal:
    __a = 10  # _Animal__a = 10
    _b = 20
    c = 30

    def __init__(self):
        self.__d = 40
        self._e = 50
        self.f = 60
        self.__a += 1  # self._Animal__a = self._Animal__a + 1

    def showa(self):
        print(self.__a)  # self._Animal__a，这里是实例的__a
        print(self.__class__.__a)  # Cat.__a ==> Cat._Animal__a，这里是类的__a

    def __showb(self):
        print(self._b)
        print(self.__a)
        print(self.__class__.__a)


class Cat(Animal):
    __a = 100  # _Cat__a
    _b = 200


c = Cat()
c.showa()
c._Animal__showb()
print(c.c)
print(c._Animal__d)
print(c._e, c.f, c._Animal__a)
print(c.__dict__)
print(c.__class__.__dict__)


# 方法的重写、覆盖
# 1 完全重写
class Animal:
    def shout(self):
        print('Animal shouts')


class Cat(Animal):
    def shout(self):  # 覆盖了父类方法
        print('miao')


a = Animal()
a.shout()
c = Cat()
c.shout()


# 2 不完全重写
class Animal:
    def shout(self):
        print('Animal shouts')


class Cat(Animal):
    def shout(self):  # 覆盖了父类方法
        print('miao')
        super().shout()  # 调用父类的方法


c = Cat()
c.shout()


# 继承中的初始化
# 1 B实例的初始化会自动调用父类A的 __init__ 方法
class A:
    def __init__(self):
        self.a1 = 'a1'
        self.__a2 = 'a2'
        print('init in A')


class B(A):
    pass


b = B()
print(b.__dict__)


# 2 覆盖父类的初始化方法
class A:
    def __init__(self):
        self.a1 = 'a1'
        self.__a2 = 'a2'
        print('init in A')


class B(A):
    def __init__(self):
        self.b1 = 'b1'
        print('init in B')


b = B()
print(b.__dict__)


# 3 不完全覆盖
class A:
    def __init__(self):
        self.a1 = 'a1'
        self.__a2 = 'a2'
        print('init in A')


class B(A):
    def __init__(self):
        super().__init__()
        self.b1 = 'b1'
        print('init in B')


b = B()
print(b.__dict__)
