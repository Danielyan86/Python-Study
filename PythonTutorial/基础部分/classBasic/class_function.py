class MyClass:
    # 类属性
    myVersion = "1.0"

    # 构造器方法
    def __init__(self):
        print('initialized')
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

    my_instance2 = MyClass()
    MyClass.myVersion = 3.0  # 修改类属性
    print(my_instance.myVersion)
    print(my_instance2.myVersion)
