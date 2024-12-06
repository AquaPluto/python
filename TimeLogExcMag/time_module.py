# datetime模块
import datetime

print(datetime.datetime(2021, 6, 17, 18, 20, 5))  # 构造时间对象
print(datetime.datetime.now())  # 返回当前时间的时间对象，无时区时间
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))))  # 有时区时间
print(datetime.datetime.now(datetime.timezone.utc))  # 0时区的时间对象
print(datetime.datetime.utcnow())  # UTC时间
print(datetime.datetime.now().timestamp())  # 获取时间戳，1970年1月1日0点到现在的秒数
print(datetime.datetime.fromtimestamp(datetime.datetime.now().timestamp()))  # 从时间戳获取时间对象

datestr = '2018-01-10 17:16:08'
dt = datetime.datetime.strptime(datestr, '%Y-%m-%d %H:%M:%S')  # 字符串变为时间对象
print(dt)
print(dt.strftime('%Y-%m-%d %H:%M:%S'))  # 时间对象变为字符串
print("{:%Y/%m/%d %H:%M:%S}".format(dt))

print(datetime.timedelta(days=2))  # 时间对象，可以用来执行日期和时间的加减运算
print(datetime.datetime.now() - datetime.timedelta(days=2))  # 计算两天前的时间
print((datetime.datetime.now() - (
        datetime.datetime.now() - datetime.timedelta(days=2))).total_seconds())  # 计算现在和两天前的时间差的总秒数

# time模块
import time

time.sleep(2)  # 挂起线程2秒
