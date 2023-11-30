import threading
from time import sleep, ctime


# loops = [4, 2]


def thread_fuc(info=None):
    print("start time", ctime())
    print(info)
    sleep(1)
    print("end time", ctime())


def multiple_fuc(fun):
    threads = [threading.Thread(target=fun, args=("hello",)) for i in range(10)]
    print(threads)
    for th in threads:
        print(th)
        th.start()
    # for th in threads:
    #     th.join()  # join 函数会等到线程结束


if __name__ == "__main__":
    multiple_fuc(thread_fuc())
    for i in range(10):
        thread_fuc()
