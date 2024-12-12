# Event：线程间通信机制中最简单的实现，使用一个内部的标记flag，通过flag的True或False的变化来进行操作
# 例子：老板雇佣了一个工人，让他生产杯子，老板一直等着这个工人，直到生产了10个杯子
import threading
import logging

FARMAT = "%(asctime)s %(threadName)s %(thread)s %(message)s"
logging.basicConfig(format=FARMAT, level=logging.INFO)

event = threading.Event()  # 1:n，n个线程等待另1个线程完成资源调度再执行


def boss():
    logging.info("I'm boss,watch u")
    event.wait()  # 阻塞等待标记为True后，解除阻塞态
    logging.info("good job")


def worker(count=10):
    logging.info("I'm worker for u")
    cups = []
    while not event.wait(0.5):
        cups.append(1)
        if len(cups) >= count:
            event.set()  # 做完了标记为True，boss线程解除阻塞态
    logging.info("finish,cups={}".format(len(cups)))


b = threading.Thread(target=boss, name='boss')
w = threading.Thread(target=worker, name='worker')
b.start()
w.start()

# Lock：锁
# 1 基本使用
import threading
import logging
import time

FARMAT = "%(asctime)s %(threadName)s %(thread)s %(message)s"
logging.basicConfig(format=FARMAT, level=logging.INFO)

lock = threading.Lock()  # 互斥mutex，跨线程
lock.acquire()  # 主线程获得锁
print('-' * 30)


def worker(l):
    logging.info('worker start')
    l.acquire()  # 由于锁已被主线程获取，它们将被阻塞，只有等释放锁了才能被获取
    logging.info('worker done')  # 任一worker获取锁之后执行完并没有释放锁，所以就又被锁住了，但是锁对象是可以跨线程操作的，对于多线程来说，都是同一个锁对象


for i in range(5):
    threading.Thread(target=worker, name='worker-{}'.format(i), args=(lock,), daemon=False).start()

while True:
    cmd = input(">>>")  # 当主线程释放锁后，被input阻塞住
    if cmd == 'r':
        lock.release()  # 主线程释放锁，那5个worker线程争夺锁；由于worker线程执行完没有释放锁，要帮忙释放
        print('released one locker')
    elif cmd == 'quit':  # 造成死锁，因为只释放了一个锁主线程就结束了，还有4个worker线程还在等待锁的释放，除非他们是daemon线程
        lock.release()
        break
    else:
        print(threading.enumerate())
        print(lock.locked())  # 是否还有锁

# 2 例子：订单要求生产1000个杯子，组织10个工人生产。请忽略老板，关注工人生成杯子
cups = []
lock = threading.Lock()


def worker(count=1000):
    logging.info("worker start")
    while True:
        lock.acquire()  # 获取锁，可以认为一个工人进工厂了，并把门锁住，其他工人等待
        if len(cups) >= count:
            lock.release()  # 有一个工人知道到1000个，解锁让其他工人也知道已经到1000个了，完成任务了
            break
        time.sleep(0.0001)
        cups.append(1)
        lock.release()  # 生产完一个杯子了，解锁，让另一个工人进来接着生产，自己去干别的事情
    logging.info('I finished my job. cups = {}'.format(len(cups)))


for i in range(1, 11):
    threading.Thread(target=worker, name=f"worker-{i}").start()


# 3 上下文支持
def worker(count=1000):
    logging.info("worker start")
    while True:
        with lock:  # 获取锁，离开with释放锁
            if len(cups) >= count:
                break
            time.sleep(0.0001)
            cups.append(1)
    logging.info('I finished my job. cups = {}'.format(len(cups)))
