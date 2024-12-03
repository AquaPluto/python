# 列表解析式
l1 = [x for x in range(10)]
l2 = [(x + 1) * 2 for x in range(10)]
l3 = [(x, x + 1) for x in range(10)]
l4 = dict([(x + 1, x) for x in range(10)])
l5 = [(i, j) for i in range(5) for j in range(3)]
l6 = [(i, j) for i in range(7) if i > 4 for j in range(20, 25) if j > 23]

# 集合解析式
s1 = {x for x in range(10)}
s2 = {(x + 1) * 2 for x in range(10)}
s3 = {(x, x + 1) for x in range(10)}
s4 = {i % 3 for i in range(4, 500)}

# 字典解析式
d1 = {x: x + 1 for x in range(10)}
d2 = {x: (x, x + 1) for x in range(10)}
d3 = {x: [x, x + 1] for x in range(10)}
d4 = {(x,): [x, x + 1] for x in range(10)}
d5 = {str(x): y for x in range(3) for y in range(4)}
d6 = {chr(0x41 + i): i for i in range(5)}

# 生成器表达式
g1 = (x for x in range(10))  # 返回生成器对象，只能迭代一次
for g in g1:  # 使用for循环迭代
    print(g)
print(next(g1))  # 使用next()函数迭代，返回下一个元素
print(next(g1, 404))  # 设置默认值，当迭代到没有元素时，返回默认值，否则报错
