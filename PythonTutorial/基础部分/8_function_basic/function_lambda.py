# lambda表达式返回可调用的函数对象
def true():
    return True


print(true())

# true方法等价于匿名函数表达式
true = lambda: True
print(true())


def add(x, y):
    return x + y


print(add(1, 2))

add = lambda x, y: x + y
print(add(1, 2))
