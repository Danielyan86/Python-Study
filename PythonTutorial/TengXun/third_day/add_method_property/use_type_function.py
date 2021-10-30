class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


# 先定义一个函数
def info(self):
    print("---info函数---", self)

if __name__ == '__main__':
    p = Person('scg', 18)

    # 导入MethodType
    from types import MethodType

    p.foo = MethodType(info, p)
    p.foo()
