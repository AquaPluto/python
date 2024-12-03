foo = lambda x: x + 1  # 定义
print(foo(1))  # 调用

# 返回常量的函数
print((lambda: 0)())
print((lambda x: 1)(1))

# 加法匿名函数，带缺省值
print((lambda x, y=30: x + y)(1))
print((lambda x, y=30: x + y)(1, 2))

# keyword-only参数
print((lambda x, *, y=30: x + y)(1))
print((lambda x, *, y=30: x + y)(1, y=2))

# 可变参数
print((lambda *args: (x for x in args))(*range(5)))
print((lambda *args: [x for x in args])(*range(5)))
print((lambda *args: {x: x + 1 for x in args})(*range(5)))
print((lambda *args: {x % 5 for x in args})(*range(5)))

# 构建字典，推荐使用生成器表达式
print(dict((lambda x: (x, x + 1))(x) for x in range(5)))
print(dict(map(lambda x: (x, x + 1), range(5))))
print(dict(map(lambda x: (str(x), x + 1), range(5))))

# 按照数字排序
x = ['a', 1, 'b', 20, 'c', 32]
print(sorted(x, key=lambda x: x if isinstance(x, int) else int(x, 16)))

# 按照年龄排序
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]
sort_people = sorted(people, key=lambda person: person['age'])
for person in sort_people:
    print(person)

# 内建函数使用
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))

fruits = ['apple', 'banana', 'cherry', 'date']
sorted_fruits = sorted(fruits, key=lambda x: len(x))

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
