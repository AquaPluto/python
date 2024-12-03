# pickle
import pickle

filename = 'test.txt'

i = 99
c = 'c'
l = list('123')
d = {'a': 127, 'b': 'abc', 'c': [1, 2, 3]}

with open(filename, 'wb') as f:  # 序列化，序列化后看到一堆二进制数据
    pickle.dump(i, f)
    pickle.dump(c, f)
    pickle.dump(l, f)
    pickle.dump(d, f)

with open(filename, 'rb') as f:  # 反序列化
    print(f.read(), f.seek(0))  # f.read()将二进制数据转换为字符串
    for i in range(4):
        x = pickle.load(f)
        print(i, x, type(x))

# Json
import json

d = {'name': 'Tom', 'age': 20, 'interest': ('music', 'movie'), 'class': ['python']}
j = json.dumps(d)  # 注意：转为json后，20是一个字符串，不是int
print(j, type(
    j))  # 请注意引号、括号的变化，注意数据类型的变化，{"name": "Tom", "age": 20, "interest": ["music", "movie"], "class": ["python"]} <class 'str'>

d1 = json.loads(j)
print(type(d1), d1)  # <class 'dict'> {'name': 'Tom', 'age': 20, 'interest': ['music', 'movie'], 'class': ['python']}
print(d == d1)  # False
print(d is d1)  # False

# CSV
import csv

rows = [
    ('id', 'name', 'age', 'comment'),
    [1, 'tom', 20, 'tom'],
    (2, 'jerry', 18, 'jerry'),
    (3, 'justin', 22, 'just\t"in'),
    "abcdefgh",
    ((1,), 2, [3])
]  # "abcdefgh"和((1,), 2, [3])并不符合CSV的行格式，因为它们要么是字符串，要么是嵌套的元组和列表，而不是扁平的序列。尽管如此，csv.writer会尝试将这些数据转换为字符串形式并写入

# newline=''，表示写入时，不要做\n的替换，那么输出就是\r\n
with open('test.txt', 'w+', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)  # 创建了一个writer对象
    writer.writerow(rows[0])  # 写入标题行
    writer.writerows(rows[1:])  # 写入数据行

# newline=''，表示读取时，也不做\n的替换
with open('test.txt', encoding='utf-8', newline='') as f:
    reader = csv.reader(f)  # 行迭代器，创建了一个reader对象
    print(next(reader))  # 打印第一行，即标题行
    print(next(reader))  # 打印第二行
    print('-' * 30)
    for line in reader:  # 遍历剩余的行
        print(line)
