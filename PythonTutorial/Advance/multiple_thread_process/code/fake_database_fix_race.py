import logging
import time

import concurrent.futures
import threading


class FakeDatabase:
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()  # 设置lock

    def locked_update(self, name):
        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)
        with self._lock:  # 使用上下文管理关键字使用锁
            logging.debug("Thread %s has lock", name)
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy
            logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = FakeDatabase()
    logging.info("Testing update. Starting value is %d.", database.value)
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        for index in range(2):
            executor.submit(database.locked_update, index)
    logging.info("Testing update. Ending value is %d.", database.value)
# 在这个输出中，你可以看到线程0获得了锁，并且在它进入睡眠状态时仍然持有它。然后线程1启动并试图获得相同的锁。因为线程0仍然持有它，线程1必须等待。这就是锁所提供的相互排斥。
