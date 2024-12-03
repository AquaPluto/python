# 说明：下列方法没有特别说明返回什么，均是返回match对象

import re

# 单次匹配
s = '''bottle\nbag\nbig\napple'''
# 1 match方法：从字符串的开头匹配
result = re.match('b', s)
print(1, result)
result = re.match('a', s)
print(2, result)  # None，因为字符串开头找不到就不找了
result = re.match('^a', s, re.M)  # 表示多行模式
print(3, result)  # 同上

regex = re.compile('a')  # 编译，作用是可以后续不在指定匹配表达式
print(4, regex.match(s, 8))  # 从索引为8的位置开始找

# 2 search方法：从头搜索直到第一个匹配
result = re.search('a', s)
print(5, result)
result = re.search('a', s, re.M)
print(6, result)
result = re.search('a', s, re.S)  # 表示单行模式
print(7, result)  # None，只会在bottle找

regex = re.compile('^b', re.M)
result = regex.search(s)
print(8, result)
result = regex.search(s, 8)
print(9, result)
result = regex.search(s, 5, 7)
print(10, result)  # None，前包后不包
result = regex.search(s, 5, 8)
print(11, result)

# 3 fullmatch方法：整个字符串和正则表达式完全匹配
result = re.fullmatch('bag', s)
print(12, result)  # None

result = regex.fullmatch(s, 7)
print(13, result)  # None
result = regex.fullmatch(s, 7, 10)
print(14, result)

# 全文搜索
s = '''bottle\nbag\nbig\nable'''
# 1 findall方法：从左至右匹配，返回所有匹配项的列表
result = re.findall('b', s)
print(15, result)

regex = re.compile('^b')
result = regex.findall(s)
print(16, result)

regex = re.compile('^b', re.M)
result = regex.findall(s, 7)
print(17, result)
result = regex.findall(s, 7, 10)
print(18, result)

regex = re.compile('^b', re.S)
result = regex.findall(s)
print(19, result)

# 2 finditer方法：从左至右匹配，返回所有匹配项，返回迭代器，本质是match对象
regex = re.compile('^b\w+', re.M)
result = regex.finditer(s)
print(20, next(result))
# print(20, s[next(result).start():next(result).end()]) # start表示匹配到的起始位置，end表示结束位置，此方法可以获取匹配的字符串
print(21, next(result))
# print(21, s[next(result).start():next(result).end()])

# 匹配替换
s = '''bottle\nbag\nbig\napple'''
# 1 sub方法：返回替换后的表达式
regex = re.compile('b\wg')
result = regex.sub('gzgs', s)
print(22, result)
result = regex.sub('gzgs', s, 1)  # 替换一次
print(23, result)

# 2 subn方法：返回替换后的表达式和替换次数，二元组
regex = re.compile('\s+')
result = regex.subn('\t', s)
print(24, result)

# 分组
# group() group(0) 返回所有整个匹配的字符串
# groups() 返回所有组
s = '''bottle\nbag\nbig\napple'''
regex = re.compile('(b\w+)')
result = regex.match(s)
print(25, 'match', result.group(), result.group(0), result[0], result.groups())
result = regex.search(s, 1)
print(26, 'search', result.groups())

# 命名分组
# groupdict() 返回所有命名的分组
regex = re.compile('(b\w+)\n(?P<name2>b\w+)\n(?P<name3>b\w+)')
result = regex.match(s)
print(27, 'match', result, result.group().encode(), result.group(1), result.group(2), result.group(3),
      result.group('name2'), result.group('name3'), result.groups(), result.groupdict())
result = regex.findall(s)
print(28, 'findall', result)  # findall返回不是match对象

regex = re.compile('(?P<head>b\w+)')
result = regex.finditer(s)
for x in result:
    print(29, 'finditer', x, x.group(), x.group('head'), x['head'], x[0])

# 分割字符串，跟字符串的split方法比起来，它可以指定多个字符分割
s = """
os.path.abspath(path)
normpath(join(os.getcwd(), path)).
"""
print(30, re.split('[\.()\s,]+', s))
print(31, *filter(None, re.split('[\.()\s,]+', s)))
