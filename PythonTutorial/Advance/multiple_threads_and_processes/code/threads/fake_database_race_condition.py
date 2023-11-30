import logging
import time

import concurrent.futures


class FakeDatabase:
    def __init__(self):
        self.value = 0  # database

    def update(self, name):
        logging.info("Thread %s: starting update", name)
        local_copy = self.value  # 读出来加一再写回去
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy  # 模拟写
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
# 该程序用两个线程创建了一个ThreadPoolExecutor，然后在每个线程上调用.submit()，告诉它们运行数据库.update()。
# .submit()允许将位置参数和命名参数传递给线程中运行的函数。

# 由于每个线程都运行.update()，并且.update()在.value上加了一个，你可能会期望数据库.value在最后被打印出来时是2。
# 因为两个线程同时进行读写，而变量只有一个，所以self变量没有增加
