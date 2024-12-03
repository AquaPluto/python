# 初始化
s1 = 'string'
s2 = "string2"
s3 = '''this's a "String" '''
s4 = 'hello \n magedu.com'
s5 = r"hello \n magedu.com"
s6 = 'c:\windows\nt'
s7 = r"c:\windows\nt"
s8 = 'c:\windows\\nt'
name = 'tom'
age = 20
s9 = f'{name}, {age}'
sql = """select * from user where name='tom' """

# 索引
print(s1[0])

# 拼接
s10 = s1 + s2  # 返回string
s11 = ''.join(sql)  # 返回string
s12 = '@'.join(s1)  # 使用@作为分隔符

# 字符查找
print(s1.find('s'))  # 返回索引，找不到返回-1，返回值int
print(s1.find('s', 1, 2))  # 在[1,2)区间找
print(s1.rfind('s'))  # 从右往左找

print(s1.index('s'))  # 返回索引，返回值int
# print(s1.index('s', 1, 2))  # 找不到会报错
print(s1.rindex('s'))

print(s1.count('s'))
print(s1.count('s', 1, 2))
print(len(s1))

# 分割
s13 = ','.join('abcd')
print(s13.split(','))  # 返回list of string
print(s13.split())  # 默认以空白字符串分割
print(s13.split(',', 2))  # 分隔2次
print(s13.rsplit(',', 2))

s14 = '\na b  \tc\nd\n'
print(s14.split())  # ['a', 'b', 'c', 'd']
print(s14.split('\n'))  # ['', 'a b  \tc', 'd', '']
print(s14.split(' '))  # ['\na', 'b', '', '\tc\nd\n']
print(s14.split('b'))  # ['\na ', '  \tc\nd\n']
print(s14.splitlines())  # ['', 'a b  \tc', 'd']

print(s13.partition(','))  # 返回tuple of string (head, sep, tail)，如果没有分割符，则返回(head, '', '')
print(s13.partition('.'))
print(s13.rpartition(','))
print(s13.rpartition('.'))

# 替换
print(s13.replace(',', ' '))  # 返回string
print(s13.replace(',', ' ', 2))  # 只替换2次

s14 = 'www.baidu.com'
print(s14.replace('w', 'a'))
print(s14.replace('ww', 'a'))
print(s14.replace('ww', 'w'))
print(s14.replace('www', 'a'))

# 移除
s15 = '\t\r\na b  c,d\ne\n\t'
print(s15.strip())  # 去除两端的空白字符，返回string
print('-' * 30)
print(s15.strip('\t\n'))  # 去除指定的字符集chars
print('-' * 30)
print(s15.strip('\t\ne\r'))
print('-' * 30)
print(s15.strip('\t\ne\rad'))

# 首尾判断
s16 = "www.magedu.edu"
print(s16.startswith('ww'))
print(s16.startswith('e', 7))
print(s16.startswith('e', 10))
print(s16.startswith('edu', 11))
print(s16.endswith('edu'))