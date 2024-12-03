# 初始化
list1 = []
list2 = [1, 2, 3]
list3 = list(range(1, 5))
list4 = [3, 'ab', True, (1, 2), {'a': 1}, [1, 2]]

# 索引访问，返回值
print(list2[0])
print(list2[-1])

# 查询
print(list2.index(2))  # 返回索引
print(list2.count(3))
print(len(list2))

# 修改
list2[1] = 4
x = [[1]] * 3
x[1][0] = 200  # [[200], [200], [200]]

# 增加单个元素，索引可以超界
list2.append(4)  # 追加，返回None
list2.insert(1, 5)  # 索引1插入5，返回None

# 增加多个元素
list2.extend([6, 7])  # 追加，返回None
list2.extend(range(2))
list2.extend(list3)
list5 = list2 + list3  # 拼接，返回新list
list6 = list3 * 2  # 重复，返回新list

# 删除
list2.remove(4)  # 指定value删除，返回None
list2.pop()  # 删除末尾，返回被删除元素
list2.pop(1)  # 删除指定索引对应的值
# list2.clear()  # 清空，返回None

# 反转
list2.reverse()  # 就地修改，返回None
x = list(range(5))
for i in range(1, len(x) + 1):  # 倒着读取
    print(i, x[-i])
for i in reversed(x):  # 只适合有序序列
    print(i)

# 排序
list2.sort()  # 返回None
list2.sort(reverse=True)  # 降序
sorted(list2)  # 返回新list

# 复制
list7 = list2.copy()
