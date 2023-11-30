class Person:
    def __init__(self):
        print(f"This is the instance id {self}")
        self.name = "default name"
        self.gender = "male"

    # self 名字可以改变，约定一般用self
    # 实例方法默认第一个参数必须是self，否则语法错误
    # 直接在类下面定义的方法默认都是实例方法
    def self_test(this):
        print(this.name)

    # 通过self访问对象属性
    def self_test2(self):
        self.self_test()
        print(self.gender)


if __name__ == "__main__":
    xiaohong = Person()
    xiaohong.self_test()
