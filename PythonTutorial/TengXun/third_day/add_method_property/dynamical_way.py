class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self, content):
        print(content)


if __name__ == '__main__':
    p = Person('scg', 18)
    # 先定义一个函数
    def info(self):
        print("---info函数---", self)
    # 动态绑定方法
    p.info = info
    p.info(p)  # python不会自动将调用者绑定到第一个参数,需要手动将调用者绑定为第一个参数
