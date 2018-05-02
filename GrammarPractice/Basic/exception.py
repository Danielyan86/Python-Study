try:
    f = open("blala", 'r')
except IOError as e:
    print("could not open the file")


# 捕获多个异常
def safe_float(obj):
    try:
        retval = float(obj)
    except (ValueError, TypeError):
        retval = "argument must be a number or tring"
    return retval


# 捕获所有异常
try:
    f = open("blala", 'r')
except Exception as e:
    print("could not open the file")

# raise ArithmeticError("raise error")
assert 1 == 1
assert 1 == 0
