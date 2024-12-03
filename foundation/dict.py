# 初始化
d1 = {}
d2 = dict()
d3 = dict(a=100, b=200)  # dict(**kwargs)
d4 = dict(d3)  # dict(mapping, **kwarg)
d5 = dict(d4, a=300, c=400)
d6 = dict([('a', 100), ['b', 200], (1, 'abc')], b=300, c=400)  # dict(iterable, **kwarg)，iterable要和name=value（二元组）配合
d7 = dict.fromkeys(range(5))  # key为解构后的range(5)，value为None
d8 = dict.fromkeys(range(5), 0)  # value为0

# 元素访问
print(d3['a'])  # key不存在会报错
print(d3.get('a'))  # key不存在返回None
print(d3.get('c', -1))  # key不存在返回-1
print(d3.setdefault('c', 1))  # key不存在便添加，value默认为None，这里设置为1

# 新增和修改
d3['a'] = 300
d3.update(d=2)
d3.update([('e', 2)])
d3.update({'f': 3})

# 删除
del d3['f']
d3.pop('e')  # 返回对应的value
d3.pop('g', None)  # key不存在返回None，否则报错
d3.popitem()  # 随机删除一个key-value并返回，如果dict为空会报错
d3.clear()

# 遍历
for k in d4:  # 遍历key
    print(k)

for v in d4.values():  # 遍历value，O(n)
    print(v)
for k in d4:  # O(1)
    print(d4[k])

for kv in d4.items():  # 遍历key-value，返回二元组
    print(kv)
for k, v in d4.items():  # 分别遍历key和value
    print(k, v)

# 遍历删除指定元素
key = []  # 使用列表保存key，避免迭代过程中dict的size变化
for k, v in d5.items():
    if v > 3:
        key.append(k)
for k in key:
    d5.pop(k)
