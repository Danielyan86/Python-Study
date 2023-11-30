class Person:
    def __init__(self, name):
        self.name = name


p = Person("scg")
# 使用getattr()获取name属性和不存在的age属性：

print(getattr(p, "name"))
print(getattr(p, "age", 23))
#
# 使用setattr
print("add property")
setattr(p, "age", 25)
print(p.__dict__)
#
print("start to delete property")
delattr(p, "age")
print(p.__dict__)
