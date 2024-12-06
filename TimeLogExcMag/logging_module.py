import logging

# 记录器
root = logging.getLogger()  # 根记录器，等价于logging.root，如果不指定名称，默认就是根记录器；级别默认是Warning（30）
print(root)

log1 = logging.getLogger('log1')
print(log1)

log2 = logging.getLogger('log1.log2')  # logging是有层次结构的，用 "." 分割
print(root.parent, log1.parent, log2.parent)  # 根记录器没有父

# 级别level
print(root.level, log1.level, log2.level)  # 没有指定，级别就为0
print(log1.getEffectiveLevel(), log2.getEffectiveLevel())  # 但是等效级别就会继承父记录器的非0级别
log1.info('log1.info')  # 没有输出，是因为这里的日志消息级别是info（20），而记录器的级别是30，20小于30，所以只有日志消息级别大于等于记录器的级别才会输出
log1.warning('log1.warning')

log3 = logging.getLogger('log3')
log3.setLevel(40)  # 设定级别，40为ERROR
print(log3.level, log3.getEffectiveLevel())
log3.warning('log3.warning')  # 不能输出

log4 = logging.getLogger('log3.log4')
print(log4.level, log4.getEffectiveLevel())  # 继承父记录器的级别

# 根记录器的使用
FORMAT = "%(asctime)s %(name)s %(threadName)s [%(message)s]"
DATEFMT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=FORMAT, datefmt=DATEFMT, level=logging.INFO)  # 对根记录器做输出信息的配置，以及handler的设置
logging.info('info message')

# 处理器Handler
# basicConfig函数执行后，默认会生成一个StreamHandler实例
# 如果设置了filename，则只会生成一个FileHandler实例
# 每一个记录器实例可以设置多个Handler实例
import sys

handler1 = logging.FileHandler('o:/test.log', 'w', 'utf-8')  # 输出到文件
handler2 = logging.StreamHandler(sys.stdout)  # 在控制台标准输出，默认标准错误
handler1.setLevel(logging.WARNING)  # 设置处理器级别，不设置默认为0，那么就会根据记录器的级别来输出信息，相当于继承记录器的级别
handler2.setLevel(logging.WARNING)

# 格式化器Formatter
# 根记录器使用basicConfig函数设置信息的格式化输出，也可以通过Formatter来设置
# 每一个记录器通过定义Formatter来设置信息的格式化输出
formatter = logging.Formatter('#%(asctime)s <%(message)s>#')  # 定义格式化器
handler1.setFormatter(formatter)  # 为处理器设置格式化器

# 范例：创建一个日志Handler将日志输出到控制台，同时也输出到文件
FORMAT = "%(asctime)s %(name)s %(threadName)s [%(message)s]"
DATEFMT = "%Y-%m-%d %H:%M:%S"
logging.basicConfig(format=FORMAT, datefmt=DATEFMT, level=logging.INFO)  # 根logger设置

logger = logging.getLogger('logger')  # 记录器设置
logger.setLevel(30)  # 决定了哪些消息可以进入处理器链

handler3 = logging.FileHandler('test.log', 'w', 'utf-8')  # 设置handler
handler4 = logging.StreamHandler(sys.stdout)
handler3.setLevel(logging.WARNING)  # 决定了哪些消息最终会被输出
handler4.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 设置Formatter，并把handler加入
handler3.setFormatter(formatter)
handler4.setFormatter(formatter)

logger.addHandler(handler3)  # 记录器加入handler
logger.addHandler(handler4)

logger.propagate = False  # 阻断向父logger的传播
logger.warning('This is an warning message')
logger.propagate = True
logger.error('This is an error message')

# handler中的RotatingFileHandler、TimedRotatingFileHandler
from logging.handlers import RotatingFileHandler, TimedRotatingFileHandler
import time

handler1 = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5)
# 在日志文件达到一定大小时创建新的日志文件
# maxBytes：每个日志文件的最大字节数；backupCount：保留的旧日志文件的数量

handler2 = TimedRotatingFileHandler('app.log', 's', 30)
# 根据时间间隔创建新的日志文件
# when：定义日志文件轮转的时间间隔单位，这里是秒（s）
# interval：时间间隔的数量，这里是30

def get_log_filename():  # 自定义日志文件名，包含日期
    return time.strftime("%Y%m%d", time.localtime()) + "-app.log"


handler3 = TimedRotatingFileHandler(get_log_filename(), when='midnight', interval=1, backupCount=7)
