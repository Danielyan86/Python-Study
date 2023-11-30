import concurrent.futures
import logging
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(thread_function, range(3))
# 这段代码创建了一个ThreadPoolExecutor作为上下文管理器，告诉它在池子里想要多少个工作线程。然后，它使用.map()遍历一个可迭代的东西，在你的例子中是range(3)，把每个东西传给池中的一个线程。

# with块的结尾会使ThreadPoolExecutor对池中的每个线程进行.join()操作。建议你尽可能使用ThreadPoolExecutor作为上下文管理器，这样你就不会忘记对线程进行.join()。
