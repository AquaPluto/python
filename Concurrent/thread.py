import threading
import time
import logging


# 线程的创建和退出
def worker1():  # 主线程创建worker函数对象，创建一个工作线程来运行
    print("start worker1")
    for i in range(5):
        print("~~~~")
        # 1 / 0  # 出现异常，工作线程崩溃退出，但不会阻碍到主线程的工作，可以看到报错是Exception in thread worker，进程退出状态码为0
        # break  # 线程退出
        # return  # 线程退出
    print("finish worker1")


t1 = threading.Thread(target=worker1, name="worker1")  # 创建一个工作线程对象
t1.start()  # 启动线程
print("=====end=====")  # 主线程执行，因为线程是并发的，所以工作线程不会阻碍


# 线程原理
def worker2():
    print("start worker2")
    worker1()  # 在worker2的线程当中运行，压在线程worker2的栈上，与主线程或其他线程并发执行
    print("finish worker2")


t2 = threading.Thread(target=worker2, name="worker2")
t2.start()
worker1()  # 在主线程当中运行


# 线程传参
def add(x, y):
    # return x + y  # 目前情况下，返回值写了白写，因为每个线程有各自的堆栈，工作线程的结果不会返回给主线程
    print('{} + {} = {}，id : {}'.format(x, y, x + y, threading.current_thread().ident))  # 表示当前线程对象的id


t1 = threading.Thread(target=add, name='add', args=(4, 5))
t1.start()
time.sleep(2)

t2 = threading.Thread(target=add, name='add', args=(6,), kwargs={'y': 7})
t2.start()
time.sleep(2)

t3 = threading.Thread(target=add, name='add', kwargs={'x': 8, 'y': 9})
t3.start()


# threading的属性和方法
def ShowThreadInfo():
    """属性依次分别为：当前线程对象；当前线程对象id；主线程对象；处于alive状态的线程个数；处于alive状态的线程列表"""
    print('current thread = {}\ncurrent thread_id = {}\nmain thread = {}\nactive count = {}\nactive list = {}'.format(
        threading.current_thread(), threading.get_ident(),
        threading.main_thread(),
        threading.active_count(), threading.enumerate()))


def worker3():
    ShowThreadInfo()  # 在worker3线程执行
    for i in range(5):
        time.sleep(1)
        print('I am working')
    print('finished')


t = threading.Thread(target=worker3, name='worker3')
ShowThreadInfo()
time.sleep(1)
t.start()


# Thread实例的属性和方法
def worker4():
    for i in range(5):
        time.sleep(1)
        print('I am working')
    print('finished')


t = threading.Thread(target=worker4, name='worker4')
print(t.name, t.ident)  # 线程的名字和id
time.sleep(1)
t.start()

while True:
    time.sleep(1)
    print("{} {} {}".format(t.name, t.ident, 'alive' if t.is_alive() else 'dead'))

    if not t.is_alive():
        # t.start()  # 线程可以重启吗？不可以
        break


# start和run方法的本质
def worker5():
    t = threading.current_thread()
    for i in range(5):
        time.sleep(1)
        print('I am working', t.name, t.ident)
    print('finished')


class MyThread(threading.Thread):
    def start(self):
        print('start~~~~')
        super().start()

    def run(self):
        print('run~~~~')
        super().run()


t = MyThread(target=worker5)
t.start()  # 启动操作系统工作线程，并运行run方法


# t.run()  # 仅仅只是调用目标函数，所以在主线程中运行

# daemon线程
def a():
    print("********")


def worker6():
    threading.Thread(target=a).start()  # 当前a线程是在worker线程中运行的，所以取当前线程（worker）的daemon值给a线程
    for i in range(5):
        time.sleep(1)
        print('I am working')
    print('finished')


t1 = threading.Thread(target=worker6, daemon=False)  # 设置为daemon线程，默认是non-daemon线程
t1.start()
print("Main Thread Exits")  # 主线程执行完就退出，不等t1线程执行完，如果是non-daemon线程，就会等待执行完才会退出


# join方法：完全阻塞
def worker7():
    for i in range(5):
        time.sleep(1)
        print('I am working')
    print('finished')


t = threading.Thread(target=worker7)  # 可以设置daemon值来测试，结果都是一样的
t.start()
t.join()  # 阻塞调用json方法的线程，当前是阻塞主线程，等待t线程执行完，主线程才会开始工作（join谁，就等待谁）
print("Main Thread Exits")  # 等待t线程执行完才会打印

# threading.local类
# 1 使用局部变量可以实现线程安全，那么全局变量呢？
FORMAT = "%(asctime)s %(threadName)s %(thread)d %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)

global_data = threading.local()  # 全局对象


def worker():
    global_data.x = 0
    for i in range(100):
        time.sleep(0.0001)
        global_data.x += 1
    logging.info(global_data.x)


for i in range(10):
    threading.Thread(target=worker, name='t-{}'.format(i)).start()  # 保证线程安全，每一个线程都有自己独立的x，最终的结果都会是1000

# 2 再来看另外一个例子
X = 'abc'
global_data = threading.local()
global_data.x = 100


def worker():
    logging.info(X)
    logging.info(global_data)
    logging.info(global_data.x)  # 在主线程可以打印，在worker线程中报错，说明global_data.x不能跨线程，x是在主线程创建的，不会共享到worker线程


worker()
print('~' * 30)
time.sleep(2)
threading.Thread(target=worker, name='worker').start()
