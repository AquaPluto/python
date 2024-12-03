# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print("{}*{}={:<{}}".format(j, i, i * j, 2 if j < 2 else 3), end='' if i != j else '\n')

# 100内奇数和
print(sum(range(1, 100, 2)))

# 100内斐波那契数列
a = 0  # f(0)
b = 1  # f(1)
while True:
    print(b)
    a, b = b, a + b
    if b >= 100:
        break

# 斐波那契数列第101项
a = 0  # f(0)
b = 1  # f(1)
count = 1
while True:
    print(count, b)
    a, b = b, a + b
    if count >= 101:
        break
    count += 1

# 打印菱形
n = 7
e = n // 2
for i in range(-e, e + 1):
    print(' ' * abs(i), '*' * (n - 2 * abs(i)), sep='')

# 从nums = [1, (2, 3, 4), 5]中，提取其中4出来
[_, [*_, a], _] = [1, [2, 3, 4], 5]
print(a)

# 从 list(range(10)) 中，提取第二个、第四个、倒数第二个元素
_, a, _, b, *_, c, _ = list(range(10))
print(a, b, c)

# 取路径中的路径名和基名
path = r'c:\windows\nt\drivers\ect'
dirname, _, basename = path.rpartition('\\')
print(dirname, basename)

# 给出3个整数，判断大小，并升序输出
nums = [2, 5, 1]
out = None
if nums[0] > nums[1]:
    if nums[1] > nums[2]:
        out = [2, 1, 0]
    else:
        if nums[0] > nums[2]:
            out = [1, 2, 0]
        else:
            out = [1, 0, 2]
else:
    if nums[2] > nums[1]:
        out = [0, 1, 2]
    else:
        if nums[0] > nums[2]:
            out = [2, 0, 1]
        else:
            out = [0, 2, 1]
print(list(nums[i] for i in out))

# 有一个列表 lst = [1,4,9,16,2,5,10,15]，生成一个新列表，要求新列表元素是 lst 相邻2项的和
lst = [1, 4, 9, 16, 2, 5, 10, 15]
print([(lst[i] + lst[i + 1]) for i in range(len(lst) - 1)])

# 随机生成100个产品ID，ID格式如下：顺序的数字6位，分隔符点号，10个随机小写英文字符，例如 000005.xcbaaduixy
import random
import string

alphabet = string.ascii_lowercase
for i in range(1, 101):
    id = "{:0>6}.{}".format(i, ''.join(random.choices(alphabet, k=10)))
    print(id)
