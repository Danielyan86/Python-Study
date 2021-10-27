class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 类方法
    def say(self, content):
        print(content)


if __name__ == '__main__':
    new_person = Person("nobody", 00)
    print(new_person.age, new_person)
    new_person.say()
