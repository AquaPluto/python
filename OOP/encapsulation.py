# 下例代码，介绍了如何定义类、调用类；类属性和实例属性的区别、属性的本质；私有属性和保护属性的区别
class Person:  # 类对象
    height = 180  # 类属性，实例间共享

    def __init__(self, name, age, waistline, arm_length):  # 初始化方法，对实例进行初始化，不能有返回值
        self.name = name  # 实例属性，self指代实例自身，即每个不同的实例都有属于自己的属性
        self.age = age
        self.__waistline = waistline  # 私有的实例属性
        self._arm_length = arm_length  # 保护的实例属性，半私有

    def print(self):  # 类方法，也是类属性
        print(self.name, self.age, self.height, self.__waistline, self._arm_length)


tom = Person("Tom", 18, 80, 65)  # 实例化
tom.print()

tom.height = 190  # 动态增加实例属性
tom.print()

jerry = Person("Jerry", 20, 70, 70)
jerry.print()

Person.weight = 70  # 动态增加类属性
print(Person.weight, tom.weight, jerry.weight)
print(Person.weight, tom.__class__.weight, jerry.__class__.weight)

print(Person.__class__, Person.__dict__)  # 类对象的类型和类属性
print(tom.__class__, tom.__dict__)  # 实例的类型和实例属性，注意私有属性
print(tom.__class__.__class__, tom.__class__.__dict__)  # 通过实例访问类

# print(tom.__waistline)  # 在类外部私有属性不能访问，但是真的不可以访问吗？
print(tom._Person__waistline)  # 这样子可以绕过限制去访问私有属性，所以python没有绝对的私有属性，但请遵守约定
print(tom._arm_length)  # 在类外部可以访问，但只有类对象和子类对象能访问这些成员，且不能用 from module import * 导入


# 下例代码，介绍了属性装饰器
class Person2:
    def __init__(self, name):
        self.__name = name

    @property  # 必须有，至少有只读属性，python中的私有成员只是摆设，可以通过property装饰器设置只读，不能修改
    def name(self):
        return self.__name

    @name.setter  # 属性可写
    def name(self, value):  # 使用property装饰器的时候方法必须同名
        self.__name = value


tom = Person2('Tom')
print(tom.name)  # 属性装饰器可以将方法装饰成属性进行访问
tom.name = "jerry"
print(tom.name)
