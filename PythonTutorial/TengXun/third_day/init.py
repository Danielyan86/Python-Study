class TheFirstDemo:
    """这是一个学习Python定义的第一个类"""

    # 构造方法 覆盖基类的init方法
    def __init__(self):
        print("调用构造方法")

    # 类属性
    add = 'hello class'


if __name__ == '__main__':
    t = TheFirstDemo()
    t.__init__()
