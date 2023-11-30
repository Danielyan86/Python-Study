import logging
import threading
import time


def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    log_format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=log_format, level=logging.INFO, datefmt="%H:%M:%S")

    threads = list()
    for index in range(3):
        logging.info("Main    : create and start thread %d.", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        logging.info("Main    : before joining thread %d.", index)
        thread.join()
        logging.info("Main    : thread %d done", index)
# - 如果你仔细阅读输出结果，你会看到所有三个线程都按照你预期的顺序启动，但在这种情况下，它们是以相反的顺序结束的。多次运行会产生不同的顺序。寻找 "线程x：结束 "的信息，告诉你每个线程是什么时候完成的。
#
# - 线程运行的顺序是由操作系统决定的，可能相当难以预测。它可能（而且很可能）在不同的运行中有所不同，所以当你设计使用线程的算法时，你需要意识到这点。
#
# - 幸运的是，Python 给你提供了几个原生方法，我们将在后面看一下，以帮助协调线程，让它们一起运行。在此之前，让我们看看如何使管理一组线程更容易一些。
