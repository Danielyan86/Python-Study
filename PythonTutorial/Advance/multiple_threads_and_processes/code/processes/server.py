from multiprocessing import Process, Manager


def f(d, l):
    d[1] = 1
    d[2] = 2
    d[3] = 3
    l.reverse()


def f2(d, l):
    print(d)
    for key in d.keys():
        d[key] = key + 1
    l.sort()


if __name__ == '__main__':
    with Manager() as manager:
        d = manager.dict()
        print(d)
        l = manager.list(range(10))
        print(l)

        p = Process(target=f, args=(d, l))
        p.start()
        p.join()
        print(f"after first time change: {d}")
        print(f"after first time change: {l}")

        p = Process(target=f2, args=(d, l))
        p.start()
        p.join()

        print(f"final dictionary value: {d}")
        print(f"final list value: {l}")
# 服务器进程管理器比使用共享内存对象更灵活，因为它们可以被做成支持任意对象类型。
# 而且，一个单一的管理器可以通过网络被不同计算机上的进程共享。然而，它们比使用共享内存要慢。
