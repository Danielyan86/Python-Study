class supcls:
    x = 3
    y = 4

    def m(self):
        x = 33
        self.x = 333
        self.y = 444
        self.z = 555

    def n(self):
        return self.x, self.y, self.z


class childcls(supcls):
    # 重写父类属性
    y = supcls.y + 1  # 通过类名访问父类属性

    def n(self):
        self.z = 5555


if __name__ == "__main__":
    print(childcls.x)  # 父类属性，搜索到父类名称空间
    print(childcls.y)  # 子类自身属性，搜索到子类名称空间

    # 子类对象自身名称空间
    # 子类的类名称空间
    # 父类的类名称空间
