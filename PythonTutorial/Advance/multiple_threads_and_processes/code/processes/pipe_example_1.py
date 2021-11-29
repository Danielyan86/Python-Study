from multiprocessing import Process, Pipe


def f(conn):
    # conn 就是pipe传进来的对象
    conn.send([42, None, 'hello'])
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()  # Pipe()函数返回一对由管道连接的连接对象，默认为双工（双向）。
    p = Process(target=f, args=(child_conn,))
    p.start()
    print(parent_conn.recv())  # prints "[42, None, 'hello']"
    p.join()
