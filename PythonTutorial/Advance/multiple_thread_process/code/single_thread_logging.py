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

    logging.info("Main    : before creating thread")
    # 把方法作为参数传给target
    x = threading.Thread(target=thread_function, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")
# 当你运行程序时，你会注意到在 __main__ 打印完它的所有信息后，在线程结束前有一个停顿 (大约 2 秒)。
# 这个停顿是Python在等待非记忆性线程的完成。当你的 Python 程序结束时，关闭过程的一部分是清理线程例程。
# 如果你看一下 Python 线程的源代码，你会看到 threading._shutdown() 遍历了所有正在运行的线程，并对每一个没有设置 daemon 标志的线程调用 .join() 。
# 所以你的程序在等待退出，因为线程本身在睡眠中等待。一旦它完成并打印了信息，.join()就会返回，程序就可以退出。
#
# 通常，这种行为是你想要的，但我们还有其他的选择。让我们首先用一个守护线程来重复这个程序。你可以通过改变你构建线程的方式来做到这一点，添加daemon=True标志。
# 添加daemon=true之后它是一个守护线程，所以当 __main__ 到达其代码的末尾，程序想要结束时，守护线程被杀死。
# 要告诉一个线程等待另一个线程完成，你可以调用.join()。如果你取消了这一行，主线程将暂停并等待线程x完成运行。
