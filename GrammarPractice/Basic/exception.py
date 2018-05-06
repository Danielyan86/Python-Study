# 捕获指定异常
def catch_specific_exception():
    try:
        f = open("blala", 'r')
    except FileNotFoundError as e:
        print(e)
        print("could not open the file")

    try:
        1 / 0
    except ZeroDivisionError as e:
        print("There is something wrong with Division,reason:{0}".format(e))


# 捕获多个异常
def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError):
        retval = "argument must be a number or tring"
    return retval


# 捕获所有异常
def catch_all_exceptions():
    try:
        f = open("blala", 'r')
    except Exception as e:
        print(e)
        print("could not open the file")
        # raise
    finally:
        print("this is the end")


def asser_keyword():
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
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
        raise


if __name__ == '__main__':
    # catch_specific_exception()
    # raise_function()
    catch_all_exceptions()
