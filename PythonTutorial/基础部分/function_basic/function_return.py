# return None
def hello():
    print('hello world')


# return one object
def return_list():
    return [1, 3, 4]


# return multiple object
def return_tuple():
    return 123, 'xyz', {"key": "value"}


if __name__ == '__main__':
    res = hello()
    print(res)  # 没有返回值

    res = return_list()
    print("返回list对象", res)

    res = return_tuple()
    print("返回元组", res, type(res))

    # 根据返回顺序，每个变量会接收到对应的返回值
    res1, res2, res3 = return_tuple()
    print(type(res3))
    print(res1, res2, res3)
