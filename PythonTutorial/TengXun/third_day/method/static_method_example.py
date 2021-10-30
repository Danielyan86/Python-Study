class Person:
    gender = None

    @staticmethod
    def info(name, age):
        print(name, age)


if __name__ == '__main__':
    # 使用类名直接调用类方法
    Person.info('xiaowang', 3)
    # 使用类对象调用类方法
    p1 = Person()
    p1.info('xixi', 1)
