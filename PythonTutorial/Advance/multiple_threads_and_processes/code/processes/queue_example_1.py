from multiprocessing import Process, Queue


def cube(x, q):
    q.put(x * x * x)  # 往队列里面放数据
    print(x * x * x)


def add(x, q):
    q.put(x + 1)


if __name__ == "__main__":
    q = Queue()
    processes = []
    # 启动一个线程数目为10的线程池,分别往队列里面写入x立方的值
    # 每个线程池依次传入0到10值
    for i in range(10):
        process = Process(
            target=cube,
            args=(
                i,
                q,
            ),
        )
        processes.append(process)

    # 启动线程池里面线程
    for process in processes:
        process.start()
    # 等待线程结束
    for process in processes:
        process.join()

    processes = []
    print("INITIAL VALUES: ")
    while not q.empty():  # 把队列里面数据取出来直到队列为空
        val = q.get()
        print(val)
        process = Process(
            target=add,
            args=(
                val,
                q,
            ),
        )  # 取出的数据再放到add方法里面加一，然后放入一个新的队列
        processes.append(process)
    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("FINAL VALUES: ")
    # 取出队列里面的值
    while not q.empty():
        print(q.get())
    # 该代码解释了对象的通信，在我们的例子中是q，在两个进程之间。empty()方法是为了确定队列是否为空，而get()则是为了返回存储在队列中的值。
    # 结果的顺序是不确定的。
