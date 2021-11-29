from multiprocessing import Process, Value


def cube(x):
    x.value = x.value * x.value * x.value


if __name__ == "__main__":
    # value方法
    # c默认情况下，返回值实际上是该对象的一个同步包装器。对象本身可以通过一个Value的value属性来访问。
    # typecode_or_type决定了返回对象的类型：它要么是ctypes类型，要么是数组模块使用的那种单字符类型码。*args被传递给该类型的构造函数。
    # 如果lock是True（默认），那么就会创建一个新的递归锁对象来同步访问该值。如果lock是一个Lock或RLock对象，那么它将被用来同步访问该值。如果lock是False，那么对返回对象的访问将不会自动受到锁的保护，所以它不一定是"进程安全的"。
    # 像 += 这样涉及读写的操作不是原子的。
    num = Value("i", 10) # 第一个参数是类型，i 相当于Integer
    p = Process(target=cube, args=(num,))
    p.start()
    p.join()
    p = Process(target=cube, args=(num,))  # 第二次启动一个进程，共享内存里面的x的value是1000
    p.start()
    p.join()

    print(num.value)
