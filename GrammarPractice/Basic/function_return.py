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
    print(res)
    res = return_list()
    print(res)
    res = return_tuple()
    print(res, type(res))
    res1, res2, res3 = return_tuple()
    print(type(res3))
    print(res1, res2, res3)
