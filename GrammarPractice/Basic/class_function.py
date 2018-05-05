class MyClass:
    myVersion = "1.0"

    # 构造器方法
    def __init__(self):
        print('initized')
        self.classvar = "2.0"

    def show_version(self):
        print(self.myVersion)


if __name__ == '__main__':
    # 方法要在绑定之后才能用
    #    MyClass.show_version()
    my_instance = MyClass()
    my_instance.show_version()
    print(my_instance.classvar)
    print(dir(my_instance))
