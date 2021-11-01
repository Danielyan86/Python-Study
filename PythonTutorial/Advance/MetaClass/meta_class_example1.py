# 常规方法创建
class Foo:
    pass


x = Foo()
print(x)

# 动态创建，和上面等价
Foo = type('Foo', (), {})
x = Foo()
print(x)
print(type(x))
