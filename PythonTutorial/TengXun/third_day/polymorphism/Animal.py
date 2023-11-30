class Animal:
    def who(self):
        print("I am an Animal")


class Duck(Animal):
    def who(self):
        print("I am a duck")


class Dog(Animal):
    def who(self):
        print("I am a dog")


class Cat(Animal):
    def who(self):
        print("I am a cat")


def func(obj):
    obj.who()


if __name__ == "__main__":
    duck = Duck()
    dog = Dog()
    cat = Cat()
    func(duck)
    func(dog)
    func(cat)
