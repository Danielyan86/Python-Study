def hello():
    print('hello world')


res = hello()
print(res)


def return_list():
    return [1, 3, 4]


res = return_list()
print(res)


def return_tuple():
    return 123, 'xyz', {"key": "value"}


res = return_tuple()
print(res, type(res))
res1, res2, res3 = return_tuple()
print(type(res3))
print(res1, res2, res3)
