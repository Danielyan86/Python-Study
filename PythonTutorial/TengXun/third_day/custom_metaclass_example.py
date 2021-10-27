class Foo:
    pass


f = Foo()


#
# That __call__() method in turn invokes the following:
#
# __new__()
# __init__()
def new(cls):
    x = object.__new__(cls)
    x.attr = 100
    return x


Foo.__new__ = new
f = Foo()
print(f.attr)

g = Foo()
print(g.attr)
