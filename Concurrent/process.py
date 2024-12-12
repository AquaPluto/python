import multiprocessing
import datetime
import logging

logging.basicConfig(level=logging.INFO, format="%(processName)s %(threadName)s %(message)s")
start = datetime.datetime.now()


def calc():
    sum = 0
    for _ in range(1000000000):  # 10亿
        sum += 1
    logging.info(sum)


if __name__ == '__main__':  # 使用多进程的时候必须有这一句
    start = datetime.datetime.now()
    ps = []  # 创建一个进程列表
    for i in range(4):  # 创建4个进程
        p = multiprocessing.Process(target=calc, name='calc-{}'.format(i))
        ps.append(p)
        p.start()

    for p in ps:
        p.join()  # 等待所有子进程完成

    delta = (datetime.datetime.now() - start).total_seconds()
    logging.info(delta)
    for p in ps:
        logging.info(f"{p.name}: {p.exitcode}")
