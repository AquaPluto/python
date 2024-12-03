# 初始化
tuple1 = ()  # 空元组
tuple2 = (1,)  # 必须有这个逗号，(1, )
tuple3 = (1,) * 5  # (1, 1, 1, 1, 1)
tuple4 = (1, 2, 3)
tuple5 = 1, 'a'  # 封装，(1, 'a')
tuple6 = (1, 2, 3, 1, 2, 3)
tuple7 = tuple()  # 空元组
tuple8 = tuple(range(5))
tuple9 = tuple([1, 2, 3])  # (1, 2, 3)
tuple10 = (1,) + (2,)

# 索引
print(tuple4[0])

# 查询
print(tuple4.index(2))
print(tuple4.count(1))
print(len(tuple4))

# 嵌套列表（增删改）
tuple11 = ([1],) * 3
tuple11[0][0] = 200
tuple11[1].append(300)  # ([200, 300], [200, 300], [200, 300])
