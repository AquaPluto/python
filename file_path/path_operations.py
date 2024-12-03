# os.path模块
from os import path

parent = path.dirname(__file__)  # 从文件路径中取出路径名
print(path.join(parent, 'code'))  # 拼接

print(path.splitext('/ete/syseonfig/mysal.tar.gz'))  # 按照最后的'.'分割两部分，返回二元组

p = path.join('/etc', 'sysconfig', 'network')
print(p)
print(path.exists(p))  # 是否存在
print(path.split(p))  # 将路径分割成目录部分和文件名部分
print(path.dirname(p), path.basename(p))  # 路径名和基名
print(path.abspath('.'))  # 绝对路径

p1 = path.abspath(__file__)
while p1 != path.dirname(p1):  # 打印父目录
    p1 = path.dirname(p1)
    print(p1)

# Path类
# 初始化
from pathlib import Path

p = Path()  # 当前目录"."
p1 = Path('c')
p2 = Path('a', 'b', 'c/d')  # 当前目录下的a/b/c/d
p3 = Path('/etc', Path('sysconfig'), 'network/ifcfg')  # 根下的etc目录

# 拼接
p4 = p / 'a'
p5 = 'b' / p
p6 = p4 / p5
p7 = p6.joinpath('d', 'e/f', Path('g/h'))
print(p, p1, p2, p3, p4, p5, p6, p7, sep='\n')

# 分解
print(p7.parts)
p8 = Path('/a/b/c/d')
print(p8.parts)

# 父目录
p = Path('/mysql/install/mysql.tar.gz')
print(p.parent)  # Path类的实例
print(p.parents)  # 生成器可迭代对象
for i in p.parents:
    print(i)

# 目录组成部分
print(p.parent)  # 父目录
print(p.name)  # 目录最后一部分
print(p.stem)  # 没有后缀的最后一部分
print(p.suffix)  # 最后一个扩展名
print(p.suffixes)  # 多个扩展名的列表
print(p.with_name('redis'))  # 修改目录最后一部分
print(p.with_name('redis').with_suffix('.zip'))  # 有扩展名替换，反之补充

# 全局方法
print(p.cwd())  # 工作目录
print(p.home())  # 家目录

# 判断方法
p.is_file()
p.is_dir()
p.exists()
p.is_absolute()  # 是否是绝对路径

# 绝对路径
print(p.absolute())

# 其他操作
p.rmdir()  # 删除空目录
p.touch()  # 创建文件
Path(p / 'b').touch()
p.as_uri()  # 返回URL
p.mkdir(parents=True, exist_ok=True)  # 创建目录，parents表示创建父目录，exist_ok表示如果存在抛异常
for path in p.iterdir():  # 迭代目录
    print(path)
p.stat()  # 包含文件的各种信息

# 通配符
list(p.glob('test*'))  # 返回当前目录对象下的test开头的文件
list(p.glob('**/*.py'))  # 递归所有目录，等同rglob
list(p.glob('**/*'))

g = p.rglob('*.py')  # 生成器，递归所有目录
next(g)
list(p.rglob('*.???'))  # 匹配扩展名为3个字符的文件
list(p.rglob('[a-z]*.???'))  # 匹配字母开头的且扩展名是3个字符的文件
