def true():
    return True


true = lambda: True
print(true())


def add(x, y):
    return x + y


add = lambda x, y: x + y
print(add(1, 2))
