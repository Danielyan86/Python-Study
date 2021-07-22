# https://foofish.net/python-decorator.html
import logging


def foo():
    print("foo")


def bar(func):
    func()


bar(foo)


def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()

    return wrapper


def foo():
    print('i am foo')


foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的时函数对象 wrapper，这条语句相当于  foo = wrapper
foo()  # 执行foo()就相当于执行 wrapper()


# use_logging 就是一个装饰器，它一个普通的函数，它把执行真正业务逻辑的函数 func 包裹在其中，看起来像 foo 被 use_logging 装饰了一样，
# use_logging 返回的也是一个函数，这个函数的名字叫 wrapper。在这个例子中，函数进入和退出时 ，被称为一个横切面，这种编程方式被称为面向切面的编程。

# @语法糖

def use_logging(func):
    def wrapper():
        logging.warning("%s is running" % func.__name__)
        return func()

    return wrapper


@use_logging
def foo():
    print("i am foo")


foo()


# 如上所示，有了 @ ，我们就可以省去foo = use_logging(foo)这一句了，直接调用 foo() 即可得到想要的结果。foo()
# 函数不需要做任何修改，只需在定义的地方加上装饰器，调用的时候还是和以前一样，如果我们有其他的类似函数，我们可以继续调用装饰器来修饰函数，
# 而不用重复修改函数或者增加新的封装。这样，我们就提高了程序的可重复利用性，并增加了程序的可读性。

class Example:
    @staticmethod
    def print_fun():
        print("this is a static method")


Example.print_fun()


# 带参数的装饰器
def decorator(func):
    def wrapper(*arg, **kwargs):
        # your function
        print()
        result = func(*arg, **kwargs)
        # your function
        return result

    return wrapper


@decorator
def foo(*arg, **kw):
    print(arg)
    print(kw)


foo("test11",key1=1)
