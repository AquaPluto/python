# 查看当前工作目录
import os

current_path = os.getcwd()
print(current_path)

# 文件操作
f1 = open('test', mode='r')  # 只读，文件不存在抛异常
f2 = open('test', mode='w')  # 只写，文件不存在则创建，文件存在则覆盖内容
f3 = open('test', mode='x')  # 只写，文件不存在则创建，文件存在抛异常
f4 = open('test', mode='a')  # 只写，文件不存在则创建，文件存在尾部追加内容
f5 = open('test', mode='t')  # 以文本模式打开
f6 = open('test', mode='b')  # 以二进制模式打开
f7 = open('test', mode='r+w')  # 增加功能

f1.seek(0)  # 偏移量为0，指针指在文件开头
f1.seek(0, 1)  # 同上
f1.seek(0, 2)  # 指针指在文件结尾
f1.tell()  # 返回当前指针所在位置
f1.read()  # 读取文件内容
f1.read(2)  # 读取2个字符或2个字节
f2.write('abc')  # 单行写入文件
lines = ['abc', '123\n', 'gzgs']
f2.writelines(lines)  # 多行写入文件
f2.close()  # 关闭文件

# 上下文管理
with open('test', 'w') as f:  # with作用于这个文件对象，f是这个文件对象的别名
    f.write('\n'.join(map(str, range(1, 4))))

with open('test') as f:
    for line in f:  # 文件对象是可迭代对象，逐行遍历
        print(line.encode())
