from multiprocessing import Process, Pipe


def cube_sender(x, x_conn):
    # conn 就是pipe传进来的对象
    x_conn.send(x * x * x)


def cube_receiver(y_conn):
    print(y_conn.recv())


if __name__ == "__main__":
    x_conn, y_conn = Pipe()
    processes = []

    p1 = Process(
        target=cube_sender,
        args=(
            19,
            x_conn,
        ),
    )

    p2 = Process(target=cube_receiver, args=(y_conn,))

    processes.extend([p1, p2])

    for p in processes:
        p.start()

    for p in processes:
        p.join()
# cube_sender和cube_receiver是两个使用管道相互通信的进程。
# 数字19的立方从管道的一端发送到另一端（x_conn到y_conn）。x_conn是进程p1的输入。当对x_conn调用send()时，输出被发送到y_conn。
# y_conn是进程p2的输入，它接收输出并打印出结果的立方。
