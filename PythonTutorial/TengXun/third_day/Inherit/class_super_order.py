# super.py
class IA(object):
    def __init__(self):
        print("call IA init ...")  # 基类IA没有super()，没有意义


class IB(IA):
    def __init__(self):
        print("call IB init ....")
        super().__init__()


class IC(IA):
    def __init__(self):
        print("call IC init ....")
        super().__init__()


class ID(IC, IB):
    def __init__(self):
        print("call ID init ...")
        super().__init__()


def test_ID():
    d = ID()
    print(ID.mro())


if __name__ == '__main__':
    # 广度优先搜索

    test_ID()
