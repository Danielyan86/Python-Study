class Person:
    gender = None

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def info(cls):
        print("正在调用类方法{}".format(cls))
        print(f"can access the class attribute {cls.gender}")


if __name__ == '__main__':
    # 使用类名直接调用类方法
    Person.info()
    # 使用类对象调用类方法
    p1 = Person('scg', 18)
    p1.info()
