# 捕获指定异常
def catch_specific_exception():
    try:
        open("blala", 'r')
    except FileNotFoundError as e:
        print(e)  # 打印系统标准异常信息
        print("could not open the file")  # 打印自定义信息
    try:
        1 / 0
    except ZeroDivisionError as e:
        print("There is something wrong with Division,reason:{0}".format(e))


# 捕获多个异常
def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError):
        retval = "argument must be a number or string"
    print(retval)
    return retval


# 捕获所有异常
def catch_all_exceptions():
    try:
        open("blala", 'r')
    except Exception as e:
        print(e)
        print("could not open the file")
        # raise
    finally:
        print("this is the end")


# 使用断言关键字抛出异常
def assert_keyword():
    assert 1 == 1
    # assert 1 == 0


# raise触发异常
# raise ZeroDivisionError("error")
def raise_function(information=None):
    print("throw out the exception")
    raise NameError('HiThere')
    # raise AssertionError("throw out the exception")
    # raise RuntimeError("run time error")


def raise_function2():
    try:
        raise NameError('HiThere')  # 抛出异常
    except NameError:
        print('An exception flew by!')
        raise  # 抛出捕获的异常


if __name__ == '__main__':
    # safe_float("1")
    # catch_specific_exception()
    # raise_function()
    catch_all_exceptions()
    assert_keyword()
    # raise_function()
    raise_function2()
