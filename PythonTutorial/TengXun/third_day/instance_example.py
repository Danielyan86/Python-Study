class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类方法
    def say(self, content):
        print(content)


if __name__ == '__main__':
    new_person = Person("Lao wang", 00)  # 实例化一个对象并初始化参数
    print(new_person.age, new_person)  # 访问对象属性
    new_person.say("I am Lao wang")  # 调用对象方法
    new_person.gender = "male"  # 给对象添加新的属性
    print(new_person.gender)