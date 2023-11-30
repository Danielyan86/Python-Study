class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def say(self):
        print("正在调用 say() 实例方法")


if __name__ == "__main__":
    p1 = Person("scg", 18)
    p1.say()
