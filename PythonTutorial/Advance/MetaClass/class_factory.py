# 自定义一个元类，还是从type继承下来，相当于多了一层
class Meta(type):
    def __init__(cls, name, bases, dct):
        cls.attr = 100


# 改写默认元类
class X(metaclass=Meta):
    pass


class Y(metaclass=Meta):
    pass


class Z(metaclass=Meta):
    pass


if __name__ == "__main__":
    x1 = X()
    print(x1.attr)
