from multiprocessing import Process, Array


def cube(x):
    for i in range(len(x)):
        x[i] = x[i] + 1


if __name__ == "__main__":
    arr = Array("i", 3)
    print(arr[:])
    p = Process(target=cube, args=(arr,))
    p.start()
    p.join()

    print(arr[:])
    p = Process(target=cube, args=(arr,))
    p.start()
    p.join()

    print(arr[:])
# Array()初始化了一个拥有int数据类型、长度为3的空数组，该数组已被循环使用，在其中的每个元素上加1。
# 你可以在不同的进程中使用Arr，就像Value一样。这实质上是共享内存的概念。
# 注意：'d'表示双精度浮点数，'i'（在Array("i", 3)中）表示有符号整数。
