class Person:
    def __init__(self):
        print(f"This is the instance id {self}")

    def self_test(this):
        print(this.__class__)

    @staticmethod
    def static_method():
        print("this a static method. It can be called without instantiate")


if __name__ == "__main__":
    xiaoming = Person()
    xiaohong = Person()
    RS = Person()
    RS.self_test()
