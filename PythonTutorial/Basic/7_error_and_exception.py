# 捕获指定异常，并让程序继续进行
def catch_specific_exception():
    try:
        open("blala", "r")
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
        retrieval = float(obj)
    except (ValueError, TypeError):
        retrieval = "argument must be a number or string"
    print(retrieval)
    return retrieval


# 捕获所有异常
def catch_all_exceptions():
    try:
        open("blala", "r")
    except Exception as e:
        print(e)
        print("could not open the file")
        # raise
    finally:  # 无论前面发生什么，最后都要执行finally里面的内容
        print("this is the end")


# else 流程
def try_else_exception():
    try:
        print("This is try block")
    except Exception as e:
        print(e)
        print("This is except block")
    else:
        print("There is no exception")


# 使用断言关键字抛出异常
def assert_keyword():
    assert 1 == 1  # 判断assert后面表达式是否为True
    assert 2 + 2 == 2 * 2
    # assert 1 == 0


# raise触发异常
def raise_function():
    print("throw out the exception")
    raise NameError("HiThere")
    # raise AssertionError("throw out the exception")
    # raise RuntimeError("run time error")


def raise_function2():
    try:
        raise NameError("HiThere")  # 抛出异常
    except NameError:
        print("An exception flew by!")
        raise  # 抛出捕获的异常


# 判断传入参数为字符串类型，否则中断程序，抛出异常
def raise_function3(input_para):
    if isinstance(input_para, str):
        print("input para".format(input_para))
    else:
        raise Exception(
            "parameter type should be string, however it is {}".format(type(input_para))
        )


if __name__ == "__main__":
    # safe_float("1")
    catch_specific_exception()
    # raise_function()
    # catch_all_exceptions()
    # assert_keyword()
    # raise_function()
    # raise_function2()
    # raise_function3()
    raise_function3(123)
