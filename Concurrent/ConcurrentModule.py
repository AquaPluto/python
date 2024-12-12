# ThreadPoolExecutor对象
from concurrent.futures import ThreadPoolExecutor, wait
import datetime
import logging

FORMAT = "%(asctime)s [%(processName)s %(threadName)s] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(base):
    sum = base
    for i in range(100000000):
        sum += 1
    logging.info(sum)
    return sum


start = datetime.datetime.now()
executor = ThreadPoolExecutor(3)  # 创建3个线程的线程池
with executor:  # 默认shutdown阻塞，阻塞到所有任务完成，跟wait的区别是with会正确地关闭线程池，释放资源
    fs = []  # 创建一个空列表用来存储`Future`对象。
    for i in range(3):  # 提交三个任务，刚刚好对应3个线程，如果超出三个任务，会等待线程池中的线程空闲，再去提交多余任务，也就是复用线程池中的线程
        future = executor.submit(calc, i * 100)  # 提交任务，返回future对象
        fs.append(future)

    # wait(fs) # 阻塞方法，阻塞到所有任务完成，类似于join方法
    print('-' * 30)

for f in fs:  # 相对于wait(fs)或者with方法，这个循环不会阻塞，一个任务做完了，就返回结果，不需要等待所有任务做完
    print(f, f.done(), f.result())  # done不阻塞，表示任务做完了没有；result阻塞，会阻塞直到任务完成。
print('=' * 30)

delta = (datetime.datetime.now() - start).total_seconds()
print(delta)

# ProcessPoolExecutor对象
from concurrent.futures import ProcessPoolExecutor, wait
import datetime
import logging

FORMAT = "%(asctime)s [%(processName)s %(threadName)s] %(message)s"
logging.basicConfig(format=FORMAT, level=logging.INFO)


def calc(base):
    sum = base
    for i in range(100000000):
        sum += 1
    logging.info(sum)
    return sum


if __name__ == '__main__':
    start = datetime.datetime.now()
    executor = ProcessPoolExecutor(3)  # 创建3个进程的进程池
    with executor:  # 默认shutdown阻塞，阻塞到所有任务完成，跟wait的区别是with会正确地关闭进程池，释放资源
        fs = []  # 创建一个空列表用来存储`Future`对象。
        for i in range(3):  # 提交三个任务，刚刚好对应3个进程，如果超出三个任务，会等待进程池中的进程空闲，再去提交多余任务，也就是复用进程池中的进程
            future = executor.submit(calc, i * 100)  # 提交任务，返回future对象
            fs.append(future)

        # wait(fs) # 阻塞方法，阻塞到所有任务完成
        print('-' * 30)

    for f in fs:  # 相对于wait(fs)或者with方法，这个循环不会阻塞，一个任务做完了，就返回结果，不需要等待所有任务做完
        print(f, f.done(), f.result())  # done不阻塞，表示任务做完了没有；result阻塞，会阻塞直到任务完成。
    print('=' * 30)

    delta = (datetime.datetime.now() - start).total_seconds()
    print(delta)
