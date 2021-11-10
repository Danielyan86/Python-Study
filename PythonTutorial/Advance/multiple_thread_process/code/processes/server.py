from multiprocessing import Process, Manager


def cube(d, l):
    d["car"] = "ford"
    l.sort()


if __name__ == "__main__":
    manager = Manager()

    manager_dic = manager.dict()
    manager_list = manager.list([9, 3])

    p = Process(
        target=cube,
        args=(
            manager_dic,
            manager_list,
        ),
    )
    p.start()
    p.join()

    print(manager_dic)
    print(manager_list)
