class Person:
    def __init__(self, name):
        self.name = name


class Person2:
    def __init__(self, name):
        self.name = name

    def __getattr__(self, attrname):
        if attrname == "name":
            print("in getattr1")
            return self.name
        elif attrname == "age":
            print("in getattr2")
            return 25
        else:
            print("in getattr3")
            raise AttributeError(attrname)


if __name__ == '__main__':
    p = Person("xiaoming")
    print(p.name)  # (1)访问p对象的name属性
    p.name = "abc"  # (2)为p对象的name属性赋值
    del p.name  # (3)删除p对象的name属性

    p = Person("scg")

    print(p.name)
    print(p.age)
