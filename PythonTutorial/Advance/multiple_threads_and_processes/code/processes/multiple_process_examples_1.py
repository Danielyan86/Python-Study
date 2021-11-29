import time
from multiprocessing import Process


def cube(x):
    print(f"start process {x}")
    print(x * x * x)
    time.sleep(1)
    print(f"end process {x}")


if __name__ == "__main__":
    processes = []
    for i in range(10):
        p = Process(target=cube, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()
# 进程类启动了10个进程。目标指定了要调用的函数，而args决定了要传递的参数。
# start()方法开始了进程。所有的进程都被循环等待，直到每个进程执行完毕，这是用join()方法检测出来的。
# join()方法有助于确保程序的其余部分在多进程完成后才运行。
# sleep()方法有助于了解进程的并发程度!



