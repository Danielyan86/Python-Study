# 打印杨辉三角形
import itertools


def triangle(n=1):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n > 2:
        init_list = [1, 1]  # 初始化第一个状态
        for i in range(3, n + 1):  # 根据前一个状态推导下一个状态
            new_list_len = i
            new_list = [1] * i  # 初始化都为1
            for j in range(1, new_list_len - 1):  # 生成新的列表
                new_list[j] = init_list[j - 1] + init_list[j]
            init_list = new_list  # 更新推导列表
        return new_list

    else:
        raise AssertionError("n should be the positive integer")


def triangle2(n=1):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n > 2:
        init_list = [1, 1]  # 初始化第一个状态
        for i in range(3, n + 1):  # 根据前一个状态推导下一个状态
            new_list = [1] + [init_list[j] + init_list[j + 1] for j in range(i - 2)] + [1]
            init_list = new_list
        return new_list

    else:
        raise AssertionError("n should be the positive integer")


def triangle3():
    yield [1]
    init_list = [1]  # 初始化第一个状态
    while True:
        new_list = [1] + [init_list[j] + init_list[j + 1] for j in range(len(init_list) - 1)] + [1]
        yield new_list
        init_list = new_list


def test_triangle():
    assert triangle(1) == [1]
    assert triangle(2) == [1, 1]
    assert triangle(3) == [1, 2, 1]
    assert triangle(4) == [1, 3, 3, 1]
    assert triangle(5) == [1, 4, 6, 4, 1]


def test_triangle2():
    assert triangle2(1) == [1]
    assert triangle2(2) == [1, 1]
    assert triangle2(3) == [1, 2, 1]
    assert triangle2(4) == [1, 3, 3, 1]


def test_triangle3():
    for i in itertools.islice(triangle3(), 1):
        print(i)
    assert i == [1]
    for i in itertools.islice(triangle3(), 2):
        print(i)
    assert i == [1, 1]
    for i in itertools.islice(triangle3(), 3):
        print(i)
    assert i == [1, 2, 1]


if __name__ == '__main__':
    # print(triangle2(10))
    for i in itertools.islice(triangle3(), 10):
        print(i)
    # print(triangle2(3))
    # print(triangle2(5))
