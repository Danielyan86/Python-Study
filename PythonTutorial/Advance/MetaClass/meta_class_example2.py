# 常规方法创建
class Foo:
    pass


# 常规方法创建
class Bar(Foo):
    attr = 100


x = Bar()
print(x)

# 动态创建，和上面等价
Bar = type("Bar", (Foo,), dict(attr=100))
x = Bar()
print(x)
print(type(x))
