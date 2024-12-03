# enumerate 迭代一个可迭代对象，返回一个迭代器
lst1 = [1, 3, 5, 7, 9]
for i, v in enumerate(lst1):
    print(i, v)
print(next(enumerate(lst1)))
it = iter(lst1)  # iter将可迭代对象转换成迭代器
for i, v in enumerate(it, 2):  # 指定索引从2开始
    print(i, v)

# sorted 排序
lst2 = [5, 3, 1, 2, 4]
print(sorted(lst2))
print(sorted(lst2, reverse=True))
print(sorted(lst2, key=lambda x: 6 - x))  # 等价上例

# filter 过滤 filter(function, iterable) 对可迭代对象进行遍历，返回一个迭代器
lst3 = range(5)
print(list(filter(lambda x: x % 2 == 0, lst2)))
print(list(filter(None, lst3)))  # False就不要了

# map 映射 map(function, *iterable) 对多个可迭代对象中的元素按照函数映射，返回一个迭代器
print(list(map(lambda x: x + 1, range(5))))
print(list(map(lambda *args: args, range(5), 'abcd', '123')))
print(dict(map(lambda x: (x % 5, x), range(500))))
print(dict(map(lambda x, y: (x, y), 'abcde', range(10))))

# zip 拉链 zip(*iterables) 把多个可迭代对象合并成一个元组，返回一个迭代器
print(list(zip(range(5), 'abcd', '123')))
print(dict(zip(range(5), 'abcd')))
print({str(x): y for x, y in zip(range(5), range(5))})
print(dict(zip('abcd', map(lambda x: 100 + x, range(5)))))
