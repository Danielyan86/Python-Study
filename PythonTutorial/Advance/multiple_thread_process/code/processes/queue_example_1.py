from multiprocessing import Process, Queue


def cube(x, q):
    q.put(x * x * x)
    print(x * x * x)


def add(x, q):
    q.put(x + 1)


if __name__ == "__main__":
    q = Queue()
    processes = []
    # 启动一个线程数目为10的线程池
    # 每个线程池依次传入0到10值
    for i in range(10):
        p = Process(target=cube, args=(i, q,))
        processes.append(p)

    # 启动线程池里面线程
    for p in processes:
        p.start()
    # 等待线程结束
    for p in processes:
        p.join()

    processes = []
    print("INITIAL VALUES: ")
    while not q.empty():
        val = q.get()
        print(val)
        p = Process(target=add, args=(val, q,))
        processes.append(p)
    for p in processes:
        p.start()

    for p in processes:
        p.join()

    print("FINAL VALUES: ")
    # 取出队列里面的值
    while not q.empty():
        print(q.get())
    # 该代码解释了对象的通信，在我们的例子中是q，在两个进程之间。empty()方法是为了确定队列是否为空，而get()则是为了返回存储在队列中的值。
# 结果的顺序是不确定的。
