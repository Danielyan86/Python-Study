class A:
    """A 实现了迭代器协议 它的实例就是一个迭代器"""

    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        print('__iter__')
        return self

    def __next__(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()


if __name__ == '__main__':

    # 迭代元素
    a = A(3)
    for i in a:
        print(i)
    # 再次迭代 没有元素输出 因为迭代器只能迭代一次
    for i in a:
        print(i)
    # for i in a 相当于执行 iter(a),再执行next(a),直到stop异常抛出，for里面处理了StopIteration异常，所以不会中断
    # 每次迭代时会执行一次 __next__ 方法，返回一个值
    # 如果没有可迭代的数据，抛出 StopIteration 异常，for 会停止迭代
    # 注意，当我们迭代完 for i in a 时，如果再次执行迭代，将不会有任何数据输出。因为对象的idx 已经到最大值
    # 每次都迭代一个对象

    a2 = A(3)
    b = iter(a2)
    print(b)
    print(b.__next__())
    print(b.__next__())
    print(b.__next__())
    print(b.__next__())
