# 背景

当一个长期运行的进程需要加速或多个进程需要并行执行时，多进程是必不可少的。在单个内核上执行一个进程会限制其能力，否则他的执行能力可以在多个内核上扩散。 如果耗时的任务有并行运行的范围，并且底层系统有多个处理器/核，Python
提供了一个易于使用的接口来使用多进程。

# 使用进程

多进程中的Process类一次性分配了内存中的所有任务。使用Processclass创建的每个任务都必须有一个单独的内存分配。 想象一下这样的场景：要创建10个并行进程，每个进程都必须是一个独立的系统进程。 查看例子

```
multiple_process_examples_1.py
```

# 如何用管道（pipe）进行通信

如果两个进程需要进行通信，Pipe是最好的选择。一个管道可以有两个端点，每个端点都有send（）和recv（）方法。如果两个进程（线程）同时从同一个端点读取或写入数据，管道中的数据可能被破坏。
参考 https://docs.python.org/3/library/multiprocessing.html
Pipes Pipe()函数返回一对由管道连接的连接对象，默认为双工（双向）。

```python
from multiprocessing import Process, Pipe


def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()
```

Pipe()返回的两个连接对象代表管道的两端。每个连接对象都有send()和recv()
方法（除此之外）。请注意，如果两个进程（或线程）试图同时从管道的同一端读取或写入数据，管道中的数据可能会被破坏。当然，如果进程同时使用管道的不同端，就不会有损坏的风险。

pipeline_example_1.py pipeline_example_2.py

# 如何用队列进行通信（queue）

为了在一个共享的通信通道中存储多个进程的输出，可以使用一个队列。例如，假设任务是找到前十个自然数的立方体，然后给每个数字加1。 定义两个函数sum（）和cube（）。然后定义一个队列（q），调用cube()函数，然后是add()函数。
查看代码

```
queue_example_1.py
```

# 如何用共享内存通信 （shared memory）

从队列中获得线索，共享内存在进程之间无缝共享数据。可以是变量或者数组 查看例子

```
shared_memory_array.py
shared_memory_value.py
```

# 使用server

服务器进程是一个Python程序开始时被触发的主要进程。其他进程可以利用其对象进行操作。一个Manager()类的经理对象控制着一个服务器进程。Manager() 支持多种数据类型，如 list, dict, Lock, RLock,
Semaphore, BoundedSemaphore, Namespace, Condition, Event, Queue, Value, 和 Array。 查看例子

```
server.py
```

## 共享内存与服务器进程。

- 与共享内存相比，Manager()支持多种数据类型
- 进程可以通过网络在不同的计算机上共享一个管理器
- 服务器进程的速度比共享内存慢

# 总结

在本教程中，你已经学会了如何使用 Python 中可用的多进程工具。你学会了进程与池的区别，并创建了一个 cube() 函数来理解所有的概念。你了解了进程通信、共享内存、服务器进程。

# 参考资料

- https://towardsdatascience.com/how-to-use-the-multiprocessing-package-in-python3-a1c808415ec2 
