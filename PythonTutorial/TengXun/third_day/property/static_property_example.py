class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def info(name, age):
        print(name, age)


# 使用类名直接调用静态方法
Person.info("scg", 18)
# 使用类对象调用静态方法
p1 = Person("xiaoshi", 20)
p1.info("scg", 18)
