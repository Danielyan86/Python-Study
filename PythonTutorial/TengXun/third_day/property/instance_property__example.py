class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        self.hobby = 'rap'


if __name__ == '__main__':
    p1 = Person('scg', 18)
    print(p1.name)
    print(p1.age)
    # 由于 p1 对象未调用 say() 方法，因此其没有 hobby 变量，下面这行代码会报错
    # print(p1.hobby)
    p2 = Person('xiaoshi', 20)
    print(p2.name)
    print(p2.age)
    # 只有调用 say()，才会拥有 hobby 实例属性
    p2.say()
    print(p2.hobby)
