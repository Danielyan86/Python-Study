class ClassProperty:
    # 下面定义了1个类属性
    name = 'hello class'

    def say(self, content):
        print(content)


if __name__ == '__main__':
    # 类属性是共用的
    cls1 = ClassProperty
    print(cls1.name)
    cls2 = ClassProperty()
    cls2.name = "nihao"
    print(cls1.name)
