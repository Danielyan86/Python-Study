class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


if __name__ == '__main__':
    p = Person("max", 10)
    # 为p对象增加一个hobby实例变量
    p.hobby = "篮球"
    print(p.hobby)
    # 删除新添加的 hobby 实例变量
    del p.hobby
    # 再次输出hobby，此时会报错
    # print(p.hobby)
